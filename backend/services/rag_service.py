"""
RAG Service - Retrieval Augmented Generation
Handles PDF extraction, chunking, embedding, and retrieval using Pinecone
"""

import os
import json
from typing import List, Dict, Any, Optional
from pathlib import Path
import numpy as np
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone, ServerlessSpec

try:
    from pypdf import PdfReader
except ImportError:
    print("Warning: pypdf not installed. Install with: pip install pypdf")
    PdfReader = None

class RAGService:
    """Service for RAG pipeline: PDF processing, embedding, and retrieval using Pinecone"""
    
    def __init__(self, docs_dir: str = "rag_docs", index_name: str = "math-mentor"):
        """
        Initialize RAG service with Pinecone
        
        Args:
            docs_dir: Directory containing organized PDF documents
            index_name: Pinecone index name
        """
        self.docs_dir = Path(docs_dir)
        self.index_name = index_name
        
        # Initialize embedding model (local, free)
        print("Loading embedding model...")
        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")
        self.embedding_dim = 384  # all-MiniLM-L6-v2 dimension
        
        # Initialize Pinecone
        api_key = os.environ.get("PINECONE_API_KEY", "")
        if not api_key:
            print("Warning: PINECONE_API_KEY not set. RAG will not work.")
            print("Set it with: export PINECONE_API_KEY='your-api-key'")
            self.pc = None
            self.index = None
            return
        
        print("Connecting to Pinecone...")
        self.pc = Pinecone(api_key=api_key)
        
        # Create or connect to index
        self._init_index()
    
    def extract_pdf_text(self, pdf_path: Path) -> str:
        """
        Extract text from PDF
        
        Args:
            pdf_path: Path to PDF file
        
        Returns:
            Extracted text
        """
        if PdfReader is None:
            return ""
        
        try:
            reader = PdfReader(pdf_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            return text
        except Exception as e:
            print(f"Error extracting {pdf_path}: {e}")
            return ""
    
    def clean_text(self, text: str) -> str:
        """
        Light cleaning of extracted text
        
        Args:
            text: Raw extracted text
        
        Returns:
            Cleaned text
        """
        # Light cleaning - preserve math notation
        text = text.replace("\n\n\n", "\n\n")
        text = text.replace("•", "-")
        text = text.strip()
        return text
    
    def chunk_text(self, text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
        """
        Chunk text into overlapping segments
        
        Args:
            text: Text to chunk
            chunk_size: Target chunk size in characters
            overlap: Overlap between chunks
        
        Returns:
            List of text chunks
        """
        if not text:
            return []
        
        chunks = []
        start = 0
        
        while start < len(text):
            end = start + chunk_size
            chunk = text[start:end]
            
            # Try to break at sentence boundary
            if end < len(text):
                last_period = chunk.rfind('.')
                last_newline = chunk.rfind('\n')
                break_point = max(last_period, last_newline)
                
                if break_point > chunk_size * 0.5:  # At least 50% into chunk
                    chunk = chunk[:break_point + 1]
                    end = start + break_point + 1
            
            chunks.append(chunk.strip())
            start = end - overlap
        
        return [c for c in chunks if len(c) > 50]  # Filter very short chunks
    
    def process_pdf_directory(self, force_rebuild: bool = False):
        """
        Process all PDFs in organized directory structure
        
        Args:
            force_rebuild: Force rebuild even if index exists
        """
        if not force_rebuild and self.index is not None:
            print("RAG index already loaded. Use force_rebuild=True to rebuild.")
            return
        
        print(f"Processing PDFs from {self.docs_dir}...")
        
        self.chunks = []
        self.metadata = []
        chunks_to_upsert = []
        
        # Process each topic folder
        for topic_dir in self.docs_dir.iterdir():
            if not topic_dir.is_dir():
                continue
            
            topic = topic_dir.name
            print(f"Processing topic: {topic}")
            
            # Process PDFs in topic folder
            for pdf_file in topic_dir.glob("*.pdf"):
                print(f"  - {pdf_file.name}")
                
                # Extract text
                text = self.extract_pdf_text(pdf_file)
                if not text:
                    continue
                
                # Clean text
                text = self.clean_text(text)
                
                # Chunk text
                chunks = self.chunk_text(text)
                
                # Add chunks with metadata
                for i, chunk in enumerate(chunks):
                    chunks_to_upsert.append({
                        "text": chunk,
                        "metadata": {
                            "source": pdf_file.stem,
                            "topic": topic,
                            "file": pdf_file.name,
                            "chunk_id": i,
                            "difficulty": "jee_basic"  # Can be extracted from filename
                        }
                    })
        
        print(f"Processed {len(chunks_to_upsert)} chunks from {len(set(m['source'] for m in self.metadata))} documents")
        
        # Upsert to Pinecone
        if chunks_to_upsert:
            self._upsert_to_pinecone(chunks_to_upsert)
    
    def _init_index(self):
        """Initialize or connect to Pinecone index"""
        if not self.pc:
            return
        
        try:
            # Check if index exists
            existing_indexes = [idx.name for idx in self.pc.list_indexes()]
            
            if self.index_name not in existing_indexes:
                print(f"Creating Pinecone index: {self.index_name}")
                self.pc.create_index(
                    name=self.index_name,
                    dimension=self.embedding_dim,
                    metric="cosine",
                    spec=ServerlessSpec(cloud="aws", region="us-east-1")
                )
                print("Index created successfully")
            else:
                print(f"Connecting to existing index: {self.index_name}")
            
            # Connect to index
            self.index = self.pc.Index(self.index_name)
            print(f"Connected to Pinecone index: {self.index_name}")
            
        except Exception as e:
            print(f"Error initializing Pinecone index: {e}")
            self.index = None
    
    def _upsert_to_pinecone(self, chunks_with_metadata):
        """Upsert chunks to Pinecone"""
        if not self.index:
            print("Pinecone index not available")
            return
        
        print("Creating embeddings...")
        texts = [item['text'] for item in chunks_with_metadata]
        embeddings = self.embedder.encode(texts, show_progress_bar=True)
        
        print("Upserting to Pinecone...")
        vectors = []
        for i, (chunk_data, embedding) in enumerate(zip(chunks_with_metadata, embeddings)):
            vector_id = f"{chunk_data['metadata']['source']}_{chunk_data['metadata']['chunk_id']}"
            vectors.append({
                "id": vector_id,
                "values": embedding.tolist(),
                "metadata": {
                    "text": chunk_data['text'],
                    "source": chunk_data['metadata']['source'],
                    "topic": chunk_data['metadata']['topic'],
                    "file": chunk_data['metadata']['file'],
                    "chunk_id": chunk_data['metadata']['chunk_id'],
                    "difficulty": chunk_data['metadata']['difficulty']
                }
            })
            
            # Batch upsert every 100 vectors
            if len(vectors) >= 100:
                self.index.upsert(vectors=vectors)
                vectors = []
        
        # Upsert remaining vectors
        if vectors:
            self.index.upsert(vectors=vectors)
        
        print(f"Upserted {len(chunks_with_metadata)} vectors to Pinecone")
        
        # Store chunks and metadata locally for reference
        for chunk_data in chunks_with_metadata:
            self.chunks.append(chunk_data['text'])
            self.metadata.append(chunk_data['metadata'])
    
    def retrieve(self, query: str, top_k: int = 5, topic_filter: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Retrieve relevant chunks for query from Pinecone
        
        Args:
            query: Query text
            top_k: Number of results to return
            topic_filter: Optional topic filter (algebra, calculus, etc.)
        
        Returns:
            List of retrieved chunks with metadata and scores
        """
        if not self.index:
            print("Pinecone index not available. Process PDFs first.")
            return []
        
        # Embed query
        query_embedding = self.embedder.encode([query])
        
        # Build filter
        filter_dict = {}
        if topic_filter:
            filter_dict = {"topic": {"$eq": topic_filter.lower()}}
        
        # Query Pinecone
        try:
            search_k = top_k * 2 if topic_filter else top_k
            query_response = self.index.query(
                vector=query_embedding.tolist(),
                top_k=search_k,
                include_metadata=True,
                filter=filter_dict if filter_dict else None
            )
            
            # Prepare results
            results = []
            for match in query_response.matches:
                results.append({
                    "text": match.metadata.get("text", ""),
                    "metadata": {
                        "source": match.metadata.get("source", ""),
                        "topic": match.metadata.get("topic", ""),
                        "file": match.metadata.get("file", ""),
                        "chunk_id": match.metadata.get("chunk_id", 0),
                        "difficulty": match.metadata.get("difficulty", "")
                    },
                    "score": float(match.score),
                    "id": match.id
                })
                
                if len(results) >= top_k:
                    break
            
            return results
            
        except Exception as e:
            print(f"Error querying Pinecone: {e}")
            return []
