"""
Health check routes
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "online",
        "service": "Math Mentor API",
        "version": "1.0.0"
    }


@router.get("/health")
async def health_check():
    """Detailed health check"""
    return {
        "status": "healthy",
        "services": {
            "ocr": "ready",
            "asr": "ready",
            "parser": "ready"
        }
    }
