# Smart Chunking Implementation Guide

## Overview

This implementation uses **document-type-aware chunking** for optimal RAG performance in math tutoring. Different content types (formulas, definitions, examples, procedures, pitfalls) are chunked using specialized strategies.

## Key Features

### ✅ Implemented Chunking Strategies

#### 1️⃣ Formula Chunking
**Strategy:** One formula per chunk with minimal context

**Example Output:**
```
Formula: Definition of Derivative

$$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$

Meaning: The derivative exists at x if the limit exists.
```

**Metadata:**
```json
{
  "type": "formula",
  "topic": "calculus",
  "subtopic": "derivative",
  "source": "limits_derivatives_examples",
  "difficulty": "basic"
}
```

**Token Range:** 30-80 tokens

---

#### 2️⃣ Definition Chunking
**Strategy:** Definition + formula together (never separated)

**Example Output:**
```
Concept: Conditional Probability

The conditional probability of B given A is defined as:

P(B|A) = P(A ∩ B) / P(A)

This is used when probability is restricted to outcomes in A.
```

**Metadata:**
```json
{
  "type": "definition",
  "topic": "probability",
  "subtopic": "conditional_probability",
  "source": "probability_examples"
}
```

**Token Range:** 80-150 tokens

---

#### 3️⃣ Example Chunking (MOST IMPORTANT)
**Strategy:** Problem + full solution in ONE chunk

**Example Output:**
```
Example 5: Conditional Probability

Problem:
In a class of 30 students, 18 play soccer and 12 play basketball. 
8 students play both. What is P(basketball | soccer)?

Solution:
P(B|S) = P(B ∩ S) / P(S)
P(B ∩ S) = 8/30
P(S) = 18/30
P(B|S) = (8/30) / (18/30) = 8/18 = 4/9

Answer: 4/9
```

**Metadata:**
```json
{
  "type": "example",
  "topic": "probability",
  "subtopic": "Conditional Probability",
  "pattern": "conditional_probability",
  "source": "probability_examples",
  "difficulty": "jee_basic",
  "example_num": 5
}
```

**Token Range:** 150-300 tokens

---

#### 4️⃣ Procedure Chunking
**Strategy:** One complete procedure per chunk

**Example Output:**
```
Procedure: Solving Conditional Probability Problems

1. Identify the conditioned event (the "given" event)
2. Count total outcomes in the conditioned set
3. Count favorable outcomes in the intersection
4. Compute P(A|B) = |A ∩ B| / |B|
```

**Metadata:**
```json
{
  "type": "procedure",
  "topic": "probability",
  "subtopic": "conditional_probability",
  "source": "probability_examples"
}
```

**Token Range:** 80-200 tokens

---

#### 5️⃣ Pitfall Chunking
**Strategy:** Each common mistake = one chunk

**Example Output:**
```
Common Mistake: Using total sample space in denominator

Wrong:
P(B|A) = |A ∩ B| / |Total|

Correct:
P(B|A) = |A ∩ B| / |A|

Why: Conditional probability restricts to event A only.
```

**Metadata:**
```json
{
  "type": "pitfall",
  "topic": "probability",
  "subtopic": "conditional_probability",
  "source": "probability_examples"
}
```

---

## Chunking Statistics

After running `build_rag_index.py`, you'll see:

```
============================================================
Chunking Summary:
============================================================
Total chunks: 285
Average length: 245 characters

By type:
  formula: 68
  definition: 12
  example: 150
  procedure: 8
  pitfall: 5

By topic:
  calculus: 95
  probability: 80
  algebra: 110
============================================================
```

---

## Metadata-Driven Retrieval

### Basic Retrieval
```python
# General retrieval
results = rag_service.retrieve("how to find derivative", top_k=5)

# Filter by topic
results = rag_service.retrieve("quadratic equation", 
                                topic_filter="algebra")

# Filter by type
results = rag_service.retrieve("derivative formula", 
                                type_filter="formula")

# Filter by difficulty
results = rag_service.retrieve("complex limit", 
                                difficulty_filter="jee_advanced")

# Filter by pattern
results = rag_service.retrieve("conditional probability", 
                                pattern_filter="conditional_probability")
```

### Hybrid Retrieval by Agent Role

