"""
ASR Service - Convert speech to text
Uses OpenAI Whisper for audio transcription
"""

import whisper
import tempfile
import os
import shutil
import subprocess
from typing import Dict, Any
import numpy as np

class ASRService:
    """Service for transcribing audio to text"""
    
    def __init__(self, model_size: str = "base"):
        """
        Initialize ASR service with Whisper
        
        Args:
            model_size: Whisper model size (tiny, base, small, medium, large)
        """
        self.model_size = model_size
        self.ffmpeg_available = self._check_ffmpeg()
        
        if not self.ffmpeg_available:
            print("⚠️ WARNING: FFmpeg not found in system PATH!")
            print("Audio transcription requires FFmpeg to be installed.")
            print("Please install FFmpeg:")
            print("1. Download from: https://www.gyan.dev/ffmpeg/builds/")
            print("2. Extract and add to system PATH")
            print("3. Or use: winget install FFmpeg")
            self.model = None
            return
        
        try:
            print(f"Loading Whisper model: {model_size}...")
            self.model = whisper.load_model(model_size)
            print(f"✅ Whisper model '{model_size}' loaded successfully")
        except Exception as e:
            print(f"❌ Error loading Whisper model: {e}")
            self.model = None
    
    def _check_ffmpeg(self) -> bool:
        """Check if FFmpeg is available in system PATH"""
        try:
            result = subprocess.run(
                ["ffmpeg", "-version"],
                capture_output=True,
                timeout=5
            )
            return result.returncode == 0
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return False
    
    def transcribe_audio(self, audio_data: bytes) -> Dict[str, Any]:
        """
        Transcribe audio to text
        
        Args:
            audio_data: Raw audio bytes
        
        Returns:
            Dict with transcribed text and confidence
        """
        if not self.ffmpeg_available:
            return {
                "text": "FFmpeg is not installed. Please install FFmpeg to use audio transcription.\n\n"
                        "Installation options:\n"
                        "1. Download from: https://www.gyan.dev/ffmpeg/builds/\n"
                        "2. Extract and add bin folder to system PATH\n"
                        "3. Or use: winget install FFmpeg\n"
                        "4. Restart the backend after installation",
                "confidence": 0.0,
                "error": "FFmpeg not found in system PATH",
                "provider": "whisper"
            }
        
        if self.model is None:
            return {
                "text": "Whisper model not loaded. Please restart backend.",
                "confidence": 0.0,
                "error": "Whisper model not loaded",
                "provider": "whisper"
            }
        
        try:
            # Debug output
            print(f"Received audio data: {len(audio_data)} bytes")
            
            # Save audio to temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".m4a") as temp_audio:
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
            
            # Extract text and confidence
            text = result["text"].strip()
            
            # Calculate average confidence from segments
            segments = result.get("segments", [])
            if segments:
                confidences = []
                for segment in segments:
                    # Whisper provides logprob which we convert to confidence
                    if "avg_logprob" in segment:
                        # Convert log probability to confidence (0-1)
                        conf = np.exp(segment["avg_logprob"])
                        confidences.append(conf)
                
                avg_confidence = sum(confidences) / len(confidences) if confidences else 0.8
            else:
                avg_confidence = 0.8  # Default confidence if no segments
            
            # Clean math-specific text
            cleaned_text = self._clean_math_speech(text)
            
            # If no text found
            if not cleaned_text.strip():
                cleaned_text = "No speech detected in audio. Please ensure audio is clear."
                avg_confidence = 0.0
            
            return {
                "text": cleaned_text,
                "confidence": round(avg_confidence, 2),
                "provider": "whisper",
                "language": result.get("language", "en")
            }
        
        except Exception as e:
            print(f"ASR error: {str(e)}")
            return {
                "text": f"ASR Error: {str(e)}",
                "confidence": 0.0,
                "error": str(e),
                "provider": "whisper"
            }
    
    def _clean_math_speech(self, text: str) -> str:
        """
        Clean and normalize math-specific speech patterns
        
        Args:
            text: Raw transcribed text
        
        Returns:
            Cleaned text with math notation
        """
        # Common math phrase replacements
        replacements = {
            "square root of": "√",
            "squared": "²",
            "cubed": "³",
            "to the power of": "^",
            "raised to": "^",
            "divided by": "÷",
            "times": "×",
            "multiplied by": "×",
            "plus": "+",
            "minus": "-",
            "equals": "=",
            "equal to": "=",
            "greater than": ">",
            "less than": "<",
            "pi": "π",
            "theta": "θ",
            "alpha": "α",
            "beta": "β",
            "gamma": "γ",
            "delta": "Δ",
            "integral of": "∫",
            "summation of": "∑",
            "limit as": "lim",
            "derivative of": "d/dx",
            "del": "∂",
        }
        
        text_lower = text.lower()
        for phrase, symbol in replacements.items():
            text_lower = text_lower.replace(phrase, symbol)
        
        return text_lower
    
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
