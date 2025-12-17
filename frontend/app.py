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
                
                # Trigger solving
                with st.spinner("🤖 AI agents are working on your problem..."):
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
                            
                            # Store partial results for display
                            st.session_state.solution = result.get('solution', {})
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
        
        # Action 2: Edit solution (if available)
        if st.session_state.solution:
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
