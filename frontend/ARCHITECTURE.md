# Math Mentor Frontend - Architecture Diagram

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     Math Mentor Frontend                         │
│                      (Streamlit App)                             │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│   📷 Image   │    │   🎤 Audio   │    │  ⌨️  Text    │
│    Input     │    │    Input     │    │   Input      │
└──────────────┘    └──────────────┘    └──────────────┘
        │                     │                     │
        │ OCR                 │ ASR                 │ Direct
        ▼                     ▼                     ▼
┌─────────────────────────────────────────────────────────┐
│              Text Extraction & Preview                   │
│         (with Confidence Indicators)                     │
└─────────────────────────────────────────────────────────┘
                              │
                              │ User Confirms
                              ▼
┌─────────────────────────────────────────────────────────┐
│                  Backend API Call                        │
│              POST /solve with problem                    │
└─────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────┐
│              Multi-Agent Workflow                        │
│  📝 Parser → 🧭 Router → 🔬 Solver → ✅ Verifier        │
│                    → 📚 Explainer                        │
└─────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────┐
│                  Solution Display                        │
│  • Agent Trace Visualization                            │
│  • Retrieved RAG Context                                 │
│  • Step-by-Step Solution                                 │
│  • Final Answer with Confidence                          │
└─────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────┐
│               Feedback & HITL System                     │
│  ✅ Correct  │  ❌ Incorrect  │  🤔 Clarification       │
└─────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────┐
│               Memory & History Storage                   │
│        (Session State + Backend Storage)                 │
└─────────────────────────────────────────────────────────┘
```

## Component Hierarchy

```
app.py (Main App)
├── Header
├── Sidebar
│   ├── Settings Panel
│   ├── Statistics Display
│   └── Action Buttons
│
├── Main Content
│   ├── Input Tabs
│   │   ├── Image Input Tab
│   │   │   ├── File Uploader
│   │   │   ├── Image Preview
│   │   │   └── Extract Button
│   │   │
│   │   ├── Audio Input Tab
│   │   │   ├── Record/Upload Toggle
│   │   │   ├── Audio Player
│   │   │   └── Transcribe Button
│   │   │
│   │   └── Text Input Tab
│   │       ├── Text Area
│   │       └── Submit Button
│   │
│   ├── Extraction Preview
│   │   ├── Confidence Indicator
│   │   ├── Editable Text Area
│   │   └── Confirm/Cancel Buttons
│   │
│   ├── Agent Workflow Panel
│   │   └── render_agent_trace()
│   │       ├── Agent Cards
│   │       └── Status Indicators
│   │
│   ├── Solution Display
│   │   ├── render_solution_card()
│   │   │   ├── Topic & Verification
│   │   │   ├── Confidence Indicator
│   │   │   ├── Final Answer Box
│   │   │   └── Step-by-Step Display
│   │   │
│   │   └── render_retrieved_context()
│   │       └── Context Cards
│   │
│   ├── Feedback Section
│   │   └── render_feedback_section()
│   │       └── Feedback Buttons
│   │
│   └── HITL Interface
│       └── render_hitl_interface()
│           ├── Issue Type Selection
│           ├── Correction Input
│           └── Submit Correction
│
└── Footer

pages/
├── 1_ℹ️_About.py
│   ├── System Overview
│   ├── Agent Details
│   ├── RAG Pipeline
│   └── Tech Stack
│
└── 2_⚙️_Settings.py
    ├── General Settings
    ├── Input Processing
    ├── RAG Configuration
    ├── Display Options
    └── Data Management
