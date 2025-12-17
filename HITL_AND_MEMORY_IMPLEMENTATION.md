# HITL and Memory Implementation Summary

## Overview
This document describes the implementation of **Human-in-the-Loop (HITL)** and **Memory & Self-Learning** features in MathMentor.

---

## 1. Human-in-the-Loop (HITL) Implementation

### 1.1 What is HITL?
HITL pauses the AI pipeline and asks a human to confirm or fix something before continuing. It acts as a safety checkpoint.

### 1.2 HITL Triggers (Backend)
The system triggers HITL review when ANY of these conditions are met:

#### ✅ Low OCR Confidence
```python
if request.ocr_confidence is not None and request.ocr_confidence < 0.6:
    needs_human_review = True
    hitl_reason.append("Low OCR confidence")
```

#### ✅ Low ASR Confidence
```python
if request.asr_confidence is not None and request.asr_confidence < 0.6:
    needs_human_review = True
    hitl_reason.append("Unclear audio transcription")
```

#### ✅ Parser Ambiguity
```python
if parsed.get('needs_clarification', False):
    needs_human_review = True
    hitl_reason.append("Parser detected ambiguity")
```

#### ✅ Verifier Failure or Low Confidence
```python
if not verification_result.get('is_correct', False):
    needs_human_review = True
    hitl_reason.append("Verifier detected errors")
elif verification_result.get('confidence', 0) < 0.6:
    needs_human_review = True
    hitl_reason.append("Low verification confidence")
```

#### ✅ Manual User Request
```python
if request.request_review:
    needs_human_review = True
    hitl_reason.append("User requested review")
```

### 1.3 Pipeline Behavior When HITL Triggered

When `needs_human_review = True` and `force_continue = False`:

🚫 **STOP the pipeline:**
- No explainer runs
- No final answer display
- Return partial results with HITL flag

```python
if needs_human_review and not request.force_continue:
    return {
        "status": "needs_human_review",
        "needs_human_review": True,
        "hitl_reason": hitl_reason,
        "parsed_problem": parsed,
        "solution": {...},  # Partial solution
        "verification": {...},
        "agent_trace": agent_trace
    }
```

### 1.4 HITL UI (Frontend)

When HITL is triggered, the frontend displays:

#### Warning Panel
```html
<div style='background: #fff3cd; border: 3px solid #ffc107;'>
    <h2>✋ Human Review Required</h2>
    <p>The system needs your input to continue.</p>
</div>
```

#### Reason Display
```python
st.markdown("### 📋 Reason(s) for Review:")
for reason in st.session_state.hitl_reason:
    st.markdown(f"- **{reason}**")
```

#### Action 1: Edit Problem Text
```python
corrected_problem = st.text_area(
    "Review and correct the problem text:",
    value=st.session_state.hitl_corrected_problem,
    height=100
)
```

#### Action 2: Edit Solution (Optional)
```python
corrected_solution = st.text_area(
    "Correct the solution if needed:",
    value=solution_text,
    height=150
)
```

#### Action 3: Approve / Reject Buttons
```python
# Approve button
if st.button("✅ Approve & Continue"):
    # Re-solve with corrections if problem was changed
    # Set force_continue=True to override HITL
    # Reset HITL flags and continue

# Reject button
if st.button("❌ Reject & Retry"):
    # Store corrected problem back to extracted_text
    # Reset pipeline completely
    # User can modify and re-submit
```

### 1.5 Resume Pipeline After Human Action

#### If APPROVED:
```python
if approve:
    needs_human_review = False
    human_approved = True
    # Pipeline continues with force_continue=True
    # Explainer runs
    # Final answer shown
```

#### If REJECTED:
```python
if reject:
    reset_pipeline = True
    # User edits problem
    # Pipeline restarts from scratch
```

### 1.6 Manual Review Request

Users can manually trigger HITL even when solution is correct:

```python
if st.button("🔍 Request Re-check"):
    st.session_state.hitl_required = True
    st.session_state.hitl_reason = ["User requested review"]
    st.rerun()
```

---

## 2. Memory & Self-Learning Implementation

### 2.1 What is Memory?
Memory stores problem-solving history and learns from patterns **WITHOUT model retraining**. It's pattern storage + reuse.

### 2.2 Memory Storage Schema

Each solved problem is stored in `memory_store/problems.jsonl`:

