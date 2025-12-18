"""
Configuration settings for Math Mentor Frontend
"""

import os

# API Configuration
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")

# File Upload Configuration
SUPPORTED_IMAGE_FORMATS = ["jpg", "jpeg", "png", "webp"]
SUPPORTED_AUDIO_FORMATS = ["mp3", "wav", "m4a", "ogg", "flac"]
MAX_FILE_SIZE_MB = 10

# OCR Configuration
OCR_CONFIDENCE_THRESHOLD = 0.85

# ASR Configuration
ASR_CONFIDENCE_THRESHOLD = 0.80

# Session Configuration
SESSION_TIMEOUT_MINUTES = 60
MAX_HISTORY_ITEMS = 100
