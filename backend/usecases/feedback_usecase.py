"""
Feedback UseCase - Business logic for user feedback
"""

from typing import Dict, Any, Optional
from repositories.memory_repository import MemoryRepository
from utils.logger import get_logger

logger = get_logger(__name__)


class FeedbackUseCase:
    """UseCase for feedback operations"""
    
    def __init__(self):
        """Initialize feedback use case"""
        self.memory_repo = MemoryRepository(storage_dir="memory_store")
    
    def submit_feedback(
        self,
        problem_id: str,
        feedback_type: str,
        user_comment: Optional[str] = None,
        corrected_solution: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Submit user feedback on solution
        
        Args:
            problem_id: Problem ID
            feedback_type: Type of feedback (approve, edit, reject)
            user_comment: User comment
            corrected_solution: Corrected solution
        
        Returns:
            Confirmation of feedback storage
        """
        try:
            logger.info(f"Storing feedback for problem {problem_id}")
            
            self.memory_repo.store_feedback(
                problem_id=problem_id,
                feedback_type=feedback_type,
                user_comment=user_comment,
                corrected_solution=corrected_solution
            )
            
            # If user provided corrected solution, log learning signal
            if corrected_solution:
                logger.info(f"Learning from correction: {user_comment or 'No comment'}")
            
            logger.info("Feedback stored successfully")
            
            return {
                "status": "success",
                "message": "Feedback stored successfully",
                "problem_id": problem_id
            }
        
        except Exception as e:
            logger.error(f"Feedback storage failed: {str(e)}")
            raise Exception(f"Feedback storage failed: {str(e)}")
