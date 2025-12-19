"""
ASR routes
"""

from fastapi import APIRouter, File, UploadFile, HTTPException
from controllers.asr_controller import ASRController
from schemas.request_response_schemas import ASRRequest, ASRResponse

router = APIRouter()
controller = ASRController()


@router.post("/transcribe", response_model=ASRResponse)
async def transcribe_audio(request: ASRRequest):
    """
    Transcribe audio to text using ASR
    
    Args:
        request: ASRRequest with base64 encoded audio
    
    Returns:
        ASRResponse with transcribed text and confidence
    """
    try:
        result = controller.transcribe_from_base64(request.audio_base64)
        return ASRResponse(**result)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/transcribe/upload")
async def transcribe_audio_upload(file: UploadFile = File(...)):
    """
    Transcribe uploaded audio file
    
    Args:
        file: Uploaded audio file
    
    Returns:
        Transcribed text and confidence
    """
    try:
        # Read audio file
        contents = await file.read()
        
        # Transcribe
        result = controller.transcribe_from_bytes(contents)
        
        return result
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