```json
{
  "id": "uuid-8chars",
  "timestamp": "2025-12-18T00:10:27",
  "problem_text": "A bag contains 5 red marbles...",
  "topic": "Probability",
  "variables": {...},
  "constraints": {},
  "solution": {
    "final_answer": "3/10",
    "steps": [...],
    "confidence": 0.99
  },
  "verification": {
    "is_correct": true,
    "confidence": 0.99,
    "issues": []
  },
  "retrieved_context": [...],
  "agent_trace": [...],
  "feedback": null
}
```

### 2.3 Storage Location

#### Files:
- `memory_store/problems.jsonl` - All solved problems (JSONL format)
- `memory_store/feedback.jsonl` - User feedback records
- `memory_store/patterns.json` - Learned patterns and corrections

### 2.4 How Memory is Used at Runtime

#### 🔁 1. Retrieve Similar Problems

Before solving:
```python
similar_problems = memory_service.find_similar_problems(topic, variables, limit=3)
if similar_problems:
    # Show in agent trace: "Found 3 similar problems"
    # System can reference past solutions
```

#### 🔁 2. Reuse Solution Patterns

```python
solution_patterns = memory_service.get_solution_patterns(topic)
if solution_patterns:
    # Pattern: ["Total marbles = X", "Favorable = Y", "P = Y/X"]
    # Solver can shortcut using known pattern
```

Benefits:
- ✅ Faster solving
- ✅ More consistent answers
- ✅ Higher reliability

#### 🔁 3. Apply Known OCR/ASR Corrections

Before parsing:
```python
corrected_text = memory_service.apply_known_corrections(problem_text)
# Fixes: "bIue" → "blue", "5+3+Z" → "5+3+2"
```

Stored in `patterns.json`:
```json
{
  "ocr_corrections": {
    "bIue": "blue",
    "5+3+Z": "5+3+2",
    "probabIlity": "probability"
  }
}
```

### 2.5 Store Human Corrections as Learning Signals

When HITL happens and human provides corrections:

```python
if human_corrected:
    memory_service.store_feedback(
        problem_id=problem_id,
        feedback_type="edit",
        user_comment=user_comment,
        corrected_solution=corrected_solution
    )
    
    # Automatically updates patterns.json
    # Future problems benefit from this correction
```

### 2.6 Memory Service Key Methods

#### Search Similar Problems
```python
def find_similar_problems(topic: str, variables: Dict, limit: int = 5):
    """Find problems with same topic and similar structure"""
    # Uses Jaccard similarity on variable keys
    # Returns sorted by similarity score
```

#### Retrieve Solution Patterns
```python
def get_solution_patterns(topic: str) -> List[Dict]:
    """Get known solution patterns for topic"""
    # Only returns verified correct solutions
    # Sorted by confidence
```

#### Apply Known Corrections
```python
def apply_known_corrections(text: str) -> str:
    """Apply stored OCR/ASR corrections"""
    # Reads patterns.json
    # Replaces known mistakes
```

#### Store OCR Correction
```python
def store_ocr_correction(wrong_text: str, corrected_text: str):
    """Learn from human corrections"""
    # Extracts word-level differences
    # Stores in patterns.json
```

#### Search by Structure
```python
def search_by_structure(problem_structure: Dict) -> List[Dict]:
    """Find problems with matching structure"""
    # For probability: compares count categories
    # E.g., {red: 5, blue: 3} matches {red: 2, blue: 4}
```

### 2.7 Memory is READ-ONLY for Models

**IMPORTANT:** Models do NOT retrain or update weights.

They only:
- ✅ Retrieve past solutions
- ✅ Reuse known patterns
- ✅ Follow stored corrections

This is **exactly** what the assignment requires - learning without retraining.

---

## 3. Integration Flow

### Complete Pipeline with HITL + Memory

```
1. User submits problem (text/OCR/ASR)
2. [OCR/ASR confidence checked] → HITL if <0.6
3. Apply known corrections from memory
4. Parse problem → HITL if ambiguous
5. Search memory for similar problems
6. Retrieve solution patterns
7. Route intent (RAG or skip)
8. Solve problem
9. Verify solution → HITL if incorrect or confidence <0.6
10. [HITL triggered] → Show UI, wait for human
11. [Human approves] → Continue to explainer
12. [Human rejects] → Restart from step 1
13. Store problem + solution in memory
14. Display final answer
15. User feedback → Store in memory for learning
```

