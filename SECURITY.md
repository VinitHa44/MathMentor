# Security Guardrails Documentation

## Overview
MathMentor implements comprehensive security guardrails to protect against malicious inputs, prompt injection attacks, and resource abuse.

## Input Validation

### Text Input Validation
- **Maximum Length**: 5,000 characters
- **Minimum Length**: Non-empty after stripping whitespace
- **Type Check**: Must be string type
- **Sanitization**: Removes control characters, normalizes whitespace

### Base64 Input Validation
- **Maximum Size**: 
  - Images: 10 MB
  - Audio: 25 MB
- **Format Check**: Validates base64 encoding format
- **Data URI Support**: Handles `data:` prefix extraction

### Confidence Score Validation
- **Range**: 0.0 to 1.0
- **Type**: Float or None
- **Error Handling**: Returns None for null values

## Prompt Injection Protection

### Detection Patterns
The system detects and blocks the following suspicious patterns:

1. **Instruction Override Attempts**
   - "ignore previous instructions"
   - "disregard all instructions"
   - "forget everything"

2. **Role Manipulation**
   - "system: you are..."
   - "pretend to be..."
   - "roleplay as..."

3. **Special Token Injection**
   - `<|im_start|>`, `<|im_end|>`
   - `[INST]`, `[/INST]`
   - `###instruction`, `###human`, `###assistant`

4. **Unicode Bypass Attempts**
   - Suspicious unicode characters (0x7F-0xA0 range)
   - Excessive special tokens (>3)

### Sanitization Process
All user inputs are sanitized before being sent to the LLM:

1. **Validation**: Check length and format
2. **Injection Detection**: Scan for suspicious patterns
3. **Character Filtering**: Remove control characters
4. **Whitespace Normalization**: Clean up excessive whitespace
5. **Token Removal**: Strip special LLM tokens

## API Route Protection

### OCR Route (`/api/ocr`)
- Validates base64 image (max 10MB)
- Handles Tesseract unavailability gracefully
- Returns user-friendly error messages

### ASR Route (`/api/transcribe`)
- Validates base64 audio (max 25MB)
- Checks audio format and size
- Sanitizes transcribed text

### Parser Route (`/api/parse`)
- Sanitizes problem text for LLM processing
- Detects prompt injection attempts
- Returns 400 Bad Request for suspicious input

### Solver Route (`/api/solve`)
- Validates problem text (max 5,000 chars)
- Checks confidence scores (0-1 range)
- Sanitizes corrected problem text
- Validates all optional parameters

### Feedback Route (`/api/feedback`)
- Validates problem ID format (alphanumeric, hyphens, underscores)
- Checks feedback type (approve/edit/reject)
- Sanitizes user comments and corrected solutions
- Limits comment length

### History Routes
- `/api/history`: Validates limit (max 100)
- `/api/similar/{problem_id}`: Validates problem ID and limit

## LLM Service Protection

### Prompt Sanitization
All prompts sent to the LLM are automatically sanitized:

```python
def _sanitize_prompt(text: str) -> str:
    """Remove special tokens and normalize whitespace"""
    # Remove injection tokens
    text = text.replace('<|im_start|>', '')
    text = text.replace('[INST]', '')
    # ... more token removal
    
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text)
    return text.strip()
```

### Temperature Limits
- Parser: 0.1 (deterministic)
- Solver: 0.3 (focused creativity)
- Verifier: 0.1 (consistent checking)
- Explainer: 0.5 (creative explanations)

### Token Limits
- Parser: 500 tokens
- Solver: 2000 tokens
- Verifier: 1500 tokens
- Explainer: 800 tokens

## Frontend Protection

### Input Sanitization
Frontend also sanitizes inputs before sending to backend:

```python
def sanitize_input(text: str) -> str:
    """Sanitize user input to prevent XSS or injection"""
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    
    # Escape special characters
    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    # ... more escaping
    
    return text
```

### File Upload Limits
- Images: JPG, PNG, JPEG (max 10MB)
- Audio: WAV, MP3, M4A, OGG, FLAC (max 25MB)

## Deployment Environment Handling

### OCR Unavailability
When Tesseract is not installed (common in cloud deployments):
- Returns graceful error message
- Guides user to Text Input tab
- Doesn't crash the system

### Audio Recorder Unavailability
When browser recording not available:
- Shows informative message
- Directs to file upload option
- Hides recorder UI

## Rate Limiting Considerations

While not implemented in the current version, consider adding:

1. **Request Rate Limiting**
   - Per IP: 100 requests/hour
   - Per endpoint: Different limits

2. **Token Budget Tracking**
   - Monitor LLM API usage
   - Implement usage caps

3. **Session Management**
   - Track user sessions
   - Implement cooldown periods

## Error Messages

### User-Friendly Errors
All errors return helpful messages:
- "Text exceeds maximum length of 5000 characters"
- "Potentially unsafe input detected: Suspicious pattern"
- "OCR is not available in this deployment environment"

### Security Errors
Suspicious activity logged but messages kept generic:
- "Invalid input detected"
- "Request validation failed"

## Testing

Run security tests:
```bash
cd backend
pytest tests/test_security.py -v
```

## Best Practices

1. **Always Validate**: Never trust user input
2. **Sanitize Early**: Clean inputs at API boundary
3. **Fail Gracefully**: Return helpful error messages
4. **Log Suspicious Activity**: Monitor for attack patterns
5. **Update Patterns**: Keep injection patterns up-to-date
6. **Test Regularly**: Run security tests in CI/CD

## Future Enhancements

1. **Rate Limiting**: Add Redis-based rate limiting
2. **API Keys**: Implement API key authentication
3. **CAPTCHA**: Add reCAPTCHA for public deployments
4. **WAF Integration**: Connect to Web Application Firewall
5. **Anomaly Detection**: ML-based suspicious activity detection
