"""
ASR Service - Convert speech to text
Uses Groq API (Whisper) for audio transcription
"""

import tempfile
import os
from typing import Dict, Any
from utils.math_speech_converter import MathSpeechConverter

# Try importing Groq
try:
    from groq import Groq
    GROQ_AVAILABLE = True
except ImportError:
    GROQ_AVAILABLE = False

class ASRService:
    """Service for transcribing audio to text using Groq API"""
    
    def __init__(self, model_size: str = "whisper-large-v3"):
        """
        Initialize ASR service with Groq API
        
        Args:
            model_size: Whisper model on Groq (whisper-large-v3)
        """
        self.model_size = model_size
        self.math_converter = MathSpeechConverter()
        
        # Initialize Groq client if API key is available
        groq_api_key = os.getenv("GROQ_API_KEY")
        
        if not GROQ_AVAILABLE:
            print("⚠️ WARNING: Groq package not installed!")
            print("Install with: pip install groq")
            self.client = None
        elif not groq_api_key:
            print("⚠️ WARNING: GROQ_API_KEY not found in environment!")
            print("Please set GROQ_API_KEY in your .env file")
            self.client = None
        else:
            try:
                self.client = Groq(api_key=groq_api_key)
                print(f"✅ Groq ASR client initialized with model: {model_size}")
            except Exception as e:
                print(f"❌ Error initializing Groq client: {e}")
                self.client = None
    
    def transcribe_audio(self, audio_data: bytes) -> Dict[str, Any]:
        """
        Transcribe audio to text using Groq API
        
        Args:
            audio_data: Raw audio bytes
        
        Returns:
            Dict with transcribed text and confidence
        """
        if not GROQ_AVAILABLE:
            return {
                "text": "Groq package not installed. Please install with: pip install groq",
                "confidence": 0.0,
                "error": "Groq package not available",
                "provider": "groq"
            }
        
        if self.client is None:
            return {
                "text": "Groq API key not configured. Please set GROQ_API_KEY environment variable.",
                "confidence": 0.0,
                "error": "Groq client not initialized",
                "provider": "groq"
            }
        
        try:
            # Debug output
            print(f"Received audio data: {len(audio_data)} bytes")
            
            # Save audio to temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
                temp_audio.write(audio_data)
                temp_audio_path = temp_audio.name
            
            print(f"Saved to temp file: {temp_audio_path}")
            
            # Transcribe audio
            result = self.model.transcribe(
                temp_audio_path,
                language="en",
                task="transcribe",
                verbose=False
            )
            
            print(f"Whisper result: {result.get('text', '')}")
            
            # Clean up temporary file
            os.unlink(temp_audio_path)
            
            
            # Transcribe using Groq API
            print(f"Transcribing with Groq ({self.model_size})...")
            
            with open(temp_audio_path, "rb") as audio_file:
                transcription = self.client.audio.transcriptions.create(
                    file=("audio.mp3", audio_file),
                    model=self.model_size,
                    response_format="verbose_json"
                )
            
            # Clean up temp file
            os.unlink(temp_audio_path)
            print("✅ Transcription successful")
            
            # Extract text
            text = transcription.text.strip()
            
            # Calculate confidence from Groq response (if available)
            # Groq doesn't always provide confidence, default to 0.90
            avg_confidence = 0.90
            
            # Convert spoken math to mathematical notation
            converted_text = self.math_converter.convert(text)
            
            # If no text found
            if not converted_text.strip():
                converted_text = "No speech detected in audio. Please ensure audio is clear."
                avg_confidence = 0.0
            
            return {
                "text": converted_text,
                "original_transcript": text,  # Keep original for reference
                "confidence": round(avg_confidence, 2),
                "provider": "groq",
                "language": getattr(transcription, "language", "en"),
                "math_notation_applied": text.lower() != converted_text.lower()
            }
        
        except Exception as e:
            print(f"ASR error: {str(e)}")
            # Clean up temp file on error
            try:
                if 'temp_audio_path' in locals():
                    os.unlink(temp_audio_path)
            except:
                pass
            
            return {
                "text": f"ASR Error: {str(e)}",
                "confidence": 0.0,
                "error": str(e),
                "provider": "groq"
            }
    
    def enhance_audio(self, audio_data: bytes) -> bytes:
        """
        Enhance audio quality (placeholder for noise reduction, etc.)
        
        Args:
            audio_data: Raw audio bytes
        
        Returns:
            Enhanced audio bytes
        """
        # TODO: Implement audio enhancement if needed
        # Could use noisereduce or similar libraries
        return audio_data
