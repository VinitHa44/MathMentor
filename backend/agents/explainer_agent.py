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
        student_level: str = "jee_basic"
    ) -> Dict[str, Any]:
        """
        Generate natural language explanation
        
        Args:
            problem_text: Original problem
            solution_text: Solution to explain
            final_answer: Final answer
            topic: Problem topic
            student_level: Target level (jee_basic, jee_intermediate, jee_advanced)
        
        Returns:
            Explanation with analogies, key concepts, common mistakes
        """
        # Build explainer prompt
        system_prompt = f"""You are a friendly math tutor explaining solutions to JEE students.

EXPLANATION STYLE:
- Use simple, clear language
- Include real-world analogies
- Highlight key concepts
- Point out common mistakes
- Encourage understanding over memorization

TARGET LEVEL: {student_level}

Your goal is to help students understand WHY, not just HOW."""

        user_prompt = f"""Explain this solution in a way that helps a student understand:

**Problem:** {problem_text}

**Solution:**
{solution_text}

**Final Answer:** {final_answer}

**Topic:** {topic}

**Your Task:**
Create a clear explanation that includes:
1. Key Concept: What's the main idea?
2. Why This Approach: Why did we solve it this way?
3. Step Breakdown: Explain each major step
4. Analogy: Real-world comparison (if applicable)
5. Common Mistakes: What to avoid
6. Pro Tip: Useful insight for similar problems

Make it engaging and easy to understand:"""

        # Generate explanation
        try:
            response = self.llm.generate(
                prompt=user_prompt,
                system=system_prompt,
                temperature=0.7,  # Higher for creative explanations
                max_tokens=2000
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
