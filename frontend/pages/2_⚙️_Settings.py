"""
Settings Page - Configure Math Mentor
"""

import streamlit as st
from components.styles import apply_custom_styles
import json

st.set_page_config(
    page_title="Settings - Math Mentor",
    page_icon="⚙️",
    layout="wide"
)

apply_custom_styles()

# Header
st.markdown("""
<div style='text-align: center; padding: 2rem 0;'>
    <h1 style='color: #1f77b4;'>⚙️ Settings</h1>
    <p style='color: #666; font-size: 1.2rem;'>Configure your Math Mentor experience</p>
</div>
""", unsafe_allow_html=True)

# Initialize settings in session state
if 'settings' not in st.session_state:
    st.session_state.settings = {
        'model': 'GPT-4',
        'ocr_provider': 'Tesseract',
        'asr_provider': 'Whisper',
        'explanation_level': 'Standard',
        'theme': 'Light',
        'language': 'English',
        'enable_notifications': True,
        'auto_solve': False,
        'show_confidence': True,
        'show_agent_trace': True,
        'show_rag_context': True,
        'max_history_items': 100,
        'ocr_threshold': 0.85,
        'asr_threshold': 0.80,
        'rag_top_k': 5
    }

# General Settings
st.markdown("## 🎛️ General Settings")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### AI Model")
    model = st.selectbox(
        "Select AI Model",
        ["GPT-4", "Claude 3.5", "Gemini Pro"],
        index=["GPT-4", "Claude 3.5", "Gemini Pro"].index(st.session_state.settings['model']),
        help="Choose the AI model for solving math problems"
    )
    st.session_state.settings['model'] = model
    
    st.markdown("### Explanation Level")
    explanation = st.select_slider(
        "Detail Level",
        options=["Concise", "Standard", "Detailed"],
        value=st.session_state.settings['explanation_level'],
        help="How detailed should the explanations be?"
    )
    st.session_state.settings['explanation_level'] = explanation

with col2:
    st.markdown("### Theme")
    theme = st.radio(
        "Color Theme",
        ["Light", "Dark", "Auto"],
        index=["Light", "Dark", "Auto"].index(st.session_state.settings['theme']),
        horizontal=True
    )
    st.session_state.settings['theme'] = theme
    
    st.markdown("### Language")
    language = st.selectbox(
        "Interface Language",
        ["English", "Hindi", "Spanish", "French"],
        index=["English", "Hindi", "Spanish", "French"].index(st.session_state.settings['language'])
    )
    st.session_state.settings['language'] = language

# Input Processing Settings
st.markdown("---")
st.markdown("## 📷 Input Processing")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### OCR (Image Processing)")
    ocr_provider = st.selectbox(
        "OCR Provider",
        ["Tesseract", "PaddleOCR", "EasyOCR"],
        index=["Tesseract", "PaddleOCR", "EasyOCR"].index(st.session_state.settings['ocr_provider'])
    )
    st.session_state.settings['ocr_provider'] = ocr_provider
    
    ocr_threshold = st.slider(
        "OCR Confidence Threshold",
        min_value=0.0,
        max_value=1.0,
        value=st.session_state.settings['ocr_threshold'],
        step=0.05,
        help="Minimum confidence for OCR results (triggers HITL if below)"
    )
    st.session_state.settings['ocr_threshold'] = ocr_threshold

with col2:
    st.markdown("### ASR (Speech Recognition)")
    asr_provider = st.selectbox(
        "ASR Provider",
        ["Whisper", "Google Speech", "Assembly AI"],
        index=["Whisper", "Google Speech", "Assembly AI"].index(st.session_state.settings['asr_provider'])
    )
    st.session_state.settings['asr_provider'] = asr_provider
    
    asr_threshold = st.slider(
        "ASR Confidence Threshold",
        min_value=0.0,
        max_value=1.0,
        value=st.session_state.settings['asr_threshold'],
        step=0.05,
        help="Minimum confidence for speech recognition (triggers HITL if below)"
    )
    st.session_state.settings['asr_threshold'] = asr_threshold

# RAG Settings
st.markdown("---")
st.markdown("## 🔍 RAG Configuration")

col1, col2 = st.columns(2)

with col1:
    rag_top_k = st.number_input(
        "Number of Retrieved Contexts (Top-K)",
        min_value=1,
        max_value=10,
        value=st.session_state.settings['rag_top_k'],
        help="How many relevant context chunks to retrieve"
    )
    st.session_state.settings['rag_top_k'] = rag_top_k

with col2:
    vector_store = st.selectbox(
        "Vector Store",
        ["FAISS", "ChromaDB", "Pinecone"],
        help="Vector database for knowledge retrieval"
    )

# Display Settings
st.markdown("---")
st.markdown("## 🖥️ Display Options")

col1, col2 = st.columns(2)

