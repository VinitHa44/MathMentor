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

# Try to import audio recorder, use fallback if not available
try:
    from audio_recorder_streamlit import audio_recorder
    AUDIO_RECORDER_AVAILABLE = True
except ImportError:
    AUDIO_RECORDER_AVAILABLE = False

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
    initial_sidebar_state="collapsed"
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
    if 'hitl_reason' not in st.session_state:
        st.session_state.hitl_reason = []
    if 'hitl_corrected_problem' not in st.session_state:
        st.session_state.hitl_corrected_problem = ""
    if 'hitl_corrected_solution' not in st.session_state:
        st.session_state.hitl_corrected_solution = ""
    if 'human_decision' not in st.session_state:
        st.session_state.human_decision = None  # 'approve', 'reject', or None
    if 'feedback_submitted' not in st.session_state:
        st.session_state.feedback_submitted = False
    if 'show_memory' not in st.session_state:
        st.session_state.show_memory = False
    if 'problem_counter' not in st.session_state:
        st.session_state.problem_counter = 0
    if 'request_timeout' not in st.session_state:
        st.session_state.request_timeout = 600  # Default 10 minutes
    if 'current_problem_id' not in st.session_state:
        st.session_state.current_problem_id = None
    if 'show_correction_form' not in st.session_state:
        st.session_state.show_correction_form = False
    if 'needs_review' not in st.session_state:
        st.session_state.needs_review = False  # Flag for OCR/ASR text that needs review

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
                                st.session_state.needs_review = True  # OCR text needs review
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
        
        # with col2:
        #     if uploaded_image:
        #         st.markdown("#### 💡 Tips")
        #         st.info("""
        #         ✓ Good lighting
        #         ✓ Clear handwriting
        #         ✓ No glare
        #         ✓ High resolution
        #         """)
    
    # AUDIO INPUT TAB
    with input_mode[1]:
        st.markdown("""
        Record your math question or upload an audio file. The system will transcribe it.
        """)
        
        # Tips for speaking math
        with st.expander("💡 Tips for Speaking Math", expanded=False):
            st.markdown("""
            **How to speak mathematical expressions:**
            
            | Say This | Gets Converted To |
            |----------|-------------------|
            | "x raised to 3" or "x to the power 3" | x³ or x^3 |
            | "x squared" | x² |
            | "2 times 3" | 2 × 3 |
            | "equals to" or "equal to" | = |
            | "sine of theta" | sin(θ) |
            | "derivative of x cubed" | d/dx(x³) |
            | "square root of 16" | √16 |
            
            **Tips:**
            - Speak clearly and at a moderate pace
            - Say "raised to" or "to the power" for exponents
            - Use "equals to" instead of just "is"
            - Pronounce Greek letters by name (theta, alpha, pi, etc.)
            - Say "with respect to x" for derivatives
            
            **Example:**
            🎤 Say: "solve x squared plus 5x minus 3 equals 0"
            📝 Gets: "solve x² + 5x - 3 = 0"
            """)
        
        audio_input_method = st.radio(
            "Audio Input Method",
            ["🎙️ Record Audio", "📁 Upload Audio File"],
            horizontal=True
        )
        
        if audio_input_method == "🎙️ Record Audio":
            if not AUDIO_RECORDER_AVAILABLE:
                st.warning("⚠️ Audio recorder component not available. Please use 'Upload Audio File' option instead.")
                st.info("To enable audio recording, install: `pip install audio-recorder-streamlit`")
            else:
                st.info("🎤 Click the button below to start/stop recording")
                
                # Audio recorder component
                audio_bytes = audio_recorder(
                    text="",
                    recording_color="#e74c3c",
                    neutral_color="#3498db",
                    icon_name="microphone",
                    icon_size="3x"
                )
                
                if audio_bytes:
                    st.success("✅ Recording captured!")
                    
                    # Play back the recorded audio
                    st.audio(audio_bytes, format="audio/wav")
                    
                    if st.button("🎯 Transcribe Recording", type="primary", key="transcribe_recording"):
                        with st.spinner("Transcribing audio..."):
                            try:
                                # Convert audio to base64
                                audio_str = base64.b64encode(audio_bytes).decode()
                                
                                # Call backend ASR API
                                response = requests.post(
                                    f"{API_BASE_URL}/api/transcribe",
                                    json={"audio_base64": audio_str, "filename": "recording.wav"},
                                    timeout=st.session_state.request_timeout
                                )
                                
                                if response.status_code == 200:
                                    result = response.json()
                                    st.session_state.extracted_text = result["text"]
                                    st.session_state.asr_confidence = result["confidence"]
                                    st.session_state.asr_original = result.get("original_transcript", result["text"])
                                    st.session_state.math_notation_applied = result.get("math_notation_applied", False)
                                    st.session_state.needs_review = True  # ASR text needs review
                                    # Increment problem counter to force text area refresh
                                    st.session_state.problem_counter += 1
                                    # Clear previous solution and agent trace
                                    st.session_state.solution = None
                                    st.session_state.agent_trace = []
                                    st.session_state.feedback_submitted = False
                                    st.success(f"✅ Transcribed: {result['text'][:100]}...")
                                    st.info(f"Confidence: {result['confidence']:.2%}")
                                    
                                    # Show math notation conversion info
                                    if st.session_state.math_notation_applied:
                                        with st.expander("🔢 Math Notation Conversion Applied", expanded=False):
                                            st.markdown("**Original Speech:**")
                                            st.code(st.session_state.asr_original, language=None)
                                            st.markdown("**Converted to Math Notation:**")
                                            st.code(result["text"], language=None)
                                            st.info("✨ Spoken math phrases were automatically converted to mathematical notation")
                                    
                                    st.rerun()
                                else:
                                    st.error(f"Transcription failed: {response.json().get('detail', 'Unknown error')}")
                            except requests.exceptions.Timeout:
                                st.error("❌ Transcription request timed out. Try again or use a shorter recording.")
                            except requests.exceptions.ConnectionError as e:
                                st.error(f"❌ Cannot connect to backend: {str(e)}")
                                st.error("Make sure backend is running on http://localhost:8000")
                            except requests.exceptions.RequestException as e:
                                st.error(f"❌ Transcription request failed: {str(e)}")
                            except Exception as e:
                                st.error(f"❌ Unexpected error: {type(e).__name__}: {str(e)}")
        
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
                                st.session_state.asr_original = result.get("original_transcript", result["text"])
                                st.session_state.math_notation_applied = result.get("math_notation_applied", False)
                                st.session_state.needs_review = True  # ASR text needs review
                                # Increment problem counter to force text area refresh
                                st.session_state.problem_counter += 1
                                # Clear previous solution and agent trace
                                st.session_state.solution = None
                                st.session_state.agent_trace = []
                                st.session_state.feedback_submitted = False
                                st.success(f"✅ Transcribed: {result['text'][:100]}...")
                                st.info(f"Confidence: {result['confidence']:.2%}")
                                
                                # Show math notation conversion info
                                if st.session_state.math_notation_applied:
                                    with st.expander("🔢 Math Notation Conversion Applied", expanded=False):
                                        st.markdown("**Original Speech:**")
                                        st.code(st.session_state.asr_original, language=None)
                                        st.markdown("**Converted to Math Notation:**")
                                        st.code(result["text"], language=None)
                                        st.info("✨ Spoken math phrases were automatically converted to mathematical notation")
                                
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
                # Clear old solution and HITL state before solving new problem
                st.session_state.solution = None
                st.session_state.agent_trace = []
                st.session_state.hitl_required = False
                st.session_state.hitl_reason = []
                st.session_state.feedback_submitted = False
                
                # For text input, solve directly without requiring "Confirm & Solve"
                try:
                    # Call backend parse API first
                    with st.spinner("🔍 Parsing your problem..."):
                        parse_response = requests.post(
                            f"{API_BASE_URL}/api/parse",
                            json={"text": text_input},
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
                    
                    # Check if clarification is needed (outside spinner context)
                    if parsed.get("needs_clarification", False):
                        st.warning(f"⚠️ Clarification needed: {parsed.get('clarification_reason', 'Additional information required')}")
                        st.info("💡 Please clarify the problem and try again.")
                        st.session_state.extracted_text = text_input
                        st.session_state.problem_counter += 1
                        st.stop()
                    
                    # Continue with solving
                    with st.spinner("🤖 AI agents are working on your problem..."):
                        solve_response = requests.post(
                            f"{API_BASE_URL}/api/solve",
                            json={
                                "problem": text_input,
                                "ocr_confidence": None,
                                "asr_confidence": None
                            },
                            timeout=st.session_state.request_timeout,
                            proxies={"http": None, "https": None}
                        )
                        
                        if solve_response.status_code != 200:
                            st.error(f"Failed to solve problem: {solve_response.json().get('detail', 'Unknown error')}")
                            st.stop()
                        
                        result = solve_response.json()
                        
                        # Store problem ID for feedback
                        st.session_state.current_problem_id = result.get('problem_id', '')
                        
                        # Check if human review needed (HITL)
                        if result.get('needs_human_review', False):
                            st.session_state.hitl_required = True
                            st.session_state.hitl_reason = result.get('hitl_reason', [])
                            st.session_state.hitl_corrected_problem = text_input
                            
                            # Store partial results only if valid and from current problem
                            solution_from_backend = result.get('solution', {})
                            if solution_from_backend and solution_from_backend.get('steps'):
                                # Tag solution with current problem for validation
                                solution_from_backend['_current_problem'] = text_input
                                st.session_state.solution = solution_from_backend
                            else:
                                st.session_state.solution = None
                                
                            st.session_state.agent_trace = result.get('agent_trace', [])
                            st.session_state.verification = result.get('verification', {})
                            st.warning("⚠️ Human review required. Please check the HITL panel below.")
                            st.rerun()
                        
                        # Store results
                        st.session_state.extracted_text = text_input
                        st.session_state.needs_review = False  # Direct text input doesn't need review
                        st.session_state.agent_trace = result.get('agent_trace', [])
                        solution_data = result.get('solution', {})
                        verification = result.get('verification', {})
                        explanation = result.get('explanation', '')
                        explanation_details = result.get('explanation_details', {})
                        retrieved_context = result.get('retrieved_context', [])
                        
                        # Create solution object for display
                        st.session_state.solution = {
                            "problem": solution_data.get('problem', text_input),
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
                                    "content": ctx.get('content', '')
                                }
                                for ctx in retrieved_context
                            ],
                            "verification": verification,
                            "explanation": explanation,
                            "concept": explanation_details.get('concept', ''),
                            "approach": explanation_details.get('approach', ''),
                            "key_insight": explanation_details.get('key_insight', ''),
                            "common_mistakes": explanation_details.get('common_mistakes', '')
                        }
                        
                        st.session_state.feedback_submitted = False
                        st.session_state.problem_counter += 1
                
                except requests.exceptions.Timeout:
                    timeout_mins = st.session_state.request_timeout / 60
                    st.error(f"❌ Request timed out after {timeout_mins:.0f} minutes.")
                    st.stop()
                except requests.exceptions.ConnectionError as e:
                    st.error(f"❌ Cannot connect to backend: {str(e)}")
                    st.stop()
                except Exception as e:
                    st.error(f"❌ Unexpected error: {type(e).__name__}: {str(e)}")
                    st.stop()
                
                st.success("✅ Solution generated!")
                st.rerun()
            else:
                st.error("Please enter a math problem")
    
    # Extracted text preview and editing (only for OCR/ASR, not direct text input)
    if st.session_state.extracted_text and st.session_state.needs_review:
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
                
                # Clear old solution and HITL state before solving new problem
                st.session_state.solution = None
                st.session_state.agent_trace = []
                st.session_state.hitl_required = False
                st.session_state.hitl_reason = []
                st.session_state.feedback_submitted = False
                
                # Trigger solving
                try:
                    # Call backend parse API first
                    with st.spinner("🔍 Parsing your problem..."):
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
                    
                    # Check if clarification is needed (outside spinner context)
                    if parsed.get("needs_clarification", False):
                        st.warning(f"⚠️ Clarification needed: {parsed.get('clarification_reason', 'Additional information required')}")
                        st.info("💡 Please update the problem text above and click 'Confirm & Solve' again.")
                        st.session_state.hitl_required = True
                        st.session_state.feedback = 'clarification'
                        st.stop()
                    
                    # Continue with solving
                    with st.spinner("🤖 AI agents are working on your problem..."):
                        
                        # Call backend solve API with full RAG + Multi-Agent pipeline
                        solve_response = requests.post(
                            f"{API_BASE_URL}/api/solve",
                            json={
                                "problem": edited_text,
                                "ocr_confidence": st.session_state.get('ocr_confidence'),
                                "asr_confidence": st.session_state.get('asr_confidence')
                            },
                            timeout=st.session_state.request_timeout,  # Configurable timeout
                            proxies={"http": None, "https": None}  # Disable proxy for localhost
                        )
                        
                        if solve_response.status_code != 200:
                            st.error(f"Failed to solve problem: {solve_response.json().get('detail', 'Unknown error')}")
                            st.stop()
                        
                        result = solve_response.json()
                        
                        # Store problem ID for feedback
                        problem_id = result.get('problem_id', '')
                        st.session_state.current_problem_id = problem_id
                        
                        # Debug: Show if problem_id is missing
                        if not problem_id:
                            st.warning("⚠️ Backend didn't return a problem_id. Feedback may not work.")
                        
                        # Check if human review needed (HITL)
                        if result.get('needs_human_review', False):
                            st.session_state.hitl_required = True
                            st.session_state.hitl_reason = result.get('hitl_reason', [])
                            st.session_state.hitl_corrected_problem = edited_text
                            
                            # Store partial results for display only if they belong to current problem
                            solution_from_backend = result.get('solution', {})
                            # Check if solution has actual steps and is not empty/old
                            if solution_from_backend and solution_from_backend.get('steps'):
                                # Tag solution with current problem text for validation
                                solution_from_backend['_current_problem'] = edited_text
                                st.session_state.solution = solution_from_backend
                            else:
                                # No valid solution from backend, keep it cleared
                                st.session_state.solution = None
                                
                            st.session_state.agent_trace = result.get('agent_trace', [])
                            st.session_state.verification = result.get('verification', {})
                            
                            st.warning("⚠️ Human review required. Please check the HITL panel below.")
                            st.rerun()
                        
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
                st.session_state.needs_review = False
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
    
    # Display HITL Interface (Human-in-the-Loop)
    if st.session_state.hitl_required:
        st.markdown("---")
        st.markdown("""
        <div style='padding: 1.5rem; background: #fff3cd; border: 3px solid #ffc107; 
                    border-radius: 12px; margin: 1rem 0;'>
            <h2 style='color: #856404; margin-top: 0;'>✋ Human Review Required</h2>
            <p style='color: #856404; font-size: 1.1rem; margin-bottom: 0;'>
                The system needs your input to continue.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 📋 Reason(s) for Review:")
        for reason in st.session_state.hitl_reason:
            st.markdown(f"- **{reason}**")
        
        st.markdown("---")
        
        # Action 1: Edit problem text
        st.markdown("### ✏️ Action 1: Edit Problem (if needed)")
        corrected_problem = st.text_area(
            "Review and correct the problem text:",
            value=st.session_state.hitl_corrected_problem,
            height=100,
            key="hitl_problem_edit"
        )
        
        # Action 2: Edit solution (only if available and matches current problem)
        solution_belongs_to_current = (
            st.session_state.solution and 
            st.session_state.solution.get('_current_problem') == corrected_problem.strip()
        )
        
        if solution_belongs_to_current:
            st.markdown("### 🔧 Action 2: Edit Solution (optional)")
            
            current_solution_steps = st.session_state.solution.get('steps', [])
            solution_text = "\\n".join([f"Step {i+1}: {step}" for i, step in enumerate(current_solution_steps)])
            
            corrected_solution = st.text_area(
                "Correct the solution if needed:",
                value=solution_text,
                height=150,
                key="hitl_solution_edit"
            )
            st.session_state.hitl_corrected_solution = corrected_solution
        
        # Action 3: Approve / Reject buttons
        st.markdown("### 🎯 Action 3: Approve or Reject")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("✅ Approve & Continue", type="primary", width="stretch", key="hitl_approve"):
                st.success("✓ Approved! Continuing pipeline...")
                
                # If problem was corrected, re-solve with corrections
                if corrected_problem != st.session_state.hitl_corrected_problem:
                    with st.spinner("🔄 Re-solving with corrected problem..."):
                        try:
                            solve_response = requests.post(
                                f"{API_BASE_URL}/api/solve",
                                json={
                                    "problem": corrected_problem,
                                    "force_continue": True,  # Override HITL
                                    "corrected_problem": corrected_problem
                                },
                                timeout=st.session_state.request_timeout,
                                proxies={"http": None, "https": None}
                            )
                            
                            if solve_response.status_code == 200:
                                result = solve_response.json()
                                st.session_state.solution = result.get('solution', {})
                                st.session_state.agent_trace = result.get('agent_trace', [])
                                st.session_state.current_problem_id = result.get('problem_id', '')
                        except Exception as e:
                            st.error(f"Failed to re-solve: {e}")
                
                # Reset HITL flags
                st.session_state.hitl_required = False
                st.session_state.hitl_reason = []
                st.rerun()
        
        with col2:
            if st.button("❌ Reject & Retry", width="stretch", key="hitl_reject"):
                st.warning("⚠️ Rejected. Please modify the problem and try again.")
                
                # Store corrected problem back to extracted_text
                st.session_state.extracted_text = corrected_problem
                
                # Reset pipeline
                st.session_state.hitl_required = False
                st.session_state.hitl_reason = []
                st.session_state.solution = None
                st.session_state.agent_trace = []
                
                # Increment problem counter to reset UI
                st.session_state.problem_counter += 1
                st.session_state.human_decision = None
                
                st.warning("⚠️ Rejected. Please modify and resubmit.")
                st.rerun()
        
        # CRITICAL: Stop execution here until human makes a decision
        st.stop()
    
    # Manual review request button (visible when solution exists)
    if st.session_state.solution and not st.session_state.hitl_required:
        col1, col2, col3 = st.columns([2, 1, 2])
        with col2:
            if st.button("🔍 Request Re-check", key="manual_review_btn"):
                st.session_state.hitl_required = True
                st.session_state.hitl_reason = ["User requested review"]
                st.session_state.hitl_corrected_problem = st.session_state.extracted_text
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
        
        # Retrieved context panel (only if exists)
        if st.session_state.solution.get('retrieved_context'):
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
