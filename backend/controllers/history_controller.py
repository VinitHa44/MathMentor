"""
History Controller - Request handling and orchestration for History
"""

from typing import Dict, Any
from usecases.history_usecase import HistoryUseCase
from utils.logger import get_logger

logger = get_logger(__name__)


class HistoryController:
    """Controller for history operations"""
    
    def __init__(self):
        """Initialize history controller"""
        self.usecase = HistoryUseCase()
    
    def get_problem_history(self, limit: int = 10) -> Dict[str, Any]:
        """
        Get problem history
        
        Args:
            limit: Number of problems to return
        
        Returns:
            Problem history
        """
        return self.usecase.get_problem_history(limit=limit)
    
    def get_similar_problems(self, problem_id: str, limit: int = 5) -> Dict[str, Any]:
        """
        Get similar problems
        
        Args:
            problem_id: Problem ID
            limit: Number of similar problems
        
        Returns:
            Similar problems
        """
        return self.usecase.get_similar_problems(problem_id=problem_id, limit=limit)
