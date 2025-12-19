"""
OCR routes
"""

from fastapi import APIRouter, File, UploadFile, HTTPException
from io import BytesIO
from PIL import Image
from controllers.ocr_controller import OCRController
from schemas.request_response_schemas import OCRRequest, OCRResponse

router = APIRouter()
controller = OCRController()


@router.post("/ocr", response_model=OCRResponse)
async def extract_text_from_image(request: OCRRequest):
    """
    Extract text from image using OCR
    
    Args:
        request: OCRRequest with base64 encoded image
    
    Returns:
        OCRResponse with extracted text and confidence
    """
    try:
        result = controller.extract_from_base64(request.image_base64)
        return OCRResponse(**result)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/ocr/upload")
async def extract_text_from_upload(file: UploadFile = File(...)):
    """
    Extract text from uploaded image file
    
    Args:
        file: Uploaded image file
    
    Returns:
        Extracted text and confidence
    """
    try:
        # Read image file
        contents = await file.read()
        image = Image.open(BytesIO(contents))
        
        # Extract text
        result = controller.extract_from_image(image)
        
        return result
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
