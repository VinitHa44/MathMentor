"""
Memory Repository - Data access layer for memory operations
Handles all interactions with memory store (files/database)
"""

from typing import Dict, Any, List, Optional
from services.memory_service import MemoryService


class MemoryRepository:
    """Repository for memory data access"""
    
    def __init__(self, storage_dir: str = "memory_store"):
        """
        Initialize memory repository
        
        Args:
            storage_dir: Directory for memory storage
        """
        self.memory_service = MemoryService(storage_dir=storage_dir)
    
    def store_problem(
        self,
        problem_text: str,
        parsed_data: Dict[str, Any],
        solution: Dict[str, Any],
        verification: Dict[str, Any],
        retrieved_context: List[Dict[str, Any]],
        agent_trace: List[Dict[str, Any]]
    ) -> str:
        """
        Store problem in memory
        
        Args:
            problem_text: The problem text
            parsed_data: Parsed problem data
            solution: Solution data
            verification: Verification data
            retrieved_context: RAG context
            agent_trace: Agent execution trace
        
        Returns:
            Problem ID
        """
        return self.memory_service.store_problem(
            problem_text=problem_text,
            parsed_data=parsed_data,
            solution=solution,
            verification=verification,
            retrieved_context=retrieved_context,
            agent_trace=agent_trace
        )
    
    def find_similar_problems(
        self,
        topic: str,
        variables: Dict[str, Any],
        limit: int = 3
    ) -> List[Dict[str, Any]]:
        """
        Find similar problems from memory
        
        Args:
            topic: Problem topic
            variables: Problem variables
            limit: Maximum number of results
        
        Returns:
            List of similar problems
        """
        return self.memory_service.find_similar_problems(
            topic=topic,
            variables=variables,
            limit=limit
        )
    
    def get_solution_patterns(self, topic: str) -> List[Dict[str, Any]]:
        """
        Get solution patterns for a topic
        
        Args:
            topic: Problem topic
        
        Returns:
            List of solution patterns
        """
        return self.memory_service.get_solution_patterns(topic)
    
    def store_feedback(
        self,
        problem_id: str,
        feedback_type: str,
        user_comment: Optional[str] = None,
        corrected_solution: Optional[str] = None
    ) -> None:
        """
        Store user feedback
        
        Args:
            problem_id: Problem ID
            feedback_type: Type of feedback
            user_comment: User comment
            corrected_solution: Corrected solution
        """
        self.memory_service.store_feedback(
            problem_id=problem_id,
            feedback_type=feedback_type,
            user_comment=user_comment,
            corrected_solution=corrected_solution
        )
    
    def get_problem_history(self, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Get problem history
        
        Args:
            limit: Maximum number of problems to return
        
        Returns:
            List of problems
        """
        return self.memory_service.get_problem_history(limit=limit)
