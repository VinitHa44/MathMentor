"""
Math Mentor Backend API
Handles OCR, ASR, and text input parsing for math problems
"""

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Dict, Any
import base64
from io import BytesIO
from PIL import Image
import os
from pathlib import Path
from dotenv import load_dotenv
import uuid
from datetime import datetime

# Global progress tracking
progress_tracker: Dict[str, Dict[str, Any]] = {}

# Load environment variables from .env file
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

# Import processing modules
from services.ocr_service import OCRService
from services.asr_service import ASRService
from services.parser_service import ParserService

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

# Initialize services
ocr_service = OCRService(provider="easyocr")  # Use EasyOCR instead of Tesseract
asr_service = ASRService()
parser_service = ParserService()

# Initialize RAG service (Pinecone)
from services.rag_service import RAGService
rag_service = RAGService(docs_dir="rag_docs", index_name="math-mentor")

# Initialize Memory service
from services.memory_service import MemoryService
memory_service = MemoryService(storage_dir="memory_store")

# Initialize LLM and agents
from services.llm_service import LLMService
from agents.parser_agent import ParserAgent
from agents.intent_router_agent import IntentRouterAgent
from agents.solver_agent import SolverAgent
from agents.verifier_agent import VerifierAgent
from agents.explainer_agent import ExplainerAgent

llm_service = LLMService()
parser_agent = ParserAgent(llm_service)
router_agent = IntentRouterAgent(llm_service)
solver_agent = SolverAgent(llm_service)
verifier_agent = VerifierAgent(llm_service)
explainer_agent = ExplainerAgent(llm_service)

# Request models
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
    session_id: Optional[str] = None  # For tracking progress

class FeedbackRequest(BaseModel):
    problem_id: str
    feedback_type: str  # 'approve', 'edit', 'reject'
    user_comment: Optional[str] = None
    corrected_solution: Optional[str] = None

# Response models
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

@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "online",
        "service": "Math Mentor API",
        "version": "1.0.0"
    }

@app.get("/health")
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

@app.post("/api/ocr", response_model=OCRResponse)
async def extract_text_from_image(request: OCRRequest):
    """
    Extract text from image using OCR
    
    Args:
        request: OCRRequest with base64 encoded image
    
    Returns:
        OCRResponse with extracted text and confidence
    """
    try:
        # Decode base64 image
        image_data = base64.b64decode(request.image_base64)
        image = Image.open(BytesIO(image_data))
        
        # Perform OCR
        result = ocr_service.extract_text(image)
        
        return OCRResponse(
            text=result["text"],
            confidence=result["confidence"],
            status="success"
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"OCR processing failed: {str(e)}")

@app.post("/api/ocr/upload")
async def extract_text_from_upload(file: UploadFile = File(...)):
    """
    Extract text from uploaded image file
    
    Args:
        file: Uploaded image file
    
    Returns:
        Extracted text and confidence
    """
    try:
        # Read image file
        contents = await file.read()
        image = Image.open(BytesIO(contents))
        
        # Perform OCR
        result = ocr_service.extract_text(image)
        
        return {
            "text": result["text"],
            "confidence": result["confidence"],
            "status": "success"
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"OCR processing failed: {str(e)}")

@app.post("/api/transcribe", response_model=ASRResponse)
async def transcribe_audio(request: ASRRequest):
    """
    Transcribe audio to text using ASR
    
    Args:
        request: ASRRequest with base64 encoded audio
    
    Returns:
        ASRResponse with transcribed text and confidence
    """
    try:
        # Decode base64 audio
        audio_data = base64.b64decode(request.audio_base64)
        
        # Perform ASR
        result = asr_service.transcribe_audio(audio_data)
        
        return ASRResponse(
            text=result["text"],
            confidence=result["confidence"],
            status="success"
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"ASR processing failed: {str(e)}")

