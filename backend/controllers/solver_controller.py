"""
Solver Controller - Request handling and orchestration for Solver
"""

from typing import Dict, Any, Optional
from usecases.solver_usecase import SolverUseCase
from utils.logger import get_logger

logger = get_logger(__name__)


class SolverController:
    """Controller for solver operations"""
    
    def __init__(self):
        """Initialize solver controller"""
        self.usecase = SolverUseCase()
    
    def solve_problem(
        self,
        problem: str,
        settings: Optional[Dict[str, Any]] = None,
        request_review: bool = False,
        force_continue: bool = False,
        corrected_problem: Optional[str] = None,
        ocr_confidence: Optional[float] = None,
        asr_confidence: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        Solve math problem
        
        Args:
            problem: Problem text
            settings: Optional settings
            request_review: Manual HITL trigger
            force_continue: Override HITL
            corrected_problem: Human-corrected problem
            ocr_confidence: OCR confidence
            asr_confidence: ASR confidence
        
        Returns:
            Complete solution
        """
        return self.usecase.solve_problem(
            problem=problem,
            settings=settings,
            request_review=request_review,
            force_continue=force_continue,
            corrected_problem=corrected_problem,
            ocr_confidence=ocr_confidence,
            asr_confidence=asr_confidence
        )