```

## Data Flow

```
User Input
    │
    ├─→ [Image] ─→ OCR ─→ Extracted Text
    │                          │
    ├─→ [Audio] ─→ ASR ─→ Transcribed Text
    │                          │
    └─→ [Text]  ────────────────┘
                                │
                                ▼
                        User Reviews & Edits
                                │
                                ▼
                        Confirmed Problem Text
                                │
                                ▼
                    ┌───────────────────────┐
                    │    Backend API        │
                    └───────────────────────┘
                                │
                    ┌───────────┴───────────┐
                    ▼                       ▼
            ┌─────────────┐         ┌─────────────┐
            │  RAG System │         │   Agents    │
            │  Retrieval  │         │  Pipeline   │
            └─────────────┘         └─────────────┘
                    │                       │
                    └───────────┬───────────┘
                                ▼
                        Solution Generated
                                │
                                ▼
                    ┌───────────────────────┐
                    │   Frontend Display    │
                    │  • Agent Trace        │
                    │  • RAG Context        │
                    │  • Solution Steps     │
                    │  • Final Answer       │
                    └───────────────────────┘
                                │
                                ▼
                        User Provides Feedback
                                │
                                ▼
                        Memory Storage
                                │
                                ▼
                        Learning & Improvement
```

## State Management

```
Session State Variables:
├── history: List[Dict]              # All past problems
├── current_problem: Optional[Dict]  # Active problem
├── extracted_text: str              # OCR/ASR output
├── ocr_confidence: float            # OCR confidence
├── asr_confidence: float            # ASR confidence
├── agent_trace: List[Dict]          # Agent execution log
├── solution: Optional[Dict]         # Current solution
├── hitl_required: bool              # HITL trigger flag
├── feedback_submitted: bool         # Feedback status
├── show_memory: bool                # Memory panel toggle
└── settings: Dict                   # User preferences
```

## API Integration Points

```
Frontend                Backend API
   │                        │
   ├─── POST /ocr ─────────→│
   │    {image: base64}     │
   │←── {text, confidence} ─┤
   │                        │
   ├─── POST /transcribe ──→│
   │    {audio: base64}     │
   │←── {text, confidence} ─┤
   │                        │
   ├─── POST /solve ───────→│
   │    {problem, settings} │
   │←── {solution, trace} ──┤
   │                        │
   └─── POST /feedback ────→│
        {feedback_data}     │
   ←─── {status} ───────────┘
```

## Deployment Architecture

```
                    Internet
                        │
                        ▼
            ┌───────────────────────┐
            │   Load Balancer       │
            │  (if applicable)      │
            └───────────────────────┘
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│  Frontend    │ │  Frontend    │ │  Frontend    │
│  Instance 1  │ │  Instance 2  │ │  Instance N  │
│  (Streamlit) │ │  (Streamlit) │ │  (Streamlit) │
└──────────────┘ └──────────────┘ └──────────────┘
        │               │               │
        └───────────────┼───────────────┘
                        │
                        ▼
            ┌───────────────────────┐
            │    Backend API        │
            │  (FastAPI/Flask)      │
            └───────────────────────┘
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│  Vector DB   │ │   LLM APIs   │ │  Memory DB   │
│  (FAISS)     │ │  (OpenAI)    │ │  (PostgreSQL)│
└──────────────┘ └──────────────┘ └──────────────┘
```

## Module Dependencies

```
app.py
├── components.ui_components
│   ├── render_confidence_indicator
│   ├── render_agent_trace
│   ├── render_retrieved_context
│   ├── render_solution_card
│   ├── render_feedback_section
│   ├── render_hitl_interface
│   └── render_memory_panel
│
├── components.styles
│   ├── apply_custom_styles
│   ├── get_color_palette
│   └── get_emoji_mapping
│
├── config
│   ├── API_BASE_URL
│   ├── SUPPORTED_FORMATS
│   ├── THRESHOLDS
│   └── SETTINGS
│
└── utils
    ├── encode_image_to_base64
    ├── clean_math_text
    ├── detect_math_topic
    └── sanitize_input
```

## Technology Stack Visualization

```
                    Math Mentor Frontend
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        ▼                   ▼                   ▼
    Frontend            Processing          Backend
        │                   │              Integration
        │                   │                   │
┌───────┴────────┐  ┌───────┴────────┐  ┌──────┴───────┐
│   Streamlit    │  │   Tesseract    │  │   REST API   │
│   Python 3.9+  │  │   Whisper      │  │   Requests   │
│   Pillow       │  │   OpenCV       │  │   HTTPX      │
│   Pandas       │  │   NumPy        │  │   JSON       │
└────────────────┘  └────────────────┘  └──────────────┘
```

This architecture provides a comprehensive, scalable, and maintainable solution for the Math Mentor frontend application.
