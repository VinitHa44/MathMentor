# Pinecone Setup for Math Mentor

## 1. Get Pinecone API Key

1. Go to https://app.pinecone.io/
2. Sign up or log in
3. Create a new project
4. Get your API key from the dashboard

## 2. Set Environment Variable

**Windows PowerShell:**
```powershell
$env:PINECONE_API_KEY="your-api-key-here"
```

**Linux/Mac:**
```bash
export PINECONE_API_KEY="your-api-key-here"
```

**Permanent (add to your shell profile):**
- Windows: Add to PowerShell profile
- Linux/Mac: Add to `~/.bashrc` or `~/.zshrc`

## 3. Install Dependencies

```powershell
pip install pinecone-client==5.0.1 sentence-transformers==3.3.1 pypdf==4.3.1
```

## 4. Build Index

```powershell
cd backend
python scripts/build_rag_index.py
```

This will:
- Create a Pinecone index named "math-mentor"
- Process all PDFs in rag_docs/
- Upload vectors to Pinecone cloud

## 5. Verify

The script will show:
```
Creating Pinecone index: math-mentor
Index created successfully
Processing PDFs from rag_docs...
Upserting to Pinecone...
✅ RAG index built and uploaded to Pinecone!
```

## Index Configuration

- **Name**: math-mentor
- **Dimension**: 384 (all-MiniLM-L6-v2)
- **Metric**: cosine
- **Cloud**: AWS
- **Region**: us-east-1 (Serverless)

## Free Tier

Pinecone free tier includes:
- 1 serverless index
- 100K vectors
- More than enough for this project
