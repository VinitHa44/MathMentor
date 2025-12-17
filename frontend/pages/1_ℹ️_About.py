"""
About Page - Information about Math Mentor
"""

import streamlit as st
from components.styles import apply_custom_styles

st.set_page_config(
    page_title="About - Math Mentor",
    page_icon="ℹ️",
    layout="wide"
)

apply_custom_styles()

# Header
st.markdown("""
<div style='text-align: center; padding: 2rem 0;'>
    <h1 style='color: #1f77b4;'>ℹ️ About Math Mentor</h1>
    <p style='color: #666; font-size: 1.2rem;'>Your AI-Powered Math Tutor</p>
</div>
""", unsafe_allow_html=True)

# Overview
st.markdown("## 🎯 Overview")
st.markdown("""
Math Mentor is an advanced AI application designed to help students solve JEE-style math problems 
with step-by-step explanations. It combines cutting-edge technologies including:

- **RAG (Retrieval-Augmented Generation)** for knowledge retrieval
- **Multi-Agent Systems** for specialized problem-solving
- **Computer Vision** for image-based input
- **Speech Recognition** for audio input
- **Human-in-the-Loop** for continuous improvement
- **Memory Systems** for learning from past interactions
""")

# Architecture
st.markdown("## 🏗️ System Architecture")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### Frontend Components
    - **Streamlit UI**: Interactive web interface
    - **Multimodal Input**: Image, audio, and text support
    - **Real-time Visualization**: Agent workflow tracking
    - **Feedback System**: User interaction and corrections
    """)

with col2:
    st.markdown("""
    ### Backend Components
    - **RAG Pipeline**: Vector database and retrieval
    - **Agent Orchestration**: Multi-agent coordination
    - **LLM Integration**: GPT-4, Claude, Gemini
    - **Memory Store**: Historical data and learning
    """)

# Agent System
st.markdown("## 🤖 Multi-Agent System")

agents_info = [
    {
        "name": "Parser Agent",
        "emoji": "📝",
        "description": "Converts raw input into structured problem format",
        "responsibilities": [
            "Clean OCR/ASR output",
            "Identify problem components",
            "Detect ambiguities",
            "Structure problem data"
        ]
    },
    {
        "name": "Intent Router Agent",
        "emoji": "🧭",
        "description": "Classifies problem type and routes to appropriate solver",
        "responsibilities": [
            "Classify math topic",
            "Determine difficulty level",
            "Select solution strategy",
            "Route to specialized solver"
        ]
    },
    {
        "name": "Solver Agent",
        "emoji": "🔬",
        "description": "Solves the math problem using RAG and tools",
        "responsibilities": [
            "Retrieve relevant knowledge",
            "Apply mathematical methods",
            "Perform calculations",
            "Generate solution steps"
        ]
    },
    {
        "name": "Verifier Agent",
        "emoji": "✅",
        "description": "Validates solution correctness and completeness",
        "responsibilities": [
            "Check mathematical correctness",
            "Verify domain constraints",
            "Test edge cases",
            "Assess confidence level"
        ]
    },
    {
        "name": "Explainer Agent",
        "emoji": "📚",
        "description": "Creates clear, student-friendly explanations",
        "responsibilities": [
            "Format step-by-step solution",
            "Add intuitive explanations",
            "Include visual aids",
            "Highlight key concepts"
        ]
    }
]

for agent in agents_info:
    with st.expander(f"{agent['emoji']} **{agent['name']}**"):
        st.markdown(f"*{agent['description']}*")
        st.markdown("**Responsibilities:**")
        for resp in agent['responsibilities']:
            st.markdown(f"- {resp}")

# RAG System
st.markdown("## 🔍 RAG Pipeline")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### 1. Knowledge Base
    - Math formulas
    - Theorems & identities
    - Solution templates
    - Common mistakes
    - Problem-solving strategies
    """)

with col2:
    st.markdown("""
    ### 2. Retrieval
    - Semantic search
    - Vector embeddings
    - Similarity matching
    - Top-K selection
    - Relevance scoring
    """)

with col3:
    st.markdown("""
    ### 3. Generation
    - Context injection
    - Solution synthesis
    - Citation tracking
    - Hallucination prevention
    - Quality assurance
    """)

# HITL System
st.markdown("## ✋ Human-in-the-Loop")

