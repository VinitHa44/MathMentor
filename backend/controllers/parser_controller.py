"""
Parser Controller - Request handling and orchestration for Parser
"""

from typing import Dict, Any
from usecases.parser_usecase import ParserUseCase
from utils.logger import get_logger

logger = get_logger(__name__)


class ParserController:
    """Controller for parser operations"""
    
    def __init__(self):
        """Initialize parser controller"""
        self.usecase = ParserUseCase()
    
    def parse_problem(self, text: str) -> Dict[str, Any]:
        """
        Parse problem text
        
        Args:
            text: Problem text
        
        Returns:
            Parsed problem data
        """
        return self.usecase.parse_problem(text)
