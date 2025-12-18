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
        retrieved_context: List[Dict[str, Any]],
        similar_problems: Optional[List[Dict[str, Any]]] = None,
        solution_patterns: Optional[List[Dict[str, Any]]] = None
    ) -> Dict[str, Any]:
        """
        Solve math problem using retrieved context and memory
        
        Args:
            problem_text: The math problem
            topic: Problem topic (algebra, calculus, etc.)
            variables: Extracted variables
            constraints: Problem constraints
            retrieved_context: Retrieved chunks from RAG
            similar_problems: Similar problems from memory (optional)
            solution_patterns: Known solution patterns from memory (optional)
        
        Returns:
            Solution with steps, answer, and metadata
        """
        # Use strict format for simple probability
        if topic.lower() == "probability" and self._is_simple_probability(problem_text):
            return self._solve_simple_probability(problem_text)
        
        # Use LLM for complex problems
        return self._solve_with_llm(problem_text, topic, variables, constraints, 
                                   retrieved_context, similar_problems, solution_patterns)
    
    def _is_simple_probability(self, problem_text: str) -> bool:
        """Check if this is a simple probability (single-event or conditional)"""
        problem_lower = problem_text.lower()
        
        # Check for conditional probability (P(B|A) type)
        is_conditional = any(kw in problem_lower for kw in [
            'given that', 'who plays', 'also plays', 'conditional probability',
            'if a', 'among those', 'of those who'
        ])
        
        # Check for simple single-event
        single_event = any(kw in problem_lower for kw in [
            'randomly pick', 'draw one', 'select one', 'randomly select'
        ])
        simple_object = any(obj in problem_lower for obj in ['marble', 'card', 'ball', 'coin'])
        no_multi_stage = 'without replacement' not in problem_lower
        
        return is_conditional or (single_event and simple_object and no_multi_stage)
    
    def _solve_simple_probability(self, problem_text: str) -> Dict[str, Any]:
        """Solve simple probability with strict format"""
        import re
        from math import gcd
        
        # Check for conditional probability pattern
        if any(kw in problem_text.lower() for kw in ['who plays', 'also plays', 'conditional', 'given that']):
            # Extract numbers
            numbers = [int(n) for n in re.findall(r'\b\d+\b', problem_text)]
            
            if len(numbers) >= 3:
                # Pattern: N total, A play sport1, B play sport2, C play both
                # P(B|A) = C/A
                
                # Identify which numbers are which
                # Look for "play both" to find intersection
                both_match = re.search(r'(\d+)\s+students?\s+play\s+both', problem_text.lower())
                
                if both_match:
                    both = int(both_match.group(1))
                    
                    # Find "play soccer" or first sport
                    first_sport_match = re.search(r'(\d+)\s+students?\s+play\s+(soccer|basketball|\w+)', problem_text.lower())
                    if first_sport_match:
                        first_count = int(first_sport_match.group(1))
                        first_sport = first_sport_match.group(2)
                        
                        # Simplify fraction
                        divisor = gcd(both, first_count)
                        num = both // divisor
                        denom = first_count // divisor
                        
                        return {
                            "success": True,
                            "solution_text": "Conditional probability using intersection over condition",
                            "steps": [
                                f"Number of students who play {first_sport} = {first_count}",
                                f"Number of students who play both sports = {both}",
                                f"Conditional probability P(both|{first_sport}) = {both}/{first_count} = {num}/{denom}"
                            ],
                            "final_answer": f"{num}/{denom}",
                            "context_used": 0,
                            "topic": "Probability"
                        }
        
        # Extract all numbers from problem
        numbers = [int(n) for n in re.findall(r'\b\d+\b', problem_text)]
        
        if len(numbers) < 2:
            return {"success": False, "error": "Cannot extract numbers"}
        
        # For "X red, Y blue, Z green" pattern
        if len(numbers) >= 2:
            # Calculate total
            total = sum(numbers)
            
            # Find target color (look for "probability of selecting X")
            target_match = re.search(r'probability of selecting (?:a |an )?(\w+)', problem_text.lower())
            if target_match:
                target_color = target_match.group(1)
                
                # Find which number corresponds to target color
                # Look for "3 blue" pattern
                color_pattern = rf'(\d+)\s+{target_color}'
                color_match = re.search(color_pattern, problem_text.lower())
                
                if color_match:
                    favorable = int(color_match.group(1))
                    
                    # Simplify fraction
                    divisor = gcd(favorable, total)
                    num = favorable // divisor
                    denom = total // divisor
                    
                    return {
                        "success": True,
                        "solution_text": "Single-event probability using favorable/total outcomes formula",
                        "steps": [
                            f"Total marbles = {' + '.join(map(str, numbers))} = {total}",
                            f"Number of {target_color} marbles = {favorable}",
                            f"Probability = {favorable}/{total} = {num}/{denom}"
                        ],
                        "final_answer": f"{num}/{denom}",
                        "context_used": 0,
                        "topic": "Probability"
                    }
        
        # Fallback to LLM if pattern matching fails
        return {"success": False, "error": "Pattern matching failed"}
    
    def _solve_with_llm(self, problem_text: str, topic: str, variables: Dict[str, Any],
                        constraints: Dict[str, Any], retrieved_context: List[Dict[str, Any]],
                        similar_problems: Optional[List[Dict[str, Any]]] = None,
                        solution_patterns: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
        """
        Solve using LLM for complex problems with memory patterns
        """
        # Build context section
        context_text = self._format_context(retrieved_context)
        
        # Build memory patterns section
        memory_text = self._format_memory_patterns(solution_patterns, similar_problems)
        
        # Build solver prompt
        system_prompt = """You are an expert math tutor solving JEE-level problems.

CRITICAL RULES:
1. Use ONLY the retrieved context below for formulas and methods
2. Reference known solution patterns when applicable
3. Show step-by-step working clearly
4. Explain your reasoning at each step
5. If context is insufficient, say so clearly
6. Verify domain constraints (e.g., x > 0 for √x)
7. Format math using LaTeX where needed

Your solution must be structured and easy to follow."""

        user_prompt = f"""Solve this math problem:

**Problem:** {problem_text}

**Topic:** {topic}

**Given Variables:** {variables}

**Constraints:** {constraints}

**Retrieved Context:**
{context_text}
{memory_text}
**Instructions:**
- Use the context to identify relevant formulas/methods
- Apply known solution patterns if applicable
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
            # Skip non-dict items
            if not isinstance(item, dict):
                continue
                
            text = item.get('text', '')
            metadata = item.get('metadata', {})
            score = item.get('score', 0)
            
            # Skip if essential fields are missing
            if not text:
                continue
            
            source = metadata.get('source', 'Unknown') if isinstance(metadata, dict) else 'Unknown'
            topic = metadata.get('topic', 'General') if isinstance(metadata, dict) else 'General'
            
            formatted.append(
                f"[Context {i}] (Source: {source}, Topic: {topic}, Relevance: {score:.2f})\n{text}"
            )
        
        return "\n\n".join(formatted) if formatted else "No relevant context found."
    
    def _format_memory_patterns(self, solution_patterns: Optional[List[Dict[str, Any]]], 
                                similar_problems: Optional[List[Dict[str, Any]]]) -> str:
        """
        Format memory patterns and similar problems for prompt
        
        Args:
            solution_patterns: Known solution patterns from memory
            similar_problems: Similar past problems
        
        Returns:
            Formatted memory section for prompt
        """
        if not solution_patterns and not similar_problems:
            return ""
        
        formatted = []
        
        # Add solution patterns
        if solution_patterns:
            formatted.append("\n**Known Solution Patterns (From Past Correct Solutions):**")
            for i, pattern in enumerate(solution_patterns[:2], 1):  # Top 2 patterns
                steps = pattern.get('steps', [])
                if steps:
                    formatted.append(f"\nPattern {i}:")
                    for j, step in enumerate(steps[:3], 1):  # First 3 steps
                        step_text = step if isinstance(step, str) else str(step)
                        formatted.append(f"  {j}. {step_text}")
                    formatted.append(f"  → Answer: {pattern.get('final_answer', 'N/A')}")
        
        # Add similar problems reference
        if similar_problems:
            formatted.append(f"\n**Similar Problems Found:** {len(similar_problems)} similar problems in memory")
            formatted.append("Use similar approaches if applicable.\n")
        
        return "\n".join(formatted) if formatted else ""
    
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
