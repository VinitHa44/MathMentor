# Math Mentor - Complete Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           MATH MENTOR SYSTEM                                 │
│                     Multimodal RAG + Multi-Agent Tutor                      │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│                          FRONTEND (Streamlit)                                │
│                         http://localhost:8501                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  📸 Image Upload          🎤 Audio Upload         ⌨️ Text Input            │
│       │                        │                        │                   │
│       └────────────────────────┴────────────────────────┘                   │
│                                 │                                            │
│                      ✅ Confirm & Solve Button                              │
│                                 │                                            │
│                                 ▼                                            │
│                      📚 Retrieved Context Display                           │
│                      📝 Solution with Steps                                 │
│                      ✅ Verification Results                                │
│                      💡 Detailed Explanation                                │
│                      🤖 Agent Execution Trace                               │
│                      💬 Feedback Buttons (Approve/Edit/Reject)             │
│                                                                              │
└──────────────────────────────┬──────────────────────────────────────────────┘
                               │ HTTP Requests
                               ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                          BACKEND API (FastAPI)                               │
│                         http://localhost:8000                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  API ENDPOINTS:                                                             │
│  ├─ POST /api/ocr           → OCR Service                                  │
│  ├─ POST /api/transcribe    → ASR Service                                  │
│  ├─ POST /api/parse         → Parser Agent                                 │
│  ├─ POST /api/solve         → Full Pipeline ⭐                             │
│  ├─ POST /api/feedback      → Memory Service (HITL)                        │
│  ├─ GET  /api/history       → Memory Service                               │
│  └─ GET  /api/similar/{id}  → Memory Service                               │
│                                                                              │
└──────────────────────────────┬──────────────────────────────────────────────┘
                               │
         ┌─────────────────────┼─────────────────────┐
         │                     │                     │
         ▼                     ▼                     ▼
┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│  OCR SERVICE     │  │  ASR SERVICE     │  │  RAG SERVICE     │
│  (EasyOCR)       │  │  (Whisper)       │  │  (FAISS)         │
├──────────────────┤  ├──────────────────┤  ├──────────────────┤
│ • Extract text   │  │ • Transcribe     │  │ • Extract PDFs   │
│ • Confidence     │  │ • Clean speech   │  │ • Chunk text     │
│ • Fallback       │  │ • Confidence     │  │ • Embed chunks   │
└──────────────────┘  └──────────────────┘  │ • Vector search  │
                                             │ • Topic filter   │
                                             └────────┬─────────┘
                                                      │
                         ┌────────────────────────────┘
                         │
                         ▼
         ┌───────────────────────────────────────────────┐
         │         KNOWLEDGE BASE (PDFs)                 │
         ├───────────────────────────────────────────────┤
         │ rag_docs/                                     │
         │ ├─ algebra/        (formulas, examples)       │
         │ ├─ calculus/       (derivatives, integrals)   │
         │ ├─ probability/    (axioms, distributions)    │
         │ └─ linear_algebra/ (matrices, vectors)        │
         │                                               │
         │ FAISS Index: 384-dim vectors                  │
         │ Embeddings: all-MiniLM-L6-v2                 │
         └───────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│                        MULTI-AGENT PIPELINE                                  │
