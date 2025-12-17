"""
Verifier Agent - Verifies solution correctness using RAG context
"""

from typing import Dict, Any, List
from services.llm_service import LLMService

class VerifierAgent:
    """Agent for verifying solution correctness"""
    
    def __init__(self, llm_service: LLMService):
        """
        Initialize Verifier Agent
        
        Args:
            llm_service: LLM service for generation
        """
        self.llm = llm_service
    
    def verify(
        self,
        problem_text: str,
        solution_text: str,
        final_answer: str,
        topic: str,
        retrieved_context: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Verify solution correctness
        
        Args:
            problem_text: Original problem
            solution_text: Solution to verify
            final_answer: Final answer
            topic: Problem topic
            retrieved_context: Retrieved chunks from RAG
        
        Returns:
            Verification result with correctness, issues, suggestions
        """
        # Build context section
        context_text = self._format_context(retrieved_context)
        
        # Build verifier prompt
        system_prompt = """You are an expert math verifier checking JEE-level solutions.

VERIFICATION CHECKLIST:
1. Formula correctness (check against retrieved context)
2. Calculation accuracy
3. Domain constraints (e.g., x > 0 for √x)
4. Edge cases handling
5. Logical flow
6. Final answer correctness

OUTPUT FORMAT:
- Is Correct: Yes/No
- Confidence: 0-100%
- Issues Found: List any problems
- Suggestions: How to fix issues

Be thorough but fair."""

        user_prompt = f"""Verify this solution:

**Problem:** {problem_text}

**Solution:**
{solution_text}

**Final Answer:** {final_answer}

**Topic:** {topic}

**Retrieved Context (for formula checking):**
{context_text}

**Your Task:**
Check if the solution is correct. Look for:
- Wrong formulas
- Calculation errors
- Missing constraints
- Logical errors

Provide your verification:"""

        # Generate verification
        try:
            response = self.llm.generate(
                prompt=user_prompt,
                system=system_prompt,
                temperature=0.2,  # Very low for consistent checking
                max_tokens=1500
            )
            
            # Extract text from response dict
            response_text = response.get("text", "")
            
            # Parse verification result
            is_correct = self._parse_correctness(response_text)
            confidence = self._parse_confidence(response_text)
            issues = self._extract_issues(response_text)
            suggestions = self._extract_suggestions(response_text)
            
            return {
                "success": True,
                "is_correct": is_correct,
                "confidence": confidence,
                "issues": issues,
                "suggestions": suggestions,
                "verification_text": response_text,
                "needs_human_review": not is_correct or confidence < 80
            }
        
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "is_correct": False,
                "confidence": 0,
                "issues": ["Verification failed"],
                "needs_human_review": True
            }
    
    def _format_context(self, retrieved_context: List[Dict[str, Any]]) -> str:
        """Format retrieved chunks for prompt"""
        if not retrieved_context:
            return "No context for verification."
        
        formatted = []
        for i, item in enumerate(retrieved_context, 1):
            text = item['text']
            metadata = item['metadata']
            
            formatted.append(
                f"[Ref {i}] (Source: {metadata['source']})\n{text}"
            )
        
        return "\n\n".join(formatted[:3])  # Top 3 for verification
    
    def _parse_correctness(self, text: str) -> bool:
        """Parse if solution is correct"""
        lower_text = text.lower()
        
        # Look for positive indicators
        if any(phrase in lower_text for phrase in [
            "is correct: yes",
            "correct: yes",
            "solution is correct",
            "appears correct",
            "looks correct"
        ]):
            return True
        
        # Look for negative indicators
        if any(phrase in lower_text for phrase in [
            "is correct: no",
            "correct: no",
            "incorrect",
            "not correct",
            "wrong",
            "error found"
        ]):
            return False
        
        # Default to uncertain -> needs review
        return False
    
    def _parse_confidence(self, text: str) -> int:
        """Parse confidence percentage"""
        import re
        
        # Look for confidence: XX%
        match = re.search(r'confidence[:\s]+(\d+)', text.lower())
        if match:
            return int(match.group(1))
        
        # Look for standalone percentage
        match = re.search(r'(\d+)%', text)
        if match:
            return int(match.group(1))
        
        # Default
        return 50
    
    def _extract_issues(self, text: str) -> List[str]:
        """Extract list of issues"""
        issues = []
        
        # Look for issues section
        lower_text = text.lower()
        if "issues found:" in lower_text:
            idx = lower_text.find("issues found:")
            after_marker = text[idx:].split('\n')
            
            for line in after_marker[1:10]:  # Next 10 lines
                line = line.strip()
                if line and line[0] in ['-', '•', '*', '1', '2', '3', '4', '5']:
                    issues.append(line.lstrip('-•* 123456789.'))
        
        # Look for common error phrases
        error_phrases = [
            "incorrect formula",
            "calculation error",
            "missing constraint",
            "wrong answer",
            "logical error"
        ]
        
        for phrase in error_phrases:
            if phrase in lower_text and not any(phrase in i.lower() for i in issues):
                issues.append(phrase.title())
        
        return issues if issues else ["No specific issues identified"]
    
    def _extract_suggestions(self, text: str) -> List[str]:
        """Extract suggestions for improvement"""
        suggestions = []
        
        # Look for suggestions section
        lower_text = text.lower()
        if "suggestions:" in lower_text or "recommendations:" in lower_text:
            marker = "suggestions:" if "suggestions:" in lower_text else "recommendations:"
            idx = lower_text.find(marker)
            after_marker = text[idx:].split('\n')
            
            for line in after_marker[1:10]:
                line = line.strip()
                if line and line[0] in ['-', '•', '*', '1', '2', '3', '4', '5']:
                    suggestions.append(line.lstrip('-•* 123456789.'))
        
        return suggestions if suggestions else ["Review the solution carefully"]
