"""
RAG Repository - Data access layer for RAG operations
Handles all interactions with RAG service and vector store
"""

from typing import List, Dict, Any, Optional
from services.rag_service import RAGService


class RAGRepository:
    """Repository for RAG data access"""
    
    def __init__(self, docs_dir: str = "rag_docs", index_name: str = "math-mentor"):
        """
        Initialize RAG repository
        
        Args:
            docs_dir: Directory containing documents
            index_name: Pinecone index name
        """
        self.rag_service = RAGService(docs_dir=docs_dir, index_name=index_name)
    
    def retrieve(
        self,
        query: str,
        top_k: int = 5,
        topic_filter: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Retrieve relevant context from RAG
        
        Args:
            query: Search query
            top_k: Number of results to retrieve
            topic_filter: Optional topic filter
        
        Returns:
            List of retrieved context items
        """
        return self.rag_service.retrieve(
            query=query,
            top_k=top_k,
            topic_filter=topic_filter
        )
