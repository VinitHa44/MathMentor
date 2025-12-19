"""
Parser routes
"""

from fastapi import APIRouter, HTTPException
from controllers.parser_controller import ParserController
from schemas.request_response_schemas import TextRequest, ParserResponse
from middleware.security import sanitize_for_llm

router = APIRouter()
controller = ParserController()


@router.post("/parse", response_model=ParserResponse)
async def parse_problem(request: TextRequest):
    """
    Parse math problem text into structured format
    
    Args:
        request: TextRequest with problem text
    
    Returns:
        ParserResponse with structured problem data
    """
    try:
        # Validate and sanitize input
        sanitized_text = sanitize_for_llm(request.text, "problem text")
        
        result = controller.parse_problem(sanitized_text)
        return ParserResponse(**result)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
