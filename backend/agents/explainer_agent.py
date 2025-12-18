"""
Explainer Agent - Generates natural language explanations with analogies
"""

from typing import Dict, Any
from services.llm_service import LLMService

class ExplainerAgent:
    """Agent for generating clear explanations of solutions"""
    
    def __init__(self, llm_service: LLMService):
        """
        Initialize Explainer Agent
        
        Args:
            llm_service: LLM service for generation
        """
        self.llm = llm_service
    
    def explain(
        self,
        problem_text: str,
        solution_text: str,
        final_answer: str,
        topic: str,
        solver_steps: list = None
    ) -> Dict[str, Any]:
        """
        Generate natural language explanation
        
        Args:
            problem_text: Original problem
            solution_text: Solution to explain
            final_answer: Final answer
            topic: Problem topic
            solver_steps: Steps from solver agent
        
        Returns:
            Explanation with analogies, key concepts, common mistakes
        """
        # Format solver steps for reference
        steps_text = "\n".join([f"{i+1}. {step}" for i, step in enumerate(solver_steps)]) if solver_steps else solution_text
        
        # Build explainer prompt
        system_prompt = """You are a clear and concise math tutor.

EXPLANATION STYLE:
- Brief and focused (3-4 sentences per section)
- No emojis or excessive storytelling
- Clear, exam-oriented language
- Suitable for high school and college students
- Reference the solver's steps directly

Your goal: Help students understand the concept quickly and clearly."""

        user_prompt = f"""Based on the solver's solution, create a brief explanation:

**Problem:** {problem_text}

**Solver Steps:**
{steps_text}

**Final Answer:** {final_answer}

**Topic:** {topic}

**Your Task:**
Provide a concise explanation with these sections:

1. Key Concept (2-3 sentences): What mathematical principle is used?

2. Why This Approach (2-3 sentences): Why is this the right method?

3. Step Explanation (brief): Reference the solver steps and explain key parts.

4. Common Mistakes (2-3 points): What errors do students typically make?

5. Quick Tip (1 sentence): One useful insight for similar problems.

**IMPORTANT:**
- Write in plain text, not markdown format
- Do NOT use ** for bold or other markdown
- Do NOT mention "with/without replacement" unless explicitly in problem
- Keep LaTeX minimal - use simple fractions like 4/13 instead of \\frac
- Be concise and direct

Provide explanation:"""

        # Generate explanation
        try:
            response = self.llm.generate(
                prompt=user_prompt,
                system=system_prompt,
                temperature=0.5,  # Lower for more focused explanations
                max_tokens=800  # Reduced for conciseness
            )
            
            # Extract text from response dict
            response_text = response.get("text", "")
            
            # Extract components
            key_concept = self._extract_section(response_text, ["key concept", "main idea"])
            why_approach = self._extract_section(response_text, ["why this approach", "approach"])
            analogy = self._extract_section(response_text, ["analogy", "real-world", "think of it"])
            common_mistakes = self._extract_section(response_text, ["common mistakes", "avoid", "watch out"])
            pro_tip = self._extract_section(response_text, ["pro tip", "tip", "useful insight"])
            
            return {
                "success": True,
                "explanation_text": response_text,
                "key_concept": key_concept,
                "why_approach": why_approach,
                "analogy": analogy,
                "common_mistakes": common_mistakes,
                "pro_tip": pro_tip,
                "topic": topic
            }
        
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "explanation_text": "Unable to generate explanation at this time.",
                "key_concept": "",
                "analogy": ""
            }
    
    def _extract_section(self, text: str, markers: list) -> str:
        """Extract a section from explanation text"""
        lower_text = text.lower()
        
        for marker in markers:
            if marker in lower_text:
                # Find marker position
                idx = lower_text.find(marker)
                
                # Get text after marker
                after_marker = text[idx:]
                
                # Find next section or end
                next_section_idx = len(after_marker)
                for next_marker in ["key concept:", "why", "analogy:", "common mistakes:", "pro tip:", "tip:"]:
                    next_idx = after_marker.lower().find(next_marker, len(marker) + 10)
                    if next_idx > 0 and next_idx < next_section_idx:
                        next_section_idx = next_idx
                
                # Extract section
                section = after_marker[:next_section_idx]
                
                # Clean up
                section = section.split(':', 1)[-1].strip()
                section = section.split('\n\n')[0].strip()
                
                return section
        
        return ""