st.markdown("""
The HITL system activates when:
- OCR/ASR confidence is below threshold (< 85%)
- Parser detects ambiguity in problem statement
- Verifier is uncertain about solution (< 75% confidence)
- User explicitly requests review or clarification

Human feedback is used to:
- ✅ Confirm correct solutions
- ❌ Identify incorrect solutions
- 🔄 Provide corrections
- 🤔 Request clarifications
- 📖 Improve future responses
""")

# Memory System
st.markdown("## 🧠 Memory & Learning")

st.markdown("""
The memory system stores:
- **Problem History**: All solved problems with metadata
- **Feedback Records**: User corrections and confirmations
- **Solution Patterns**: Successful solution strategies
- **Error Patterns**: Common mistakes and how to avoid them
- **OCR/ASR Corrections**: Text extraction improvements

This enables:
- Pattern recognition for similar problems
- Solution template reuse
- Improved OCR/ASR accuracy over time
- Personalized learning paths
""")

# Supported Topics
st.markdown("## 📐 Supported Math Topics")

topics = {
    "Algebra": [
        "Linear equations",
        "Quadratic equations",
        "Polynomials",
        "Inequalities",
        "Systems of equations"
    ],
    "Probability": [
        "Basic probability",
        "Conditional probability",
        "Permutations & combinations",
        "Random variables",
        "Distributions"
    ],
    "Calculus": [
        "Limits",
        "Derivatives",
        "Integration",
        "Optimization",
        "Applications"
    ],
    "Linear Algebra": [
        "Matrices",
        "Vectors",
        "Determinants",
        "Systems of linear equations",
        "Eigenvalues & eigenvectors"
    ]
}

cols = st.columns(2)
for idx, (topic, subtopics) in enumerate(topics.items()):
    with cols[idx % 2]:
        st.markdown(f"### {topic}")
        for subtopic in subtopics:
            st.markdown(f"- {subtopic}")

# Technologies
st.markdown("## 💻 Technologies Used")

tech_stack = {
    "Frontend": [
        "Streamlit",
        "Python",
        "Pillow (Image Processing)",
        "Requests (API Client)"
    ],
    "OCR": [
        "Tesseract",
        "PaddleOCR",
        "EasyOCR"
    ],
    "Speech Recognition": [
        "OpenAI Whisper",
        "Audio Processing Libraries"
    ],
    "AI Models": [
        "GPT-4 (OpenAI)",
        "Claude 3.5 (Anthropic)",
        "Gemini Pro (Google)"
    ],
    "Vector Databases": [
        "FAISS",
        "ChromaDB",
        "Pinecone"
    ],
    "Deployment": [
        "Streamlit Cloud",
        "HuggingFace Spaces",
        "Docker"
    ]
}

cols = st.columns(3)
for idx, (category, technologies) in enumerate(tech_stack.items()):
    with cols[idx % 3]:
        st.markdown(f"### {category}")
        for tech in technologies:
            st.markdown(f"- {tech}")

# Performance
st.markdown("## ⚡ Performance Metrics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("OCR Latency", "~2s", delta="Fast")

with col2:
    st.metric("ASR Latency", "~3s", delta="Fast")

with col3:
    st.metric("Solution Time", "~10s", delta="Optimized")

with col4:
    st.metric("Target Accuracy", "90%+", delta="High")

# Future Enhancements
st.markdown("## 🚀 Future Enhancements")

st.markdown("""
- 🎨 **LaTeX Rendering**: Beautiful mathematical equation display
- 📊 **Advanced Visualizations**: Graphs, plots, and diagrams
- 🌐 **Multi-language Support**: Support for regional languages
- 📱 **Mobile App**: Native mobile applications
- 🎓 **Personalized Learning**: Adaptive difficulty and recommendations
- 🔗 **Integration**: Connect with learning management systems
- 🎯 **Practice Mode**: Generate similar problems for practice
- 📝 **Handwriting Recognition**: Better OCR for handwritten problems
""")

# Contact & Support
st.markdown("## 📞 Contact & Support")

st.markdown("""
For questions, feedback, or support:
- 📧 Email: support@mathmentor.ai (example)
- 💬 Discord: Join our community (example)
- 🐛 Issues: Report on GitHub (example)
- 📖 Documentation: Full docs available (example)
""")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 1rem;'>
    <p><strong>Math Mentor v1.0</strong></p>
    <p>Built with ❤️ for students preparing for JEE and competitive exams</p>
    <p style='font-size: 0.9rem;'>© 2025 Math Mentor. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
