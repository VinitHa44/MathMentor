"""
History UseCase - Business logic for problem history and similar problems
"""

from typing import Dict, Any, List
from repositories.memory_repository import MemoryRepository
from utils.logger import get_logger

logger = get_logger(__name__)


class HistoryUseCase:
    """UseCase for history operations"""
    
    def __init__(self):
        """Initialize history use case"""
        self.memory_repo = MemoryRepository(storage_dir="memory_store")
    
    def get_problem_history(self, limit: int = 10) -> Dict[str, Any]:
        """
        Get problem-solving history
        
        Args:
            limit: Number of recent problems to return
        
        Returns:
            List of recent problems
        """
        try:
            logger.info(f"Retrieving problem history (limit: {limit})")
            
            history = self.memory_repo.get_problem_history(limit=limit)
            
            logger.info(f"Retrieved {len(history)} problems from history")
            
            return {
                "status": "success",
                "count": len(history),
                "problems": history
            }
        
        except Exception as e:
            logger.error(f"History retrieval failed: {str(e)}")
            raise Exception(f"History retrieval failed: {str(e)}")
    
    def get_similar_problems(self, problem_id: str, limit: int = 5) -> Dict[str, Any]:
        """
        Get similar problems from history
        
        Args:
            problem_id: Problem ID to find similar problems for
            limit: Number of similar problems to return
        
        Returns:
            List of similar problems
        """
        try:
            logger.info(f"Finding similar problems for {problem_id}")
            
            # Get the problem
            history = self.memory_repo.get_problem_history(limit=100)
            target_problem = None
            
            for problem in history:
                if problem['id'] == problem_id:
                    target_problem = problem
                    break
            
            if not target_problem:
                logger.error(f"Problem {problem_id} not found")
                raise Exception(f"Problem not found: {problem_id}")
            
            # Find similar
            similar = self.memory_repo.find_similar_problems(
                topic=target_problem['topic'],
                variables=target_problem.get('variables', {}),
                limit=limit
            )
            
            logger.info(f"Found {len(similar)} similar problems")
            
            return {
                "status": "success",
                "count": len(similar),
                "similar_problems": similar
            }
        
        except Exception as e:
            logger.error(f"Similar problems retrieval failed: {str(e)}")
            raise Exception(f"Similar problems retrieval failed: {str(e)}")
