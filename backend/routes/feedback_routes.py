"""
Feedback routes
"""

from fastapi import APIRouter, HTTPException
from controllers.feedback_controller import FeedbackController
from schemas.request_response_schemas import FeedbackRequest, FeedbackResponse
from middleware.security import validate_problem_id, validate_text_input

router = APIRouter()
controller = FeedbackController()


@router.post("/feedback", response_model=FeedbackResponse)
async def submit_feedback(request: FeedbackRequest):
    """
    Submit user feedback on solution (HITL)
    
    Args:
        request: FeedbackRequest with problem_id and feedback details
    
    Returns:
        Confirmation of feedback storage
    """
    try:
        # Validate problem ID
        problem_id = validate_problem_id(request.problem_id)
        
        # Validate feedback type
        valid_types = ['approve', 'edit', 'reject']
        if request.feedback_type not in valid_types:
            raise HTTPException(status_code=400, detail=f"Invalid feedback_type. Must be one of: {valid_types}")
        
        # Validate optional fields
        user_comment = None
        if request.user_comment:
            user_comment = validate_text_input(request.user_comment, "user_comment")
        
        corrected_solution = None
        if request.corrected_solution:
            corrected_solution = validate_text_input(request.corrected_solution, "corrected_solution")
        
        result = controller.submit_feedback(
            problem_id=problem_id,
            feedback_type=request.feedback_type,
            user_comment=user_comment,
            corrected_solution=corrected_solution
        )
        
        return FeedbackResponse(**result)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
