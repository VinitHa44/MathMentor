# Quick Testing Guide - HITL & Memory

## Prerequisites
- Backend running: `cd backend && uvicorn app:app --reload`
- Frontend running: `cd frontend && streamlit run app.py`

---

## Test 1: HITL - Low OCR Confidence ✅

**Steps:**
1. Upload blurry image with math problem
2. Click "Extract Text from Image"
3. If confidence < 60%, HITL will trigger automatically
4. Look for yellow warning panel: "✋ Human Review Required"
5. Reason will show: "Low OCR confidence"
6. Edit the problem text in the provided text area
7. Click "✅ Approve & Continue" to solve with corrections

**Expected:** Pipeline stops, shows HITL panel, allows correction, resumes after approval

---

## Test 2: HITL - Parser Ambiguity ✅

**Steps:**
1. Type ambiguous problem: "Find x"
2. Click "Confirm & Solve"
3. Parser detects ambiguity
4. HITL panel appears
5. Reason: "Parser detected ambiguity"
6. Clarify: "Solve for x: 2x + 5 = 11"
7. Click "❌ Reject & Retry"
8. Re-submit clarified problem

**Expected:** HITL triggers, user can clarify and restart

---

## Test 3: HITL - Verifier Failure ✅

**Steps:**
1. Enter complex problem
2. Let system solve
3. If solution is incorrect, verifier will trigger HITL
4. Reason: "Verifier detected errors"
5. Review the solution in HITL panel
6. Either approve anyway or reject and retry

**Expected:** HITL stops pipeline when verification fails

---

## Test 4: HITL - Manual Review Request ✅

**Steps:**
1. Solve any problem successfully
2. Scroll down to see solution
3. Click "🔍 Request Re-check" button below solution
4. HITL panel appears
5. Reason: "User requested review"
6. Edit and approve/reject

**Expected:** User can manually trigger HITL anytime

---

## Test 5: Memory - Similar Problem Recognition 🧠

**Steps:**
1. **Problem 1:** "A bag contains 5 red, 3 blue, 2 green marbles. What is probability of picking blue?"
2. Solve completely
3. Check "Agent Workflow" section - no similar problems yet
4. **Problem 2:** "A bag contains 10 red, 5 blue, 3 green marbles. What is probability of picking red?"
5. Solve
6. Check "Agent Workflow" - should show "Memory Service: Found similar problems"

**Expected:** Second problem recognizes first problem as similar

---

## Test 6: Memory - Solution Pattern Reuse 🧠

**Steps:**
1. Solve 3 simple probability problems (all marble-picking type)
2. All should verify as correct
3. Solve 4th similar probability problem
4. Check "Agent Workflow"
5. Look for "Memory Service: Retrieved solution patterns"

**Expected:** System retrieves and references past solution patterns

---

## Test 7: Memory - OCR Correction Learning 🧠

**Manual simulation (automatic detection requires actual OCR errors):**

1. Add correction manually to `backend/memory_store/patterns.json`:
```json
{
  "ocr_corrections": {
    "probabIlity": "probability",
    "caIculate": "calculate",
    "5+3+Z": "5+3+2"
  }
}
```

2. Type problem with these errors: "Find the probabIlity when picking from 5+3+Z marbles"
3. Submit to solve
4. System automatically corrects before parsing
5. Check Agent Workflow - should show "Memory Service: Applied known corrections"

**Expected:** System learns and applies corrections automatically

---

## Test 8: Memory - View History 📊

**Steps:**
1. Solve multiple problems (3-5)
2. Click "📚 View Memory & History" in sidebar
3. View statistics: Problems solved, accuracy, etc.
4. Browse historical interactions
5. Filter by "All", "Correct", "Corrected", "Clarifications"

**Expected:** Complete history visible with statistics

---

## Test 9: Feedback & Learning 💬

**Steps:**
1. Solve a problem
2. Scroll to "Feedback" section
3. Click "✅ Approve" - stores positive feedback
4. OR click "✏️ Edit/Correct" - provide correction
5. OR click "❌ Reject" - stores negative feedback
6. Check `backend/memory_store/feedback.jsonl` - feedback saved
7. Negative feedback updates `patterns.json`

**Expected:** All feedback stored, system learns from corrections

---

## Verification Checklist

After testing, verify these files exist and have content:

- [ ] `backend/memory_store/problems.jsonl` - Contains solved problems
- [ ] `backend/memory_store/feedback.jsonl` - Contains user feedback
- [ ] `backend/memory_store/patterns.json` - Contains learned patterns

Example `problems.jsonl` entry:
```json
{"id": "a1b2c3d4", "timestamp": "2025-12-18T10:30:00", "problem_text": "A bag contains...", "topic": "Probability", ...}
```

Example `patterns.json`:
```json
{
  "Probability": {
    "common_mistakes": [],
    "correction_count": 2
  },
  "ocr_corrections": {
    "probabIlity": "probability"
  }
}
```

---

## Backend Logs to Watch

When testing, watch terminal for these log messages:

```
Memory Service: Applied known corrections
Memory Service: Found similar problems: 2
Memory Service: Retrieved solution patterns: 3
HITL Triggered: Low OCR confidence
HITL Triggered: Parser detected ambiguity
HITL Triggered: Verifier detected errors
```

---

## Troubleshooting

### HITL not triggering?
- Check confidence thresholds: OCR/ASR must be < 0.6
- Check verifier confidence: Must be < 0.6 or is_correct = false
- Try manual trigger: Click "🔍 Request Re-check"

### Memory not finding similar problems?
- Solve at least 2 problems with same topic
- Ensure problems have similar structure
- Check `problems.jsonl` exists and has entries

### Corrections not applying?
- Verify `patterns.json` has `ocr_corrections` section
- Ensure exact match of wrong text
- Restart backend after editing patterns.json

---

## Success Criteria ✅

✅ HITL panel appears when confidence < 60%  
✅ HITL panel appears when parser ambiguous  
✅ HITL panel appears when verifier fails  
✅ Manual review button works  
✅ Human can edit and approve/reject  
✅ Pipeline stops during HITL, resumes after approval  
✅ Similar problems found in memory  
✅ Solution patterns retrieved  
✅ OCR corrections applied automatically  
✅ Feedback stored in memory files  
✅ System learns from human corrections  

---

## Done! 🎉

Your MathMentor now has:
- **Human-in-the-Loop (HITL)** - 5 trigger conditions, full UI control
- **Memory & Self-Learning** - Pattern storage, retrieval, and reuse
- **No Model Retraining** - All learning is pattern-based

The system is **production-ready** for your assignment demo! 🚀
