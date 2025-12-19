"""
Solver routes
"""

from fastapi import APIRouter, HTTPException
from controllers.solver_controller import SolverController
from schemas.request_response_schemas import SolveRequest

router = APIRouter()
controller = SolverController()


@router.post("/solve")
async def solve_problem(request: SolveRequest):
    """
    Solve math problem using RAG + Multi-Agent System
    
    Args:
        request: SolveRequest with problem and settings
    
    Returns:
        Complete solution with RAG context, agent trace, verification
    """
    try:
        result = controller.solve_problem(
            problem=request.problem,
            settings=request.settings,
            request_review=request.request_review,
            force_continue=request.force_continue,
            corrected_problem=request.corrected_problem,
            ocr_confidence=request.ocr_confidence,
            asr_confidence=request.asr_confidence
        )
        
        return result
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
