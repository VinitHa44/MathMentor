# Math Mentor - Streamlit Cloud Deployment Guide

## Prerequisites
- GitHub account
- Streamlit Cloud account (sign up at share.streamlit.io)
- Backend API deployed and accessible

## Deployment Steps

### 1. Prepare Repository
```bash
# Ensure all files are committed
git add .
git commit -m "Prepare for deployment"
git push origin main
```

### 2. Configure Streamlit Cloud

1. Go to https://share.streamlit.io
2. Click "New app"
3. Select your repository
4. Configure:
   - **Main file path**: `frontend/app.py`
   - **Python version**: 3.9+
   - **Branch**: main (or your deployment branch)

### 3. Set Environment Variables

In Streamlit Cloud app settings, add:

```
API_BASE_URL=https://your-backend-api.com
OCR_PROVIDER=Tesseract
ASR_PROVIDER=Whisper
DEFAULT_MODEL=GPT-4
LOG_LEVEL=INFO
```

### 4. Advanced Settings (Optional)

Create `.streamlit/secrets.toml` (not committed to git):

```toml
# API Keys (if needed)
OPENAI_API_KEY = "your-key-here"
ANTHROPIC_API_KEY = "your-key-here"
GOOGLE_API_KEY = "your-key-here"

# Backend Configuration
[backend]
url = "https://your-backend-api.com"
timeout = 30

[ocr]
provider = "Tesseract"
confidence_threshold = 0.85

[asr]
provider = "Whisper"
confidence_threshold = 0.80
```

### 5. Deploy

Click "Deploy" and wait for the build to complete.

## Alternative Deployment Options

### HuggingFace Spaces

1. Create new Space on HuggingFace
2. Select Streamlit SDK
3. Upload files or connect GitHub
4. Add `requirements.txt`
5. Space will auto-deploy

### Render

```yaml
# render.yaml
services:
  - type: web
    name: math-mentor-frontend
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
    envVars:
      - key: API_BASE_URL
        value: https://your-backend.onrender.com
```

### Railway

```toml
# railway.toml
[build]
builder = "NIXPACKS"

[deploy]
startCommand = "streamlit run app.py --server.port=$PORT --server.address=0.0.0.0"
restartPolicyType = "ON_FAILURE"
restartPolicyMaxRetries = 10
```

### Docker

```dockerfile
# Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Create directories
RUN mkdir -p data/memory logs

# Expose port
EXPOSE 8501

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Start Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

## Post-Deployment

### Verify Deployment
- [ ] App loads successfully
- [ ] All input modes work (Image, Audio, Text)
- [ ] Backend API connection works
- [ ] Solutions are generated correctly
- [ ] Feedback system works
- [ ] History/Memory persists

### Monitor
- Check Streamlit Cloud logs
- Monitor performance metrics
- Track error rates
- Review user feedback

### Maintenance
- Regular dependency updates
- Backend API compatibility
- Performance optimization
- Bug fixes and improvements

## Troubleshooting

### App Not Loading
- Check requirements.txt for conflicts
- Verify Python version compatibility
- Check Streamlit Cloud logs

### Backend Connection Failed
- Verify API_BASE_URL is correct
- Check CORS settings on backend
- Ensure backend is publicly accessible

### OCR Not Working
- Tesseract should be in base image
- Check file upload size limits
- Verify image format support

### Memory Issues
- Reduce max_history_items
- Clear old data periodically
- Optimize data storage

## Performance Optimization

1. **Caching**: Use `@st.cache_data` for expensive operations
2. **Lazy Loading**: Load components on demand
3. **Image Compression**: Compress before upload
4. **Pagination**: Limit items displayed at once
5. **CDN**: Use CDN for static assets

## Security Checklist

- [ ] API keys in secrets, not code
- [ ] Input validation enabled
- [ ] File upload size limits set
- [ ] HTTPS enabled
- [ ] CORS properly configured
- [ ] Rate limiting on backend

## Monitoring & Analytics

Consider adding:
- Google Analytics
- Sentry for error tracking
- LogRocket for session replay
- Custom metrics dashboard
