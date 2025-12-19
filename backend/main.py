"""
Math Mentor Backend API
Main entry point - FastAPI application setup
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

# Import routes
from routes.health_routes import router as health_router
from routes.ocr_routes import router as ocr_router
from routes.asr_routes import router as asr_router
from routes.parser_routes import router as parser_router
from routes.solver_routes import router as solver_router
from routes.feedback_routes import router as feedback_router
from routes.history_routes import router as history_router

# Create FastAPI app
app = FastAPI(
    title="Math Mentor API",
    description="Backend API for multimodal math problem solving",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(health_router, tags=["Health"])
app.include_router(ocr_router, prefix="/api", tags=["OCR"])
app.include_router(asr_router, prefix="/api", tags=["ASR"])
app.include_router(parser_router, prefix="/api", tags=["Parser"])
app.include_router(solver_router, prefix="/api", tags=["Solver"])
app.include_router(feedback_router, prefix="/api", tags=["Feedback"])
app.include_router(history_router, prefix="/api", tags=["History"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