```python
# Solver agent (prefers procedures + formulas)
results = rag_service.retrieve_by_agent_role(
    "solve derivative problem", 
    agent_role="solver"
)

# Explainer agent (prefers examples + definitions)
results = rag_service.retrieve_by_agent_role(
    "explain derivatives", 
    agent_role="explainer"
)

# Verifier agent (prefers pitfalls + formulas)
results = rag_service.retrieve_by_agent_role(
    "check derivative solution", 
    agent_role="verifier"
)
```

---

## Chunk Size Guidelines

| Content Type | Ideal Size | Overlap |
|-------------|-----------|---------|
| Formula | 30–80 tokens | 0 |
| Definition | 80–150 tokens | 0 |
| Example | 150–300 tokens | 0 |
| Procedure | 80–200 tokens | 0 |
| Pitfall | 50–150 tokens | 0 |

**Note:** Math content doesn't need overlap like general text because each chunk is semantically complete.

---

## What NOT to Do ❌

1. ❌ **Don't chunk PDFs blindly** - Use structured markdown files
2. ❌ **Don't mix topics** - Keep calculus and probability separate
3. ❌ **Don't split formulas** - One formula = one chunk
4. ❌ **Don't separate problem from solution** - Keep together
5. ❌ **Don't use fixed 500-token chunks** - Use content-aware boundaries
6. ❌ **Don't store OCR-garbled math** - Clean markdown only
7. ❌ **Don't skip metadata** - Every chunk must have metadata

---

## File Structure

```
backend/
├── services/
│   ├── smart_chunker.py      # Smart chunking logic
│   └── rag_service.py         # Updated RAG service
├── scripts/
│   └── build_rag_index.py     # Index builder script
└── rag_docs/
    ├── algebra/
    │   ├── quadratic_equations_examples.md
    │   └── matrices_linear_algebra_50examples.md
    ├── calculus/
    │   └── limits_derivatives_examples.md
    └── probability/
        ├── probability_examples.md
        └── statistics_examples.md
```

---

## Usage

### 1. Build Index

```bash
cd backend
python scripts/build_rag_index.py
```

### 2. Query in Code

```python
from services.rag_service import RAGService

# Initialize
rag = RAGService()

# Basic query
results = rag.retrieve("what is derivative")

# Agent-specific query
results = rag.retrieve_by_agent_role(
    "solve this limit problem",
    agent_role="solver"
)

# Print results
for result in results:
    print(f"Type: {result['metadata']['type']}")
    print(f"Text: {result['text'][:100]}...")
    print(f"Score: {result['score']}")
    print()
```

---

## Advantages of This Approach

### 🎯 Better Retrieval Quality
- Formulas retrieved cleanly (no surrounding noise)
- Examples include full solutions (no partial retrievals)
- Definitions include their formulas (context preserved)

### 🚀 Agent-Specific Optimization
- Solver gets procedures and formulas
- Explainer gets examples and definitions
- Verifier gets pitfalls and formulas

### 📊 Metadata Filtering
- Filter by topic, difficulty, pattern, type
- Enables precise retrieval
- Reduces hallucinations

### 🔧 Maintainable
- Clear chunk types
- Standardized metadata
- Easy to debug retrieval issues

---

## Pattern Recognition

The chunker automatically identifies patterns:

| Pattern | Keywords |
|---------|----------|
| limit | "limit", "lim" |
| derivative | "derivative", "differentiation" |
| conditional_probability | "conditional", "given" |
| matrix | "matrix", "determinant" |
| quadratic | "quadratic", "parabola" |
| vector | "vector", "dot product" |

These patterns enable retrieval like:
```python
results = rag.retrieve(
    "probability problem",
    pattern_filter="conditional_probability"
)
```

---

## Next Steps

1. ✅ Smart chunking implemented
2. ⏭️ Expand markdown files to 50 examples each
3. ⏭️ Build Pinecone index
4. ⏭️ Test retrieval quality
5. ⏭️ Integrate with agents

---

## Troubleshooting

### No chunks found?
- Check that markdown files are in `rag_docs/<topic>/`
- Ensure files follow the example format with `## Example N:` headings

### Formulas not extracting?
- Use LaTeX notation: `$$formula$$`
- Label formulas: `Formula: Name`

### Examples incomplete?
- Ensure `**Problem:**` and `**Solution:**` markers are present
- Keep example structure consistent

---

## References

- Markdown files: `backend/rag_docs/`
- Chunker implementation: `backend/services/smart_chunker.py`
- RAG service: `backend/services/rag_service.py`
- Build script: `backend/scripts/build_rag_index.py`
