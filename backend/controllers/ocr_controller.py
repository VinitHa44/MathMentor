"""
OCR Controller - Request handling and orchestration for OCR
"""

from typing import Dict, Any
from PIL import Image
from usecases.ocr_usecase import OCRUseCase
from utils.logger import get_logger

logger = get_logger(__name__)


class OCRController:
    """Controller for OCR operations"""
    
    def __init__(self):
        """Initialize OCR controller"""
        self.usecase = OCRUseCase()
    
    def extract_from_base64(self, image_base64: str) -> Dict[str, Any]:
        """
        Extract text from base64 image
        
        Args:
            image_base64: Base64 encoded image
        
        Returns:
            OCR result
        """
        return self.usecase.extract_text_from_base64(image_base64)
    
    def extract_from_image(self, image: Image.Image) -> Dict[str, Any]:
        """
        Extract text from PIL Image
        
        Args:
            image: PIL Image object
        
        Returns:
            OCR result
        """
        return self.usecase.extract_text_from_image(image)
