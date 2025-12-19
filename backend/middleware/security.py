"""
Security middleware and validation utilities
"""

import re
from typing import Any, Optional
from fastapi import HTTPException

# Constants for validation
MAX_TEXT_LENGTH = 5000
MAX_IMAGE_SIZE_MB = 10
MAX_AUDIO_SIZE_MB = 25
MAX_BASE64_SIZE = MAX_IMAGE_SIZE_MB * 1024 * 1024 * 4 / 3  # Base64 is ~33% larger

# Dangerous patterns that might indicate prompt injection
INJECTION_PATTERNS = [
    r'ignore\s+(previous|above|all)\s+instructions?',
    r'disregard\s+(previous|above|all)\s+instructions?',
    r'forget\s+(previous|everything|all)',
    r'system\s*:\s*you\s+are',
    r'<\|im_start\|>',
    r'<\|im_end\|>',
    r'###\s*instruction',
    r'###\s*human',
    r'###\s*assistant',
    r'\[INST\]',
    r'\[\/INST\]',
    r'<s>\[INST\]',
    r'roleplay',
    r'pretend\s+(you|to\s+be)',
]

# Compiled regex patterns for efficiency
INJECTION_REGEX = [re.compile(pattern, re.IGNORECASE) for pattern in INJECTION_PATTERNS]


def validate_text_input(text: str, field_name: str = "text") -> str:
    """
    Validate text input
    
    Args:
        text: Input text
        field_name: Name of the field for error messages
        
    Returns:
        Validated text
        
    Raises:
        HTTPException: If validation fails
    """
    if not text:
        raise HTTPException(status_code=400, detail=f"{field_name} is required")
    
    if not isinstance(text, str):
        raise HTTPException(status_code=400, detail=f"{field_name} must be a string")
    
    # Length validation
    if len(text) > MAX_TEXT_LENGTH:
        raise HTTPException(
            status_code=400, 
            detail=f"{field_name} exceeds maximum length of {MAX_TEXT_LENGTH} characters"
        )
    
    if len(text.strip()) == 0:
        raise HTTPException(status_code=400, detail=f"{field_name} cannot be empty")
    
    return text.strip()


def validate_base64_input(base64_str: str, field_name: str = "data", max_size_mb: int = MAX_IMAGE_SIZE_MB) -> str:
    """
    Validate base64 encoded input
    
    Args:
        base64_str: Base64 encoded string
        field_name: Name of the field
        max_size_mb: Maximum size in MB
        
    Returns:
        Validated base64 string
        
    Raises:
        HTTPException: If validation fails
    """
    if not base64_str:
        raise HTTPException(status_code=400, detail=f"{field_name} is required")
    
    if not isinstance(base64_str, str):
        raise HTTPException(status_code=400, detail=f"{field_name} must be a string")
    
    # Check base64 format (remove data URI prefix if present)
    if base64_str.startswith('data:'):
        # Extract base64 part after comma
        parts = base64_str.split(',', 1)
        if len(parts) != 2:
            raise HTTPException(status_code=400, detail=f"Invalid {field_name} format")
        base64_str = parts[1]
    
    # Size validation
    max_size_bytes = max_size_mb * 1024 * 1024 * 4 / 3
    if len(base64_str) > max_size_bytes:
        raise HTTPException(
            status_code=400,
            detail=f"{field_name} exceeds maximum size of {max_size_mb}MB"
        )
    
    # Basic base64 validation
    if not re.match(r'^[A-Za-z0-9+/]*={0,2}$', base64_str):
        raise HTTPException(status_code=400, detail=f"Invalid {field_name} encoding")
    
    return base64_str


def detect_prompt_injection(text: str) -> tuple[bool, Optional[str]]:
    """
    Detect potential prompt injection attempts
    
    Args:
        text: Input text to check
        
    Returns:
        Tuple of (is_suspicious, reason)
    """
    text_lower = text.lower()
    
    # Check for injection patterns
    for pattern in INJECTION_REGEX:
        if pattern.search(text):
            return True, f"Suspicious pattern detected: {pattern.pattern}"
    
    # Check for excessive special tokens
    special_tokens = ['<|', '|>', '[INST]', '[/INST]', '###', '<s>', '</s>']
    token_count = sum(text.count(token) for token in special_tokens)
    if token_count > 3:
        return True, "Excessive special tokens detected"
    
    # Check for unusual unicode characters that might bypass filters
    if any(ord(c) > 0x7F and ord(c) < 0xA0 for c in text):
        return True, "Suspicious unicode characters detected"
    
    return False, None


def sanitize_for_llm(text: str, field_name: str = "input") -> str:
    """
    Sanitize text before sending to LLM
    
    Args:
        text: Input text
        field_name: Field name for error messages
        
    Returns:
        Sanitized text
        
    Raises:
        HTTPException: If suspicious content detected
    """
    # Validate first
    text = validate_text_input(text, field_name)
    
    # Detect injection
    is_suspicious, reason = detect_prompt_injection(text)
    if is_suspicious:
        raise HTTPException(
            status_code=400,
            detail=f"Potentially unsafe {field_name} detected: {reason}"
        )
    
    # Remove control characters except newlines and tabs
    text = ''.join(char for char in text if ord(char) >= 32 or char in ['\n', '\t'])
    
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    
    return text


def validate_confidence_score(confidence: Optional[float], field_name: str = "confidence") -> Optional[float]:
    """
    Validate confidence score
    
    Args:
        confidence: Confidence score (0-1 or None)
        field_name: Field name for error messages
        
    Returns:
        Validated confidence score
        
    Raises:
        HTTPException: If validation fails
    """
    if confidence is None:
        return None
    
    if not isinstance(confidence, (int, float)):
        raise HTTPException(status_code=400, detail=f"{field_name} must be a number")
    
    if confidence < 0 or confidence > 1:
        raise HTTPException(status_code=400, detail=f"{field_name} must be between 0 and 1")
    
    return float(confidence)


def validate_problem_id(problem_id: str) -> str:
    """
    Validate problem ID format
    
    Args:
        problem_id: Problem ID string
        
    Returns:
        Validated problem ID
        
    Raises:
        HTTPException: If validation fails
    """
    if not problem_id:
        raise HTTPException(status_code=400, detail="problem_id is required")
    
    if not isinstance(problem_id, str):
        raise HTTPException(status_code=400, detail="problem_id must be a string")
    
    # Problem IDs should be alphanumeric with hyphens/underscores
    if not re.match(r'^[a-zA-Z0-9_-]+$', problem_id):
        raise HTTPException(status_code=400, detail="Invalid problem_id format")
    
    if len(problem_id) > 100:
        raise HTTPException(status_code=400, detail="problem_id too long")
    
    return problem_id


def validate_limit(limit: int, max_limit: int = 50, field_name: str = "limit") -> int:
    """
    Validate limit parameter
    
    Args:
        limit: Limit value
        max_limit: Maximum allowed limit
        field_name: Field name for error messages
        
    Returns:
        Validated limit
        
    Raises:
        HTTPException: If validation fails
    """
    if not isinstance(limit, int):
        raise HTTPException(status_code=400, detail=f"{field_name} must be an integer")
    
    if limit < 1:
        raise HTTPException(status_code=400, detail=f"{field_name} must be at least 1")
    
    if limit > max_limit:
        raise HTTPException(status_code=400, detail=f"{field_name} cannot exceed {max_limit}")
    
    return limit
