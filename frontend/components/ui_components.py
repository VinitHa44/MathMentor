"""
Reusable UI Components for Math Mentor
"""

import streamlit as st
from datetime import datetime
import json
from typing import List, Dict, Any, Optional

def render_confidence_indicator(confidence: float, label: str = "Confidence"):
    """
    Render a confidence indicator with color coding
    
    Args:
        confidence: Float between 0 and 1
        label: Label for the indicator
    """
    confidence_percent = confidence * 100
    
    if confidence >= 0.9:
        color = "#28a745"
        emoji = "🟢"
        status = "High"
    elif confidence >= 0.7:
        color = "#ffc107"
        emoji = "🟡"
        status = "Medium"
    else:
        color = "#dc3545"
        emoji = "🔴"
        status = "Low"
    
    st.markdown(f"""
    <div style='padding: 0.75rem; background: linear-gradient(135deg, {color}22, {color}11); 
                border-left: 4px solid {color}; border-radius: 8px; margin: 1rem 0;'>
        <div style='display: flex; justify-content: space-between; align-items: center;'>
            <span style='font-weight: 600; color: #333;'>{emoji} {label}</span>
            <span style='font-size: 1.2rem; font-weight: bold; color: {color};'>
                {confidence_percent:.1f}% <span style='font-size: 0.9rem; color: #666;'>({status})</span>
            </span>
        </div>
        <div style='margin-top: 0.5rem; background: #f0f0f0; height: 8px; border-radius: 4px; overflow: hidden;'>
            <div style='background: {color}; height: 100%; width: {confidence_percent}%; transition: width 0.3s;'></div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_agent_trace(agent_trace: List[Dict[str, Any]]):
    """
    Render the agent workflow trace
    
    Args:
        agent_trace: List of agent execution records
    """
    st.markdown("""
    <style>
    .agent-card {
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 10px;
        border: 1px solid #e0e0e0;
        background: white;
        transition: all 0.3s;
    }
    .agent-card:hover {
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        transform: translateY(-2px);
    }
    .agent-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 0.5rem;
    }
    .agent-name {
        font-weight: 600;
        font-size: 1.1rem;
        color: #1f77b4;
    }
    .agent-status {
        padding: 0.25rem 0.75rem;
        border-radius: 12px;
        font-size: 0.85rem;
        font-weight: 600;
    }
    .status-completed {
        background: #d4edda;
        color: #155724;
    }
    .status-running {
        background: #fff3cd;
        color: #856404;
    }
    .status-failed {
        background: #f8d7da;
        color: #721c24;
    }
    </style>
    """, unsafe_allow_html=True)
    
    for i, trace in enumerate(agent_trace, 1):
        agent_name = trace.get('agent', 'Unknown Agent')
        status = trace.get('status', 'unknown')
        output = trace.get('output', {})
        
        status_class = f"status-{status}"
        status_emoji = {
            'completed': '✅',
            'running': '⏳',
            'failed': '❌'
        }.get(status, '❓')
        
        with st.expander(f"{i}. {status_emoji} {agent_name}", expanded=(i == len(agent_trace))):
            st.markdown(f"""
            <div class='agent-card'>
                <div class='agent-header'>
                    <span class='agent-name'>{agent_name}</span>
                    <span class='agent-status {status_class}'>{status.upper()}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            if output:
                st.json(output)
            
            if 'timestamp' in trace:
                st.caption(f"🕐 {trace['timestamp']}")


def render_retrieved_context(contexts: List[Dict[str, Any]]):
    """
    Render retrieved RAG context
    
    Args:
        contexts: List of retrieved context chunks
    """
    if not contexts:
        st.info("No context retrieved for this problem.")
        return
    
    for i, ctx in enumerate(contexts, 1):
        relevance = ctx.get('relevance', 0)
        relevance_percent = relevance * 100
        
        # Color based on relevance
        if relevance >= 0.8:
            border_color = "#28a745"
        elif relevance >= 0.6:
            border_color = "#ffc107"
        else:
            border_color = "#6c757d"
        
        with st.container():
            st.markdown(f"""
            <div style='padding: 1rem; margin: 0.5rem 0; border-left: 4px solid {border_color}; 
                        background: #f8f9fa; border-radius: 8px;'>
                <div style='display: flex; justify-content: space-between; margin-bottom: 0.5rem;'>
                    <strong style='color: #1f77b4;'>📄 {ctx.get('source', 'Unknown Source')}</strong>
                    <span style='background: {border_color}; color: white; padding: 0.2rem 0.6rem; 
                                 border-radius: 12px; font-size: 0.85rem;'>
                        {relevance_percent:.0f}% relevant
                    </span>
                </div>
                <p style='margin: 0; color: #333; line-height: 1.6;'>{ctx.get('content', '')}</p>
            </div>
            """, unsafe_allow_html=True)


