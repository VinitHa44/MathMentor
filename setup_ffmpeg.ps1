# FFmpeg Setup Script for MathMentor
# This script helps install FFmpeg on Windows for audio transcription

Write-Host "=====================================" -ForegroundColor Cyan
Write-Host "  MathMentor - FFmpeg Setup" -ForegroundColor Cyan
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host ""

# Check if FFmpeg is already installed
Write-Host "Checking for FFmpeg installation..." -ForegroundColor Yellow
$ffmpegExists = Get-Command ffmpeg -ErrorAction SilentlyContinue

if ($ffmpegExists) {
    Write-Host "✅ FFmpeg is already installed!" -ForegroundColor Green
    Write-Host ""
    Write-Host "FFmpeg Location: $($ffmpegExists.Source)" -ForegroundColor Green
    Write-Host ""
    
    # Show version
    Write-Host "FFmpeg Version:" -ForegroundColor Cyan
    ffmpeg -version | Select-Object -First 1
    Write-Host ""
    Write-Host "✅ Audio transcription should work!" -ForegroundColor Green
    Write-Host ""
    Write-Host "If you're still seeing errors, please restart the backend server." -ForegroundColor Yellow
    exit 0
}

Write-Host "❌ FFmpeg not found in system PATH" -ForegroundColor Red
Write-Host ""
Write-Host "FFmpeg is required for audio transcription with Whisper." -ForegroundColor Yellow
Write-Host ""

# Check if winget is available
$wingetExists = Get-Command winget -ErrorAction SilentlyContinue

if ($wingetExists) {
    Write-Host "Option 1: Install via Winget (Recommended)" -ForegroundColor Cyan
    Write-Host "==========================================" -ForegroundColor Cyan
    Write-Host ""
    $installChoice = Read-Host "Would you like to install FFmpeg using winget? (y/n)"
    
    if ($installChoice -eq 'y' -or $installChoice -eq 'Y') {
        Write-Host ""
        Write-Host "Installing FFmpeg via winget..." -ForegroundColor Yellow
        winget install FFmpeg
        
        Write-Host ""
        Write-Host "✅ FFmpeg installation complete!" -ForegroundColor Green
        Write-Host ""
        Write-Host "⚠️ IMPORTANT: Please restart your terminal and backend server!" -ForegroundColor Yellow
        Write-Host ""
        Write-Host "To verify installation, run: ffmpeg -version" -ForegroundColor Cyan
        exit 0
    }
}

Write-Host ""
Write-Host "Manual Installation Options:" -ForegroundColor Cyan
Write-Host "=============================" -ForegroundColor Cyan
Write-Host ""

Write-Host "Option A: Download from official website" -ForegroundColor Yellow
Write-Host "  1. Visit: https://www.gyan.dev/ffmpeg/builds/" -ForegroundColor White
Write-Host "  2. Download: ffmpeg-release-essentials.zip" -ForegroundColor White
Write-Host "  3. Extract to: C:\ffmpeg" -ForegroundColor White
Write-Host "  4. Add to PATH: C:\ffmpeg\bin" -ForegroundColor White
Write-Host ""

Write-Host "Option B: Using Chocolatey" -ForegroundColor Yellow
Write-Host "  Run: choco install ffmpeg" -ForegroundColor White
Write-Host ""

Write-Host "Option C: Download and add to PATH automatically" -ForegroundColor Yellow
$autoDownload = Read-Host "Would you like me to download FFmpeg for you? (y/n)"

if ($autoDownload -eq 'y' -or $autoDownload -eq 'Y') {
    Write-Host ""
    Write-Host "Downloading FFmpeg..." -ForegroundColor Yellow
    
    # Create temp directory
    $tempDir = "$env:TEMP\ffmpeg_download"
    New-Item -ItemType Directory -Force -Path $tempDir | Out-Null
    
    # Download FFmpeg
    $ffmpegUrl = "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip"
    $zipPath = "$tempDir\ffmpeg.zip"
    
    try {
        Write-Host "Downloading from GitHub..." -ForegroundColor Yellow
        Invoke-WebRequest -Uri $ffmpegUrl -OutFile $zipPath -UseBasicParsing
        
        Write-Host "Extracting..." -ForegroundColor Yellow
        Expand-Archive -Path $zipPath -DestinationPath $tempDir -Force
        
        # Find the bin directory
        $binDir = Get-ChildItem -Path $tempDir -Recurse -Directory | Where-Object { $_.Name -eq "bin" } | Select-Object -First 1
        
        if ($binDir) {
            $installPath = "C:\ffmpeg"
            Write-Host "Installing to: $installPath" -ForegroundColor Yellow
            
            # Copy to C:\ffmpeg
            if (Test-Path $installPath) {
                Remove-Item -Path $installPath -Recurse -Force
            }
            
            Copy-Item -Path $binDir.Parent.FullName -Destination $installPath -Recurse -Force
            
            Write-Host "Adding to system PATH..." -ForegroundColor Yellow
            
            # Add to PATH
            $currentPath = [Environment]::GetEnvironmentVariable("Path", "Machine")
            if ($currentPath -notlike "*$installPath\bin*") {
                [Environment]::SetEnvironmentVariable(
                    "Path",
                    "$currentPath;$installPath\bin",
                    "Machine"
                )
                Write-Host "✅ Added to system PATH" -ForegroundColor Green
            }
            
            Write-Host ""
            Write-Host "✅ FFmpeg installed successfully!" -ForegroundColor Green
            Write-Host ""
            Write-Host "⚠️ IMPORTANT: Please restart your terminal and backend server!" -ForegroundColor Yellow
            Write-Host ""
            Write-Host "To verify: ffmpeg -version" -ForegroundColor Cyan
        }
    }
    catch {
        Write-Host "❌ Error during installation: $_" -ForegroundColor Red
        Write-Host ""
        Write-Host "Please install manually using Option A above." -ForegroundColor Yellow
    }
    finally {
        # Clean up
        Remove-Item -Path $tempDir -Recurse -Force -ErrorAction SilentlyContinue
    }
}
else {
    Write-Host ""
    Write-Host "Please install FFmpeg manually using one of the options above." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "For detailed instructions, see: backend\FFMPEG_SETUP.md" -ForegroundColor Cyan
}

Write-Host ""
Write-Host "After installation:" -ForegroundColor Cyan
Write-Host "  1. Restart your terminal" -ForegroundColor White
Write-Host "  2. Restart the backend server" -ForegroundColor White
Write-Host "  3. Test audio transcription" -ForegroundColor White
Write-Host ""
