"""
Validation helpers for business logic
"""

from typing import Dict, Any, List, Tuple
from utils.constants import (
    OCR_CONFIDENCE_THRESHOLD,
    ASR_CONFIDENCE_THRESHOLD,
    VERIFICATION_CONFIDENCE_THRESHOLD
)


def check_hitl_triggers(
    parsed_problem: Dict[str, Any],
    ocr_confidence: float = None,
    asr_confidence: float = None,
    request_review: bool = False,
    verification_result: Dict[str, Any] = None
) -> Tuple[bool, List[str]]:
    """
    Check if Human-in-the-Loop intervention is needed
    
    Args:
        parsed_problem: Parsed problem data
        ocr_confidence: OCR confidence score
        asr_confidence: ASR confidence score
        request_review: Manual review request
        verification_result: Verification result
    
    Returns:
        Tuple of (needs_review, reasons)
    """
    needs_review = False
    reasons = []
    
    # Check OCR confidence
    if ocr_confidence is not None and ocr_confidence < OCR_CONFIDENCE_THRESHOLD:
        needs_review = True
        reasons.append("Low OCR confidence")
    
    # Check ASR confidence
    if asr_confidence is not None and asr_confidence < ASR_CONFIDENCE_THRESHOLD:
        needs_review = True
        reasons.append("Unclear audio transcription")
    
    # Check manual review request
    if request_review:
        needs_review = True
        reasons.append("User requested review")
    
    # Check parser ambiguity
    if parsed_problem.get('needs_clarification', False):
        needs_review = True
        reasons.append("Parser detected ambiguity")
    
    # Check verification results
    if verification_result:
        if not verification_result.get('is_correct', False):
            needs_review = True
            reasons.append("Verifier detected errors")
        elif verification_result.get('confidence', 0) < VERIFICATION_CONFIDENCE_THRESHOLD:
            needs_review = True
            reasons.append("Low verification confidence")
    
    return needs_review, reasons


def validate_problem_text(problem_text: str) -> bool:
    """
    Validate problem text
    
    Args:
        problem_text: Problem text to validate
    
    Returns:
        True if valid, False otherwise
    """
    if not problem_text or not isinstance(problem_text, str):
        return False
    
    if len(problem_text.strip()) == 0:
        return False
    
    return True


def should_skip_rag(routing: Dict[str, Any]) -> bool:
    """
    Check if RAG should be skipped
    
    Args:
        routing: Routing decision from intent router
    
    Returns:
        True if RAG should be skipped
    """
    return routing.get('skip_rag', False)
