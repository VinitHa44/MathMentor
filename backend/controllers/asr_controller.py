"""
ASR Controller - Request handling and orchestration for ASR
"""

from typing import Dict, Any
from usecases.asr_usecase import ASRUseCase
from utils.logger import get_logger

logger = get_logger(__name__)


class ASRController:
    """Controller for ASR operations"""
    
    def __init__(self):
        """Initialize ASR controller"""
        self.usecase = ASRUseCase()
    
    def transcribe_from_base64(self, audio_base64: str) -> Dict[str, Any]:
        """
        Transcribe audio from base64
        
        Args:
            audio_base64: Base64 encoded audio
        
        Returns:
            ASR result
        """
        return self.usecase.transcribe_from_base64(audio_base64)
    
    def transcribe_from_bytes(self, audio_bytes: bytes) -> Dict[str, Any]:
        """
        Transcribe audio from bytes
        
        Args:
            audio_bytes: Audio data as bytes
        
        Returns:
            ASR result
        """
        return self.usecase.transcribe_from_bytes(audio_bytes)
