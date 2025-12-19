"""
LLM Service - Interface for Groq API
Uses Groq's llama-3.3-70b-versatile for math problem solving
"""

import os
import re
from typing import Dict, Any, Optional

try:
    from groq import Groq
    GROQ_AVAILABLE = True
except ImportError:
    print("⚠️ Groq not installed. Install with: pip install groq")
    GROQ_AVAILABLE = False
    Groq = None

class LLMService:
    """Service for interacting with Groq API (llama-3.3-70b-versatile)"""
    
    def __init__(self, model_name: str = "llama-3.3-70b-versatile", base_url: str = None):
        """
        Initialize LLM service with Groq
        
        Args:
            model_name: Groq model name (default: llama-3.3-70b-versatile)
            base_url: Not used (kept for compatibility)
        """
        self.model_name = model_name
        
        # Initialize Groq client
        groq_api_key = os.getenv("GROQ_API_KEY")
        
        if not GROQ_AVAILABLE:
            print("⚠️ Groq package not installed!")
            self.client = None
        elif not groq_api_key:
            print("⚠️ GROQ_API_KEY not found in environment!")
            self.client = None
        else:
            try:
                self.client = Groq(api_key=groq_api_key)
                print(f"✅ Groq LLM client initialized with model: {model_name}")
            except Exception as e:
                print(f"❌ Error initializing Groq client: {e}")
                self.client = None
    
    def _sanitize_prompt(self, text: str) -> str:
        """Sanitize prompt to prevent injection"""
        # Remove excessive special tokens
        text = text.replace('<|im_start|>', '')
        text = text.replace('<|im_end|>', '')
        text = text.replace('[INST]', '')
        text = text.replace('[/INST]', '')
        text = text.replace('<s>', '')
        text = text.replace('</s>', '')
        
        # Normalize whitespace
        text = re.sub(r'\s+', ' ', text)
        
        return text.strip()
    
    def generate(self, prompt: str, system: Optional[str] = None, temperature: float = 0.1, max_tokens: int = 2000) -> Dict[str, Any]:
        """
        Generate completion from prompt using Groq
        
        Args:
            prompt: User prompt
            system: System prompt
            temperature: Sampling temperature (0-1)
            max_tokens: Maximum tokens to generate
        
        Returns:
            Dict with response and metadata
        """
        if not self.client:
            return {
                "text": "",
                "success": False,
                "error": "Groq client not initialized. Check GROQ_API_KEY."
            }
        
        try:
            # Sanitize inputs
            sanitized_prompt = self._sanitize_prompt(prompt)
            sanitized_system = self._sanitize_prompt(system) if system else None
            
            messages = []
            if sanitized_system:
                messages.append({"role": "system", "content": sanitized_system})
            messages.append({"role": "user", "content": sanitized_prompt})
            
            completion = self.client.chat.completions.create(
                model=self.model_name,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens
            )
            
            return {
                "text": completion.choices[0].message.content,
                "success": True,
                "model": self.model_name
            }
        
        except Exception as e:
            return {
                "text": "",
                "success": False,
                "error": f"Groq API error: {str(e)}"
            }
    
    def chat(self, messages: list, temperature: float = 0.1, max_tokens: int = 2000) -> Dict[str, Any]:
        """
        Chat completion with message history using Groq
        
        Args:
            messages: List of message dicts with 'role' and 'content'
            temperature: Sampling temperature
            max_tokens: Maximum tokens to generate
        
        Returns:
            Dict with response and metadata
        """
        if not self.client:
            return {
                "text": "",
                "success": False,
                "error": "Groq client not initialized. Check GROQ_API_KEY."
            }
        
        try:
            completion = self.client.chat.completions.create(
                model=self.model_name,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens
            )
            
            return {
                "text": completion.choices[0].message.content,
                "success": True,
                "model": self.model_name
            }
        
        except Exception as e:
            return {
                "text": "",
                "success": False,
                "error": f"Groq API error: {str(e)}"
            }