def render_solution_card(solution: Dict[str, Any]):
    """
    Render the solution with steps
    
    Args:
        solution: Solution dictionary with steps and answer
    """
    # Header with topic and confidence
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown(f"**Topic:** {solution.get('topic', 'General')}")
    
    with col2:
        if solution.get('verification_passed'):
            st.success("✓ Verified")
        else:
            st.warning("⚠ Needs Review")
    
    # Confidence indicator
    render_confidence_indicator(solution.get('confidence', 0.5), "Solution Confidence")
    
    # Final answer box
    st.markdown(f"""
    <div style='padding: 1.5rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                border-radius: 12px; margin: 1rem 0; box-shadow: 0 4px 15px rgba(0,0,0,0.2);'>
        <h3 style='color: white; margin: 0 0 0.5rem 0; font-size: 1.2rem;'>🎯 Final Answer</h3>
        <div style='background: white; padding: 1rem; border-radius: 8px; 
                    font-size: 1.3rem; font-weight: 600; color: #333; text-align: center;'>
            {solution.get('final_answer', 'No answer provided')}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Step-by-step solution
    st.markdown("### 📖 Step-by-Step Solution")
    
    steps = solution.get('steps', [])
    
    for step in steps:
        step_num = step.get('step_number', 0)
        description = step.get('description', '')
        content = step.get('content', '')
        
        with st.expander(f"**Step {step_num}: {description}**", expanded=(step_num == 1)):
            st.markdown(content)
            
            # Add visual separator
            if step_num < len(steps):
                st.markdown("---")


def render_feedback_section():
    """
    Render the feedback and HITL section with backend integration
    """
    st.markdown("### 💬 Feedback")
    st.markdown("Help us improve by providing feedback:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("✅ Approve", key="feedback_approve_btn", type="primary"):
            problem_id = st.session_state.get('current_problem_id', '')
            
            if problem_id:
                try:
                    import requests
                    response = requests.post(
                        "http://localhost:8000/api/feedback",
                        json={
                            "problem_id": problem_id,
                            "feedback_type": "approve",
                            "user_comment": "Solution approved"
                        }
                    )
                    
                    if response.status_code == 200:
                        st.success("✅ Thank you! Feedback saved.")
                        st.session_state.feedback_submitted = True
                        st.balloons()
                except Exception as e:
                    st.error(f"Failed to submit feedback: {e}")
    
    with col2:
        if st.button("✏️ Edit/Correct", key="feedback_edit_btn"):
            st.session_state.show_correction_form = True
    
    with col3:
        if st.button("❌ Reject", key="feedback_reject_btn"):
            problem_id = st.session_state.get('current_problem_id', '')
            
            if problem_id:
                try:
                    import requests
                    response = requests.post(
                        "http://localhost:8000/api/feedback",
                        json={
                            "problem_id": problem_id,
                            "feedback_type": "reject",
                            "user_comment": "Solution rejected"
                        }
                    )
                    
                    if response.status_code == 200:
                        st.warning("⚠️ Feedback recorded. We'll learn from this.")
                        st.session_state.feedback_submitted = True
                except Exception as e:
                    st.error(f"Failed to submit feedback: {e}")
    
    # Correction form
    if st.session_state.get('show_correction_form', False):
        with st.form("correction_form"):
            st.markdown("**📝 Provide Correction:**")
            user_comment = st.text_area("What's wrong with this solution?", key="correction_comment")
            corrected_solution = st.text_area("Your corrected solution (optional):", key="correction_solution")
            
            if st.form_submit_button("Submit Correction"):
                problem_id = st.session_state.get('current_problem_id', '')
                
                if problem_id:
                    try:
                        import requests
                        response = requests.post(
                            "http://localhost:8000/api/feedback",
                            json={
                                "problem_id": problem_id,
                                "feedback_type": "edit",
                                "user_comment": user_comment,
                                "corrected_solution": corrected_solution
                            }
                        )
                        
                        if response.status_code == 200:
                            st.success("✅ Thank you! Your correction helps us learn.")
                            st.session_state.show_correction_form = False
                            st.session_state.feedback_submitted = True
                    except Exception as e:
                        st.error(f"Failed to submit correction: {e}")
    
    with col3:
        if st.button("🤔 Need Clarification", width='stretch'):
            st.session_state.hitl_required = True
            st.session_state.feedback = 'clarification'
            st.rerun()


def render_hitl_interface():
    """
    Render Human-in-the-Loop interface for corrections
    """
    st.markdown("""
    <div style='padding: 1.5rem; background: #fff3cd; border: 2px solid #ffc107; 
                border-radius: 12px; margin: 1rem 0;'>
        <h3 style='color: #856404; margin-top: 0;'>✋ Human Review Required</h3>
        <p style='color: #856404; margin-bottom: 0;'>
            The system needs your input to improve the solution.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    feedback_type = st.session_state.get('feedback', 'clarification')
    
    if feedback_type == 'incorrect':
        st.markdown("#### What was incorrect about the solution?")
        
        issue_type = st.multiselect(
            "Issue Type",
            ["Wrong Final Answer", "Incorrect Steps", "Missing Steps", "Wrong Method", "Calculation Error"]
        )
        
        correct_answer = st.text_input("What is the correct answer?", placeholder="e.g., x = 5")
        
        explanation = st.text_area(
            "Additional explanation (optional)",
            placeholder="Explain what went wrong or provide the correct approach...",
            height=100
        )
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("Submit Correction", type="primary", width='stretch'):
                if correct_answer:
                    # Save correction to memory
                    correction_data = {
                        'problem': st.session_state.solution['problem'],
                        'incorrect_answer': st.session_state.solution['final_answer'],
                        'correct_answer': correct_answer,
                        'issue_types': issue_type,
                        'explanation': explanation,
                        'feedback': 'corrected',
                        'timestamp': datetime.now().isoformat()
                    }
                    st.session_state.history.append(correction_data)
                    
                    st.success("✅ Correction submitted! The system will learn from this.")
                    st.session_state.hitl_required = False
                    st.session_state.feedback_submitted = True
                    st.rerun()
                else:
                    st.error("Please provide the correct answer.")
        
        with col2:
            if st.button("Cancel", width='stretch'):
                st.session_state.hitl_required = False
                st.rerun()
    
    elif feedback_type == 'clarification':
        st.markdown("#### What needs clarification?")
        
        clarification_request = st.text_area(
            "Describe what's unclear",
            placeholder="e.g., Can you explain step 3 in more detail? What formula was used?",
            height=100
        )
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("Request Clarification", type="primary", width='stretch'):
                if clarification_request:
                    st.info("🔄 Regenerating solution with more detail...")
                    
                    # Log clarification request
                    clarification_data = {
                        'problem': st.session_state.solution['problem'],
                        'clarification_request': clarification_request,
                        'timestamp': datetime.now().isoformat()
                    }
                    st.session_state.history.append(clarification_data)
                    
                    st.session_state.hitl_required = False
                    st.rerun()
                else:
                    st.error("Please describe what needs clarification.")
        
        with col2:
            if st.button("Cancel", width='stretch'):
                st.session_state.hitl_required = False
                st.rerun()


def render_memory_panel(history: List[Dict[str, Any]]):
    """
    Render the memory and history panel
    
    Args:
        history: List of historical interactions
    """
    if not history:
        st.info("📭 No history yet. Solve some problems to build your memory!")
        return
    
    st.markdown(f"### 📊 Total Interactions: {len(history)}")
    
    # Statistics
    col1, col2, col3, col4 = st.columns(4)
    
    correct_count = sum(1 for h in history if h.get('feedback') == 'correct')
    incorrect_count = sum(1 for h in history if h.get('feedback') in ['incorrect', 'corrected'])
    clarification_count = len([h for h in history if 'clarification_request' in h])
    
    with col1:
        st.metric("✅ Correct", correct_count)
    with col2:
        st.metric("❌ Corrected", incorrect_count)
    with col3:
        st.metric("🤔 Clarifications", clarification_count)
    with col4:
        accuracy = (correct_count / len(history) * 100) if history else 0
        st.metric("📈 Accuracy", f"{accuracy:.1f}%")
    
    st.markdown("---")
    
    # Filter options
    filter_type = st.selectbox(
        "Filter by",
        ["All", "Correct", "Corrected", "Clarifications"]
    )
    
    # Display history
    filtered_history = history
    if filter_type != "All":
        if filter_type == "Correct":
            filtered_history = [h for h in history if h.get('feedback') == 'correct']
        elif filter_type == "Corrected":
            filtered_history = [h for h in history if h.get('feedback') in ['incorrect', 'corrected']]
        elif filter_type == "Clarifications":
            filtered_history = [h for h in history if 'clarification_request' in h]
    
    st.markdown(f"### 📜 History ({len(filtered_history)} items)")
    
    for i, record in enumerate(reversed(filtered_history), 1):
        with st.expander(f"{i}. {record.get('problem', 'Problem')[:60]}... - {record.get('timestamp', '')[:19]}"):
            st.markdown(f"**Problem:** {record.get('problem', 'N/A')}")
            
            if 'answer' in record:
                st.markdown(f"**Answer:** {record.get('answer')}")
            
            if 'correct_answer' in record:
                st.markdown(f"**Incorrect Answer:** {record.get('incorrect_answer')}")
                st.markdown(f"**Correct Answer:** {record.get('correct_answer')}")
                st.markdown(f"**Explanation:** {record.get('explanation', 'N/A')}")
            
            if 'clarification_request' in record:
                st.markdown(f"**Clarification Request:** {record.get('clarification_request')}")
            
            feedback_emoji = {
                'correct': '✅',
                'incorrect': '❌',
                'corrected': '🔄',
                'clarification': '🤔'
            }.get(record.get('feedback'), '❓')
            
            st.markdown(f"**Feedback:** {feedback_emoji} {record.get('feedback', 'N/A').title()}")
    
    # Export button
    if st.button("💾 Export History as JSON", width='stretch'):
        json_str = json.dumps(history, indent=2)
        st.download_button(
            label="Download JSON",
            data=json_str,
            file_name=f"math_mentor_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json"
        )
