"""
Intent Router Agent - Routes requests to appropriate agents
"""

from typing import Dict, Any, Optional
from services.llm_service import LLMService

class IntentRouterAgent:
    """Agent for routing user intents to appropriate downstream agents"""
    
    def __init__(self, llm_service: LLMService):
        """
        Initialize Intent Router Agent
        
        Args:
            llm_service: LLM service for intent classification
        """
        self.llm = llm_service
    
    def route(self, parsed_data: Dict[str, Any], user_message: Optional[str] = None) -> Dict[str, Any]:
        """
        Route intent based on parsed data and optional user message
        
        Args:
            parsed_data: Parsed problem data from Parser Agent
            user_message: Optional user message for additional context
        
        Returns:
            Routing decision with target agents and parameters
        """
        problem_text = parsed_data.get('problem_text', '')
        topic = parsed_data.get('topic', 'general')
        needs_clarification = parsed_data.get('needs_clarification', False)
        
        # If needs clarification, route to HITL
        if needs_clarification:
            return {
                "primary_agent": "hitl",
                "reason": "Problem needs clarification",
                "clarification_needed": parsed_data.get('clarification_reason', 'Unclear problem statement'),
                "next_agents": []
            }
        
        # Check if user is asking for explanation only
        if user_message and self._is_explanation_request(user_message):
            return {
                "primary_agent": "explainer",
                "reason": "User requested explanation",
                "next_agents": [],
                "skip_solving": True
            }
        
        # Check if user is asking for verification only
        if user_message and self._is_verification_request(user_message):
            return {
                "primary_agent": "verifier",
                "reason": "User requested verification",
                "next_agents": [],
                "needs_solution": True  # Need solution to verify
            }
        
        # Standard flow: Solve -> Verify -> Explain
        return {
            "primary_agent": "solver",
            "reason": f"Standard problem solving for {topic}",
            "next_agents": ["verifier", "explainer"],
            "pipeline": "full"  # Full pipeline
        }
    
    def _is_explanation_request(self, message: str) -> bool:
        """Check if user is asking for explanation"""
        message_lower = message.lower()
        explanation_keywords = [
            "explain",
            "why",
            "how does",
            "help me understand",
            "what does",
            "clarify",
            "tell me about"
        ]
        return any(keyword in message_lower for keyword in explanation_keywords)
    
    def _is_verification_request(self, message: str) -> bool:
        """Check if user is asking for verification"""
        message_lower = message.lower()
        verification_keywords = [
            "check",
            "verify",
            "correct",
            "is this right",
            "validate",
            "review"
        ]
        return any(keyword in message_lower for keyword in verification_keywords)
