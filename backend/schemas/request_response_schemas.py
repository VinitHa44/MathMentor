"""
Pydantic schemas for API requests and responses
"""

from pydantic import BaseModel
from typing import Optional, Dict, Any, List


# Request Models
class OCRRequest(BaseModel):
    image_base64: str  # base64 encoded image


class ASRRequest(BaseModel):
    audio_base64: str  # base64 encoded audio
    filename: Optional[str] = "audio.wav"


class TextRequest(BaseModel):
    text: str


class SolveRequest(BaseModel):
    problem: str
    settings: Optional[Dict[str, Any]] = None
    request_review: Optional[bool] = False  # Manual HITL trigger
    force_continue: Optional[bool] = False  # Override HITL and continue
    corrected_problem: Optional[str] = None  # Human-corrected problem text
    ocr_confidence: Optional[float] = None  # OCR confidence for HITL trigger
    asr_confidence: Optional[float] = None  # ASR confidence for HITL trigger


class FeedbackRequest(BaseModel):
    problem_id: str
    feedback_type: str  # 'approve', 'edit', 'reject'
    user_comment: Optional[str] = None
    corrected_solution: Optional[str] = None


# Response Models
class OCRResponse(BaseModel):
    text: str
    confidence: float
    status: str


class ASRResponse(BaseModel):
    text: str
    confidence: float
    status: str


class ParserResponse(BaseModel):
    problem_text: str
    topic: str
    variables: list
    constraints: list
    needs_clarification: bool
    confidence: float


class SolutionData(BaseModel):
    problem: str
    topic: str
    final_answer: str
    steps: List[str]
    solution_text: str
    confidence: float
    verification_passed: bool
    verification_confidence: Optional[float] = 0


class ExplanationDetails(BaseModel):
    key_concept: str
    analogy: str
    common_mistakes: str


class VerificationData(BaseModel):
    is_correct: bool
    confidence: float
    issues: List[str]
    suggestions: Optional[List[str]] = []
    needs_human_review: Optional[bool] = False


class RetrievedContextItem(BaseModel):
    text: str
    source: str
    topic: str
    score: float


class SolveResponse(BaseModel):
    status: str
    problem_id: Optional[str] = None
    needs_human_review: Optional[bool] = False
    hitl_reason: Optional[List[str]] = []
    parsed_problem: Optional[Dict[str, Any]] = None
    solution: Optional[SolutionData] = None
    explanation: Optional[str] = None
    explanation_details: Optional[ExplanationDetails] = None
    verification: Optional[VerificationData] = None
    agent_trace: Optional[List[Dict[str, Any]]] = []
    retrieved_context: Optional[List[RetrievedContextItem]] = []
    clarification_reason: Optional[str] = None


class FeedbackResponse(BaseModel):
    status: str
    message: str
    problem_id: str


class HistoryResponse(BaseModel):
    status: str
    count: int
    problems: List[Dict[str, Any]]


class SimilarProblemsResponse(BaseModel):
    status: str
    count: int
    similar_problems: List[Dict[str, Any]]