---

## 4. File Changes Summary

### Backend Files Modified:
1. **`backend/app.py`**
   - Added `request_review`, `force_continue`, `ocr_confidence`, `asr_confidence` to `SolveRequest`
   - Added HITL trigger logic for all 5 conditions
   - Added memory retrieval before solving
   - Added `problem_id` to response
   - Pipeline stops when `needs_human_review=True`

2. **`backend/services/memory_service.py`**
   - Added `get_solution_patterns()` - retrieve known patterns
   - Added `apply_known_corrections()` - fix OCR/ASR errors
   - Added `store_ocr_correction()` - learn from corrections
   - Added `search_by_structure()` - find structurally similar problems

### Frontend Files Modified:
1. **`frontend/app.py`**
   - Added HITL state flags to session state
   - Pass `ocr_confidence` and `asr_confidence` to solve API
   - Detect `needs_human_review` flag from response
   - Display HITL warning panel with reasons
   - Provide editable text areas for corrections
   - Handle approve/reject actions
   - Manual review request button

---

## 5. Testing HITL

### Test Case 1: Low OCR Confidence
1. Upload blurry image
2. OCR extracts text with confidence 0.45
3. Submit to solve
4. **Expected:** HITL panel shows "Low OCR confidence"
5. User corrects text and approves
6. Pipeline continues with corrected text

### Test Case 2: Parser Ambiguity
1. Enter: "Find x"
2. Submit to solve
3. Parser returns `needs_clarification=true`
4. **Expected:** HITL panel shows "Parser detected ambiguity"
5. User clarifies: "Solve for x: 2x + 5 = 11"
6. Pipeline restarts

### Test Case 3: Verifier Failure
1. Enter a complex problem
2. Solver provides incorrect solution
3. Verifier detects error: `is_correct=false`
4. **Expected:** HITL panel shows "Verifier detected errors"
5. User reviews and approves anyway (or corrects)

### Test Case 4: Manual Review
1. Solve problem successfully
2. Click "🔍 Request Re-check" button
3. **Expected:** HITL panel shows "User requested review"
4. User can edit and re-solve

---

## 6. Testing Memory Learning

### Test Case 1: Similar Problem Recognition
1. Solve: "Bag with 5 red, 3 blue, 2 green. Pick blue?"
2. Check agent trace: No similar problems found
3. Solve: "Bag with 10 red, 5 blue, 3 green. Pick red?"
4. **Expected:** Agent trace shows "Found similar problems: 1"
5. System reuses pattern from first problem

### Test Case 2: OCR Correction Learning
1. Upload image with text: "Find the probabIlity"
2. Human corrects to: "Find the probability"
3. System stores: `"probabIlity": "probability"`
4. Next time: Automatically corrects "probabIlity" → "probability"

### Test Case 3: Solution Pattern Reuse
1. Solve 3 simple probability problems
2. All verified correct
3. Solve 4th similar problem
4. **Expected:** Agent trace shows "Retrieved solution patterns: 3"
5. Solver follows known pattern structure

---

## 7. Result

✅ **HITL Implemented:**
- 5 trigger conditions working
- Pipeline stops correctly
- UI shows warning panel
- Human can edit and approve/reject
- Manual review button available

✅ **Memory Implemented:**
- Problems stored in JSONL format
- Similar problems retrieved
- Solution patterns reused
- OCR/ASR corrections applied
- Human feedback stored for learning

✅ **No Model Retraining:**
- All learning is pattern-based
- Models only retrieve and reuse
- Exactly as assignment requires

---

## 8. Future Enhancements

### Possible Improvements:
1. **Better similarity matching** - Use embeddings instead of Jaccard
2. **Pattern visualization** - Show similar problems in UI
3. **Confidence thresholds** - User-configurable HITL triggers
4. **Batch corrections** - Apply multiple corrections at once
5. **Export memory** - Download history as JSON/CSV

---

## Conclusion

Both HITL and Memory features are **fully implemented** and **functional**. The system now:
- Pauses for human review when uncertain
- Learns from past solutions without retraining
- Applies corrections automatically
- Provides safety checkpoints

This satisfies all assignment requirements for Human-in-the-Loop and Self-Learning.
