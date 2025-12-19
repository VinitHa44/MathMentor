# 🧮 Math Mentor

> An intelligent, multimodal AI math tutor powered by RAG and multi-agent systems, designed for JEE-style math problems.

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.39+-red.svg)](https://streamlit.io/)

## 📋 Overview

Math Mentor is a comprehensive AI-powered math tutoring system that combines:
- **Multimodal Input**: Text, images (OCR), and audio (speech-to-text)
- **Multi-Agent Architecture**: Specialized agents for parsing, solving, verifying, and explaining
- **RAG Pipeline**: Retrieval-Augmented Generation for context-aware solutions
- **Human-in-the-Loop (HITL)**: Interactive feedback and correction system
- **Memory System**: Learning from past problems and user feedback

## ✨ Key Features

### 🎯 Multimodal Problem Input
- 📷 **Image OCR**: Upload photos or screenshots with text extraction (Tesseract, EasyOCR)
- 🎤 **Speech-to-Text**: Record or upload audio with Whisper transcription
- ⌨️ **Direct Text**: Traditional text input for math problems

### 🤖 AI-Powered Solution Engine
- **Multi-Agent System**: 5 specialized agents working collaboratively
  - Intent Router: Classifies problem type
  - Parser Agent: Extracts mathematical entities
  - Solver Agent: Generates step-by-step solutions
  - Verifier Agent: Validates correctness
  - Explainer Agent: Provides clear explanations
- **RAG Knowledge Base**: Retrieves relevant formulas, examples, and solution templates
- **Symbolic Math**: SymPy integration for algebraic manipulation

### 🔄 Human-in-the-Loop
- Smart triggers for ambiguous or low-confidence problems
- Real-time feedback collection (correct/incorrect/clarify)
- Correction learning and memory updates
- Pattern recognition for similar problems

### 📊 Analytics & Memory
- Complete interaction history tracking
- Accuracy metrics and performance statistics
- Problem pattern recognition
- JSON export capabilities

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        Frontend (Streamlit)                  │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │  Image   │  │  Audio   │  │   Text   │  │ Feedback │   │
│  │  Upload  │  │  Upload  │  │  Input   │  │  System  │   │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘   │
└───────┼─────────────┼─────────────┼─────────────┼──────────┘
        │             │             │             │
        │    REST API (FastAPI)     │             │
        ▼             ▼             ▼             ▼
┌─────────────────────────────────────────────────────────────┐
│                     Backend Services                         │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │   OCR    │  │   ASR    │  │   RAG    │  │  Memory  │   │
│  │ Service  │  │ Service  │  │ Service  │  │ Service  │   │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘   │
└───────┼─────────────┼─────────────┼─────────────┼──────────┘
        │             │             │             │
        └─────────────┴─────────────┴─────────────┘
                          ▼
        ┌─────────────────────────────────────────┐
        │          Multi-Agent System              │
        │  ┌────────────────────────────────────┐ │
        │  │  Intent Router → Parser → Solver  │ │
        │  │  → Verifier → Explainer            │ │
        │  └────────────────────────────────────┘ │
        └─────────────────────────────────────────┘
                          ▼
        ┌─────────────────────────────────────────┐
        │      LLM Backends (Ollama)       │
        │      Vector DB (Pinecone)         │
        └─────────────────────────────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- **Python**: 3.9 or higher
- **Tesseract OCR**: For image text extraction
- **FFmpeg**: For audio processing
- **Ollama** (optional): For local LLM inference

### Installation

1. **Clone the repository**:
```bash
git clone <repository-url>
cd MathMentor
```

2. **Create virtual environment**:
```bash
python -m venv venv

# Windows
.\venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Install system dependencies**:

**Windows:**
- [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki)
- [FFmpeg](https://ffmpeg.org/download.html)

**Linux:**
```bash
sudo apt-get install tesseract-ocr ffmpeg
```

**Mac:**
```bash
brew install tesseract ffmpeg
```

5. **Configure environment variables**:
```bash
# Create .env file at root
PINECONE_API_KEY=your_pinecone_key
COHERE_API_KEY=your_cohere_key
GROQ_API_KEY=your_groq_key  # For LLM inference
NO_PROXY=localhost,127.0.0.1
```

**Get free API keys:**
- Pinecone: https://app.pinecone.io/ (vector database for RAG)
- Cohere: https://dashboard.cohere.com/api-keys (embeddings for RAG)
- Groq: https://console.groq.com/keys (fast LLM inference)

### Running the Application

#### Option 1: Run Both Services

```bash
# Terminal 1 - Start Backend
cd backend
python main.py
# Backend runs on http://localhost:8000

# Terminal 2 - Start Frontend
cd frontend
streamlit run app.py
# Frontend runs on http://localhost:8501
```

#### Option 2: Use PowerShell Scripts

```bash
# Frontend
cd frontend
.\start.ps1

# Backend
cd backend
python main.py
```

### First-Time Setup

1. **Build Pinecone RAG Index** (Required for full functionality):
   
   The system includes 43+ curated markdown files with math examples, formulas, and solutions. To enable RAG-powered context retrieval:
   
   ```bash
   # Navigate to backend directory
   cd backend
   
   # Build and upload index to Pinecone
   python scripts/build_rag_index.py
   ```
   
   This will:
   - Process all markdown files in `rag_docs/` (algebra, calculus, probability)
   - Create smart chunks (formulas, examples, definitions)
   - Generate embeddings using Cohere API (free tier)
   - Upload to Pinecone vector database
   
   **Note**: You need `PINECONE_API_KEY` and `COHERE_API_KEY` in your `.env` file. The script takes 2-5 minutes to complete.

2. **Add custom RAG documents** (optional):
   - Add your own markdown (.md) or PDF files to `backend/rag_docs/` organized by topic folders
   - Markdown is preferred for better quality chunking
   - Rerun `python scripts/build_rag_index.py` to rebuild the index

## 📁 Project Structure

```
MathMentor/
├── backend/                    # FastAPI backend
│   ├── main.py                # API entry point
│   ├── agents/                # Multi-agent system
│   │   ├── intent_router_agent.py
│   │   ├── parser_agent.py
│   │   ├── solver_agent.py
│   │   ├── verifier_agent.py
│   │   └── explainer_agent.py
│   ├── controllers/           # API controllers
│   ├── routes/                # API endpoints
│   ├── services/              # Core services
│   │   ├── asr_service.py    # Speech-to-text
│   │   ├── ocr_service.py    # Image text extraction
│   │   ├── llm_service.py    # LLM integration
│   │   ├── rag_service.py    # RAG pipeline
│   │   └── memory_service.py # Learning system
│   ├── usecases/              # Business logic
│   ├── repositories/          # Data access
│   ├── schemas/               # Pydantic models
│   ├── rag_docs/              # Knowledge base PDFs
│   ├── memory_store/          # Persistent storage
│   └── logs/                  # Application logs
│
├── frontend/                  # Streamlit frontend
│   ├── app.py                 # Main application
│   ├── config.py              # Configuration
│   ├── components/            # UI components
│   │   ├── ui_components.py
│   │   └── styles.py
│   └── pages/                 # Multi-page sections
│
├── .env                       # Environment variables
├── .gitignore                # Git ignore rules
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## 🛠️ Technology Stack

### Backend
- **FastAPI**: High-performance async API framework
- **Ollama**: LLM inference backends
- **Pinecone**: Vector database for RAG
- **SymPy**: Symbolic mathematics engine
- **Tesseract/EasyOCR**: OCR engines
- **Whisper**: Speech-to-text transcription

### Frontend
- **Streamlit**: Interactive web interface
- **Pillow**: Image processing
- **audio-recorder-streamlit**: Audio capture
- **Pandas**: Data visualization

### Storage & Memory
- **JSON Lines**: Problem/feedback storage
- **Vector Embeddings**: Semantic search
- **Pattern Matching**: Solution templates

## 📚 API Documentation

Once the backend is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Key Endpoints

```
POST /ocr/extract          - Extract text from images
POST /asr/transcribe       - Transcribe audio to text
POST /parse                - Parse mathematical expressions
POST /solve                - Solve math problems (main endpoint)
POST /feedback             - Submit solution feedback
GET  /history              - Retrieve problem history
GET  /health               - Health check
```

## 🎓 Usage Examples

### Basic Problem Solving
```python
import requests

response = requests.post('http://localhost:8000/solve', json={
    "problem": "Solve the quadratic equation x² - 5x + 6 = 0",
    "settings": {
        "model": "llama3",
        "topic_filter": "algebra",
        "difficulty": "medium"
    }
})

solution = response.json()
print(solution['solution']['steps'])
```

### Image Upload (OCR)
1. Upload image via frontend
2. Review extracted text
3. Click "Solve Problem"
4. View solution with agent trace

### Audio Upload (ASR)
1. Record or upload audio file
2. Review transcription
3. Edit if needed
4. Submit for solving

## 🔧 Configuration

### Backend Configuration
Edit `backend/.env`:
```env
PINECONE_API_KEY=your_key_here
LLM_PROVIDER=ollama  # or openai
OLLAMA_BASE_URL=http://localhost:11434
```

### Frontend Configuration
Edit `frontend/config.py`:
```python
API_BASE_URL = "http://localhost:8000"
MAX_FILE_SIZE_MB = 10
OCR_CONFIDENCE_THRESHOLD = 0.85
ASR_CONFIDENCE_THRESHOLD = 0.80
```

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request


## 📝 License

This project is licensed under the MIT License.

## 📧 Contact

For questions or support, please open an issue on GitHub.

---

Made with ❤️ for better math education
