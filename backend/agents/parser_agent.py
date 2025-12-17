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
1. Clean OCR/ASR noise and fix common transcription errors
2. Identify the mathematical topic (algebra, calculus, geometry, probability, etc.)
3. Extract variables and constraints
4. Detect if the problem is ambiguous or missing information
5. Convert to structured JSON format

Topics: Algebra, Calculus, Linear Algebra, Probability, Trigonometry, Geometry, Number Theory, Statistics

Respond ONLY with valid JSON in this exact format:
{
  "problem_text": "cleaned problem statement",
  "topic": "topic name",
  "variables": ["list", "of", "variables"],
  "constraints": ["list of constraints like 'x > 0'"],
  "needs_clarification": false,
  "clarification_reason": "why clarification is needed (if any)",
  "confidence": 0.95
}

Examples:
Input: "solve 2x squared plus 5x minus 3 equals 0"
Output: {"problem_text": "Solve 2x² + 5x - 3 = 0", "topic": "Algebra", "variables": ["x"], "constraints": [], "needs_clarification": false, "clarification_reason": "", "confidence": 0.95}

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
