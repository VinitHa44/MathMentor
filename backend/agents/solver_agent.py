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
        # Try strict format for simple probability, fallback to LLM if it fails
        if topic.lower() == "probability" and self._is_simple_probability(problem_text):
            simple_result = self._solve_simple_probability(problem_text)
            if simple_result.get('success', False):
                return simple_result
            # If pattern matching fails, continue to LLM solver
        
        # Use LLM for complex problems or when pattern matching fails
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
        system_prompt = """You are a precise math tutor. Follow the provided context and examples EXACTLY.

CRITICAL RULES:
1. If the problem matches an example in the context, USE THAT EXACT SOLUTION METHOD
2. Copy formulas and steps from the context - do NOT modify the approach
3. If user corrections are provided, those are the CORRECT solutions - follow them exactly
4. Be brief and show calculations clearly
5. Use simple notation (e.g., 4/13 instead of LaTeX)

NEVER invent your own approach when the context shows the correct method."""

        user_prompt = f"""**Problem:** {problem_text}

**Topic:** {topic}

**Retrieved Context with Correct Solutions:**
{context_text}
{memory_text}
**IMPORTANT:**
- If this problem matches an example above, use EXACTLY that method
- The context examples show the CORRECT approach - follow them precisely
- User corrections in memory are verified correct solutions

**Your Task:**
1. Find the matching example/pattern in context
2. Apply the EXACT same steps with your problem's numbers
3. Show your calculation
4. State: Final Answer: [number]

Solve:"""

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
        
        # Add solution patterns from user corrections - THESE ARE CORRECT!
        if solution_patterns:
            formatted.append("\n**USER-CORRECTED SOLUTIONS (Verified Correct - Use These!):**")
            for i, pattern in enumerate(solution_patterns[:3], 1):  # Top 3 patterns
                steps = pattern.get('steps', [])
                problem_snippet = pattern.get('problem_snippet', 'N/A')
                formatted.append(f"\nCorrected Solution {i}:")
                formatted.append(f"Problem: {problem_snippet}")
                if steps:
                    for j, step in enumerate(steps[:5], 1):  # Show more steps
                        step_text = step if isinstance(step, str) else str(step)
                        formatted.append(f"  Step {j}: {step_text}")
                formatted.append(f"  **Final Answer: {pattern.get('final_answer', 'N/A')}**")
                formatted.append("")
        
        # Add similar problems reference
        if similar_problems:
            formatted.append(f"\n**Similar Problems Found:** {len(similar_problems)} similar problems in memory")
            formatted.append("Use similar approaches.\n")
        
        return "\n".join(formatted) if formatted else ""
    
    def _extract_steps(self, solution_text: str) -> List[str]:
        """Extract solution steps from text"""
        import re
        
        lines = solution_text.split('\n')
        steps = []
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # Remove duplicate step prefixes like "Step 1: Step 1"
            line = re.sub(r'^(Step\s+\d+:)\s*\1', r'\1', line, flags=re.IGNORECASE)
            
            # Clean up LaTeX issues
            line = re.sub(r'\\endterm:', '', line)  # Remove \endterm:
            line = re.sub(r'\\frac\{(\d+)\}\{(\d+)\}', r'\1/\2', line)  # Convert \frac to simple fractions
            
            # Only add lines that look like steps or have content
            if line and any([
                line.lower().startswith('step'),
                re.match(r'^\d+\.', line),
                ':' in line and len(line) > 10,
                'formula' in line.lower(),
                'calculate' in line.lower(),
                '=' in line
            ]):
                steps.append(line)
        
        # If no steps found, return the whole text as one step
        if not steps:
            return [solution_text]
        
        return steps
    
    def _extract_final_answer(self, solution_text: str) -> str:
        """Extract final answer from solution"""
        import re
        
        # Clean up common LaTeX issues first
        solution_text = re.sub(r'\\endterm:', '', solution_text)
        solution_text = re.sub(r'\\frac\{(\d+)\}\{(\d+)\}', r'\1/\2', solution_text)
        
        # Look for boxed answers first (most explicit)
        boxed_match = re.search(r'\\boxed\{([^}]+)\}', solution_text)
        if boxed_match:
            answer = boxed_match.group(1).strip()
            # Convert LaTeX fractions in boxed answer
            answer = re.sub(r'\\frac\{(\d+)\}\{(\d+)\}', r'\1/\2', answer)
            return answer
        
        # Look for "Final Answer: X" or "Answer: X" with simple fraction
        answer_match = re.search(r'(?:Final\s+)?Answer[:\s]+(\d+/\d+|\d+\.?\d*)', solution_text, re.IGNORECASE)
        if answer_match:
            return answer_match.group(1).strip()
        
        # Look for fractions or numbers after "= " at the end
        equals_matches = re.findall(r'=\s*(\d+/\d+|\d+\.?\d*)', solution_text)
        if equals_matches:
            return equals_matches[-1].strip()
        
        # Look for standalone fractions near the end
        fraction_matches = re.findall(r'\b(\d+/\d+)\b', solution_text)
        if fraction_matches:
            return fraction_matches[-1]
        
        # Look for common conclusion patterns
        lower_text = solution_text.lower()
        answer_markers = [
            ("final answer:", 50),
            ("answer:", 50),
            ("therefore", 80),
        ]
        
        for marker, max_len in answer_markers:
            if marker in lower_text:
                idx = lower_text.find(marker)
                after_marker = solution_text[idx + len(marker):].strip()
                
                # Extract up to max_len characters or first newline
                end_idx = min(len(after_marker), max_len)
                newline_idx = after_marker.find('\n')
                if newline_idx != -1 and newline_idx < end_idx:
                    end_idx = newline_idx
                
                answer = after_marker[:end_idx].strip()
                # Clean up
                answer = re.sub(r'^(the\s+)?(answer\s+is\s+)?', '', answer, flags=re.IGNORECASE)
                answer = re.sub(r'\s+', ' ', answer)  # Collapse whitespace
                if answer and len(answer) < 100:
                    return answer
        
        # Fallback: last line with a number or fraction
        lines = [l.strip() for l in solution_text.split('\n') if l.strip()]
        for line in reversed(lines[-3:]):
            if re.search(r'\d+/\d+|=\s*\d+', line) and len(line) < 100:
                return line
        
        return lines[-1] if lines else "See solution above"