@app.post("/api/transcribe/upload")
async def transcribe_audio_upload(file: UploadFile = File(...)):
    """
    Transcribe uploaded audio file
    
    Args:
        file: Uploaded audio file
    
    Returns:
        Transcribed text and confidence
    """
    try:
        # Read audio file
        contents = await file.read()
        
        # Perform ASR
        result = asr_service.transcribe_audio(contents)
        
        return {
            "text": result["text"],
            "confidence": result["confidence"],
            "status": "success"
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"ASR processing failed: {str(e)}")

@app.post("/api/parse", response_model=ParserResponse)
async def parse_problem(request: TextRequest):
    """
    Parse math problem text into structured format
    
    Args:
        request: TextRequest with problem text
    
    Returns:
        ParserResponse with structured problem data
    """
    try:
        # Use LLM-powered Parser Agent
        result = parser_agent.parse(request.text)
        
        return ParserResponse(
            problem_text=result["problem_text"],
            topic=result["topic"],
            variables=result["variables"],
            constraints=result["constraints"],
            needs_clarification=result["needs_clarification"],
            confidence=result["confidence"]
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Parsing failed: {str(e)}")

@app.get("/api/progress/{session_id}")
async def get_progress(session_id: str):
    """
    Get current progress of a solve operation
    
    Args:
        session_id: Unique session identifier
        
    Returns:
        Current progress status and step information
    """
    if session_id not in progress_tracker:
        raise HTTPException(status_code=404, detail="Session not found")
    
    return progress_tracker[session_id]


@app.post("/api/solve")
async def solve_problem(request: SolveRequest):
    """
    Solve math problem using RAG + Multi-Agent System
    
    Args:
        request: SolveRequest with problem and settings
    
    Returns:
        Complete solution with RAG context, agent trace, verification
    """
    try:
        from datetime import datetime
        agent_trace = []
        
        # Generate session ID if not provided
        session_id = request.session_id or str(uuid.uuid4())
        
        # Initialize progress tracking
        progress_tracker[session_id] = {
            "status": "in_progress",
            "current_step": "Parsing problem",
            "step_number": 1,
            "total_steps": 6,
            "details": "Analyzing problem structure and extracting key information",
            "timestamp": datetime.now().isoformat()
        }
        
        # STEP 1: Parse the problem
        parsed = parser_agent.parse(request.problem)
        agent_trace.append({
            "agent": "Parser Agent",
            "status": "completed",
            "output": parsed,
            "timestamp": datetime.now().isoformat()
        })
        
        # Update progress
        progress_tracker[session_id].update({
            "current_step": "Routing to agents",
            "step_number": 2,
            "details": f"Problem identified as {parsed.get('topic', 'general')} - routing to appropriate solver",
            "timestamp": datetime.now().isoformat()
        })
        
        # Check if clarification needed
        if parsed.get('needs_clarification', False):
            progress_tracker[session_id].update({
                "status": "needs_clarification",
                "current_step": "Clarification required",
                "details": parsed.get('clarification_reason', 'Problem unclear')
            })
            return {
                "status": "needs_clarification",
                "parsed_problem": parsed,
                "clarification_reason": parsed.get('clarification_reason', 'Problem unclear'),
                "agent_trace": agent_trace,
                "session_id": session_id
            }
        
        # STEP 2: Route intent
        routing = router_agent.route(parsed)
        agent_trace.append({
            "agent": "Intent Router Agent",
            "status": "completed",
            "output": routing,
            "timestamp": datetime.now().isoformat()
        })
        
        # Update progress
        progress_tracker[session_id].update({
            "current_step": "Retrieving knowledge",
            "step_number": 3,
            "details": "Searching knowledge base for relevant examples and concepts",
            "timestamp": datetime.now().isoformat()
        })
        
        # STEP 3: RAG Retrieval
        topic = parsed.get('topic', 'general')
        retrieved_context = rag_service.retrieve(
            query=request.problem,
            top_k=5,
            topic_filter=topic if topic != 'general' else None
        )
        agent_trace.append({
            "agent": "RAG Retrieval",
            "status": "completed",
            "output": {"chunks_retrieved": len(retrieved_context)},
            "timestamp": datetime.now().isoformat()
        })
        
        # Update progress
        progress_tracker[session_id].update({
            "current_step": "Solving problem",
            "step_number": 4,
            "details": f"Applying {topic} techniques with {len(retrieved_context)} reference examples",
            "timestamp": datetime.now().isoformat()
        })
        
        # STEP 4: Solve with retrieved context
        solution_result = solver_agent.solve(
            problem_text=request.problem,
            topic=topic,
            variables=parsed.get('variables', {}),
            constraints=parsed.get('constraints', {}),
            retrieved_context=retrieved_context
        )
        agent_trace.append({
            "agent": "Solver Agent",
            "status": "completed" if solution_result['success'] else "failed",
            "output": solution_result,
            "timestamp": datetime.now().isoformat()
        })
        
        if not solution_result['success']:
            progress_tracker[session_id].update({
                "status": "failed",
                "current_step": "Solving failed",
                "details": solution_result.get('error', 'Unknown error')
            })
            raise Exception(solution_result.get('error', 'Solving failed'))
        
        # Update progress
        progress_tracker[session_id].update({
            "current_step": "Verifying solution",
            "step_number": 5,
            "details": "Checking solution correctness and consistency",
            "timestamp": datetime.now().isoformat()
        })
        
        # STEP 5: Verify solution
        verification_result = verifier_agent.verify(
            problem_text=request.problem,
            solution_text=solution_result['solution_text'],
            final_answer=solution_result['final_answer'],
            topic=topic,
            retrieved_context=retrieved_context
        )
        agent_trace.append({
            "agent": "Verifier Agent",
            "status": "completed" if verification_result['success'] else "failed",
            "output": verification_result,
            "timestamp": datetime.now().isoformat()
        })
        
        # Update progress
        progress_tracker[session_id].update({
            "current_step": "Generating explanation",
            "step_number": 6,
            "details": "Creating detailed explanation with examples",
            "timestamp": datetime.now().isoformat()
        })
        
        # STEP 6: Generate explanation
        explanation_result = explainer_agent.explain(
            problem_text=request.problem,
            solution_text=solution_result['solution_text'],
            final_answer=solution_result['final_answer'],
            topic=topic
        )
        agent_trace.append({
            "agent": "Explainer Agent",
            "status": "completed" if explanation_result['success'] else "failed",
            "output": explanation_result,
            "timestamp": datetime.now().isoformat()
        })
        
        # Update progress - completed
        progress_tracker[session_id].update({
            "status": "completed",
            "current_step": "Complete",
            "step_number": 6,
            "details": "Solution ready!",
            "timestamp": datetime.now().isoformat()
        })
        
        # Build final response
        return {
            "status": "success",
            "parsed_problem": parsed,
            "solution": {
                "problem": request.problem,
                "topic": topic,
                "final_answer": solution_result['final_answer'],
                "steps": solution_result['steps'],
                "solution_text": solution_result['solution_text'],
                "confidence": parsed.get('confidence', 0.8),
                "verification_passed": verification_result.get('is_correct', False),
                "verification_confidence": verification_result.get('confidence', 0)
            },
            "explanation": explanation_result.get('explanation_text', ''),
            "explanation_details": {
                "key_concept": explanation_result.get('key_concept', ''),
                "analogy": explanation_result.get('analogy', ''),
                "common_mistakes": explanation_result.get('common_mistakes', '')
            },
            "verification": {
                "is_correct": verification_result.get('is_correct', False),
                "confidence": verification_result.get('confidence', 0),
                "issues": verification_result.get('issues', []),
                "suggestions": verification_result.get('suggestions', []),
                "needs_human_review": verification_result.get('needs_human_review', False)
            },
            "agent_trace": agent_trace,
            "retrieved_context": [
                {
                    "text": item['text'],
                    "source": item['metadata']['source'],
                    "topic": item['metadata']['topic'],
                    "score": item['score']
                }
                for item in retrieved_context
            ]
        }
        
        # Store in memory for learning
        problem_id = memory_service.store_problem(
            problem_text=request.problem,
            parsed_data=parsed,
            solution=solution_result,
            verification=verification_result,
            retrieved_context=retrieved_context,
            agent_trace=agent_trace
        )
        
        # Add problem_id to response
        result = {
            "status": "success",
            "problem_id": problem_id,
            "session_id": session_id,
            "parsed_problem": parsed,
            "solution": {
                "problem": request.problem,
                "topic": topic,
                "final_answer": solution_result['final_answer'],
                "steps": solution_result['steps'],
                "solution_text": solution_result['solution_text'],
                "confidence": parsed.get('confidence', 0.8),
                "verification_passed": verification_result.get('is_correct', False),
                "verification_confidence": verification_result.get('confidence', 0)
            },
            "explanation": explanation_result.get('explanation_text', ''),
            "explanation_details": {
                "key_concept": explanation_result.get('key_concept', ''),
                "analogy": explanation_result.get('analogy', ''),
                "common_mistakes": explanation_result.get('common_mistakes', '')
            },
            "verification": {
                "is_correct": verification_result.get('is_correct', False),
                "confidence": verification_result.get('confidence', 0),
                "issues": verification_result.get('issues', []),
                "suggestions": verification_result.get('suggestions', []),
                "needs_human_review": verification_result.get('needs_human_review', False)
            },
            "agent_trace": agent_trace,
            "retrieved_context": [
                {
                    "text": item['text'],
                    "source": item['metadata']['source'],
                    "topic": item['metadata']['topic'],
                    "score": item['score']
                }
                for item in retrieved_context
            ]
        }
        
        return result
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Solving failed: {str(e)}")

@app.post("/api/feedback")
async def submit_feedback(request: FeedbackRequest):
    """
    Submit user feedback on solution (HITL)
    
    Args:
        request: FeedbackRequest with problem_id and feedback details
    
    Returns:
        Confirmation of feedback storage
    """
    try:
        memory_service.store_feedback(
            problem_id=request.problem_id,
            feedback_type=request.feedback_type,
            user_comment=request.user_comment,
            corrected_solution=request.corrected_solution
        )
        
        return {
            "status": "success",
            "message": "Feedback stored successfully",
            "problem_id": request.problem_id
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Feedback storage failed: {str(e)}")

@app.get("/api/history")
async def get_history(limit: int = 10):
    """
    Get problem-solving history
    
    Args:
        limit: Number of recent problems to return
    
    Returns:
        List of recent problems
    """
    try:
        history = memory_service.get_problem_history(limit=limit)
        return {
            "status": "success",
            "count": len(history),
            "problems": history
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"History retrieval failed: {str(e)}")

@app.get("/api/similar/{problem_id}")
async def get_similar_problems(problem_id: str, limit: int = 5):
    """
    Get similar problems from history
    
    Args:
        problem_id: Problem ID to find similar problems for
        limit: Number of similar problems to return
    
    Returns:
        List of similar problems
    """
    try:
        # Get the problem
        history = memory_service.get_problem_history(limit=100)
        target_problem = None
        
        for problem in history:
            if problem['id'] == problem_id:
                target_problem = problem
                break
        
        if not target_problem:
            raise HTTPException(status_code=404, detail="Problem not found")
        
        # Find similar
        similar = memory_service.find_similar_problems(
            topic=target_problem['topic'],
            variables=target_problem.get('variables', {}),
            limit=limit
        )
        
        return {
            "status": "success",
            "count": len(similar),
            "similar_problems": similar
        }
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Similar problems retrieval failed: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Solving failed: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
