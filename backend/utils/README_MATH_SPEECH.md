# Math Speech Converter

A comprehensive utility for converting spoken mathematical expressions into proper mathematical notation.

## 🎯 Problem Statement

When students speak math problems to an AI tutor, they use natural language that doesn't match written notation:

| What Users Say | What We Need |
|---------------|--------------|
| "2 raised to 3" | `2^3` |
| "x squared" | `x²` |
| "sine of theta" | `sin(θ)` |
| "derivative of x cubed" | `d/dx(x³)` |
| "square root of 16" | `√16` |

ASR systems like Whisper transcribe the **spoken words**, not the mathematical notation. This converter bridges that gap.

## 🚀 Features

### Supported Conversions

#### Powers & Exponents
- "x raised to 3" → `x^3`
- "x to the power of 5" → `x^5`
- "x upto 2" → `x^2`
- "x squared" → `x²`
- "x cubed" → `x³`

#### Roots
- "square root of 16" → `√(16)`
- "cube root of 27" → `∛(27)`

#### Trigonometry
- "sine of theta" → `sin(θ)`
- "cosine of x" → `cos(x)`
- "tangent of 45" → `tan(45)`
- "secant of x" → `sec(x)`
- "arc sine of x" → `arcsin(x)`

#### Calculus
- "derivative of x cubed" → `d/dx(x³)`
- "derivative of y with respect to x" → `dy/dx`
- "integral of x squared" → `∫(x²)`
- "limit as x approaches 0 of sin x" → `lim[x→0](sin x)`
- "partial derivative of f with respect to x" → `∂f/∂x`

#### Series & Summations
- "summation from i equals 1 to n of x" → `Σ[i=1 to n](x)`
- "product from i equals 1 to n of x" → `Π[i=1 to n](x)`

#### Logarithms
- "log base 2 of 8" → `log_2(8)`
- "natural log of x" → `ln(x)`
- "log of x" → `log(x)`

#### Basic Operators
- "equals to" / "equal to" → `=`
- "plus" → `+`
- "minus" → `-`
- "times" / "multiplied by" → `×`
- "divided by" → `÷`
- "greater than" → `>`
- "less than" → `<`

#### Greek Letters
- "pi" → `π`
- "theta" → `θ`
- "alpha" → `α`
- "beta" → `β`
- "gamma" → `γ`
- "delta" → `Δ`
- "infinity" → `∞`

#### Other
- "x factorial" → `x!`
- "absolute value of x" → `|x|`
- "x over y" → `(x/y)`

## 📖 Usage

### Basic Usage

```python
from utils.math_speech_converter import MathSpeechConverter

converter = MathSpeechConverter()

# Simple conversion
result = converter.convert("x squared plus 5x minus 3 equals 0")
print(result)  # Output: "x² + 5x - 3 = 0"

# With preview (shows before/after)
preview = converter.convert_with_preview("2 raised to 3 equals 8")
print(preview["original"])    # "2 raised to 3 equals 8"
print(preview["converted"])   # "2^3 = 8"
print(preview["changed"])     # True

# Detect math phrases
phrases = converter.detect_math_phrases("x squared plus sine of theta")
for phrase, notation in phrases:
    print(f"{phrase} → {notation}")
```

### Integration with ASR Service

The converter is automatically integrated into the ASR service:

```python
from services.asr_service import ASRService

asr = ASRService()
result = asr.transcribe_audio(audio_bytes)

print(result["text"])                    # Converted notation
print(result["original_transcript"])     # Original speech
print(result["math_notation_applied"])   # True if conversion occurred
```

### Demo Script

Run the interactive demo:

```bash
cd backend
python scripts/demo_math_speech.py
```

## 🧪 Testing

Run the comprehensive test suite:

```bash
cd backend
pytest tests/test_math_speech_converter.py -v
```

Test coverage includes:
- Basic operators
- Powers and exponents  
- Roots
- Trigonometry
- Calculus notation
- Greek letters
- Complex expressions
- Edge cases