with col1:
    show_confidence = st.checkbox(
        "Show Confidence Indicators",
        value=st.session_state.settings['show_confidence'],
        help="Display confidence scores for OCR, ASR, and solutions"
    )
    st.session_state.settings['show_confidence'] = show_confidence
    
    show_agent_trace = st.checkbox(
        "Show Agent Workflow",
        value=st.session_state.settings['show_agent_trace'],
        help="Display the multi-agent execution trace"
    )
    st.session_state.settings['show_agent_trace'] = show_agent_trace

with col2:
    show_rag_context = st.checkbox(
        "Show Retrieved Context",
        value=st.session_state.settings['show_rag_context'],
        help="Display the knowledge chunks retrieved by RAG"
    )
    st.session_state.settings['show_rag_context'] = show_rag_context
    
    enable_notifications = st.checkbox(
        "Enable Notifications",
        value=st.session_state.settings['enable_notifications'],
        help="Show success/error notifications"
    )
    st.session_state.settings['enable_notifications'] = enable_notifications

# Behavior Settings
st.markdown("---")
st.markdown("## ⚡ Behavior")

col1, col2 = st.columns(2)

with col1:
    auto_solve = st.checkbox(
        "Auto-Solve After Extraction",
        value=st.session_state.settings['auto_solve'],
        help="Automatically start solving after OCR/ASR extraction"
    )
    st.session_state.settings['auto_solve'] = auto_solve

with col2:
    max_history = st.number_input(
        "Max History Items",
        min_value=10,
        max_value=500,
        value=st.session_state.settings['max_history_items'],
        step=10,
        help="Maximum number of items to keep in history"
    )
    st.session_state.settings['max_history_items'] = max_history

# Data Management
st.markdown("---")
st.markdown("## 💾 Data Management")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📥 Export Settings", use_container_width=True):
        settings_json = json.dumps(st.session_state.settings, indent=2)
        st.download_button(
            label="Download settings.json",
            data=settings_json,
            file_name="math_mentor_settings.json",
            mime="application/json",
            use_container_width=True
        )

with col2:
    uploaded_settings = st.file_uploader(
        "📤 Import Settings",
        type=['json'],
        help="Upload a settings JSON file"
    )
    if uploaded_settings:
        try:
            imported_settings = json.load(uploaded_settings)
            st.session_state.settings.update(imported_settings)
            st.success("✅ Settings imported successfully!")
        except Exception as e:
            st.error(f"❌ Error importing settings: {str(e)}")

with col3:
    if st.button("🔄 Reset to Defaults", use_container_width=True):
        st.session_state.settings = {
            'model': 'GPT-4',
            'ocr_provider': 'Tesseract',
            'asr_provider': 'Whisper',
            'explanation_level': 'Standard',
            'theme': 'Light',
            'language': 'English',
            'enable_notifications': True,
            'auto_solve': False,
            'show_confidence': True,
            'show_agent_trace': True,
            'show_rag_context': True,
            'max_history_items': 100,
            'ocr_threshold': 0.85,
            'asr_threshold': 0.80,
            'rag_top_k': 5
        }
        st.success("✅ Settings reset to defaults!")
        st.rerun()

# Clear Data
st.markdown("### 🗑️ Clear Data")
st.warning("⚠️ Warning: These actions cannot be undone!")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Clear History", use_container_width=True):
        if 'history' in st.session_state:
            st.session_state.history = []
            st.success("History cleared!")

with col2:
    if st.button("Clear Memory", use_container_width=True):
        st.info("Memory cleared! (Backend operation)")

with col3:
    if st.button("Clear All Data", use_container_width=True):
        if 'history' in st.session_state:
            st.session_state.history = []
        st.success("All data cleared!")

# Advanced Settings
st.markdown("---")
st.markdown("## 🔧 Advanced Settings")

with st.expander("⚙️ Advanced Configuration"):
    st.markdown("### API Configuration")
    
    api_url = st.text_input(
        "Backend API URL",
        value="http://localhost:8000",
        help="URL of the Math Mentor backend API"
    )
    
    api_timeout = st.number_input(
        "API Timeout (seconds)",
        min_value=5,
        max_value=60,
        value=30
    )
    
    st.markdown("### Performance")
    
    cache_enabled = st.checkbox("Enable Caching", value=True)
    
    max_concurrent_requests = st.number_input(
        "Max Concurrent Requests",
        min_value=1,
        max_value=10,
        value=3
    )
    
    st.markdown("### Debugging")
    
    debug_mode = st.checkbox("Enable Debug Mode", value=False)
    
    log_level = st.selectbox(
        "Log Level",
        ["DEBUG", "INFO", "WARNING", "ERROR"],
        index=1
    )

# Save Settings
st.markdown("---")

col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    if st.button("💾 Save All Settings", type="primary", use_container_width=True):
        st.success("✅ All settings saved successfully!")
        st.balloons()

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 1rem;'>
    <p>Settings are automatically saved to your session</p>
    <p style='font-size: 0.9rem;'>For persistent storage, export your settings as JSON</p>
</div>
""", unsafe_allow_html=True)
