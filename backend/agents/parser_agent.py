"""
Parser Agent - Parse and structure math problems using LLM
Cleans OCR/ASR noise, detects ambiguity, identifies topics and variables
"""

import json
import re
from typing import Dict, Any
from services.llm_service import LLMService

class ParserAgent:
    """Agent for parsing math problems into structured format"""
    
    def __init__(self, llm_service: LLMService):
        """
        Initialize Parser Agent
        
        Args:
            llm_service: LLM service instance
        """
        self.llm = llm_service
        self.system_prompt = """You are a math problem parser AI. Your job is to:
1. Clean OCR/ASR noise and fix common transcription errors (typos, spacing)
2. Normalize math notation (convert symbols like ^, ×, ÷ to proper LaTeX or readable format)
3. Identify the mathematical topic (algebra, calculus, geometry, probability, etc.)
4. Extract variables and constraints
5. Detect if the problem is ambiguous or missing information
6. Convert to structured JSON format

CRITICAL: PRESERVE the EXACT QUESTION STRUCTURE, especially:
- "If [equation], then [expression] = ?" - DO NOT change to "Solve for x"
- "Find [expression] if [equation]" - Keep both parts
- Multi-part questions - Keep all parts intact

MATH NOTATION HANDLING:
- Convert ^ to proper exponent format (e.g., "x^2" → "x²" or "x^2")
- Convert × to * or · for clarity
- Convert ÷ to / for clarity
- Keep √, ∫, Σ, and other symbols as-is
- Ensure proper spacing around operators

Only fix typos/OCR errors and normalize notation. DO NOT rephrase or simplify the question.

Topics: Algebra, Calculus, Linear Algebra, Probability, Trigonometry, Geometry, Number Theory, Statistics

Respond ONLY with valid JSON in this exact format:
{
  "problem_text": "cleaned problem (preserve structure!)",
  "topic": "topic name",
  "variables": ["list", "of", "variables"],
  "constraints": ["list of constraints like 'x > 0'"],
  "needs_clarification": false,
  "clarification_reason": "why clarification is needed (if any)",
  "confidence": 0.95
}

Examples:
Input: "solve 2x^2 + 5x - 3 = 0"
Output: {"problem_text": "Solve 2x² + 5x - 3 = 0", "topic": "Algebra", "variables": ["x"], "constraints": [], "needs_clarification": false, "clarification_reason": "", "confidence": 0.95}

Input: "If 3x = 6x - 15, then x + 8 = ?"
Output: {"problem_text": "If 3x = 6x - 15, then x + 8 = ?", "topic": "Algebra", "variables": ["x"], "constraints": [], "needs_clarification": false, "clarification_reason": "", "confidence": 0.98}

Input: "find d/dx(x³)"
Output: {"problem_text": "Find d/dx(x³)", "topic": "Calculus", "variables": ["x"], "constraints": [], "needs_clarification": false, "clarification_reason": "", "confidence": 0.95}

Input: "sin(θ) = 0.5, find θ"
Output: {"problem_text": "If sin(θ) = 0.5, find θ", "topic": "Trigonometry", "variables": ["θ"], "constraints": ["0 ≤ θ ≤ 2π"], "needs_clarification": false, "clarification_reason": "", "confidence": 0.90}

Input: "find derivative"
Output: {"problem_text": "Find derivative", "topic": "Calculus", "variables": [], "constraints": [], "needs_clarification": true, "clarification_reason": "Missing function to differentiate", "confidence": 0.3}
"""
    
    def parse(self, problem_text: str) -> Dict[str, Any]:
        """
        Parse problem text into structured format
        
        Args:
            problem_text: Raw problem text from OCR/ASR/text input
        
        Returns:
            Structured problem data with metadata
        """
        # Create prompt
        user_prompt = f"""Parse this math problem:

"{problem_text}"

Return only the JSON object, no additional text."""
        
        # Call LLM
        response = self.llm.generate(
            prompt=user_prompt,
            system=self.system_prompt,
            temperature=0.1,
            max_tokens=500
        )
        
        if not response["success"]:
            # Fallback to basic parsing if LLM fails
            return {
                "problem_text": problem_text,
                "topic": "General",
                "variables": self._extract_variables_fallback(problem_text),
                "constraints": [],
                "needs_clarification": len(problem_text.strip()) < 10,
                "clarification_reason": "LLM service unavailable" if not response["success"] else "",
                "confidence": 0.3,
                "error": response.get("error", ""),
                "agent": "parser"
            }
        
        # Parse JSON response
        try:
            # Extract JSON from response (in case LLM adds extra text)
            response_text = response["text"].strip()
            
            # Find JSON object
            json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
            if json_match:
                json_str = json_match.group(0)
                parsed = json.loads(json_str)
                
                # Add metadata
                parsed["agent"] = "parser"
                parsed["raw_llm_response"] = response_text
                
                return parsed
            else:
                raise ValueError("No JSON found in LLM response")
        
        except (json.JSONDecodeError, ValueError) as e:
            # Fallback parsing
            return {
                "problem_text": problem_text,
                "topic": "General",
                "variables": self._extract_variables_fallback(problem_text),
                "constraints": [],
                "needs_clarification": True,
                "clarification_reason": f"Failed to parse LLM response: {str(e)}",
                "confidence": 0.2,
                "agent": "parser",
                "error": str(e)
            }
    
    def _extract_variables_fallback(self, text: str) -> list:
        """Fallback method to extract variables using regex"""
        # Find single-letter variables
        variables = set(re.findall(r'\b([a-z])\b', text.lower()))
        
        # Remove common words
        common_words = {'a', 'i', 'x', 'y', 'z', 'n', 't', 'r'}
        variables = variables.intersection(common_words)
        
        return sorted(list(variables))
