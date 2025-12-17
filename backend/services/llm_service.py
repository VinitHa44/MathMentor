"""
LLM Service - Interface for local Llama 3.1 8B Instruct
Uses Ollama for local LLM inference
"""

import requests
import json
from typing import Dict, Any, Optional

class LLMService:
    """Service for interacting with local Llama model via Ollama"""
    
    def __init__(self, model_name: str = "phi3:mini", base_url: str = "http://localhost:11434"):
        """
        Initialize LLM service
        
        Args:
            model_name: Name of the Ollama model to use
            base_url: Ollama API base URL
        """
        self.model_name = model_name
        self.base_url = base_url
        self.api_url = f"{base_url}/api/generate"
        self.chat_url = f"{base_url}/api/chat"
    
    def generate(self, prompt: str, system: Optional[str] = None, temperature: float = 0.1, max_tokens: int = 2000) -> Dict[str, Any]:
        """
        Generate completion from prompt
        
        Args:
            prompt: User prompt
            system: System prompt
            temperature: Sampling temperature (0-1)
            max_tokens: Maximum tokens to generate
        
        Returns:
            Dict with response and metadata
        """
        try:
            payload = {
                "model": self.model_name,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": temperature,
                    "num_predict": max_tokens
                }
            }
            
            if system:
                payload["system"] = system
            
            response = requests.post(self.api_url, json=payload, timeout=120)
            
            if response.status_code == 200:
                result = response.json()
                return {
                    "text": result.get("response", ""),
                    "success": True,
                    "model": self.model_name
                }
            else:
                return {
                    "text": "",
                    "success": False,
                    "error": f"HTTP {response.status_code}: {response.text}"
                }
        
        except requests.exceptions.ConnectionError:
            return {
                "text": "",
                "success": False,
                "error": "Cannot connect to Ollama. Make sure Ollama is running (ollama serve)"
            }
        except Exception as e:
            return {
                "text": "",
                "success": False,
                "error": str(e)
            }
    
    def chat(self, messages: list, temperature: float = 0.1, max_tokens: int = 2000) -> Dict[str, Any]:
        """
        Chat completion with message history
        
        Args:
            messages: List of message dicts with 'role' and 'content'
            temperature: Sampling temperature
            max_tokens: Maximum tokens to generate
        
        Returns:
            Dict with response and metadata
        """
        try:
            payload = {
                "model": self.model_name,
                "messages": messages,
                "stream": False,
                "options": {
                    "temperature": temperature,
                    "num_predict": max_tokens
                }
            }
            
            response = requests.post(self.chat_url, json=payload, timeout=120)
            
            if response.status_code == 200:
                result = response.json()
                return {
                    "text": result.get("message", {}).get("content", ""),
                    "success": True,
                    "model": self.model_name
                }
            else:
                return {
                    "text": "",
                    "success": False,
                    "error": f"HTTP {response.status_code}: {response.text}"
                }
        
        except requests.exceptions.ConnectionError:
            return {
                "text": "",
                "success": False,
                "error": "Cannot connect to Ollama. Make sure Ollama is running (ollama serve)"
            }
        except Exception as e:
            return {
                "text": "",
                "success": False,
                "error": str(e)
            }
