"""
OCR UseCase - Business logic for OCR processing
"""

from typing import Dict, Any
import base64
from io import BytesIO
from PIL import Image
from services.ocr_service import OCRService
from utils.logger import get_logger

logger = get_logger(__name__)


class OCRUseCase:
    """UseCase for OCR operations"""
    
    def __init__(self):
        """Initialize OCR use case"""
        self.ocr_service = OCRService(provider="easyocr")
    
    def extract_text_from_base64(self, image_base64: str) -> Dict[str, Any]:
        """
        Extract text from base64 encoded image
        
        Args:
            image_base64: Base64 encoded image
        
        Returns:
            Dict with text, confidence, and status
        """
        try:
            logger.info("Processing OCR request from base64 image")
            
            # Decode base64 image
            image_data = base64.b64decode(image_base64)
            image = Image.open(BytesIO(image_data))
            
            # Perform OCR
            result = self.ocr_service.extract_text(image)
            
            logger.info(f"OCR completed with confidence: {result['confidence']}")
            
            return {
                "text": result["text"],
                "confidence": result["confidence"],
                "status": "success"
            }
        
        except Exception as e:
            logger.error(f"OCR processing failed: {str(e)}")
            raise Exception(f"OCR processing failed: {str(e)}")
    
    def extract_text_from_image(self, image: Image.Image) -> Dict[str, Any]:
        """
        Extract text from PIL Image
        
        Args:
            image: PIL Image object
        
        Returns:
            Dict with text, confidence, and status
        """
        try:
            logger.info("Processing OCR request from uploaded image")
            
            # Perform OCR
            result = self.ocr_service.extract_text(image)
            
            logger.info(f"OCR completed with confidence: {result['confidence']}")
            
            return {
                "text": result["text"],
                "confidence": result["confidence"],
                "status": "success"
            }
        
        except Exception as e:
            logger.error(f"OCR processing failed: {str(e)}")
            raise Exception(f"OCR processing failed: {str(e)}")
