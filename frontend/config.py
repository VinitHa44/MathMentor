"""
Configuration settings for Math Mentor Frontend
"""

import os
from typing import List

# API Configuration
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")

# File Upload Configuration
SUPPORTED_IMAGE_FORMATS = ["jpg", "jpeg", "png", "webp"]
SUPPORTED_AUDIO_FORMATS = ["mp3", "wav", "m4a", "ogg", "flac"]
MAX_FILE_SIZE_MB = 10

# OCR Configuration
OCR_CONFIDENCE_THRESHOLD = 0.85
OCR_PROVIDERS = ["Tesseract", "PaddleOCR", "EasyOCR"]
DEFAULT_OCR_PROVIDER = "Tesseract"

# ASR Configuration
ASR_CONFIDENCE_THRESHOLD = 0.80
ASR_PROVIDERS = ["Whisper", "Google Speech", "Assembly AI"]
DEFAULT_ASR_PROVIDER = "Whisper"

# RAG Configuration
RAG_TOP_K = 5
RAG_SIMILARITY_THRESHOLD = 0.7
VECTOR_STORE_TYPE = "FAISS"  # Options: FAISS, Chroma, Pinecone

# Agent Configuration
AGENTS = [
    "Parser Agent",
    "Intent Router Agent",
    "Solver Agent",
    "Verifier Agent",
    "Explainer Agent"
]

# Model Configuration
AVAILABLE_MODELS = {
    "GPT-4": {
        "provider": "OpenAI",
        "model_id": "gpt-4-turbo-preview",
        "max_tokens": 4096
    },
    "Claude 3.5": {
        "provider": "Anthropic",
        "model_id": "claude-3-5-sonnet-20241022",
        "max_tokens": 4096
    },
    "Gemini Pro": {
        "provider": "Google",
        "model_id": "gemini-pro",
        "max_tokens": 8192
    }
}

# Math Topics
MATH_TOPICS = [
    "Algebra",
    "Probability",
    "Calculus",
    "Linear Algebra",
    "Trigonometry",
    "Geometry",
    "Number Theory"
]

# Difficulty Levels
DIFFICULTY_LEVELS = [
    "Easy",
    "Medium",
    "Hard",
    "JEE Mains",
    "JEE Advanced"
]

# Explanation Levels
EXPLANATION_LEVELS = {
    "Concise": {
        "description": "Brief explanations with key steps only",
        "detail_level": 1
    },
    "Standard": {
        "description": "Balanced explanations with reasoning",
        "detail_level": 2
    },
    "Detailed": {
        "description": "Comprehensive explanations with examples",
        "detail_level": 3
    }
}

# HITL Triggers
HITL_TRIGGERS = {
    "low_ocr_confidence": OCR_CONFIDENCE_THRESHOLD,
    "low_asr_confidence": ASR_CONFIDENCE_THRESHOLD,
    "parser_ambiguity": True,
    "verifier_uncertainty": 0.75,
    "explicit_request": True
}

# Memory Configuration
MEMORY_STORAGE_PATH = os.getenv("MEMORY_STORAGE_PATH", "./data/memory")
MEMORY_MAX_ITEMS = 1000
MEMORY_SIMILARITY_THRESHOLD = 0.85

# UI Configuration
UI_THEME = {
    "primaryColor": "#667eea",
    "backgroundColor": "#ffffff",
    "secondaryBackgroundColor": "#f8f9fa",
    "textColor": "#2c3e50",
    "font": "Inter"
}

# Session Configuration
SESSION_TIMEOUT_MINUTES = 60
MAX_HISTORY_ITEMS = 100

# Logging Configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE_PATH = "./logs/math_mentor.log"

# Feature Flags
FEATURES = {
    "image_input": True,
    "audio_input": True,
    "text_input": True,
    "rag_retrieval": True,
    "multi_agent": True,
    "hitl": True,
    "memory": True,
    "feedback": True,
    "export_history": True,
    "web_search": False,  # Optional feature
    "mcp_integration": False  # Optional feature
}

# Error Messages
ERROR_MESSAGES = {
    "file_too_large": f"File size exceeds {MAX_FILE_SIZE_MB}MB limit",
    "unsupported_format": "Unsupported file format",
    "ocr_failed": "Failed to extract text from image",
    "asr_failed": "Failed to transcribe audio",
    "api_error": "Backend API error. Please try again",
    "network_error": "Network connection error",
    "invalid_input": "Invalid input provided"
}

# Success Messages
SUCCESS_MESSAGES = {
    "ocr_success": "Text extracted successfully",
    "asr_success": "Audio transcribed successfully",
    "solution_generated": "Solution generated successfully",
    "feedback_submitted": "Feedback submitted successfully",
    "correction_saved": "Correction saved to memory"
}

# Math Symbols and Notation
MATH_SYMBOLS = {
    "sqrt": "√",
    "pi": "π",
    "theta": "θ",
    "alpha": "α",
    "beta": "β",
    "gamma": "γ",
    "delta": "Δ",
    "infinity": "∞",
    "integral": "∫",
    "sum": "∑",
    "product": "∏"
}

# Common Math Phrases for ASR
MATH_PHRASES = [
    "square root of",
    "raised to",
    "to the power of",
    "divided by",
    "multiplied by",
    "equals",
    "greater than",
    "less than",
    "plus",
    "minus",
    "integral of",
    "derivative of",
    "limit as",
    "summation of"
]

# Knowledge Base Categories
KNOWLEDGE_BASE_CATEGORIES = [
    "Formulas",
    "Theorems",
    "Solution Templates",
    "Common Mistakes",
    "Problem-Solving Strategies",
    "Mathematical Concepts"
]

# Agent Response Templates
AGENT_TEMPLATES = {
    "parser": {
        "success": "Problem parsed successfully",
        "needs_clarification": "The problem needs clarification"
    },
    "router": {
        "routed": "Problem routed to appropriate solver"
    },
    "solver": {
        "solving": "Solving the problem...",
        "solved": "Problem solved successfully"
    },
    "verifier": {
        "verified": "Solution verified",
        "needs_review": "Solution needs review"
    },
    "explainer": {
        "explaining": "Generating explanation...",
        "explained": "Explanation generated"
    }
}

# Performance Metrics
PERFORMANCE_TARGETS = {
    "ocr_latency_ms": 2000,
    "asr_latency_ms": 3000,
    "solution_latency_ms": 10000,
    "accuracy_target": 0.90
}

# Deployment Configuration
DEPLOYMENT = {
    "platform": "Streamlit Cloud",  # Options: Streamlit Cloud, HuggingFace Spaces, Render, Railway
    "port": 8501,
    "host": "0.0.0.0"
}
