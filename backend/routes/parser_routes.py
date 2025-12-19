"""
Parser routes
"""

from fastapi import APIRouter, HTTPException
from controllers.parser_controller import ParserController
from schemas.request_response_schemas import TextRequest, ParserResponse

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
        result = controller.parse_problem(request.text)
        return ParserResponse(**result)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
