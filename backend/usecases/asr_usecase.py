"""
ASR UseCase - Business logic for audio transcription
"""

from typing import Dict, Any
import base64
from services.asr_service import ASRService
from utils.logger import get_logger

logger = get_logger(__name__)


class ASRUseCase:
    """UseCase for ASR operations"""
    
    def __init__(self):
        """Initialize ASR use case"""
        self.asr_service = ASRService()
    
    def transcribe_from_base64(self, audio_base64: str) -> Dict[str, Any]:
        """
        Transcribe audio from base64 encoded data
        
        Args:
            audio_base64: Base64 encoded audio
        
        Returns:
            Dict with text, confidence, and status
        """
        try:
            logger.info("Processing ASR request from base64 audio")
            
            # Decode base64 audio
            audio_data = base64.b64decode(audio_base64)
            
            # Perform ASR
            result = self.asr_service.transcribe_audio(audio_data)
            
            logger.info(f"ASR completed with confidence: {result['confidence']}")
            
            return {
                "text": result["text"],
                "confidence": result["confidence"],
                "status": "success"
            }
        
        except Exception as e:
            logger.error(f"ASR processing failed: {str(e)}")
            raise Exception(f"ASR processing failed: {str(e)}")
    
    def transcribe_from_bytes(self, audio_bytes: bytes) -> Dict[str, Any]:
        """
        Transcribe audio from bytes
        
        Args:
            audio_bytes: Audio data as bytes
        
        Returns:
            Dict with text, confidence, and status
        """
        try:
            logger.info("Processing ASR request from uploaded audio")
            
            # Perform ASR
            result = self.asr_service.transcribe_audio(audio_bytes)
            
            logger.info(f"ASR completed with confidence: {result['confidence']}")
            
            return {
                "text": result["text"],
                "confidence": result["confidence"],
                "status": "success"
            }
        
        except Exception as e:
            logger.error(f"ASR processing failed: {str(e)}")
            raise Exception(f"ASR processing failed: {str(e)}")
