# FFmpeg Setup Guide for Audio Transcription

## Why FFmpeg is Required

The audio transcription feature uses OpenAI's Whisper model, which requires FFmpeg to process audio files. Without FFmpeg, you'll see the error:

```
[WinError 2] The system cannot find the file specified
```

## Installation Options

### Option 1: Using Winget (Recommended - Easiest)

1. Open PowerShell or Command Prompt
2. Run:
   ```powershell
   winget install FFmpeg
   ```
3. Restart your backend server
4. Test: `ffmpeg -version`

### Option 2: Manual Installation

1. **Download FFmpeg:**
   - Go to: https://www.gyan.dev/ffmpeg/builds/
   - Download: `ffmpeg-release-essentials.zip` (smaller) or `ffmpeg-release-full.zip`

2. **Extract:**
   - Extract the zip file to a permanent location
   - Example: `C:\ffmpeg`

3. **Add to System PATH:**
   
   **Method A - Using GUI:**
   - Press `Win + X` and select "System"
   - Click "Advanced system settings"
   - Click "Environment Variables"
   - Under "System variables", find and select "Path"
   - Click "Edit"
   - Click "New"
   - Add the path to the `bin` folder: `C:\ffmpeg\bin`
   - Click "OK" on all windows

   **Method B - Using PowerShell (Admin):**
   ```powershell
   [Environment]::SetEnvironmentVariable(
       "Path",
       [Environment]::GetEnvironmentVariable("Path", "Machine") + ";C:\ffmpeg\bin",
       "Machine"
   )
   ```

4. **Verify Installation:**
   - Open a **NEW** PowerShell/Command Prompt window
   - Run: `ffmpeg -version`
   - You should see version information

5. **Restart Backend:**
   - Stop your backend server (Ctrl+C)
   - Start it again: `uvicorn app:app --reload`

### Option 3: Using Chocolatey

If you have Chocolatey installed:

```powershell
choco install ffmpeg
```

## Verification

After installation, verify FFmpeg is accessible:

```powershell
# Check if FFmpeg is in PATH
where ffmpeg

# Check FFmpeg version
ffmpeg -version
```

You should see output showing the FFmpeg location and version.

## Troubleshooting

### "FFmpeg still not found" after installation

1. **Restart everything:**
   - Close all PowerShell/CMD windows
   - Open a NEW terminal
   - Navigate to backend directory
   - Start backend: `uvicorn app:app --reload`

2. **Check PATH:**
   ```powershell
   $env:Path -split ';' | Select-String ffmpeg
   ```
   Should show the FFmpeg path

3. **Temporary PATH (for testing):**
   ```powershell
   $env:Path += ";C:\ffmpeg\bin"
   uvicorn app:app --reload
   ```

### Permission Issues

If you see permission errors:
- Run PowerShell as Administrator when adding to system PATH
- Or add to User PATH instead of System PATH

## Alternative: Use Portable FFmpeg

You can place FFmpeg in the project directory:

1. Download and extract FFmpeg
2. Copy `ffmpeg.exe` to: `MathMentor\backend\ffmpeg.exe`
3. The application will automatically find it there (future enhancement)

## After FFmpeg is Installed

1. Restart the backend server
2. Try audio transcription again
3. You should now see proper transcription instead of the error

## Supported Audio Formats

Once FFmpeg is installed, these formats are supported:
- WAV
- MP3
- M4A
- OGG
- FLAC
- AAC

## Need Help?

If you're still experiencing issues:
1. Check backend logs for specific error messages
2. Verify FFmpeg version: `ffmpeg -version`
3. Ensure you've restarted the backend after installation
