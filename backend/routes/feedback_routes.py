"""
Feedback routes
"""

from fastapi import APIRouter, HTTPException
from controllers.feedback_controller import FeedbackController
from schemas.request_response_schemas import FeedbackRequest, FeedbackResponse

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
        result = controller.submit_feedback(
            problem_id=request.problem_id,
            feedback_type=request.feedback_type,
            user_comment=request.user_comment,
            corrected_solution=request.corrected_solution
        )
        
        return FeedbackResponse(**result)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
