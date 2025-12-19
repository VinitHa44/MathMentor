"""
Quick reference data for math speech conversions
Used in UI tooltips and help sections
"""

COMMON_MATH_PHRASES = {
    "Powers & Exponents": [
        ("2 raised to 3", "2³ or 2^3"),
        ("x squared", "x²"),
        ("x cubed", "x³"),
        ("x to the power of n", "x^n"),
        ("x upto 5", "x^5"),
    ],
    
    "Roots": [
        ("square root of 16", "√16"),
        ("cube root of 27", "∛27"),
    ],
    
    "Trigonometry": [
        ("sine of theta", "sin(θ)"),
        ("cosine of x", "cos(x)"),
        ("tangent of 45", "tan(45)"),
        ("arc sine of x", "arcsin(x)"),
    ],
    
    "Calculus": [
        ("derivative of x cubed", "d/dx(x³)"),
        ("integral of x squared", "∫(x²)"),
        ("limit as x approaches 0", "lim[x→0]"),
    ],
    
    "Operators": [
        ("equals to", "="),
        ("plus", "+"),
        ("minus", "-"),
        ("times", "×"),
        ("divided by", "÷"),
    ],
    
    "Greek Letters": [
        ("pi", "π"),
        ("theta", "θ"),
        ("alpha", "α"),
        ("beta", "β"),
        ("gamma", "γ"),
        ("delta", "Δ"),
    ],
}

TIPS_FOR_SPEAKING_MATH = [
    "Speak clearly and at a moderate pace",
    "Say 'raised to' or 'to the power' for exponents",
    "Use 'squared' and 'cubed' for common powers",
    "Say 'equals to' or 'equal to' instead of just 'is'",
    "Pronounce Greek letters by name (theta, alpha, etc.)",
    "Say 'derivative of' or 'integral of' explicitly",
    "Use 'with respect to x' for partial derivatives",
    "Say 'open bracket' and 'close bracket' for grouping",
]

EXAMPLE_PROBLEMS = [
    {
        "spoken": "if 3x equals 6x minus 15 then x plus 8 equals what",
        "notation": "If 3x = 6x - 15, then x + 8 = ?",
        "topic": "Algebra"
    },
    {
        "spoken": "solve x squared plus 5x minus 3 equals 0",
        "notation": "Solve x² + 5x - 3 = 0",
        "topic": "Algebra"
    },
    {
        "spoken": "find derivative of x cubed with respect to x",
        "notation": "Find d/dx(x³)",
        "topic": "Calculus"
    },
    {
        "spoken": "sine of theta squared plus cosine of theta squared equals 1",
        "notation": "sin²(θ) + cos²(θ) = 1",
        "topic": "Trigonometry"
    },
    {
        "spoken": "integral from 0 to 1 of x squared",
        "notation": "∫[0 to 1](x²)",
        "topic": "Calculus"
    },
]
