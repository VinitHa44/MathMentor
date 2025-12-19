"""
Parser UseCase - Business logic for problem parsing
"""

from typing import Dict, Any
from agents.parser_agent import ParserAgent
from services.llm_service import LLMService
from utils.logger import get_logger

logger = get_logger(__name__)


class ParserUseCase:
    """UseCase for parsing operations"""
    
    def __init__(self):
        """Initialize parser use case"""
        self.llm_service = LLMService()
        self.parser_agent = ParserAgent(self.llm_service)
    
    def parse_problem(self, text: str) -> Dict[str, Any]:
        """
        Parse math problem text
        
        Args:
            text: Problem text
        
        Returns:
            Parsed problem data
        """
        try:
            logger.info("Parsing problem text")
            
            # Use LLM-powered Parser Agent
            result = self.parser_agent.parse(text)
            
            logger.info(f"Parsing completed - Topic: {result.get('topic', 'unknown')}")
            
            return {
                "problem_text": result["problem_text"],
                "topic": result["topic"],
                "variables": result["variables"],
                "constraints": result["constraints"],
                "needs_clarification": result["needs_clarification"],
                "confidence": result["confidence"]
            }
        
        except Exception as e:
            logger.error(f"Parsing failed: {str(e)}")
            raise Exception(f"Parsing failed: {str(e)}")
