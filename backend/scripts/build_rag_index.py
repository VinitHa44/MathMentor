"""
Script to build RAG index from PDFs and upload to Pinecone
Run this after adding PDFs to rag_docs/
"""

import sys
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = Path(__file__).parent.parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from services.rag_service import RAGService

def main():
    """Build RAG index from PDFs and upload to Pinecone"""
    print("=" * 60)
    print("RAG Index Builder (Pinecone)")
    print("=" * 60)
    print()
    
    # Check for API key
    if not os.environ.get("PINECONE_API_KEY"):
        print("❌ ERROR: PINECONE_API_KEY environment variable not set")
        print()
        print("Please set your Pinecone API key:")
        print("  Windows (PowerShell): $env:PINECONE_API_KEY='your-api-key'")
        print("  Linux/Mac: export PINECONE_API_KEY='your-api-key'")
        print("  Or add to .env file: PINECONE_API_KEY=your-api-key")
        print()
        print("Get your API key from: https://app.pinecone.io/")
        return
    
    # Initialize RAG service
    rag_service = RAGService(docs_dir="rag_docs", index_name="math-mentor")
    
    # Check if PDFs exist
    from pathlib import Path
    docs_dir = Path("rag_docs")
    pdf_count = len(list(docs_dir.glob("**/*.pdf")))
    
    if pdf_count == 0:
        print("⚠️  No PDFs found in rag_docs/")
        print()
        print("Please add PDF documents to:")
        print("  - rag_docs/algebra/")
        print("  - rag_docs/calculus/")
        print("  - rag_docs/probability/")
        print("  - rag_docs/linear_algebra/")
        print()
        print("Then run this script again.")
        return
    
    print(f"Found {pdf_count} PDF(s)")
    print()
    
    # Build index
    print("Processing PDFs and building index...")
    print("This may take a few minutes...")
    print()
    
    rag_service.process_pdf_directory(force_rebuild=True)
    
    print()
    print("=" * 60)
    print("✅ RAG index built and uploaded to Pinecone!")
    print("=" * 60)
    print()
    print("The backend will now retrieve from Pinecone.")
    print("Restart the backend server if it's already running.")

if __name__ == "__main__":
    main()
