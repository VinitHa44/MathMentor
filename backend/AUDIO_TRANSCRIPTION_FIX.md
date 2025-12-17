# Quick Fix: Audio Transcription Error

## Problem
You're seeing this error when trying to transcribe audio:
```
ASR Error: [WinError 2] The system cannot find the file specified
```

## Cause
FFmpeg is not installed or not in your system PATH. Whisper requires FFmpeg to process audio files.

## Quick Solution

### Option 1: One-Command Install (Easiest)
Open PowerShell and run:
```powershell
winget install FFmpeg
```

### Option 2: Use Setup Script
From the MathMentor root directory:
```powershell
.\setup_ffmpeg.ps1
```

### Option 3: Manual Install
1. Download: https://www.gyan.dev/ffmpeg/builds/ 
2. Extract to `C:\ffmpeg`
3. Add `C:\ffmpeg\bin` to system PATH
4. Restart terminal

## After Installing FFmpeg

1. **Verify installation:**
   ```powershell
   ffmpeg -version
   ```
   
2. **Restart the backend:**
   - Press `Ctrl+C` in the backend terminal
   - Run: `uvicorn app:app --reload`

3. **Test audio transcription** in the frontend

## Need More Help?

See detailed instructions in [FFMPEG_SETUP.md](./FFMPEG_SETUP.md)
