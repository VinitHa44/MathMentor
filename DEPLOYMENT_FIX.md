# Deployment Configuration Guide

## Streamlit Cloud Deployment (Frontend)

### Required Files:
1. **`frontend/requirements.txt`** ✅ - Python packages
2. **`frontend/packages.txt`** ✅ - System packages (NEW!)

### What `packages.txt` Does:
Installs system-level dependencies on Streamlit Cloud's Linux containers:
- `tesseract-ocr` - OCR engine for image text extraction
- `tesseract-ocr-eng` - English language data
- `ffmpeg` - Audio processing for recording feature
- `libtesseract-dev` - Development libraries

### Deployment Steps:
1. Push changes to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repo: `VinitHa44/MathMentor`
4. Set main file: `frontend/app.py`
5. Advanced settings → Secrets: Add API keys
   ```toml
   API_BASE_URL = "https://your-backend-url.onrender.com"
   ```

---

## Render Deployment (Backend)

### Required Files:
1. **`render.yaml`** ✅ - Service configuration
2. **`backend/requirements.txt`** ✅ - Python packages

### What Updated `render.yaml` Does:
Added system package installation in `buildCommand`:
```yaml
buildCommand: |
  apt-get update
  apt-get install -y tesseract-ocr tesseract-ocr-eng libtesseract-dev ffmpeg
  pip install -r backend/requirements.txt
```

### Environment Variables to Set on Render:
- `GROQ_API_KEY` - Your Groq API key
- `COHERE_API_KEY` - Your Cohere API key  
- `PINECONE_API_KEY` - Your Pinecone API key
- `PYTHON_VERSION` - 3.11.0

### Deployment Steps:
1. Push changes to GitHub
2. Render will auto-deploy (if connected)
3. Or manually: Dashboard → Deploy latest commit

---

## Why This Fixes Your Issues

### ❌ Before (Missing Dependencies):
```
Frontend: ⚠️ Audio recorder not available
Backend:  ❌ Tesseract is not installed
```

### ✅ After (With packages.txt & updated render.yaml):
```
Frontend: 🎙️ Audio recording works!
Backend:  ✅ OCR extracts text from images!
```

---

## Verify Deployment

### Check Frontend:
1. Navigate to Image tab → Upload image
2. Should extract text (not show Tesseract error)
3. Navigate to Audio tab → Record Audio button should work

### Check Backend:
```bash
curl https://your-backend.onrender.com/health
# Should return: {"status": "healthy", "services": {...}}
```

---

## Common Issues

### Issue: Still seeing errors after deployment
**Solution**: 
- Streamlit Cloud: Reboot app from settings
- Render: Trigger manual deploy

### Issue: Deployment fails during build
**Solution**: Check build logs
- Streamlit: Settings → Logs
- Render: Logs tab in dashboard

### Issue: "Module not found" errors
**Solution**: Ensure requirements.txt has all packages
```bash
# Test locally first
pip install -r frontend/requirements.txt
pip install -r backend/requirements.txt
```

---

## Quick Reference

### Frontend Dependencies:
- **Python packages**: `requirements.txt`
- **System packages**: `packages.txt` (NEW!)

### Backend Dependencies:
- **Python packages**: `requirements.txt`
- **System packages**: `render.yaml` buildCommand (UPDATED!)

### After Pushing:
1. Git add, commit, push
2. Streamlit Cloud: Auto-rebuilds (~2-3 mins)
3. Render: Auto-deploys (~5-7 mins)
4. Test both Image OCR and Audio Recording
