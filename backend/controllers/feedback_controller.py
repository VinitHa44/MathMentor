"""
Feedback Controller - Request handling and orchestration for Feedback
"""

from typing import Dict, Any, Optional
from usecases.feedback_usecase import FeedbackUseCase
from utils.logger import get_logger

logger = get_logger(__name__)


class FeedbackController:
    """Controller for feedback operations"""
    
    def __init__(self):
        """Initialize feedback controller"""
        self.usecase = FeedbackUseCase()
    
    def submit_feedback(
        self,
        problem_id: str,
        feedback_type: str,
        user_comment: Optional[str] = None,
        corrected_solution: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Submit user feedback
        
        Args:
            problem_id: Problem ID
            feedback_type: Type of feedback
            user_comment: User comment
            corrected_solution: Corrected solution
        
        Returns:
            Confirmation
        """
        return self.usecase.submit_feedback(
            problem_id=problem_id,
            feedback_type=feedback_type,
            user_comment=user_comment,
            corrected_solution=corrected_solution
        )
