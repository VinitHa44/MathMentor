# Setup Ollama with Llama 3.1 8B Instruct

## Install Ollama

1. **Download Ollama**:
   - Windows: https://ollama.com/download/windows
   - Or: `winget install Ollama.Ollama`

2. **Install and start Ollama**:
   ```powershell
   # Ollama installs as a service and starts automatically
   # Or manually: ollama serve
   ```

3. **Pull Llama 3.1 8B Instruct (quantized)**:
   ```powershell
   ollama pull llama3.1:8b-instruct-q4_K_M
   ```
   
   This downloads ~4.7GB quantized model (faster, less RAM)

4. **Test Ollama**:
   ```powershell
   ollama run llama3.1:8b-instruct-q4_K_M "What is 2+2?"
   ```

5. **Verify API**:
   ```powershell
   curl http://localhost:11434/api/tags
   ```

## Model Options

- `llama3.1:8b-instruct` - Full precision (16GB RAM)
- `llama3.1:8b-instruct-q4_K_M` - 4-bit quantized (8GB RAM) ✓ Recommended
- `llama3.1:8b-instruct-q3_K_M` - 3-bit quantized (6GB RAM)

## Backend Configuration

The backend is configured to use `llama3.1:8b-instruct-q4_K_M` by default.

To change model, edit `backend/app.py`:
```python
llm_service = LLMService(model_name="llama3.1:8b-instruct")
```

## Usage

Once Ollama is running with the model pulled:

1. Start backend: `uvicorn app:app --reload`
2. The Parser Agent will use Llama 3.1 8B to:
   - Clean OCR/ASR noise
   - Identify math topics
   - Extract variables and constraints
   - Detect ambiguities requiring clarification

## Troubleshooting

- **"Cannot connect to Ollama"**: Start Ollama service (`ollama serve`)
- **Model not found**: Pull the model (`ollama pull llama3.1:8b-instruct-q4_K_M`)
- **Slow responses**: Use smaller quantized model or reduce max_tokens
