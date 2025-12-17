"""
Utility functions for Math Mentor Frontend
"""

import base64
from io import BytesIO
from PIL import Image
from typing import Optional, Dict, Any
import re


def encode_image_to_base64(image: Image.Image, format: str = "PNG") -> str:
    """
    Encode PIL Image to base64 string
    
    Args:
        image: PIL Image object
        format: Image format (PNG, JPEG, etc.)
    
    Returns:
        Base64 encoded string
    """
    buffered = BytesIO()
    image.save(buffered, format=format)
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str


def decode_base64_to_image(base64_string: str) -> Image.Image:
    """
    Decode base64 string to PIL Image
    
    Args:
        base64_string: Base64 encoded image string
    
    Returns:
        PIL Image object
    """
    img_data = base64.b64decode(base64_string)
    image = Image.open(BytesIO(img_data))
    return image


def validate_file_size(file_size: int, max_size_mb: int = 10) -> bool:
    """
    Validate file size against maximum allowed size
    
    Args:
        file_size: File size in bytes
        max_size_mb: Maximum allowed size in MB
    
    Returns:
        True if valid, False otherwise
    """
    max_size_bytes = max_size_mb * 1024 * 1024
    return file_size <= max_size_bytes


def clean_math_text(text: str) -> str:
    """
    Clean and normalize math text from OCR/ASR
    
    Args:
        text: Raw text string
    
    Returns:
        Cleaned text string
    """
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Fix common OCR errors
    text = text.replace('O', '0')  # In numeric contexts
    text = text.replace('l', '1')  # In numeric contexts (careful with variables)
    
    # Normalize math operators
    text = text.replace('×', '*')
    text = text.replace('÷', '/')
    text = text.replace('−', '-')
    
    # Remove leading/trailing whitespace
    text = text.strip()
    
    return text


def format_latex(expression: str) -> str:
    """
    Format mathematical expression with LaTeX
    
    Args:
        expression: Math expression string
    
    Returns:
        LaTeX formatted string
    """
    # Add $ delimiters for inline math
    if not expression.startswith('$'):
        expression = f"${expression}$"
    
    return expression


def extract_numbers(text: str) -> list:
    """
    Extract all numbers from text
    
    Args:
        text: Input text string
    
    Returns:
        List of numbers found
    """
    numbers = re.findall(r'-?\d+\.?\d*', text)
    return [float(n) if '.' in n else int(n) for n in numbers]


def detect_math_topic(text: str) -> str:
    """
    Detect math topic from problem text
    
    Args:
        text: Problem text
    
    Returns:
        Detected topic
    """
    text_lower = text.lower()
    
    # Keywords for different topics
    algebra_keywords = ['equation', 'solve', 'polynomial', 'quadratic', 'linear', 'variable']
    probability_keywords = ['probability', 'random', 'chance', 'dice', 'coin', 'card']
    calculus_keywords = ['derivative', 'integral', 'limit', 'differentiate', 'integrate']
    linear_algebra_keywords = ['matrix', 'vector', 'determinant', 'eigenvalue']
    
    # Count keyword matches
    topics = {
        'Algebra': sum(1 for kw in algebra_keywords if kw in text_lower),
        'Probability': sum(1 for kw in probability_keywords if kw in text_lower),
        'Calculus': sum(1 for kw in calculus_keywords if kw in text_lower),
        'Linear Algebra': sum(1 for kw in linear_algebra_keywords if kw in text_lower)
    }
    
    # Return topic with highest count
    detected_topic = max(topics, key=topics.get)
    return detected_topic if topics[detected_topic] > 0 else 'General'


def format_step_content(content: str) -> str:
    """
    Format step content with proper markdown
    
    Args:
        content: Step content text
    
    Returns:
        Formatted markdown string
    """
    # Replace ** with bold
    content = re.sub(r'\*\*(.*?)\*\*', r'**\1**', content)
    
    # Add line breaks for readability
    content = content.replace('. ', '.\n\n')
    
    return content


def calculate_confidence_color(confidence: float) -> str:
    """
    Get color for confidence level
    
    Args:
        confidence: Confidence value (0-1)
    
    Returns:
        Hex color code
    """
    if confidence >= 0.9:
        return "#28a745"  # Green
    elif confidence >= 0.7:
        return "#ffc107"  # Yellow
    else:
        return "#dc3545"  # Red


def truncate_text(text: str, max_length: int = 100) -> str:
    """
    Truncate text to maximum length
    
    Args:
        text: Input text
        max_length: Maximum length
    
    Returns:
        Truncated text with ellipsis if needed
    """
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."


def parse_math_expression(expression: str) -> Dict[str, Any]:
    """
    Parse mathematical expression into components
    
    Args:
        expression: Math expression string
    
    Returns:
        Dictionary with expression components
    """
    result = {
        'original': expression,
        'variables': [],
        'numbers': [],
        'operators': []
    }
    
    # Extract variables (single letters)
    result['variables'] = list(set(re.findall(r'\b[a-zA-Z]\b', expression)))
    
    # Extract numbers
    result['numbers'] = extract_numbers(expression)
    
    # Extract operators
    operators = re.findall(r'[+\-*/=<>]', expression)
    result['operators'] = list(set(operators))
    
    return result


def format_time_ago(timestamp: str) -> str:
    """
    Format timestamp as 'time ago'
    
    Args:
        timestamp: ISO format timestamp
    
    Returns:
        Human-readable time ago string
    """
    from datetime import datetime
    
    try:
        dt = datetime.fromisoformat(timestamp)
        now = datetime.now()
        diff = now - dt
        
        seconds = diff.total_seconds()
        
        if seconds < 60:
            return "just now"
        elif seconds < 3600:
            minutes = int(seconds / 60)
            return f"{minutes} minute{'s' if minutes > 1 else ''} ago"
        elif seconds < 86400:
            hours = int(seconds / 3600)
            return f"{hours} hour{'s' if hours > 1 else ''} ago"
        else:
            days = int(seconds / 86400)
            return f"{days} day{'s' if days > 1 else ''} ago"
    except:
        return timestamp


def sanitize_input(text: str) -> str:
    """
    Sanitize user input to prevent XSS or injection
    
    Args:
        text: User input text
    
    Returns:
        Sanitized text
    """
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    
    # Remove script tags and content
    text = re.sub(r'<script.*?</script>', '', text, flags=re.DOTALL | re.IGNORECASE)
    
    # Escape special characters
    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')
    text = text.replace('"', '&quot;')
    text = text.replace("'", '&#x27;')
    
    return text
