"""
Math Mentor - Multimodal AI Math Tutor
A comprehensive Streamlit frontend for solving JEE-style math problems
"""

import streamlit as st
import requests
import json
from datetime import datetime
from typing import Optional, Dict, Any
import base64
from io import BytesIO
from PIL import Image
import time

# Import custom components
from components.ui_components import (
    render_agent_trace,
    render_retrieved_context,
    render_solution_card,
    render_confidence_indicator,
    render_feedback_section,
    render_memory_panel,
    render_hitl_interface
)
from components.styles import apply_custom_styles
from config import (
    API_BASE_URL,
    SUPPORTED_IMAGE_FORMATS,
    SUPPORTED_AUDIO_FORMATS,
    MAX_FILE_SIZE_MB
)

# Page configuration
st.set_page_config(
    page_title="Math Mentor - AI Math Tutor",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom styling
apply_custom_styles()

# Initialize session state
def initialize_session_state():
    """Initialize all session state variables"""
    if 'history' not in st.session_state:
        st.session_state.history = []
    if 'current_problem' not in st.session_state:
        st.session_state.current_problem = None
    if 'extracted_text' not in st.session_state:
        st.session_state.extracted_text = ""
    if 'agent_trace' not in st.session_state:
        st.session_state.agent_trace = []
    if 'solution' not in st.session_state:
        st.session_state.solution = None
    if 'hitl_required' not in st.session_state:
        st.session_state.hitl_required = False
    if 'feedback_submitted' not in st.session_state:
        st.session_state.feedback_submitted = False
    if 'show_memory' not in st.session_state:
        st.session_state.show_memory = False
    if 'problem_counter' not in st.session_state:
        st.session_state.problem_counter = 0
    if 'request_timeout' not in st.session_state:
        st.session_state.request_timeout = 600  # Default 10 minutes

initialize_session_state()

# Header
def render_header():
    """Render the application header"""
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        st.markdown("""
        <div style='text-align: center; padding: 1rem 0;'>
            <h1 style='color: #1f77b4; margin: 0;'>🧮 Math Mentor</h1>
            <p style='color: #666; font-size: 1.1rem; margin: 0.5rem 0;'>
                Your AI-Powered Math Tutor for JEE Problems
            </p>
        </div>
        """, unsafe_allow_html=True)

render_header()

# Sidebar
with st.sidebar:
    st.markdown("### 📋 Settings")
    
    # Model selection
    model_choice = st.selectbox(
        "AI Model",
        ["GPT-4", "Claude 3.5", "Gemini Pro"],
        help="Select the AI model for solving"
    )
    
    # Topic filter
    topic_filter = st.multiselect(
        "Focus Topics",
        ["Algebra", "Probability", "Calculus", "Linear Algebra", "All"],
        default=["All"]
    )
    
    # Difficulty level
    difficulty = st.select_slider(
        "Difficulty Level",
        options=["Easy", "Medium", "Hard", "JEE Advanced"],
        value="Medium"
    )
    
    # Explanation detail
    explanation_level = st.radio(
        "Explanation Detail",
        ["Concise", "Standard", "Detailed"],
        index=1
    )
    
    # Advanced settings expander
    with st.expander("⚙️ Advanced Settings"):
        timeout_minutes = st.slider(
            "Request Timeout (minutes)",
            min_value=1,
            max_value=20,
            value=10,
            help="Maximum time to wait for LLM response. Increase for complex problems."
        )
        st.session_state.request_timeout = timeout_minutes * 60
    
    st.markdown("---")
    
    # Memory toggle
    if st.button("📚 View Memory & History", width='stretch'):
        st.session_state.show_memory = not st.session_state.show_memory
    
    # Stats
    st.markdown("### 📊 Session Stats")
    st.metric("Problems Solved", len(st.session_state.history))
    if st.session_state.history:
        correct_count = sum(1 for h in st.session_state.history if h.get('feedback') == 'correct')
        accuracy = (correct_count / len(st.session_state.history)) * 100
        st.metric("Accuracy", f"{accuracy:.1f}%")
    
    st.markdown("---")
    
    # About section
    with st.expander("ℹ️ About"):
        st.markdown("""
        **Math Mentor** uses:
        - 🔍 RAG for knowledge retrieval
        - 🤖 Multi-agent system
        - 👁️ OCR for images
        - 🎤 Speech-to-text
        - 🧠 Self-learning memory
        - ✋ Human-in-the-loop
        """)
    
    if st.button("🔄 Reset Session", width='stretch'):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

# Main content area
if st.session_state.show_memory:
    # Memory panel view
    st.markdown("## 📚 Memory & History")
    render_memory_panel(st.session_state.history)
    
    if st.button("← Back to Solver", width='stretch'):
        st.session_state.show_memory = False
        st.rerun()
else:
    # Main solver interface
    
    # Input mode selection
    st.markdown("## 📝 Input Your Math Problem")
    
    input_mode = st.tabs(["📷 Image", "🎤 Audio", "⌨️ Text"])
    
    # IMAGE INPUT TAB
    with input_mode[0]:
        st.markdown("""
        Upload a photo or screenshot of your math problem. The system will extract the text using OCR.
        """)
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            uploaded_image = st.file_uploader(
                "Choose an image",
                type=SUPPORTED_IMAGE_FORMATS,
                help=f"Supported formats: {', '.join(SUPPORTED_IMAGE_FORMATS)}. Max size: {MAX_FILE_SIZE_MB}MB"
            )
            
            if uploaded_image:
                # Display uploaded image
                image = Image.open(uploaded_image)
                st.image(image, caption="Uploaded Image", width='stretch')
                
                # Extract text button
                if st.button("🔍 Extract Text from Image", type="primary", width='stretch'):
                    with st.spinner("Extracting text using OCR..."):
                        try:
                            # Convert image to base64
                            buffered = BytesIO()
                            image.save(buffered, format="PNG")
                            img_str = base64.b64encode(buffered.getvalue()).decode()
                            
                            # Call backend OCR API
                            response = requests.post(
                                f"{API_BASE_URL}/api/ocr",
                                json={"image_base64": img_str},
                                timeout=30
                            )
                            
                            if response.status_code == 200:
                                result = response.json()
                                st.session_state.extracted_text = result["text"]
                                st.session_state.ocr_confidence = result["confidence"]
                                # Increment problem counter to force text area refresh
                                st.session_state.problem_counter += 1
                                # Clear previous solution and agent trace
                                st.session_state.solution = None
                                st.session_state.agent_trace = []
                                st.session_state.feedback_submitted = False
                                st.success(f"✅ Text extracted: {result['text'][:100]}...")
                                st.info(f"Confidence: {result['confidence']:.2%}")
                                st.rerun()
                            else:
                                st.error(f"OCR failed: {response.json().get('detail', 'Unknown error')}")
                        except requests.exceptions.Timeout:
                            st.error("❌ OCR request timed out. Try again.")
                        except requests.exceptions.ConnectionError as e:
                            st.error(f"❌ Cannot connect to backend: {str(e)}")
                            st.error("Make sure backend is running on http://localhost:8000")
                        except requests.exceptions.RequestException as e:
                            st.error(f"❌ OCR request failed: {str(e)}")
                        except Exception as e:
                            st.error(f"❌ Unexpected error: {type(e).__name__}: {str(e)}")
        
        with col2:
            if uploaded_image:
                st.markdown("#### 💡 Tips")
                st.info("""
                ✓ Good lighting
                ✓ Clear handwriting
                ✓ No glare
                ✓ High resolution
                """)
    
    # AUDIO INPUT TAB
    with input_mode[1]:
        st.markdown("""
        Record your math question or upload an audio file. The system will transcribe it.
        """)
        
        audio_input_method = st.radio(
            "Audio Input Method",
            ["🎙️ Record Audio", "📁 Upload Audio File"],
            horizontal=True
        )
        
        if audio_input_method == "🎙️ Record Audio":
            st.warning("🎤 Click the record button below to start recording")
            
            # Audio recorder component (would need streamlit-audiorecorder or similar)
            # For now, showing placeholder
            st.markdown("""
            <div style='border: 2px dashed #ccc; padding: 3rem; text-align: center; border-radius: 10px;'>
                <p style='font-size: 1.2rem; color: #666;'>🎤 Audio Recorder</p>
                <p style='color: #999;'>Click to start/stop recording</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Simulate recording
            if st.button("🔴 Start Recording", type="primary"):
                st.info("Recording... (This is a placeholder - implement with audio recorder library)")
        
        else:
            uploaded_audio = st.file_uploader(
                "Choose an audio file",
                type=SUPPORTED_AUDIO_FORMATS,
                help=f"Supported formats: {', '.join(SUPPORTED_AUDIO_FORMATS)}"
            )
            
            if uploaded_audio:
                st.audio(uploaded_audio)
                
                if st.button("🎯 Transcribe Audio", type="primary", width='stretch'):
                    with st.spinner("Transcribing audio..."):
                        try:
                            # Convert audio to base64
                            audio_bytes = uploaded_audio.read()
                            audio_str = base64.b64encode(audio_bytes).decode()
                            
                            # Call backend ASR API
                            response = requests.post(
                                f"{API_BASE_URL}/api/transcribe",
                                json={"audio_base64": audio_str, "filename": uploaded_audio.name},
                                timeout=60
                            )
                            
                            if response.status_code == 200:
                                result = response.json()
                                st.session_state.extracted_text = result["text"]
                                st.session_state.asr_confidence = result["confidence"]
                                # Increment problem counter to force text area refresh
                                st.session_state.problem_counter += 1
                                # Clear previous solution and agent trace
                                st.session_state.solution = None
                                st.session_state.agent_trace = []
                                st.session_state.feedback_submitted = False
                                st.success(f"✅ Transcribed: {result['text'][:100]}...")
                                st.info(f"Confidence: {result['confidence']:.2%}")
                                st.rerun()
                            else:
                                st.error(f"Transcription failed: {response.json().get('detail', 'Unknown error')}")
                        except requests.exceptions.Timeout:
                            st.error("❌ Transcription request timed out. Try again.")
                        except requests.exceptions.ConnectionError as e:
                            st.error(f"❌ Cannot connect to backend: {str(e)}")
                            st.error("Make sure backend is running on http://localhost:8000")
                        except requests.exceptions.RequestException as e:
                            st.error(f"❌ Transcription request failed: {str(e)}")
                        except Exception as e:
                            st.error(f"❌ Unexpected error: {type(e).__name__}: {str(e)}")
    
    # TEXT INPUT TAB
    with input_mode[2]:
        st.markdown("Type your math problem directly below:")
        
        # Use a separate key for text input to avoid cross-contamination
        text_input = st.text_area(
            "Math Problem",
            height=150,
            placeholder="Example: Solve the equation 3x² - 5x + 2 = 0\n\nOr: Find the derivative of f(x) = x³ + 2x² - 5x + 1",
            key="text_input_area"
        )
        
        if st.button("➡️ Submit Problem", type="primary", width='stretch'):
            if text_input.strip():
                st.session_state.extracted_text = text_input
                # Increment problem counter to force text area refresh
                st.session_state.problem_counter += 1
                # Clear OCR/ASR confidence flags since this is manual text input
                if hasattr(st.session_state, 'ocr_confidence'):
                    delattr(st.session_state, 'ocr_confidence')
                if hasattr(st.session_state, 'asr_confidence'):
                    delattr(st.session_state, 'asr_confidence')
                # Clear previous solution and agent trace
                st.session_state.solution = None
                st.session_state.agent_trace = []
                st.session_state.feedback_submitted = False
                st.success("✅ Problem submitted!")
                st.rerun()
            else:
                st.error("Please enter a math problem")
    
    # Extracted text preview and editing
    if st.session_state.extracted_text:
        st.markdown("---")
        st.markdown("## 📄 Extracted Problem")
        
        # Show confidence if OCR/ASR was used
        if hasattr(st.session_state, 'ocr_confidence'):
            confidence = st.session_state.ocr_confidence
            render_confidence_indicator(confidence, "OCR Confidence")
            
            if confidence < 0.85:
                st.warning("⚠️ Low OCR confidence detected. Please review and correct the extracted text.")
        
        elif hasattr(st.session_state, 'asr_confidence'):
            confidence = st.session_state.asr_confidence
            render_confidence_indicator(confidence, "Transcription Confidence")
            
            if confidence < 0.85:
                st.warning("⚠️ Low transcription confidence. Please review the text.")
        
        # Editable text area with unique key based on problem counter
        edited_text = st.text_area(
            "Review and edit if needed:",
            value=st.session_state.extracted_text,
            height=100,
            key=f"edited_text_area_{st.session_state.problem_counter}"
        )
        
        col1, col2, col3 = st.columns([1, 1, 2])
        
        with col1:
            if st.button("✅ Confirm & Solve", type="primary", width='stretch'):
                st.session_state.extracted_text = edited_text
                
                # Generate session ID for progress tracking
                import uuid
                session_id = str(uuid.uuid4())
                
                # Create progress display area
                progress_container = st.empty()
                status_container = st.empty()
                time_container = st.empty()
                
                # Trigger solving with progress tracking
                start_time = time.time()
                
                try:
                    # Call backend parse API first
                    parse_response = requests.post(
                        f"{API_BASE_URL}/api/parse",
                        json={"text": edited_text},
                        proxies={"http": None, "https": None}
                    )
                    
                    if parse_response.status_code != 200:
                        st.error(f"Failed to parse problem: {parse_response.json().get('detail', 'Unknown error')}")
                        st.stop()
                    
                    parsed = parse_response.json()
                    
                    # Use actual parsed data from LLM Parser Agent
                    st.session_state.agent_trace = [
                        {
                            "agent": "Parser Agent",
                            "status": "completed",
                            "output": parsed,
                            "timestamp": datetime.now().isoformat()
                        }
                    ]
                    
                    # Check if clarification is needed
                    if parsed.get("needs_clarification", False):
                        st.warning(f"⚠️ Clarification needed: {parsed.get('clarification_reason', 'Additional information required')}")
                        st.session_state.hitl_required = True
                        st.session_state.feedback = 'clarification'
                        st.stop()
                    
                    # Store timeout value before thread (threads can't access session_state)
                    request_timeout = st.session_state.request_timeout
                    
                    # Start async solve request in background
                    import threading
                    solve_complete = threading.Event()
                    solve_response_data = {'response': None, 'error': None}
                    
                    def call_solve_api():
                        try:
                            response = requests.post(
                                f"{API_BASE_URL}/api/solve",
                                json={"problem": edited_text, "session_id": session_id},
                                timeout=request_timeout,
                                proxies={"http": None, "https": None}
                            )
                            solve_response_data['response'] = response
                        except Exception as e:
                            solve_response_data['error'] = e
                        finally:
                            solve_complete.set()
                    
                    # Start solve request in thread
                    solve_thread = threading.Thread(target=call_solve_api)
                    solve_thread.start()
                    
                    # Wait a moment for backend to initialize progress tracking
                    time.sleep(0.3)
                    
                    # Show spinner with periodic updates using st.empty()
                    progress_text = st.empty()
                    detail_text = st.empty()
                    time_text = st.empty()
                    
                    with st.spinner(""):
                        last_step_num = 0
                        
                        # Poll for progress updates
                        while not solve_complete.is_set():
                            try:
                                progress_response = requests.get(
                                    f"{API_BASE_URL}/api/progress/{session_id}",
                                    timeout=2,
                                    proxies={"http": None, "https": None}
                                )
                                
                                if progress_response.status_code == 200:
                                    progress_data = progress_response.json()
                                    current_step = progress_data.get('current_step', '')
                                    step_num = progress_data.get('step_number', 0)
                                    total_steps = progress_data.get('total_steps', 6)
                                    details = progress_data.get('details', '')
                                    
                                    # Update displays using empty containers
                                    progress_text.markdown(f"### 🤖 Step {step_num}/{total_steps}: {current_step}")
                                    detail_text.info(f"💡 {details}")
                                    
                                    elapsed = int(time.time() - start_time)
                                    time_text.caption(f"⏱️ Time elapsed: {elapsed}s")
                                    
                                    last_step_num = step_num
                            
                            except:
                                pass  # Continue silently
                            
                            time.sleep(0.5)  # Poll every 500ms
                    
                    # Clear progress displays
                    progress_text.empty()
                    detail_text.empty()
                    time_text.empty()
                    
                    # Wait for thread to complete
                    solve_thread.join()
                    
                    # Check for errors
                    if solve_response_data['error']:
                        error = solve_response_data['error']
                        st.error(f"❌ Error during solve: {type(error).__name__}: {str(error)}")
                        raise error
                    
                    solve_response = solve_response_data['response']
                    
                    if solve_response is None:
                        st.error("❌ No response received from backend")
                        st.stop()
                    
                    elapsed_time = time.time() - start_time
                    
                    if solve_response.status_code != 200:
                        st.error(f"Failed to solve problem: {solve_response.json().get('detail', 'Unknown error')}")
                        st.stop()
                    
                    result = solve_response.json()
                    
                    # Store problem ID for feedback
                    st.session_state.current_problem_id = result.get('problem_id', '')
                    
                    # Store agent trace
                    st.session_state.agent_trace = result.get('agent_trace', [])
                    
                    # Extract solution details
                    solution_data = result.get('solution', {})
                    verification = result.get('verification', {})
                    explanation = result.get('explanation', '')
                    explanation_details = result.get('explanation_details', {})
                    retrieved_context = result.get('retrieved_context', [])
                    
                    # Create solution object for display
                    st.session_state.solution = {
                        "problem": solution_data.get('problem', edited_text),
                        "topic": solution_data.get('topic', 'General'),
                        "final_answer": solution_data.get('final_answer', 'N/A'),
                        "steps": [
                            {
                                "step_number": i + 1,
                                "description": f"Step {i + 1}",
                                "content": step if isinstance(step, str) else step.get('description', str(step))
                            }
                            for i, step in enumerate(solution_data.get('steps', []))
                        ],
                        "solution_text": solution_data.get('solution_text', ''),
                        "retrieved_context": [
                            {
                                "source": ctx.get('source', 'Unknown'),
                                "topic": ctx.get('topic', 'N/A'),
                                "content": ctx.get('text', ''),
                                "relevance": ctx.get('score', 0)
                            }
                            for ctx in retrieved_context
                        ],
                        "confidence": solution_data.get('confidence', 0.5),
                        "verification_passed": verification.get('is_correct', False),
                        "verification_confidence": verification.get('confidence', 0),
                        "verification_issues": verification.get('issues', []),
                        "verification_suggestions": verification.get('suggestions', []),
                        "needs_human_review": verification.get('needs_human_review', False),
                        "explanation": explanation,
                        "key_concept": explanation_details.get('key_concept', ''),
                        "analogy": explanation_details.get('analogy', ''),
                        "common_mistakes": explanation_details.get('common_mistakes', '')
                    }
                    
                    st.session_state.feedback_submitted = False
                
                except requests.exceptions.Timeout:
                    timeout_mins = st.session_state.request_timeout / 60
                    st.error(f"❌ Request timed out after {timeout_mins:.0f} minutes. The LLM might be overloaded or the problem is very complex.")
                    st.warning("""
                    **Possible solutions:**
                    - Try a simpler problem first to verify the system is working
                    - Check if the backend LLM service (Ollama) is running and responsive
                    - Restart the backend server if it's stuck
                    - Increase the timeout in Advanced Settings (sidebar)
                    - The problem might require multiple LLM calls - try breaking it into smaller parts
                    """)
                    st.info("🔧 You can check backend logs for more details")
                    st.stop()
                except requests.exceptions.ConnectionError as e:
                    st.error(f"❌ Cannot connect to backend: {str(e)}")
                    st.error("Make sure backend is running on http://localhost:8000")
                    st.stop()
                except requests.exceptions.RequestException as e:
                    st.error(f"❌ Request failed: {str(e)}")
                    st.stop()
                except Exception as e:
                    st.error(f"❌ Unexpected error: {type(e).__name__}: {str(e)}")
                    st.stop()
                
                st.success("✅ Solution generated!")
                st.rerun()
        
        with col2:
            if st.button("🗑️ Clear", width='stretch'):
                st.session_state.extracted_text = ""
                # Increment problem counter to force text area refresh
                st.session_state.problem_counter += 1
                # Clear the text input area key
                if 'text_input_area' in st.session_state:
                    del st.session_state['text_input_area']
                if hasattr(st.session_state, 'ocr_confidence'):
                    delattr(st.session_state, 'ocr_confidence')
                if hasattr(st.session_state, 'asr_confidence'):
                    delattr(st.session_state, 'asr_confidence')
                # Clear solution and agent trace
                st.session_state.solution = None
                st.session_state.agent_trace = []
                st.session_state.feedback_submitted = False
                st.rerun()
    
    # Display agent trace
    if st.session_state.agent_trace:
        st.markdown("---")
        st.markdown("## 🤖 Agent Workflow")
        render_agent_trace(st.session_state.agent_trace)
    
    # Display solution
    if st.session_state.solution:
        st.markdown("---")
        st.markdown("## ✨ Solution")
        
        render_solution_card(st.session_state.solution)
        
        # Retrieved context panel
        st.markdown("### 📚 Retrieved Knowledge")
        render_retrieved_context(st.session_state.solution['retrieved_context'])
        
        # Feedback section
        if not st.session_state.feedback_submitted:
            st.markdown("---")
            st.markdown("### 💬 How was this solution?")
            render_feedback_section()
    
    # HITL Interface
    if st.session_state.hitl_required:
        st.markdown("---")
        render_hitl_interface()

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 1rem;'>
    <p>Math Mentor v1.0 | Built with ❤️ using Streamlit, RAG, and Multi-Agent AI</p>
    <p style='font-size: 0.9rem;'>Supports Algebra • Probability • Calculus • Linear Algebra</p>
</div>
""", unsafe_allow_html=True)
