# Smart Chunking Quick Reference

## 🎯 What Was Implemented

**Document-type-aware chunking** for math RAG with 5 chunk types:

| Type | What | Size | Count |
|------|------|------|-------|
| **formula** | One formula per chunk | 30-80 tokens | 161 |
| **example** | Problem + solution together | 150-300 tokens | 71 |
| **definition** | Definition + formula | 80-150 tokens | 0* |
| **procedure** | Step-by-step methods | 80-200 tokens | 0* |
| **pitfall** | Common mistakes | 50-150 tokens | 0* |

*These types will be extracted once you add them to markdown files

## 📊 Current Stats

- **Total chunks:** 232
- **Files processed:** 4 markdown files
- **Average chunk size:** 216 characters
- **Formula chunks:** 69.4%
- **Example chunks:** 30.6%

## 🚀 Quick Start

### 1. Build Pinecone Index
```bash
cd backend
python scripts/build_rag_index.py
```

### 2. Query in Code
```python
from services.rag_service import RAGService

rag = RAGService()

# Get formulas only
formulas = rag.retrieve("derivative", type_filter="formula")

# Get examples only
examples = rag.retrieve("matrix problem", type_filter="example")

# Agent-specific retrieval
solver_context = rag.retrieve_by_agent_role(
    "solve this problem",
    agent_role="solver"  # gets procedures + formulas
)
```

## 📋 Metadata Schema

Every chunk has:
```json
{
  "text": "content",
  "type": "formula|example|definition|procedure|pitfall",
  "topic": "algebra|calculus|probability",
  "subtopic": "specific topic",
  "source": "filename",
  "difficulty": "basic|jee_basic|jee_advanced",
  "pattern": "limit|derivative|matrix|..." 
}
```

## 🔍 Agent-Role Retrieval

| Agent | Gets | Why |
|-------|------|-----|
| **solver** | procedures + formulas | Needs actionable methods |
| **explainer** | examples + definitions | Needs teaching material |
| **verifier** | pitfalls + formulas | Needs error detection |

## ✅ Advantages

1. **Clean formulas** - No surrounding noise
2. **Complete examples** - Problem + solution together
3. **Smart filtering** - By type, topic, difficulty, pattern
4. **Agent-optimized** - Different content for different roles
5. **No overlap** - Math chunks are semantically complete

## 📁 Files

- **Chunker:** `services/smart_chunker.py`
- **RAG:** `services/rag_service.py`
- **Builder:** `scripts/build_rag_index.py`
- **Docs:** `SMART_CHUNKING_GUIDE.md`

## 🎯 Next Steps

1. Set PINECONE_API_KEY environment variable
2. Run `python scripts/build_rag_index.py`
3. Test retrieval quality
4. Integrate with agents

---

**Ready to upsert to Pinecone!** 🚀
