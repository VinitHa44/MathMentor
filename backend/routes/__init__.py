"""
Routes package initialization
"""

from .health_routes import router as health_router
from .ocr_routes import router as ocr_router
from .asr_routes import router as asr_router
from .parser_routes import router as parser_router
from .solver_routes import router as solver_router
from .feedback_routes import router as feedback_router
from .history_routes import router as history_router

__all__ = [
    "health_router",
    "ocr_router",
    "asr_router",
    "parser_router",
    "solver_router",
    "feedback_router",
    "history_router"
]
