"""
History routes
"""

from fastapi import APIRouter, HTTPException
from controllers.history_controller import HistoryController
from schemas.request_response_schemas import HistoryResponse, SimilarProblemsResponse
from middleware.security import validate_limit, validate_problem_id

router = APIRouter()
controller = HistoryController()


@router.get("/history", response_model=HistoryResponse)
async def get_history(limit: int = 10):
    """
    Get problem-solving history
    
    Args:
        limit: Number of recent problems to return
    
    Returns:
        List of recent problems
    """
    try:
        result = controller.get_problem_history(limit=limit)
        return HistoryResponse(**result)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/similar/{problem_id}", response_model=SimilarProblemsResponse)
async def get_similar_problems(problem_id: str, limit: int = 5):
    """
    Get similar problems from history
    
    Args:
        problem_id: Problem ID to find similar problems for
        limit: Number of similar problems to return
    
    Returns:
        List of similar problems
    """
    try:
        result = controller.get_similar_problems(problem_id=problem_id, limit=limit)
        return SimilarProblemsResponse(**result)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
