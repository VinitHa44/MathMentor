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
        # Try algebraic verification for algebra problems
        if topic.lower() == "algebra":
            algebra_result = self._verify_algebra_substitution(problem_text, final_answer)
            if algebra_result:
                return algebra_result
        
        # Try rule-based verification first for deterministic topics
        if topic.lower() == "probability":
            rule_result = self._verify_probability(problem_text, solution_text, final_answer)
            if rule_result:
                return rule_result
        
        # Fall back to LLM-based verification for complex cases
        return self._verify_with_llm(problem_text, solution_text, final_answer, topic, retrieved_context)
    
    def _verify_algebra_substitution(self, problem_text: str, final_answer: str) -> Dict[str, Any]:
        """
        Verify algebra solutions by substituting answer back into equation
        """
        try:
            from sympy import symbols, Eq, sympify, simplify
            from sympy.parsing.sympy_parser import parse_expr
            import re
            
            # Extract the main equation from problem
            problem_lower = problem_text.lower()
            
            # Pattern: "If [equation], then [expression] = ?"
            if_then_match = re.search(r'if\s+([^,]+),\s*then\s+([^=?]+)', problem_text, re.IGNORECASE)
            
            if if_then_match:
                equation_text = if_then_match.group(1).strip()
                query_expr_text = if_then_match.group(2).strip()
                
                # Clean equation
                equation_text = equation_text.replace('×', '*').replace('÷', '/')
                
                # Parse equation
                if '=' not in equation_text:
                    return None
                
                left_str, right_str = equation_text.split('=', 1)
                left_str = left_str.strip()
                right_str = right_str.strip()
                
                # Detect variable
                var_candidates = set(re.findall(r'\b([a-z])\b', equation_text.lower()))
                if not var_candidates:
                    return None
                
                var_name = 'x' if 'x' in var_candidates else list(var_candidates)[0]
                var = symbols(var_name)
                
                # Parse expressions
                try:
                    left_expr = parse_expr(left_str, transformations='all')
                    right_expr = parse_expr(right_str, transformations='all')
                except:
                    left_expr = sympify(left_str)
                    right_expr = sympify(right_str)
                
                # First, solve to find the correct x value
                equation = Eq(left_expr, right_expr)
                from sympy import solve
                solution = solve(equation, var)
                
                if not solution:
                    return None
                
                if isinstance(solution, list):
                    correct_x = solution[0]
                else:
                    correct_x = solution
                
                # Now evaluate the query expression with correct x
                query_clean = query_expr_text.replace('×', '*').replace('÷', '/')
                query_parsed = parse_expr(query_clean, transformations='all')
                correct_answer = simplify(query_parsed.subs(var, correct_x))
                
                # Compare with provided answer
                try:
                    provided_answer = sympify(final_answer.strip())
                    is_correct = simplify(provided_answer - correct_answer) == 0
                except:
                    # If can't parse provided answer, compare as strings
                    is_correct = str(correct_answer) == final_answer.strip()
                
                if is_correct:
                    return {
                        "success": True,
                        "is_correct": True,
                        "confidence": 1.0,
                        "issues": [],
                        "suggestions": [],
                        "verification_text": f"Verified by substitution: {var_name} = {correct_x}, {query_expr_text} = {correct_answer}",
                        "needs_human_review": False
                    }
                else:
                    return {
                        "success": True,
                        "is_correct": False,
                        "confidence": 1.0,
                        "issues": [
                            f"Incorrect answer. Expected {correct_answer}, got {final_answer}",
                            f"Equation {equation_text} solves to {var_name} = {correct_x}",
                            f"Therefore {query_expr_text} = {correct_answer}"
                        ],
                        "suggestions": [
                            f"Solve the equation {left_str} = {right_str} to get {var_name} = {correct_x}",
                            f"Then substitute into {query_expr_text} to get {correct_answer}"
                        ],
                        "verification_text": f"Substitution check failed. Correct answer is {correct_answer}",
                        "needs_human_review": False
                    }
            
            # If pattern doesn't match, return None to try other methods
            return None
            
        except Exception as e:
            # If verification fails, return None to fallback to LLM
            return None
    
    def _verify_probability(self, problem_text: str, solution_text: str, final_answer: str) -> Dict[str, Any]:
        """Rule-based verification for probability problems"""
        import re
        from math import gcd
        
        # Check for conditional probability pattern
        if any(kw in problem_text.lower() for kw in ['who plays', 'also plays', 'conditional', 'given that']):
            # Extract numbers
            numbers = [int(n) for n in re.findall(r'\b\d+\b', problem_text)]
            
            if len(numbers) >= 3:
                # Find "play both" to get intersection
                both_match = re.search(r'(\d+)\s+students?\s+play\s+both', problem_text.lower())
                first_sport_match = re.search(r'(\d+)\s+students?\s+play\s+(soccer|basketball|\w+)', problem_text.lower())
                
                if both_match and first_sport_match:
                    both = int(both_match.group(1))
                    first_count = int(first_sport_match.group(1))
                    
                    # Expected answer: both/first_count simplified
                    divisor = gcd(both, first_count)
                    expected_num = both // divisor
                    expected_denom = first_count // divisor
                    expected = f"{expected_num}/{expected_denom}"
                    
                    # Check if final answer matches
                    answer_clean = final_answer.strip()
                    is_correct = answer_clean == expected
                    
                    if not is_correct:
                        return {
                            "success": True,
                            "is_correct": False,
                            "confidence": 0.99,
                            "issues": [f"Expected {expected}, got {answer_clean}"],
                            "suggestions": [f"Conditional probability P(both|first) = {both}/{first_count} = {expected}"],
                            "verification_text": f"Conditional probability should be {expected}"
                        }
                    
                    return {
                        "success": True,
                        "is_correct": True,
                        "confidence": 0.99,
                        "issues": [],
                        "suggestions": [],
                        "verification_text": "Correct conditional probability calculation"
                    }
        
        # Original simple probability check
        import re
        
        # Extract numbers from PROBLEM (not solution)
        problem_numbers = [int(n) for n in re.findall(r'\b\d+\b', problem_text)]
        if len(problem_numbers) < 2:
            return None  # Too complex for rule-based
        
        # Check if it's a simple single-event probability
        keywords = ['marble', 'card', 'ball', 'coin', 'die', 'dice']
        if not any(kw in problem_text.lower() for kw in keywords):
            return None
        
        # Extract answer fraction from final_answer
        answer_match = re.search(r'(\d+)/(\d+)', final_answer)
        if not answer_match:
            return None  # Cannot parse answer
        
        numerator = int(answer_match.group(1))
        denominator = int(answer_match.group(2))
        
        issues = []
        
        # Check 1: Total should equal sum of parts
        total_from_problem = sum(problem_numbers)
        if denominator != total_from_problem:
            issues.append(f"Denominator ({denominator}) should equal total from problem ({total_from_problem})")
        
        # Check 2: Probability should be between 0 and 1
        if numerator > denominator:
            issues.append(f"Probability ({numerator}/{denominator}) is greater than 1")
        
        # Check 3: Numerator should be one of the numbers in problem
        if numerator not in problem_numbers:
            issues.append(f"Numerator ({numerator}) should be one of the counts from problem")
        
        # Check 4: Check if fraction is simplified
        from math import gcd
        if gcd(numerator, denominator) > 1:
            issues.append(f"Fraction {numerator}/{denominator} is not in simplest form")
        
        # Determine correctness
        is_correct = len(issues) == 0
        
        return {
            "success": True,
            "is_correct": is_correct,
            "confidence": 0.99 if is_correct else 0.70,  # Return as 0-1 range
            "issues": issues if issues else [],
            "suggestions": [] if is_correct else ["Review calculations", "Check if fraction is simplified"],
            "verification_text": "Rule-based verification for basic probability",
            "needs_human_review": not is_correct
        }
    
    def _verify_with_llm(self, problem_text: str, solution_text: str, final_answer: str, 
                         topic: str, retrieved_context: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        LLM-based verification for complex problems
        """
        # Build context section
        context_text = self._format_context(retrieved_context)
        
        # Build verifier prompt with explicit substitution check
        system_prompt = """You are a CRITICAL math verifier for JEE-level problems. Your job is to find errors.

MANDATORY VERIFICATION STEPS FOR ALGEBRA:
1. **Extract the original equation** from the problem
2. **Solve it step-by-step yourself** to find the correct value
3. **Substitute the claimed answer back** into the original equation
4. **Check if both sides are equal** - if not, the answer is WRONG

VERIFICATION CHECKLIST (ALL topics):
1. Formula correctness (check against retrieved context)
2. Calculation accuracy - recalculate each step
3. Substitution verification - does the answer satisfy the equation?
4. Domain constraints (e.g., x > 0 for √x)
5. Edge cases handling
6. Logical flow
7. Units and reasonableness

BE SKEPTICAL. If you find ANY error, mark as incorrect.

OUTPUT FORMAT (strict):
Is Correct: Yes/No
Confidence: 0-100%
Issues Found: [list any problems, be specific]
Suggestions: [how to fix]

If you cannot verify with 100% certainty, state that clearly."""

        user_prompt = f"""Verify this solution CRITICALLY:

**Problem:** {problem_text}

**Claimed Solution:**
{solution_text}

**Claimed Final Answer:** {final_answer}

**Topic:** {topic}

**Retrieved Context (for formula checking):**
{context_text}

**CRITICAL VERIFICATION TASK:**

FOR ALGEBRA PROBLEMS:
1. Extract the equation from the problem
2. Solve it yourself step-by-step
3. Substitute the claimed answer back into the original equation
4. Check if both sides are equal
5. If they're not equal, the answer is WRONG

FOR ALL PROBLEMS:
- Recalculate every step
- Check formulas against context
- Verify units and constraints
- Look for calculation errors

**Be thorough. If anything seems wrong, mark it as incorrect.**

Your verification:"""

        # Generate verification
        try:
            response = self.llm.generate(
                prompt=user_prompt,
                system=system_prompt,
                temperature=0.1,  # Very low for consistent checking
                max_tokens=1500
            )
            
            # Extract text from response dict
            response_text = response.get("text", "")
            
            # Parse verification result
            is_correct = self._parse_correctness(response_text)
            confidence = self._parse_confidence(response_text)
            issues = self._extract_issues(response_text)
            suggestions = self._extract_suggestions(response_text)
            
            # Convert confidence from 0-100 to 0-1 range
            confidence_normalized = confidence / 100.0 if confidence > 1 else confidence
            
            # Lower confidence threshold - if verifier is unsure, mark for review
            needs_review = not is_correct or confidence_normalized < 0.85
            
            return {
                "success": True,
                "is_correct": is_correct,
                "confidence": confidence_normalized,
                "issues": issues,
                "suggestions": suggestions,
                "verification_text": response_text,
                "needs_human_review": needs_review
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
            # Skip non-dict items
            if not isinstance(item, dict):
                continue
                
            text = item.get('text', '')
            metadata = item.get('metadata', {})
            
            # Skip if essential fields are missing
            if not text:
                continue
            
            source = metadata.get('source', 'Unknown') if isinstance(metadata, dict) else 'Unknown'
            
            formatted.append(
                f"[Ref {i}] (Source: {source})\n{text}"
            )
        
        return "\n\n".join(formatted[:3]) if formatted else "No context for verification."  # Top 3 for verification
    
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
