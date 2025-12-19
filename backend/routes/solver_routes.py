"""
Solver routes
"""

from fastapi import APIRouter, HTTPException
from controllers.solver_controller import SolverController
from schemas.request_response_schemas import SolveRequest
from middleware.security import sanitize_for_llm, validate_confidence_score

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
        # Validate and sanitize problem text
        sanitized_problem = sanitize_for_llm(request.problem, "problem")
        
        # Validate corrected problem if provided
        corrected_problem = None
        if request.corrected_problem:
            corrected_problem = sanitize_for_llm(request.corrected_problem, "corrected_problem")
        
        # Validate confidence scores
        ocr_confidence = validate_confidence_score(request.ocr_confidence, "ocr_confidence")
        asr_confidence = validate_confidence_score(request.asr_confidence, "asr_confidence")
        
        result = controller.solve_problem(
            problem=sanitized_problem,
            settings=request.settings,
            request_review=request.request_review,
            force_continue=request.force_continue,
            corrected_problem=corrected_problem,
            ocr_confidence=ocr_confidence,
            asr_confidence=asr_confidence
        )
        
        return result
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
