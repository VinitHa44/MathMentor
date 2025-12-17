# 🧮 Math Mentor - Frontend

A comprehensive Streamlit-based frontend for the Math Mentor AI application - your intelligent math tutor for JEE-style problems.

## ✨ Features

### Multimodal Input
- 📷 **Image Input**: Upload photos/screenshots with OCR text extraction
- 🎤 **Audio Input**: Record or upload audio with speech-to-text transcription
- ⌨️ **Text Input**: Direct text input for math problems

### AI-Powered Solving
- 🤖 **Multi-Agent System**: 5+ specialized agents working together
- 🔍 **RAG Pipeline**: Knowledge retrieval from curated math resources
- ✅ **Solution Verification**: Automated correctness checking
- 📖 **Step-by-Step Explanations**: Clear, detailed solution breakdowns

### Human-in-the-Loop (HITL)
- ✋ **Smart Triggers**: Activates when confidence is low or ambiguity detected
- 💬 **Feedback System**: Correct, incorrect, or request clarification
- 🔄 **Correction Learning**: System learns from human corrections

### Memory & Learning
- 📚 **History Tracking**: All interactions saved with feedback
- 🧠 **Pattern Reuse**: Similar problem detection and solution templates
- 📊 **Analytics**: Accuracy metrics and performance stats
- 💾 **Export**: Download history as JSON

## 🚀 Quick Start

### Prerequisites
- Python 3.9 or higher
- pip package manager

### Installation

1. **Clone the repository** (if not already done):
```bash
cd d:\projects_current\MathMentor\frontend
```

2. **Create a virtual environment** (recommended):
```bash
python -m venv venv
```

3. **Activate the virtual environment**:

**Windows:**
```bash
.\venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

4. **Install dependencies**:
```bash
pip install -r requirements.txt
```

5. **Install Tesseract OCR** (required for image processing):

**Windows:**
- Download from: https://github.com/UB-Mannheim/tesseract/wiki
- Install and add to PATH

**Linux:**
```bash
sudo apt-get install tesseract-ocr
```

**Mac:**
```bash
brew install tesseract
```

### Running the Application

1. **Set environment variables** (optional):
```bash
# Windows PowerShell
$env:API_BASE_URL="http://localhost:8000"

# Linux/Mac
export API_BASE_URL="http://localhost:8000"
```

2. **Start the Streamlit app**:
```bash
streamlit run app.py
```

3. **Open in browser**:
The app will automatically open at `http://localhost:8501`

## 📁 Project Structure

```
frontend/
├── app.py                      # Main Streamlit application
├── config.py                   # Configuration settings
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── components/
│   ├── __init__.py
│   ├── ui_components.py        # Reusable UI components
│   └── styles.py               # Custom CSS styling
├── data/                       # Data storage (created at runtime)
│   └── memory/                 # Memory storage
└── logs/                       # Application logs (created at runtime)
```

## 🎨 UI Components

### Main Interface
- **Header**: App branding and title
- **Input Tabs**: Switch between Image/Audio/Text input modes
- **Extraction Preview**: Review OCR/ASR output before solving
- **Agent Trace**: Real-time agent workflow visualization
- **Solution Card**: Formatted solution with steps
- **Context Panel**: Retrieved RAG knowledge sources
- **Feedback Section**: User feedback buttons

### Sidebar
- **Settings**: Model selection, topic filter, difficulty level
- **Memory Toggle**: View history and statistics
- **Session Stats**: Problems solved, accuracy metrics
- **Reset**: Clear current session

## 🔧 Configuration

Edit `config.py` to customize:

```python
# API Configuration
API_BASE_URL = "http://localhost:8000"

# File Upload Limits
MAX_FILE_SIZE_MB = 10

# Confidence Thresholds
OCR_CONFIDENCE_THRESHOLD = 0.85
ASR_CONFIDENCE_THRESHOLD = 0.80

# RAG Settings
RAG_TOP_K = 5
RAG_SIMILARITY_THRESHOLD = 0.7
```

## 🎯 Usage Guide

### Solving a Problem from Image

1. Click the **📷 Image** tab
2. Upload a photo/screenshot of the math problem
3. Click **🔍 Extract Text from Image**
4. Review and edit the extracted text if needed
5. Click **✅ Confirm & Solve**
6. View the agent workflow and solution
7. Provide feedback: ✅ Correct / ❌ Incorrect / 🤔 Need Clarification

### Solving a Problem from Audio

1. Click the **🎤 Audio** tab
2. Choose "Record Audio" or "Upload Audio File"
3. Record/upload your math question
4. Click **🎯 Transcribe Audio**
5. Review the transcript
6. Click **✅ Confirm & Solve**
7. View solution and provide feedback

