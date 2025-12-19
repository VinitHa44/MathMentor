#!/usr/bin/env bash
# Build script for Render deployment
# Installs system dependencies and Python packages

set -o errexit

# Install system dependencies
apt-get update
apt-get install -y tesseract-ocr tesseract-ocr-eng libtesseract-dev ffmpeg

# Install Python dependencies
pip install --upgrade pip
pip install -r backend/requirements.txt
