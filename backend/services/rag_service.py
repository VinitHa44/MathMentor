"""
RAG Service - Retrieval Augmented Generation
Handles PDF extraction, chunking, embedding, and retrieval using Pinecone
Uses smart document-type-aware chunking strategies
"""

import os
import json
from typing import List, Dict, Any, Optional
from pathlib import Path
import numpy as np
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone, ServerlessSpec
from services.smart_chunker import SmartChunker, ChunkType

try:
    from pypdf import PdfReader
except ImportError:
    print("Warning: pypdf not installed. Install with: pip install pypdf")
    PdfReader = None

class RAGService:
    """Service for RAG pipeline with smart document-type-aware chunking"""
    
    def __init__(self, docs_dir: str = "rag_docs", index_name: str = "math-mentor"):
        """
        Initialize RAG service with Pinecone and smart chunker
        
        Args:
            docs_dir: Directory containing organized documents (markdown preferred)
            index_name: Pinecone index name
        """
        self.docs_dir = Path(docs_dir)
        self.index_name = index_name
        
        # Initialize smart chunker
        self.chunker = SmartChunker()
        
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
    
    def process_documents_directory(self, force_rebuild: bool = False):
        """
        Process all markdown files with smart chunking
        Prioritizes markdown over PDFs for better quality
        
        Args:
            force_rebuild: Force rebuild even if index exists
        """
        if not force_rebuild and self.index is not None:
            print("RAG index already loaded. Use force_rebuild=True to rebuild.")
            return
        
        print(f"Processing documents from {self.docs_dir}...")
        
        all_chunks = []
        
        # Process each topic folder
        for topic_dir in self.docs_dir.iterdir():
            if not topic_dir.is_dir():
                continue
            
            topic = topic_dir.name
            print(f"\nProcessing topic: {topic}")
            
            # Process markdown files (preferred)
            md_files = list(topic_dir.glob("*.md"))
            if md_files:
                print(f"  Found {len(md_files)} markdown file(s)")
                for md_file in md_files:
                    print(f"    - {md_file.name}")
                    chunks = self.chunker.chunk_markdown_file(md_file, topic)
                    all_chunks.extend(chunks)
                    print(f"      → {len(chunks)} chunks")
            
            # Fallback to PDFs if no markdown
            elif list(topic_dir.glob("*.pdf")):
                print(f"  No markdown files found, falling back to PDFs")
                for pdf_file in topic_dir.glob("*.pdf"):
                    print(f"    - {pdf_file.name}")
                    chunks = self._process_pdf_basic(pdf_file, topic)
                    all_chunks.extend(chunks)
                    print(f"      → {len(chunks)} chunks")
        
        # Get statistics
        stats = self.chunker.get_chunk_stats(all_chunks)
        print(f"\n{'='*60}")
        print(f"Chunking Summary:")
        print(f"{'='*60}")
        print(f"Total chunks: {stats['total']}")
        print(f"Average length: {stats['avg_length']} characters")
        print(f"\nBy type:")
        for chunk_type, count in stats['by_type'].items():
            print(f"  {chunk_type}: {count}")
        print(f"\nBy topic:")
        for topic, count in stats['by_topic'].items():
            print(f"  {topic}: {count}")
        print(f"{'='*60}\n")
        
        # Upsert to Pinecone
        if all_chunks:
            self._upsert_chunks_to_pinecone(all_chunks)
    
    def _process_pdf_basic(self, pdf_path: Path, topic: str) -> List[Dict[str, Any]]:
        """
        Basic PDF processing with simple chunking (fallback)
        
        Args:
            pdf_path: Path to PDF file
            topic: Topic name
        
        Returns:
            List of chunks with metadata
        """
        # Extract text
        text = self.extract_pdf_text(pdf_path)
        if not text:
            return []
        
        # Clean text
        text = self.clean_text(text)
        
        # Simple chunking
        text_chunks = self.chunk_text(text, chunk_size=400, overlap=50)
        
        # Convert to chunk format
        chunks = []
        for i, chunk_text in enumerate(text_chunks):
            chunks.append({
                "text": chunk_text,
                "type": "general",
                "topic": topic,
                "subtopic": "general",
                "source": pdf_path.stem,
                "difficulty": "basic",
                "chunk_id": i
            })
        
        return chunks
    
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
    
    def _upsert_chunks_to_pinecone(self, chunks: List[Dict[str, Any]]):
        """
        Upsert smart chunks to Pinecone with rich metadata
        
        Args:
            chunks: List of chunks with metadata
        """
        if not self.index:
            print("Pinecone index not available")
            return
        
        print("\n" + "="*60)
        print("Upserting to Pinecone...")
        print("="*60)
        
        # Create embeddings
        texts = [chunk['text'] for chunk in chunks]
        print(f"Creating embeddings for {len(texts)} chunks...")
        embeddings = self.embedder.encode(texts, show_progress_bar=True)
        
        print("Preparing vectors...")
        vectors = []
        for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
            # Create unique ID
            vector_id = f"{chunk['source']}_{chunk['type']}_{i}"
            
            # Build metadata - include full text (Pinecone limit is ~40KB per metadata)
            metadata = {
                "text": chunk['text'],  # Full text of chunk
                "type": chunk['type'],  # formula, example, definition, etc.
                "topic": chunk['topic'],
                "subtopic": chunk.get('subtopic', 'general'),
                "source": chunk['source'],
                "difficulty": chunk.get('difficulty', 'basic'),
            }
            
            # Add optional metadata
            if 'pattern' in chunk:
                metadata['pattern'] = chunk['pattern']
            
            vectors.append({
                "id": vector_id,
                "values": embedding.tolist(),
                "metadata": metadata
            })
            
            # Batch upsert every 100 vectors
            if len(vectors) >= 100:
                self.index.upsert(vectors=vectors)
                print(f"  Upserted {len(vectors)} vectors...")
                vectors = []
        
        # Upsert remaining vectors
        if vectors:
            self.index.upsert(vectors=vectors)
            print(f"  Upserted {len(vectors)} vectors...")
        
        print(f"\n✅ Successfully upserted {len(chunks)} chunks to Pinecone")
        print("="*60 + "\n")
    
    def retrieve(self, query: str, top_k: int = 5, 
                 topic_filter: Optional[str] = None,
                 type_filter: Optional[str] = None,
                 difficulty_filter: Optional[str] = None,
                 pattern_filter: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Retrieve relevant chunks for query from Pinecone with advanced filtering
        
        Args:
            query: Query text
            top_k: Number of results to return
            topic_filter: Optional topic filter (algebra, calculus, etc.)
            type_filter: Optional type filter (formula, example, definition, etc.)
            difficulty_filter: Optional difficulty filter (basic, jee_basic, jee_advanced)
            pattern_filter: Optional pattern filter (limit, derivative, probability, etc.)
        
        Returns:
            List of retrieved chunks with metadata and scores
        """
        if not self.index:
            print("Pinecone index not available. Process documents first.")
            return []
        
        # Embed query
        query_embedding = self.embedder.encode([query])
        
        # Build advanced filter
        filter_dict = {}
        
        if topic_filter:
            filter_dict["topic"] = {"$eq": topic_filter.lower()}
        
        if type_filter:
            filter_dict["type"] = {"$eq": type_filter.lower()}
        
        if difficulty_filter:
            filter_dict["difficulty"] = {"$eq": difficulty_filter.lower()}
        
        if pattern_filter:
            filter_dict["pattern"] = {"$eq": pattern_filter.lower()}
        
        # Query Pinecone
        try:
            # Get more results if filtering
            search_k = top_k * 3 if filter_dict else top_k
            
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
                        "type": match.metadata.get("type", ""),
                        "topic": match.metadata.get("topic", ""),
                        "subtopic": match.metadata.get("subtopic", ""),
                        "source": match.metadata.get("source", ""),
                        "difficulty": match.metadata.get("difficulty", ""),
                        "pattern": match.metadata.get("pattern", ""),
                        "example_num": match.metadata.get("example_num", 0)
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
    
    def retrieve_by_agent_role(self, query: str, agent_role: str, top_k: int = 5) -> List[Dict[str, Any]]:
        """
        Retrieve chunks optimized for specific agent roles
        
        Args:
            query: Query text
            agent_role: Role (solver, explainer, verifier)
            top_k: Number of results
        
        Returns:
            Retrieved chunks
        """
        if agent_role == "solver":
            # Solver prefers procedures + formulas
            procedures = self.retrieve(query, top_k=top_k//2, type_filter="procedure")
            formulas = self.retrieve(query, top_k=top_k//2, type_filter="formula")
            return procedures + formulas
        
        elif agent_role == "explainer":
            # Explainer prefers examples + definitions
            examples = self.retrieve(query, top_k=top_k//2, type_filter="example")
            definitions = self.retrieve(query, top_k=top_k//2, type_filter="definition")
            return examples + definitions
        
        elif agent_role == "verifier":
            # Verifier prefers pitfalls + formulas
            pitfalls = self.retrieve(query, top_k=top_k//2, type_filter="pitfall")
            formulas = self.retrieve(query, top_k=top_k//2, type_filter="formula")
            return pitfalls + formulas
        
        else:
            # Default retrieval
            return self.retrieve(query, top_k=top_k)
