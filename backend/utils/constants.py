"""
Constants for the application
"""

# Application metadata
APP_NAME = "Math Mentor API"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "Backend API for multimodal math problem solving"

# HITL thresholds
OCR_CONFIDENCE_THRESHOLD = 0.6
ASR_CONFIDENCE_THRESHOLD = 0.6
VERIFICATION_CONFIDENCE_THRESHOLD = 0.6

# RAG settings
DEFAULT_RAG_TOP_K = 5
DEFAULT_SIMILAR_PROBLEMS_LIMIT = 3
DEFAULT_HISTORY_LIMIT = 10

# Status messages
STATUS_SUCCESS = "success"
STATUS_ERROR = "error"
STATUS_NEEDS_CLARIFICATION = "needs_clarification"
STATUS_NEEDS_HUMAN_REVIEW = "needs_human_review"

# Feedback types
FEEDBACK_APPROVE = "approve"
FEEDBACK_EDIT = "edit"
FEEDBACK_REJECT = "reject"
