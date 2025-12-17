"""
Solver Agent - Solves math problems using RAG-retrieved context
"""

from typing import Dict, Any, Optional, List
from services.llm_service import LLMService

class SolverAgent:
    """Agent for solving math problems with RAG context"""
    
    def __init__(self, llm_service: LLMService):
        """
        Initialize Solver Agent
        
        Args:
            llm_service: LLM service for generation
        """
        self.llm = llm_service
    
    def solve(
        self, 
        problem_text: str, 
        topic: str, 
        variables: Dict[str, Any],
        constraints: Dict[str, Any],
        retrieved_context: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Solve math problem using retrieved context
        
        Args:
            problem_text: The math problem
            topic: Problem topic (algebra, calculus, etc.)
            variables: Extracted variables
            constraints: Problem constraints
            retrieved_context: Retrieved chunks from RAG
        
        Returns:
            Solution with steps, answer, and metadata
        """
        # Build context section
        context_text = self._format_context(retrieved_context)
        
        # Build solver prompt
        system_prompt = """You are an expert math tutor solving JEE-level problems.

CRITICAL RULES:
1. Use ONLY the retrieved context below for formulas and methods
2. Show step-by-step working clearly
3. Explain your reasoning at each step
4. If context is insufficient, say so clearly
5. Verify domain constraints (e.g., x > 0 for √x)
6. Format math using LaTeX where needed

Your solution must be structured and easy to follow."""

        user_prompt = f"""Solve this math problem:

**Problem:** {problem_text}

**Topic:** {topic}

**Given Variables:** {variables}

**Constraints:** {constraints}

**Retrieved Context:**
{context_text}

**Instructions:**
- Use the context to identify relevant formulas/methods
- Show all steps clearly
- State your final answer
- If you need more information, say so

Provide your solution:"""

        # Generate solution
        try:
            response = self.llm.generate(
                prompt=user_prompt,
                system=system_prompt,
                temperature=0.3,  # Lower for more consistent math
                max_tokens=2000
            )
            
            # Extract text from response dict
            response_text = response.get("text", "")
            
            # Extract solution steps
            solution_steps = self._extract_steps(response_text)
            final_answer = self._extract_final_answer(response_text)
            
            return {
                "success": True,
                "solution_text": response_text,
                "steps": solution_steps,
                "final_answer": final_answer,
                "context_used": len(retrieved_context),
                "topic": topic
            }
        
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "solution_text": "",
                "steps": [],
                "final_answer": "Error generating solution"
            }
    
    def _format_context(self, retrieved_context: List[Dict[str, Any]]) -> str:
        """Format retrieved chunks for prompt"""
        if not retrieved_context:
            return "No relevant context found."
        
        formatted = []
        for i, item in enumerate(retrieved_context, 1):
            text = item['text']
            metadata = item['metadata']
            score = item['score']
            
            formatted.append(
                f"[Context {i}] (Source: {metadata['source']}, Topic: {metadata['topic']}, Relevance: {score:.2f})\n{text}"
            )
        
        return "\n\n".join(formatted)
    
    def _extract_steps(self, solution_text: str) -> List[str]:
        """Extract solution steps from text"""
        # Simple extraction - look for numbered steps or lines
        lines = solution_text.split('\n')
        steps = []
        
        for line in lines:
            line = line.strip()
            if line and (
                line.startswith(('Step', 'step', '1.', '2.', '3.', '4.', '5.', '-', '•'))
                or ':' in line
            ):
                steps.append(line)
        
        return steps if steps else [solution_text]
    
    def _extract_final_answer(self, solution_text: str) -> str:
        """Extract final answer from solution"""
        # Look for common answer patterns
        lower_text = solution_text.lower()
        
        answer_markers = [
            "final answer:",
            "answer:",
            "therefore,",
            "thus,",
            "hence,",
            "result:"
        ]
        
        for marker in answer_markers:
            if marker in lower_text:
                # Get text after marker
                idx = lower_text.find(marker)
                after_marker = solution_text[idx + len(marker):].strip()
                
                # Get first sentence/line
                end_idx = after_marker.find('\n')
                if end_idx == -1:
                    end_idx = len(after_marker)
                
                answer = after_marker[:end_idx].strip()
                if answer:
                    return answer
        
        # Fallback: last non-empty line
        lines = [l.strip() for l in solution_text.split('\n') if l.strip()]
        return lines[-1] if lines else "See solution above"
