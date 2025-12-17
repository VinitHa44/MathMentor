"""
Parser Service - Parse and structure math problems
Extracts variables, identifies topics, and detects ambiguities
"""

import re
from typing import Dict, Any, List

class ParserService:
    """Service for parsing math problem text into structured format"""
    
    def __init__(self):
        """Initialize parser with math patterns and topic keywords"""
        self.topic_keywords = {
            "Algebra": [
                "equation", "solve", "polynomial", "quadratic", "linear", 
                "variable", "factor", "expand", "simplify", "inequality"
            ],
            "Probability": [
                "probability", "chance", "random", "dice", "coin", "card",
                "permutation", "combination", "event", "outcome", "distribution"
            ],
            "Calculus": [
                "derivative", "integral", "limit", "differentiate", "integrate",
                "maximum", "minimum", "rate", "slope", "tangent", "area", "volume"
            ],
            "Linear Algebra": [
                "matrix", "vector", "determinant", "eigenvalue", "eigenvector",
                "system", "row", "column", "rank", "dimension"
            ],
            "Trigonometry": [
                "sin", "cos", "tan", "angle", "triangle", "hypotenuse",
                "sine", "cosine", "tangent", "radian", "degree"
            ],
            "Geometry": [
                "circle", "triangle", "square", "rectangle", "polygon",
                "area", "perimeter", "angle", "line", "point", "radius"
            ]
        }
    
    def parse_problem(self, text: str) -> Dict[str, Any]:
        """
        Parse math problem text into structured format
        
        Args:
            text: Problem text (from OCR, ASR, or direct input)
        
        Returns:
            Structured problem data
        """
        # Clean the text
        cleaned_text = self._clean_text(text)
        
        # Extract variables
        variables = self._extract_variables(cleaned_text)
        
        # Identify topic
        topic = self._identify_topic(cleaned_text)
        
        # Extract constraints
        constraints = self._extract_constraints(cleaned_text)
        
        # Check for ambiguities
        needs_clarification = self._check_ambiguity(cleaned_text, variables)
        
        # Calculate confidence
        confidence = self._calculate_confidence(cleaned_text, variables, topic)
        
        return {
            "problem_text": cleaned_text,
            "topic": topic,
            "variables": variables,
            "constraints": constraints,
            "needs_clarification": needs_clarification,
            "confidence": confidence
        }
    
    def _clean_text(self, text: str) -> str:
        """Clean and normalize problem text"""
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        
        # Remove leading/trailing whitespace
        text = text.strip()
        
        # Capitalize first letter
        if text:
            text = text[0].upper() + text[1:]
        
        return text
    
    def _extract_variables(self, text: str) -> List[str]:
        """
        Extract mathematical variables from text
        
        Args:
            text: Problem text
        
        Returns:
            List of identified variables
        """
        # Find single-letter variables (x, y, z, a, b, c, etc.)
        variables = set(re.findall(r'\b([a-z])\b', text.lower()))
        
        # Remove common words that are single letters
        common_words = {'a', 'i'}
        variables = variables - common_words
        
        # Find Greek letters if present
        greek_letters = re.findall(r'[α-ωΑ-Ω]', text)
        variables.update(greek_letters)
        
        return sorted(list(variables))
    
    def _identify_topic(self, text: str) -> str:
        """
        Identify the mathematical topic of the problem
        
        Args:
            text: Problem text
        
        Returns:
            Identified topic
        """
        text_lower = text.lower()
        
        # Count keyword matches for each topic
        topic_scores = {}
        for topic, keywords in self.topic_keywords.items():
            score = sum(1 for keyword in keywords if keyword in text_lower)
            topic_scores[topic] = score
        
        # Get topic with highest score
        if max(topic_scores.values()) > 0:
            return max(topic_scores, key=topic_scores.get)
        
        return "General"
    
    def _extract_constraints(self, text: str) -> List[str]:
        """
        Extract constraints and conditions from problem
        
        Args:
            text: Problem text
        
        Returns:
            List of constraints
        """
        constraints = []
        
        # Look for inequality symbols
        if '>' in text or '<' in text or '≥' in text or '≤' in text:
            # Extract inequality expressions
            inequality_patterns = [
                r'([a-z]\s*[><=≥≤]\s*[-+]?\d+)',
                r'([-+]?\d+\s*[><=≥≤]\s*[a-z])'
            ]
            for pattern in inequality_patterns:
                matches = re.findall(pattern, text.lower())
                constraints.extend(matches)
        
        # Look for domain restrictions
        domain_patterns = [
            r'where\s+([^,\.]+)',
            r'given\s+([^,\.]+)',
            r'such that\s+([^,\.]+)'
        ]
        for pattern in domain_patterns:
            matches = re.findall(pattern, text.lower())
            constraints.extend(matches)
        
        return constraints[:5]  # Limit to first 5 constraints
    
    def _check_ambiguity(self, text: str, variables: List[str]) -> bool:
        """
        Check if the problem statement is ambiguous or unclear
        
        Args:
            text: Problem text
            variables: Extracted variables
        
        Returns:
            True if clarification needed, False otherwise
        """
        # Check for very short text
        if len(text.split()) < 5:
            return True
        
        # Check for missing information indicators
        ambiguous_phrases = [
            "?",  # Only question mark, no clear question
            "find",  # "find" without clear what to find
            "calculate",  # "calculate" without clear what
        ]
        
        # Check if problem is too vague
        if len(text.split()) < 10 and any(phrase in text.lower() for phrase in ambiguous_phrases):
            return True
        
        # Check for variables without context
        if len(variables) > 5:  # Too many variables might indicate OCR errors
            return True
        
        return False
    
    def _calculate_confidence(self, text: str, variables: List[str], topic: str) -> float:
        """
        Calculate confidence in parsing
        
        Args:
            text: Problem text
            variables: Extracted variables
            topic: Identified topic
        
        Returns:
            Confidence score (0-1)
        """
        confidence = 1.0
        
        # Reduce confidence for short text
        if len(text.split()) < 10:
            confidence -= 0.2
        
        # Reduce confidence if no topic identified
        if topic == "General":
            confidence -= 0.1
        
        # Reduce confidence for too many variables (likely OCR errors)
        if len(variables) > 5:
            confidence -= 0.2
        
        # Reduce confidence if no mathematical symbols found
        math_symbols = ['=', '+', '-', '×', '÷', '^', '²', '³', '√']
        if not any(symbol in text for symbol in math_symbols):
            confidence -= 0.1
        
        return max(0.0, min(1.0, confidence))