### Typing a Problem

1. Click the **⌨️ Text** tab
2. Type your math problem in the text area
3. Click **➡️ Submit Problem**
4. View solution and provide feedback

### Viewing History

1. Click **📚 View Memory & History** in sidebar
2. Review past problems and solutions
3. Filter by Correct/Corrected/Clarifications
4. Export history as JSON

## 🐛 Troubleshooting

### OCR Not Working
- Ensure Tesseract is installed and in PATH
- Check image quality (clear, good lighting, no glare)
- Try a different OCR provider in settings

### Audio Transcription Fails
- Check audio format (MP3, WAV supported)
- Ensure audio is clear with minimal background noise
- Verify microphone permissions

### Backend Connection Error
- Verify `API_BASE_URL` is correct
- Ensure backend server is running
- Check network connectivity

### Dependencies Installation Issues
```bash
# Upgrade pip first
pip install --upgrade pip

# Install dependencies one by one if batch fails
pip install streamlit
pip install Pillow
pip install pytesseract
# ... continue for each package
```

## 🌐 Deployment

### Streamlit Cloud

1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Set main file path: `frontend/app.py`
5. Add environment variables in Settings
6. Deploy!

### HuggingFace Spaces

1. Create new Space on HuggingFace
2. Select Streamlit SDK
3. Upload files or connect Git repo
4. Add `requirements.txt`
5. Space will auto-deploy

### Render / Railway

1. Create new Web Service
2. Connect GitHub repository
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `streamlit run app.py --server.port=$PORT`
5. Deploy!

## 📊 Features Checklist

- ✅ Multimodal Input (Image, Audio, Text)
- ✅ OCR with confidence indicators
- ✅ Speech-to-text transcription
- ✅ Parser Agent with structured output
- ✅ Multi-agent workflow visualization
- ✅ RAG context retrieval display
- ✅ Step-by-step solution rendering
- ✅ Confidence indicators
- ✅ HITL triggers and interface
- ✅ Feedback collection system
- ✅ Memory and history tracking
- ✅ Session statistics
- ✅ Export functionality
- ✅ Responsive design
- ✅ Custom styling

## 🎨 Customization

### Changing Colors
Edit `components/styles.py`:
```python
def get_color_palette():
    return {
        'primary': '#667eea',  # Change primary color
        'secondary': '#764ba2',
        # ... other colors
    }
```

### Adding New Topics
Edit `config.py`:
```python
MATH_TOPICS = [
    "Algebra",
    "Probability",
    "Your New Topic",  # Add here
]
```

### Modifying Agents
Edit `config.py`:
```python
AGENTS = [
    "Parser Agent",
    "Your New Agent",  # Add here
]
```

## 📝 API Integration

The frontend expects the backend API to have these endpoints:

```python
POST /ocr
    - Input: {"image": "base64_string"}
    - Output: {"text": "extracted_text", "confidence": 0.95}

POST /transcribe
    - Input: {"audio": "base64_string"}
    - Output: {"text": "transcribed_text", "confidence": 0.88}

POST /solve
    - Input: {"problem": "text", "settings": {...}}
    - Output: {"solution": {...}, "agent_trace": [...], "context": [...]}

POST /feedback
    - Input: {"problem_id": "...", "feedback": "correct", ...}
    - Output: {"status": "success"}
```

## 🤝 Contributing

Contributions are welcome! Areas for improvement:
- Real-time audio recording widget
- Advanced visualization for agent traces
- Math equation rendering (LaTeX support)
- Mobile optimization
- Dark mode theme
- Multi-language support

## 📄 License

This project is part of the Math Mentor AI Engineer Assignment.

## 🙋‍♂️ Support

For issues or questions:
1. Check the troubleshooting section
2. Review configuration settings
3. Check backend logs
4. Verify all dependencies are installed

## 🎓 Math Topics Supported

- ✅ Algebra (Equations, Polynomials, Inequalities)
- ✅ Probability (Basic & Conditional Probability)
- ✅ Calculus (Limits, Derivatives, Integration)
- ✅ Linear Algebra (Matrices, Vectors, Systems)

## 📈 Performance

- OCR Latency: ~2 seconds
- ASR Latency: ~3 seconds
- Solution Generation: ~10 seconds
- Target Accuracy: 90%+

## 🔒 Security Notes

- API keys should be stored in environment variables
- File uploads are validated for type and size
- User inputs are sanitized
- No sensitive data stored in frontend

---

**Built with ❤️ using Streamlit, RAG, and Multi-Agent AI**

*Math Mentor - Making JEE Math Learning Intelligent and Interactive*
