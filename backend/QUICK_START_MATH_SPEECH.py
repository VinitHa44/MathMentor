"""
Quick Start Guide for Math Speech Converter
============================================

## 🎤 How to Speak Math Problems

### Powers & Exponents
✓ Say: "x raised to 3"        → Gets: x^3
✓ Say: "x squared"             → Gets: x²
✓ Say: "2 to the power 5"      → Gets: 2^5
✓ Say: "x upto n"              → Gets: x^n

### Basic Operations
✓ Say: "x plus 5"              → Gets: x + 5
✓ Say: "y minus 3"             → Gets: y - 3
✓ Say: "2 times 3"             → Gets: 2 × 3
✓ Say: "10 divided by 2"       → Gets: 10 ÷ 2
✓ Say: "equals to"             → Gets: =

### Trigonometry
✓ Say: "sine of theta"         → Gets: sin(θ)
✓ Say: "cosine of x"           → Gets: cos(x)
✓ Say: "tangent of 45"         → Gets: tan(45)

### Calculus
✓ Say: "derivative of x cubed" → Gets: d/dx(x³)
✓ Say: "integral of x squared" → Gets: ∫(x²)
✓ Say: "limit as x approaches 0" → Gets: lim[x→0]

### Greek Letters
✓ Say: "pi"                    → Gets: π
✓ Say: "theta"                 → Gets: θ
✓ Say: "alpha"                 → Gets: α

### Roots
✓ Say: "square root of 16"     → Gets: √(16)
✓ Say: "cube root of 27"       → Gets: ∛(27)

## 📝 Complete Examples

### Example 1: Quadratic Equation
🎤 Say: "solve x squared plus 5x minus 3 equals 0"
📝 Get: "solve x² + 5x - 3 = 0"

### Example 2: Calculus Problem
🎤 Say: "find derivative of x cubed with respect to x"
📝 Get: "find d/dx(x³) with respect to x"

### Example 3: Trigonometry
🎤 Say: "if sine of theta equals 0.5 find theta"
📝 Get: "if sin(θ) = 0.5 find θ"

### Example 4: Complex Expression
🎤 Say: "2 raised to 3 plus square root of 16 equals 12"
📝 Get: "2^3 + √(16) = 12"

## 💡 Pro Tips

1. **Speak Clearly**: Enunciate mathematical terms clearly
2. **Natural Pace**: Don't speak too fast or too slow
3. **Use Full Phrases**: Say "raised to" not just "to"
4. **Say "Equals To"**: Don't just say "is", say "equals to"
5. **Greek by Name**: Say "theta" not "that symbol"
6. **Pause Between Terms**: Brief pause after each term helps

## ⚠️ Common Mistakes

❌ Don't say: "x is 5"
✅ Do say: "x equals to 5"

❌ Don't say: "x power 3"
✅ Do say: "x raised to 3" or "x to the power 3"

❌ Don't say: "root of 16"
✅ Do say: "square root of 16"

❌ Don't say: "log x"
✅ Do say: "log of x" or "natural log of x"

## 🎯 Testing Your Speech

Try the demo script:
```bash
cd backend
python scripts/demo_math_speech.py
```

This will show you:
- How your speech gets converted
- Interactive mode to test phrases
- Examples of common conversions

## 🔧 Need Help?

Check the full documentation:
- backend/utils/README_MATH_SPEECH.md (comprehensive guide)
- MATH_SPEECH_IMPLEMENTATION.md (implementation details)

## 🎓 JEE-Style Practice Problems

### Algebra
🎤 "if 3x equals 6x minus 15 then x plus 8 equals what"
📝 "if 3x = 6x - 15 then x + 8 = what"

### Calculus
🎤 "find derivative of 2x squared plus 3x minus 5"
📝 "find d/dx(2x²) 3x - 5"

### Trigonometry
🎤 "sine of theta squared plus cosine of theta squared equals 1"
📝 "sin(θ)² + cos(θ)² = 1"

### Probability
🎤 "find probability that x equals 3"
📝 "find probability that x = 3"

## ⚡ Quick Reference Table

| Category | Say This | Get This |
|----------|----------|----------|
| Power | "x raised to 3" | x^3 |
| Square | "x squared" | x² |
| Cube | "x cubed" | x³ |
| Root | "square root of x" | √x |
| Sin | "sine of theta" | sin(θ) |
| Cos | "cosine of x" | cos(x) |
| Derivative | "derivative of x" | d/dx(x) |
| Integral | "integral of x" | ∫(x) |
| Equals | "equals to" | = |
| Plus | "plus" | + |
| Minus | "minus" | - |
| Times | "times" | × |
| Divided | "divided by" | ÷ |
| Pi | "pi" | π |
| Theta | "theta" | θ |

## 🚀 Start Speaking Math Now!

Just speak naturally using the phrases above, and the system will automatically convert your speech to proper mathematical notation!
"""

if __name__ == "__main__":
    print(__doc__)