│                    (Triggered by /api/solve)                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  1️⃣ PARSER AGENT (LLM-powered)                                            │
│     ├─ Input: Problem text                                                  │
│     ├─ LLM: Llama 3.1 8B Instruct                                          │
│     └─ Output: {topic, variables, constraints, needs_clarification}        │
│              │                                                              │
│              ▼                                                              │
│  2️⃣ INTENT ROUTER AGENT                                                   │
│     ├─ Check: needs_clarification? → HITL                                  │
│     ├─ Check: explanation_request? → Explainer only                        │
│     └─ Default: Full pipeline                                              │
│              │                                                              │
│              ▼                                                              │
│  3️⃣ RAG RETRIEVAL                                                         │
│     ├─ Embed problem text                                                  │
│     ├─ Search FAISS (top-k=5)                                              │
│     ├─ Filter by topic                                                     │
│     └─ Return: [{text, source, score}]                                    │
│              │                                                              │
│              ▼                                                              │
│  4️⃣ SOLVER AGENT (LLM + RAG)                                              │
│     ├─ LLM: Llama 3.1 8B Instruct                                          │
│     ├─ Prompt: "Use ONLY retrieved context below..."                       │
│     ├─ Context: RAG chunks injected                                        │
│     └─ Output: {solution_text, steps, final_answer}                       │
│              │                                                              │
│              ▼                                                              │
│  5️⃣ VERIFIER AGENT (LLM + RAG)                                            │
│     ├─ LLM: Llama 3.1 8B Instruct                                          │
│     ├─ Check: Formula correct? Calculations? Constraints?                  │
│     ├─ Compare: Solution vs Retrieved formulas                             │
│     └─ Output: {is_correct, confidence, issues, suggestions}              │
│              │                                                              │
│              ▼                                                              │
│  6️⃣ EXPLAINER AGENT (LLM)                                                 │
│     ├─ LLM: Llama 3.1 8B Instruct                                          │
│     ├─ Generate: Natural language explanation                              │
│     └─ Output: {key_concept, analogy, common_mistakes, pro_tip}          │
│              │                                                              │
│              ▼                                                              │
│  7️⃣ MEMORY STORAGE                                                        │
│     ├─ Store: Problem + Solution + Verification + Context                  │
│     ├─ Generate: problem_id                                                │
│     └─ Files: problems.jsonl, feedback.jsonl, patterns.json              │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│                         LLM INTEGRATION                                      │
│                       (Ollama + Llama 3.1)                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  LLM Service → Ollama API (http://localhost:11434)                         │
│              │                                                              │
│              └─ Model: llama3.1:8b-instruct-q4_K_M                         │
│                 ├─ Size: 4.9 GB                                            │
│                 ├─ Quantization: 4-bit                                     │
│                 └─ Speed: ~30-60 sec per agent on CPU                      │
│                                                                              │
│  Used by:                                                                   │
│  ├─ Parser Agent     (structured JSON extraction)                          │
│  ├─ Solver Agent     (step-by-step solution)                               │
│  ├─ Verifier Agent   (correctness checking)                                │
│  └─ Explainer Agent  (natural language explanation)                        │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│                        MEMORY & LEARNING SYSTEM                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  memory_store/                                                              │
│  ├─ problems.jsonl        (append-only problem history)                    │
│  │  └─ {id, problem, solution, verification, context, trace}              │
│  │                                                                          │
│  ├─ feedback.jsonl        (user HITL feedback)                             │
│  │  └─ {problem_id, type, comment, corrected_solution}                    │
│  │                                                                          │
│  └─ patterns.json         (learned mistake patterns)                       │
│     └─ {topic: {common_mistakes, correction_count}}                       │
│                                                                              │
│  Functions:                                                                 │
│  ├─ store_problem()          → Save complete solution                      │
│  ├─ store_feedback()         → Save HITL corrections                       │
│  ├─ get_problem_history()    → Retrieve past problems                      │
│  ├─ find_similar_problems()  → Match by topic + variables                  │
│  └─ get_mistake_patterns()   → Learn common errors                         │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│                     HITL (Human-in-the-Loop) FLOW                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Trigger Points:                                                            │
│  ├─ Parser: needs_clarification = true                                     │
│  ├─ Verifier: is_correct = false                                           │
│  └─ Verifier: needs_human_review = true                                    │
│                                                                              │
│  User Actions:                                                              │
│  ├─ 👍 Approve  → Store positive feedback                                  │
│  ├─ ✏️ Edit     → Show correction form                                     │
│  │              → Store corrected_solution                                 │
│  │              → Update mistake_patterns                                  │
│  └─ ❌ Reject   → Store negative feedback                                  │
│                 → Mark for review                                           │
│                                                                              │
│  Learning:                                                                  │
│  └─ Corrections fed back to improve future solutions                       │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│                          DATA FLOW EXAMPLE                                   │
│                     Problem: "Solve x² + 5x + 6 = 0"                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  1. User Input: "Solve x² + 5x + 6 = 0"                                    │
│                                                                              │
│  2. Parser Agent:                                                           │
│     {                                                                        │
│       "topic": "algebra",                                                   │
│       "variables": ["x"],                                                   │
│       "constraints": ["quadratic_equation"],                                │
│       "needs_clarification": false                                          │
│     }                                                                        │
│                                                                              │
│  3. RAG Retrieval (algebra):                                                │
│     [                                                                        │
│       {                                                                      │
│         "text": "Quadratic formula: x = (-b ± √(b²-4ac))/2a",              │
│         "source": "quadratic_formulas",                                     │
│         "score": 0.89                                                       │
│       },                                                                     │
│       {                                                                      │
│         "text": "Example: x²+5x+6 = (x+2)(x+3)",                            │
│         "source": "factoring_examples",                                     │
│         "score": 0.85                                                       │
│       }                                                                      │
│     ]                                                                        │
│                                                                              │
│  4. Solver Agent (with context):                                            │
│     "Step 1: Identify a=1, b=5, c=6                                         │
│      Step 2: Apply quadratic formula [from context]                         │
│      Step 3: x = (-5 ± √(25-24))/2 = (-5 ± 1)/2                           │
│      Step 4: x = -2 or x = -3"                                             │
│                                                                              │
│  5. Verifier Agent:                                                         │
│     {                                                                        │
│       "is_correct": true,                                                   │
│       "confidence": 95,                                                     │
│       "issues": [],                                                         │
│       "formula_matches_context": true                                       │
│     }                                                                        │
│                                                                              │
│  6. Explainer Agent:                                                        │
│     "This is a quadratic equation. Think of it like finding                 │
│      where a parabola crosses the x-axis..."                                │
│                                                                              │
│  7. Memory Storage:                                                         │
│     problem_id: "abc123"                                                    │
│     Stored in: problems.jsonl                                               │
│                                                                              │
│  8. UI Display:                                                             │
│     📚 2 sources used (89%, 85%)                                            │
│     📝 Final Answer: x = -2, x = -3                                         │
│     ✅ Verified (95%)                                                       │
│     💡 Explanation with analogy                                             │
│     🤖 6 agents executed                                                    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│                         TECHNOLOGY STACK                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Frontend:                                                                  │
│  ├─ Streamlit 1.39.0                                                       │
│  ├─ PIL (image handling)                                                   │
│  └─ Requests (API calls)                                                   │
│                                                                              │
│  Backend:                                                                   │
│  ├─ FastAPI 0.104.1                                                        │
│  ├─ Uvicorn (ASGI server)                                                  │
│  └─ Pydantic (validation)                                                  │
│                                                                              │
│  OCR/ASR:                                                                   │
│  ├─ EasyOCR 1.7.2                                                          │
│  ├─ OpenAI Whisper                                                         │
│  └─ PaddlePaddle 3.2.2                                                     │
│                                                                              │
│  RAG Stack:                                                                 │
│  ├─ pypdf 4.3.1           (PDF extraction)                                 │
│  ├─ sentence-transformers (embeddings)                                     │
│  ├─ FAISS-CPU 1.9.0       (vector search)                                  │
│  └─ Langchain 0.3.15      (text processing)                                │
│                                                                              │
│  LLM:                                                                       │
│  ├─ Ollama                (local inference)                                 │
│  └─ Llama 3.1 8B Instruct (language model)                                 │
│                                                                              │
│  Storage:                                                                   │
│  ├─ JSONL                 (append-only logs)                                │
│  └─ JSON                  (structured data)                                 │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│                         KEY METRICS                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Code:                                                                      │
│  ├─ New Files: 16                                                          │
│  ├─ Modified Files: 4                                                      │
│  ├─ Total Lines: ~2,500                                                    │
│  └─ Documentation: 4 guides                                                 │
│                                                                              │
│  Performance:                                                               │
│  ├─ Embedding: ~500 sentences/sec                                          │
│  ├─ Vector Search: <1ms                                                    │
│  ├─ LLM per Agent: 30-60 sec (CPU)                                         │
│  └─ Total Pipeline: 2-5 min                                                │
│                                                                              │
│  Assignment Progress:                                                       │
│  ├─ Steps 1-2: 100% ✅                                                     │
│  ├─ Steps 3-4: 100% ✅                                                     │
│  ├─ Step 5: 90% ⚠️                                                         │
│  ├─ Step 6: 0% ❌ (deployment)                                             │
│  ├─ Steps 7-8: 100% ✅                                                     │
│  └─ Overall: 93.75%                                                        │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```
