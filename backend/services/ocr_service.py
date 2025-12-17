"""
OCR Service - Extract text from images
Supports multiple OCR backends: Tesseract, EasyOCR, PaddleOCR
"""

from PIL import Image
import pytesseract
import re
import numpy as np
from typing import Dict, Any
import os

# Set Tesseract path for Windows (adjust if installed elsewhere)
if os.name == 'nt':  # Windows
    tesseract_paths = [
        r'C:\Program Files\Tesseract-OCR\tesseract.exe',
        r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe',
        r'C:\Users\vinit\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
    ]
    for path in tesseract_paths:
        if os.path.exists(path):
            pytesseract.pytesseract.tesseract_cmd = path
            break

class OCRService:
    """Service for extracting text from images"""
    
    def __init__(self, provider: str = "tesseract"):
        """
        Initialize OCR service
        
        Args:
            provider: OCR provider to use (tesseract, easyocr, paddleocr)
        """
        self.provider = provider.lower()
        
        if self.provider == "easyocr":
            try:
                import easyocr
                self.reader = easyocr.Reader(['en'])
            except ImportError:
                print("EasyOCR not installed, falling back to Tesseract")
                self.provider = "tesseract"
        
        elif self.provider == "paddleocr":
            try:
                from paddleocr import PaddleOCR
                self.reader = PaddleOCR(use_angle_cls=True, lang='en')
            except ImportError:
                print("PaddleOCR not installed, falling back to Tesseract")
                self.provider = "tesseract"
    
    def extract_text(self, image: Image.Image) -> Dict[str, Any]:
        """
        Extract text from image using configured OCR provider
        
        Args:
            image: PIL Image object
        
        Returns:
            Dict with extracted text and confidence
        """
        if self.provider == "tesseract":
            return self._extract_with_tesseract(image)
        elif self.provider == "easyocr":
            return self._extract_with_easyocr(image)
        elif self.provider == "paddleocr":
            return self._extract_with_paddleocr(image)
        else:
            return self._extract_with_tesseract(image)
    
    def _extract_with_tesseract(self, image: Image.Image) -> Dict[str, Any]:
        """Extract text using Tesseract OCR"""
        try:
            # Get detailed data with confidence
            data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
            
            # Extract text
            text = pytesseract.image_to_string(image)
            
            # Debug output
            print(f"Tesseract extracted text: '{text}'")
            print(f"Text length: {len(text)}")
            
            # Calculate average confidence
            confidences = [int(conf) for conf in data['conf'] if int(conf) > 0]
            avg_confidence = sum(confidences) / len(confidences) / 100 if confidences else 0.0
            
            # Clean the text
            cleaned_text = self._clean_ocr_text(text)
            
            # If no text found, return placeholder
            if not cleaned_text.strip():
                cleaned_text = "No text detected in image. Please ensure image is clear and contains text."
                avg_confidence = 0.0
            
            return {
                "text": cleaned_text,
                "confidence": round(avg_confidence, 2),
                "provider": "tesseract"
            }
        
        except Exception as e:
            print(f"Tesseract error: {str(e)}")
            return {
                "text": f"OCR Error: {str(e)}. Make sure Tesseract is installed.",
                "confidence": 0.0,
                "error": str(e),
                "provider": "tesseract"
            }
    
    def _extract_with_easyocr(self, image: Image.Image) -> Dict[str, Any]:
        """Extract text using EasyOCR"""
        try:
            # Convert PIL Image to numpy array
            img_array = np.array(image)
            
            # Perform OCR
            results = self.reader.readtext(img_array)
            
            # Combine text and calculate average confidence
            texts = []
            confidences = []
            
            for (bbox, text, conf) in results:
                texts.append(text)
                confidences.append(conf)
            
            combined_text = " ".join(texts)
            avg_confidence = sum(confidences) / len(confidences) if confidences else 0.0
            
            # Clean the text
            cleaned_text = self._clean_ocr_text(combined_text)
            
            return {
                "text": cleaned_text,
                "confidence": round(avg_confidence, 2),
                "provider": "easyocr"
            }
        
        except Exception as e:
            return {
                "text": "",
                "confidence": 0.0,
                "error": str(e),
                "provider": "easyocr"
            }
    
    def _extract_with_paddleocr(self, image: Image.Image) -> Dict[str, Any]:
        """Extract text using PaddleOCR"""
        try:
            # Convert PIL Image to numpy array
            img_array = np.array(image)
            
            # Perform OCR
            results = self.reader.ocr(img_array, cls=True)
            
            # Extract text and confidence
            texts = []
            confidences = []
            
            if results and results[0]:
                for line in results[0]:
                    texts.append(line[1][0])
                    confidences.append(line[1][1])
            
            combined_text = " ".join(texts)
            avg_confidence = sum(confidences) / len(confidences) if confidences else 0.0
            
            # Clean the text
            cleaned_text = self._clean_ocr_text(combined_text)
            
            return {
                "text": cleaned_text,
                "confidence": round(avg_confidence, 2),
                "provider": "paddleocr"
            }
        
        except Exception as e:
            return {
                "text": "",
                "confidence": 0.0,
                "error": str(e),
                "provider": "paddleocr"
            }
    
    def _clean_ocr_text(self, text: str) -> str:
        """
        Clean OCR output text
        
        Args:
            text: Raw OCR text
        
        Returns:
            Cleaned text
        """
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        
        # Remove leading/trailing whitespace
        text = text.strip()
        
        # Fix common OCR mistakes in math
        replacements = {
            ' x ': ' × ',  # Multiplication
            ' / ': ' ÷ ',  # Division
            '|': 'l',      # Common mistake
        }
        
        for old, new in replacements.items():
            text = text.replace(old, new)
        
        return text
    
    def preprocess_image(self, image: Image.Image) -> Image.Image:
        """
        Preprocess image for better OCR results
        
        Args:
            image: Input image
        
        Returns:
            Preprocessed image
        """
        # Convert to grayscale
        image = image.convert('L')
        
        # Increase contrast
        from PIL import ImageEnhance
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(2.0)
        
        # Resize if too small
        if image.size[0] < 300 or image.size[1] < 300:
            scale = max(300 / image.size[0], 300 / image.size[1])
            new_size = (int(image.size[0] * scale), int(image.size[1] * scale))
            image = image.resize(new_size, Image.Resampling.LANCZOS)
        
        return image
