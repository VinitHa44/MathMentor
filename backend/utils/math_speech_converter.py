"""
Math Speech Converter - Convert spoken math phrases to mathematical notation
Handles natural language math expressions from ASR transcription
"""

import re
from typing import Dict, Tuple, List


class MathSpeechConverter:
    """Converts spoken math expressions to mathematical notation"""
    
    def __init__(self):
        """Initialize converter with comprehensive phrase mappings"""
        
        # Power and exponent patterns (order matters - check longer phrases first)
        self.power_patterns = [
            (r'\b(\w+)\s+raised\s+to\s+(?:the\s+power\s+(?:of\s+)?)?(\w+)', r'\1^\2'),
            (r'\b(\w+)\s+to\s+the\s+power\s+(?:of\s+)?(\w+)', r'\1^\2'),
            (r'\b(\w+)\s+upto\s+(\w+)', r'\1^\2'),
            (r'\b(\w+)\s+power\s+(\w+)', r'\1^\2'),
            (r'\b(\w+)\s+squared\b', r'\1²'),
            (r'\b(\w+)\s+cubed\b', r'\1³'),
            (r'\bsquare\s+of\s+(\w+)', r'\1²'),
            (r'\bcube\s+of\s+(\w+)', r'\1³'),
        ]
        
        # Root patterns
        self.root_patterns = [
            (r'\bsquare\s+root\s+of\s+([^,\.;]+?)(?:\s+(?:plus|minus|times|divided|equals|and|then|if)|\.|,|;|$)', r'√(\1) '),
            (r'\bcube\s+root\s+of\s+([^,\.;]+?)(?:\s+(?:plus|minus|times|divided|equals|and|then|if)|\.|,|;|$)', r'∛(\1) '),
            (r'\bnth\s+root\s+of\s+([^,\.;]+?)(?:\s+(?:plus|minus|times|divided|equals|and|then|if)|\.|,|;|$)', r'ⁿ√(\1) '),
        ]
        
        # Trigonometric functions
        self.trig_patterns = [
            (r'\bsine\s+of\s+(\w+)', r'sin(\1)'),
            (r'\bsin\s+(\w+)', r'sin(\1)'),
            (r'\bcosine\s+of\s+(\w+)', r'cos(\1)'),
            (r'\bcos\s+(\w+)', r'cos(\1)'),
            (r'\btangent\s+of\s+(\w+)', r'tan(\1)'),
            (r'\btan\s+(\w+)', r'tan(\1)'),
            (r'\bcosec\s+of\s+(\w+)', r'cosec(\1)'),
            (r'\bcosec\s+(\w+)', r'cosec(\1)'),
            (r'\bsecant\s+of\s+(\w+)', r'sec(\1)'),
            (r'\bsec\s+(\w+)', r'sec(\1)'),
            (r'\bcotangent\s+of\s+(\w+)', r'cot(\1)'),
            (r'\bcot\s+(\w+)', r'cot(\1)'),
            (r'\barc\s+sine\s+of\s+(\w+)', r'arcsin(\1)'),
            (r'\barc\s+cosine\s+of\s+(\w+)', r'arccos(\1)'),
            (r'\barc\s+tan\s+of\s+(\w+)', r'arctan(\1)'),
        ]
        
        # Calculus patterns
        self.calculus_patterns = [
            (r'\bderivative\s+of\s+([^,\.;]+?)\s+with\s+respect\s+to\s+(\w+)', r'd\1/d\2'),
            (r'\bderivative\s+of\s+([^,\.;]+?)(?:\s+(?:with|equals|and|then|if|plus|minus)|\.|,|;|$)', r'd/dx(\1) '),
            (r'\bd\s+by\s+d\s*(\w+)\s+of\s+([^,\.;]+?)(?:\s+(?:with|equals|and|then|if)|\.|,|;|$)', r'd\2/d\1 '),
            (r'\bintegral\s+of\s+([^,\.;]+?)(?:\s+(?:from|with|equals|and|then|if)|\.|,|;|$)', r'∫(\1) '),
            (r'\bintegral\s+from\s+(\w+)\s+to\s+(\w+)\s+of\s+([^,\.;]+?)(?:\s+(?:with|equals|and|then|if)|\.|,|;|$)', r'∫[\1 to \2](\3) '),
            (r'\blimit\s+as\s+(\w+)\s+approaches\s+(\w+)\s+of\s+([^,\.;]+?)(?:\s+(?:with|equals|and|then|if)|\.|,|;|$)', r'lim[\1→\2](\3) '),
            (r'\blimit\s+of\s+([^,\.;]+?)\s+as\s+(\w+)\s+approaches\s+(\w+)', r'lim[\2→\3](\1)'),
            (r'\bpartial\s+derivative\s+of\s+([^,\.;]+?)\s+with\s+respect\s+to\s+(\w+)', r'∂\1/∂\2'),
            (r'\bpartial\s+([^,\.;]+?)\s+by\s+partial\s+(\w+)', r'∂\1/∂\2'),
        ]
        
        # Summation and product patterns
        self.series_patterns = [
            (r'\bsummation\s+from\s+(\w+)\s*=\s*(\w+)\s+to\s+(\w+)\s+of\s+([^\s]+)', r'Σ[\1=\2 to \3](\4)'),
            (r'\bsum\s+from\s+(\w+)\s*=\s*(\w+)\s+to\s+(\w+)\s+of\s+([^\s]+)', r'Σ[\1=\2 to \3](\4)'),
            (r'\bproduct\s+from\s+(\w+)\s*=\s*(\w+)\s+to\s+(\w+)\s+of\s+([^\s]+)', r'Π[\1=\2 to \3](\4)'),
        ]
        
        # Basic operators (apply these last, after complex patterns)
        self.operator_replacements = {
            r'\bequals\s+to\b': '=',
            r'\bequal\s+to\b': '=',
            r'\bequals\b': '=',
            r'\bequal\b': '=',
            r'\bis\s+equal\s+to\b': '=',
            r'\bplus\b': '+',
            r'\bminus\b': '-',
            r'\btimes\b': '×',
            r'\bmultiplied\s+by\b': '×',
            r'\bmultiply\b': '×',
            r'\bdivided\s+by\b': '÷',
            r'\bdivide\s+by\b': '÷',
            r'\bover\b': '/',
            r'\bgreater\s+than\s+or\s+equal\s+to\b': '≥',
            r'\bless\s+than\s+or\s+equal\s+to\b': '≤',
            r'\bgreater\s+than\b': '>',
            r'\bless\s+than\b': '<',
            r'\bnot\s+equal\s+to\b': '≠',
            r'\bapproximately\s+equal\s+to\b': '≈',
            r'\bapproximately\b': '≈',
        }
        
        # Greek letters and symbols
        self.symbol_replacements = {
            r'\bpi\b': 'π',
            r'\btheta\b': 'θ',
            r'\balpha\b': 'α',
            r'\bbeta\b': 'β',
            r'\bgamma\b': 'γ',
            r'\bdelta\b': 'Δ',
            r'\bepsilon\b': 'ε',
            r'\bzeta\b': 'ζ',
            r'\beta\b': 'η',
            r'\biota\b': 'ι',
            r'\bkappa\b': 'κ',
            r'\blambda\b': 'λ',
            r'\bmu\b': 'μ',
            r'\bnu\b': 'ν',
            r'\bxi\b': 'ξ',
            r'\bomicron\b': 'ο',
            r'\brho\b': 'ρ',
            r'\bsigma\b': 'σ',
            r'\btau\b': 'τ',
            r'\bupsilon\b': 'υ',
            r'\bphi\b': 'φ',
            r'\bchi\b': 'χ',
            r'\bpsi\b': 'ψ',
            r'\bomega\b': 'ω',
            r'\binfinity\b': '∞',
            r'\binfinity\b': '∞',
        }
        
        # Fractions
        self.fraction_patterns = [
            (r'\b(\w+)\s+over\s+(\w+)', r'(\1/\2)'),
            (r'\bfraction\s+(\w+)\s+over\s+(\w+)', r'(\1/\2)'),
        ]
        
        # Absolute value and other brackets
        self.bracket_patterns = [
            (r'\babsolute\s+value\s+of\s+([^,\.;]+?)(?:\s+(?:plus|minus|times|divided|equals|and|then|if)|\.|,|;|$)', r'|\1| '),
            (r'\bmod\s+of\s+([^,\.;]+?)(?:\s+(?:plus|minus|times|divided|equals|and|then|if)|\.|,|;|$)', r'|\1| '),
            (r'\bopen\s+bracket\b', '('),
            (r'\bclose\s+bracket\b', ')'),
            (r'\bopen\s+paren\b', '('),
            (r'\bclose\s+paren\b', ')'),
        ]
        
        # Factorial
        self.factorial_pattern = (r'\b(\w+)\s+factorial\b', r'\1!')
        
        # Logarithms
        self.log_patterns = [
            (r'\blog\s+base\s+(\w+)\s+of\s+(\w+)', r'log_\1(\2)'),
            (r'\bnatural\s+log\s+of\s+(\w+)', r'ln(\1)'),
            (r'\bln\s+of\s+(\w+)', r'ln(\1)'),
            (r'\blog\s+of\s+(\w+)', r'log(\1)'),
        ]
    
    def convert(self, text: str) -> str:
        """
        Convert spoken math to mathematical notation
        
        Args:
            text: Raw transcribed text from ASR
        
        Returns:
            Text with mathematical notation
        """
        # Make case-insensitive
        result = text.lower()
        
        # Apply patterns in specific order
        # Note: Powers/roots BEFORE calculus so "x cubed" becomes "x³" first
        
        # 1. Greek letters and symbols (first, as they're simple and don't conflict)
        for pattern, replacement in self.symbol_replacements.items():
            result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)
        
        # 2. Powers and exponents (early, so calculus patterns can use them)
        for pattern, replacement in self.power_patterns:
            result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)
        
        # 3. Roots (after powers, before calculus)
        for pattern, replacement in self.root_patterns:
            result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)
        
        # 4. Calculus (after powers are converted)
        for pattern, replacement in self.calculus_patterns:
            result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)
        
        # 5. Series and summations
        for pattern, replacement in self.series_patterns:
            result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)
        
        # 6. Logarithms
        for pattern, replacement in self.log_patterns:
            result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)
        
        # 7. Trigonometric functions
        for pattern, replacement in self.trig_patterns:
            result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)
        
        # 8. Fractions
        for pattern, replacement in self.fraction_patterns:
            result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)
        
        # 9. Absolute values and brackets
        for pattern, replacement in self.bracket_patterns:
            result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)
        
        # 10. Factorial
        pattern, replacement = self.factorial_pattern
        result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)
        
        # 11. Basic operators (after complex patterns)
        for pattern, replacement in self.operator_replacements.items():
            result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)
        
        # Clean up extra spaces
        result = re.sub(r'\s+', ' ', result).strip()
        
        return result
    
    def convert_with_preview(self, text: str) -> Dict[str, str]:
        """
        Convert with before/after preview for debugging
        
        Args:
            text: Raw transcribed text
        
        Returns:
            Dict with original and converted text
        """
        converted = self.convert(text)
        
        return {
            "original": text,
            "converted": converted,
            "changed": text.lower() != converted
        }
    
    def detect_math_phrases(self, text: str) -> List[Tuple[str, str]]:
        """
        Detect math phrases in text without converting
        Useful for showing user what will be converted
        
        Args:
            text: Raw text
        
        Returns:
            List of (phrase, notation) tuples
        """
        detected = []
        text_lower = text.lower()
        
        # Check all patterns
        all_patterns = (
            self.power_patterns +
            self.root_patterns +
            self.trig_patterns +
            self.calculus_patterns +
            self.series_patterns +
            self.log_patterns +
            self.fraction_patterns +
            self.bracket_patterns +
            [(self.factorial_pattern[0], self.factorial_pattern[1])]
        )
        
        for pattern, replacement in all_patterns:
            matches = re.finditer(pattern, text_lower, flags=re.IGNORECASE)
            for match in matches:
                phrase = match.group(0)
                notation = re.sub(pattern, replacement, phrase, flags=re.IGNORECASE)
                detected.append((phrase, notation))
        
        return detected


# Singleton instance for easy import
converter = MathSpeechConverter()