## 🎓 Real-World Examples

### JEE-Style Problems

**Algebra:**
```
Input:  "if 3x equals 6x minus 15 then x plus 8 equals what"
Output: "if 3x = 6x - 15 then x + 8 = what"
```

**Calculus:**
```
Input:  "find derivative of x cubed plus 2x with respect to x"
Output: "find dx³/dx + 2x with respect to x"
```

**Trigonometry:**
```
Input:  "sine of theta squared plus cosine of theta squared equals 1"
Output: "sin(θ)² + cos(θ)² = 1"
```

**Probability:**
```
Input:  "find probability of x equals 2"
Output: "find probability of x = 2"
```

## 🏗️ Architecture

### Pattern Matching Strategy

The converter uses ordered regex patterns to handle complex cases first:

1. **Calculus** (most specific) - derivatives, integrals, limits
2. **Series** - summations, products
3. **Logarithms** - log, ln, log base n
4. **Trigonometry** - sin, cos, tan, etc.
5. **Roots** - square root, cube root
6. **Powers** - raised to, squared, cubed
7. **Fractions** - x over y
8. **Brackets** - absolute value, parentheses
9. **Factorial**
10. **Operators** - equals, plus, minus, etc.
11. **Symbols** - Greek letters, infinity

This ordering prevents conflicts (e.g., "square root" is matched before "squared").

### Design Decisions

**Why regex over LLM?**
- Deterministic and fast
- No API calls or model loading
- Consistent results
- Easy to test and debug
- Can fallback to LLM if needed in parser agent

**Case Insensitivity:**
All patterns are case-insensitive to handle various speech recognition outputs.

**Greedy vs. Non-Greedy:**
Patterns use non-greedy matching with lookahead to avoid over-matching.

## 🔧 Configuration

### Adding New Patterns

To add new math phrase conversions, edit `math_speech_converter.py`:

```python
# Add to appropriate pattern list in __init__
self.trig_patterns.append(
    (r'\bhyperbolic\s+sine\s+of\s+(\w+)', r'sinh(\1)')
)
```

### Pattern Priority

Longer, more specific phrases should be checked before shorter ones:

```python
# ✅ Correct order
(r'\b(\w+)\s+raised\s+to\s+the\s+power\s+of\s+(\w+)', r'\1^\2'),
(r'\b(\w+)\s+raised\s+to\s+(\w+)', r'\1^\2'),

# ❌ Wrong order (second pattern would never match)
(r'\b(\w+)\s+raised\s+to\s+(\w+)', r'\1^\2'),
(r'\b(\w+)\s+raised\s+to\s+the\s+power\s+of\s+(\w+)', r'\1^\2'),
```

## 🚦 Limitations

1. **Context-Free:** Doesn't understand mathematical context
2. **Ambiguity:** "log" could be base 10 or natural log
3. **Complex Nested Expressions:** May struggle with deeply nested phrases
4. **Language:** English only
5. **Accents:** Works on transcription, so ASR quality matters

## 🔮 Future Enhancements

- [ ] Multi-language support
- [ ] Context-aware conversions (using LLM)
- [ ] LaTeX output mode
- [ ] MathML output mode
- [ ] Confidence scores per conversion
- [ ] Spell-checking for math terms
- [ ] Abbreviation expansion (e.g., "int" → "integral")

## 📚 Resources

- [OpenAI Whisper](https://github.com/openai/whisper) - ASR system
- [Unicode Math Symbols](https://en.wikipedia.org/wiki/Mathematical_operators_and_symbols_in_Unicode)
- [LaTeX Math Symbols](https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols)

## 🤝 Contributing

When adding new patterns:
1. Add to appropriate pattern list
2. Add tests in `test_math_speech_converter.py`
3. Add examples to this README
4. Consider pattern ordering/conflicts

## 📄 License

Part of the Math Mentor project.
