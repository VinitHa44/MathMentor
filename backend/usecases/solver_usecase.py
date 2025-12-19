"""
Solver UseCase - Business logic for problem solving pipeline
Contains the complete multi-agent solving logic with RAG and Memory
"""

from typing import Dict, Any, List, Optional
from agents.parser_agent import ParserAgent
from agents.intent_router_agent import IntentRouterAgent
from agents.solver_agent import SolverAgent
from agents.verifier_agent import VerifierAgent
from agents.explainer_agent import ExplainerAgent
from services.llm_service import LLMService
from repositories.memory_repository import MemoryRepository
from repositories.rag_repository import RAGRepository
from usecases.helpers.validation_helper import check_hitl_triggers, should_skip_rag
from usecases.helpers.data_helper import (
    format_retrieved_context,
    build_solution_data,
    build_verification_data,
    build_explanation_details
)
from usecases.helpers.trace_helper import add_agent_trace
from utils.response import clarification_response, hitl_response
from utils.logger import get_logger

logger = get_logger(__name__)


class SolverUseCase:
    """UseCase for problem solving operations"""
    
    def __init__(self):
        """Initialize solver use case"""
        # Initialize services
        self.llm_service = LLMService()
        
        # Initialize agents
        self.parser_agent = ParserAgent(self.llm_service)
        self.router_agent = IntentRouterAgent(self.llm_service)
        self.solver_agent = SolverAgent(self.llm_service)
        self.verifier_agent = VerifierAgent(self.llm_service)
        self.explainer_agent = ExplainerAgent(self.llm_service)
        
        # Initialize repositories
        self.memory_repo = MemoryRepository(storage_dir="memory_store")
        self.rag_repo = RAGRepository(docs_dir="rag_docs", index_name="math-mentor")
    
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
        Solve math problem using multi-agent pipeline
        
        Args:
            problem: Problem text
            settings: Optional settings
            request_review: Manual HITL trigger
            force_continue: Override HITL
            corrected_problem: Human-corrected problem
            ocr_confidence: OCR confidence for HITL
            asr_confidence: ASR confidence for HITL
        
        Returns:
            Complete solution with verification and explanation
        """
        try:
            logger.info(f"Starting problem solving pipeline")
            
            agent_trace = []
            
            # Use corrected problem if provided (human override)
            problem_text = corrected_problem if corrected_problem else problem
            
            # STEP 1: Parse the problem
            logger.info("Step 1: Parsing problem")
            parsed = self.parser_agent.parse(problem_text)
            add_agent_trace(agent_trace, "Parser Agent", "completed", parsed)
            
            # Check HITL triggers (initial)
            needs_human_review, hitl_reason = check_hitl_triggers(
                parsed_problem=parsed,
                ocr_confidence=ocr_confidence,
                asr_confidence=asr_confidence,
                request_review=request_review
            )
            
            # Check if clarification needed
            if parsed.get('needs_clarification', False) and not force_continue:
                logger.info("Problem needs clarification")
                return clarification_response(
                    parsed_problem=parsed,
                    reason=parsed.get('clarification_reason', 'Problem unclear'),
                    agent_trace=agent_trace,
                    needs_human_review=needs_human_review,
                    hitl_reason=hitl_reason
                )
            
            # STEP 2: Route intent
            logger.info("Step 2: Routing intent")
            routing = self.router_agent.route(parsed)
            add_agent_trace(agent_trace, "Intent Router Agent", "completed", routing)
            
            # STEP 3: Memory lookup - Find similar problems and patterns
            logger.info("Step 3: Memory lookup")
            topic = parsed.get('topic', 'general')
            variables = parsed.get('variables', {})
            
            similar_problems = self.memory_repo.find_similar_problems(topic, variables, limit=3)
            if similar_problems:
                add_agent_trace(
                    agent_trace,
                    "Memory Service",
                    "completed",
                    {
                        "action": "Found similar problems",
                        "count": len(similar_problems),
                        "similarity_scores": [p.get('similarity', 0) for p in similar_problems]
                    }
                )
            
            solution_patterns = self.memory_repo.get_solution_patterns(topic)
            if solution_patterns:
                add_agent_trace(
                    agent_trace,
                    "Memory Service",
                    "completed",
                    {
                        "action": "Retrieved solution patterns",
                        "pattern_count": len(solution_patterns),
                        "top_pattern": solution_patterns[0]['steps'][:2] if solution_patterns else []
                    }
                )
            
            # STEP 4: RAG Retrieval (conditional)
            logger.info("Step 4: RAG retrieval")
            skip_rag = should_skip_rag(routing)
            
            if skip_rag:
                retrieved_context = []
                add_agent_trace(
                    agent_trace,
                    "RAG Retrieval",
                    "skipped",
                    {"reason": "Simple problem - no context needed"}
                )
            else:
                retrieved_context = self.rag_repo.retrieve(
                    query=problem,
                    top_k=5,
                    topic_filter=topic if topic != 'general' else None
                )
                add_agent_trace(
                    agent_trace,
                    "RAG Retrieval",
                    "completed",
                    {"chunks_retrieved": len(retrieved_context)}
                )
            
            # STEP 5: Solve with context and memory patterns
            logger.info("Step 5: Solving problem")
            solution_result = self.solver_agent.solve(
                problem_text=problem,
                topic=topic,
                variables=parsed.get('variables', {}),
                constraints=parsed.get('constraints', {}),
                retrieved_context=retrieved_context,
                similar_problems=similar_problems if similar_problems else None,
                solution_patterns=solution_patterns if solution_patterns else None
            )
            
            status = "completed" if solution_result['success'] else "failed"
            add_agent_trace(agent_trace, "Solver Agent", status, solution_result)
            
            if not solution_result['success']:
                raise Exception(solution_result.get('error', 'Solving failed'))
            
            # STEP 6: Verify solution
            logger.info("Step 6: Verifying solution")
            verification_result = self.verifier_agent.verify(
                problem_text=problem,
                solution_text=solution_result['solution_text'],
                final_answer=solution_result['final_answer'],
                topic=topic,
                retrieved_context=retrieved_context
            )
            
            status = "completed" if verification_result['success'] else "failed"
            add_agent_trace(agent_trace, "Verifier Agent", status, verification_result)
            
            # Check HITL triggers (post-verification)
            needs_human_review, hitl_reason = check_hitl_triggers(
                parsed_problem=parsed,
                ocr_confidence=ocr_confidence,
                asr_confidence=asr_confidence,
                request_review=request_review,
                verification_result=verification_result
            )
            
            # If HITL required, stop pipeline and return for human review
            if needs_human_review and not force_continue:
                logger.info(f"HITL triggered: {hitl_reason}")
                
                # Store partial problem in memory to get problem_id
                problem_id = self.memory_repo.store_problem(
                    problem_text=problem_text,
                    parsed_data=parsed,
                    solution=solution_result,
                    verification=verification_result,
                    retrieved_context=retrieved_context,
                    agent_trace=agent_trace
                )
                
                solution_data = build_solution_data(problem, topic, solution_result, verification_result)
                verification_data = build_verification_data(verification_result)
                
                return hitl_response(
                    problem_id=problem_id,
                    hitl_reason=hitl_reason,
                    parsed_problem=parsed,
                    solution=solution_data,
                    verification=verification_data,
                    agent_trace=agent_trace
                )
            
            # STEP 7: Generate explanation (ONLY if verification passed)
            logger.info("Step 7: Generating explanation")
            if verification_result.get('is_correct', False):
                explanation_result = self.explainer_agent.explain(
                    problem_text=problem,
                    solution_text=solution_result['solution_text'],
                    final_answer=solution_result['final_answer'],
                    topic=topic,
                    solver_steps=solution_result.get('steps', [])
                )
                
                status = "completed" if explanation_result['success'] else "failed"
                add_agent_trace(agent_trace, "Explainer Agent", status, explanation_result)
            else:
                # Skip explainer when verification fails
                explanation_result = {
                    "success": False,
                    "explanation_text": "Solution needs review before explanation can be generated.",
                    "key_concept": "",
                    "analogy": "",
                    "common_mistakes": ""
                }
                add_agent_trace(
                    agent_trace,
                    "Explainer Agent",
                    "skipped",
                    {"reason": "Verification failed"}
                )
            
            # Store in memory for self-learning
            logger.info("Storing problem in memory")
            problem_id = self.memory_repo.store_problem(
                problem_text=problem,
                parsed_data=parsed,
                solution=solution_result,
                verification=verification_result,
                retrieved_context=retrieved_context,
                agent_trace=agent_trace
            )
            
            # Build final response
            logger.info("Building final response")
            solution_data = build_solution_data(problem, topic, solution_result, verification_result)
            verification_data = build_verification_data(verification_result)
            explanation_details = build_explanation_details(explanation_result)
            formatted_context = format_retrieved_context(retrieved_context)
            
            return {
                "status": "success",
                "problem_id": problem_id,
                "needs_human_review": needs_human_review,
                "hitl_reason": hitl_reason,
                "parsed_problem": parsed,
                "solution": solution_data,
                "explanation": explanation_result.get('explanation_text', ''),
                "explanation_details": explanation_details,
                "verification": verification_data,
                "agent_trace": agent_trace,
                "retrieved_context": formatted_context
            }
        
        except Exception as e:
            logger.error(f"Solving failed: {str(e)}")
            raise Exception(f"Solving failed: {str(e)}")
