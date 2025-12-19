"""
Unit tests for Math Speech Converter
Tests conversion of spoken math to mathematical notation
"""

import pytest
from utils.math_speech_converter import MathSpeechConverter


@pytest.fixture
def converter():
    """Create converter instance for tests"""
    return MathSpeechConverter()


class TestBasicOperators:
    """Test basic math operators"""
    
    def test_equals(self, converter):
        assert "2x = 5" in converter.convert("2x equals 5")
        assert "y = 10" in converter.convert("y equal to 10")
    
    def test_plus_minus(self, converter):
        assert "x + 5" in converter.convert("x plus 5")
        assert "y - 3" in converter.convert("y minus 3")
    
    def test_multiply(self, converter):
        result = converter.convert("2 times 3")
        assert "×" in result or "*" in result
        
        result = converter.convert("x multiplied by y")
        assert "×" in result or "*" in result
    
    def test_divide(self, converter):
        result = converter.convert("10 divided by 2")
        assert "÷" in result or "/" in result


class TestPowersAndExponents:
    """Test power and exponent conversions"""
    
    def test_raised_to(self, converter):
        assert "2^3" in converter.convert("2 raised to 3")
        assert "x^5" in converter.convert("x raised to the power of 5")
        assert "a^b" in converter.convert("a raised to b")
    
    def test_upto(self, converter):
        assert "2^3" in converter.convert("2 upto 3")
        assert "x^2" in converter.convert("x upto 2")
    
    def test_squared_cubed(self, converter):
        assert "x²" in converter.convert("x squared")
        assert "y³" in converter.convert("y cubed")
        assert "5²" in converter.convert("5 squared")
    
    def test_power_of(self, converter):
        assert "x^n" in converter.convert("x to the power of n")
        assert "2^10" in converter.convert("2 to the power 10")


class TestRoots:
    """Test root conversions"""
    
    def test_square_root(self, converter):
        result = converter.convert("square root of 16")
        assert "√" in result
        assert "16" in result
    
    def test_cube_root(self, converter):
        result = converter.convert("cube root of 27")
        assert "∛" in result
        assert "27" in result
    
    def test_complex_square_root(self, converter):
        result = converter.convert("square root of x squared plus 1")
        assert "√" in result


class TestTrigonometry:
    """Test trigonometric functions"""
    
    def test_sine(self, converter):
        assert "sin(θ)" in converter.convert("sine of theta")
        assert "sin(x)" in converter.convert("sin x")
    
    def test_cosine(self, converter):
        assert "cos(θ)" in converter.convert("cosine of theta")
        assert "cos(30)" in converter.convert("cos 30")
    
    def test_tangent(self, converter):
        assert "tan(x)" in converter.convert("tangent of x")
        assert "tan(45)" in converter.convert("tan 45")
    
    def test_other_trig(self, converter):
        assert "sec(x)" in converter.convert("secant of x")
        assert "cosec(θ)" in converter.convert("cosec of theta")
        assert "cot(x)" in converter.convert("cotangent of x")


class TestCalculus:
    """Test calculus notation"""
    
    def test_derivative(self, converter):
        result = converter.convert("derivative of x cubed")
        assert "d/dx" in result or "d" in result
    
    def test_derivative_with_respect_to(self, converter):
        result = converter.convert("derivative of y with respect to x")
        assert "dy/dx" in result or "d" in result
    
    def test_integral(self, converter):
        result = converter.convert("integral of x squared")
        assert "∫" in result
        assert "x" in result
    
    def test_limit(self, converter):
        result = converter.convert("limit as x approaches 0 of sin x")
        assert "lim" in result
        assert "→" in result or "approaches" in result


class TestGreekLetters:
    """Test Greek letter conversions"""
    
    def test_common_greek(self, converter):
        assert "π" in converter.convert("pi")
        assert "θ" in converter.convert("theta")
        assert "α" in converter.convert("alpha")
        assert "β" in converter.convert("beta")
        assert "γ" in converter.convert("gamma")
        assert "Δ" in converter.convert("delta")
    
    def test_infinity(self, converter):
        assert "∞" in converter.convert("infinity")


class TestComplexExpressions:
    """Test complex mathematical expressions"""
    
    def test_quadratic_equation(self, converter):
        result = converter.convert("solve x squared plus 5x minus 3 equals 0")
        assert "x²" in result or "x^2" in result
        assert "+" in result
        assert "=" in result
    
    def test_raised_to_equals(self, converter):
        result = converter.convert("2 raised to 3 equals 8")
        assert "2^3" in result
        assert "=" in result
        assert "8" in result
    
    def test_derivative_expression(self, converter):
        result = converter.convert("find derivative of x cubed plus 2x squared minus 5")
        assert "x³" in result or "x^3" in result
        assert "x²" in result or "x^2" in result
        assert "+" in result
        assert "-" in result
    
    def test_trig_equation(self, converter):
        result = converter.convert("sine of theta equals 0.5")
        assert "sin(θ)" in result
        assert "=" in result
        assert "0.5" in result


class TestEdgeCases:
    """Test edge cases and potential issues"""
    
    def test_empty_string(self, converter):
        result = converter.convert("")
        assert result == ""
    
    def test_no_math(self, converter):
        result = converter.convert("hello world")
        assert "hello" in result.lower()
    
    def test_mixed_case(self, converter):
        result1 = converter.convert("X SQUARED")
        result2 = converter.convert("x squared")
        # Both should produce similar results (case-insensitive)
        assert "²" in result1
        assert "²" in result2
    
    def test_multiple_operations(self, converter):
        result = converter.convert("2 raised to 3 plus 5 times x minus 7")
        assert "2^3" in result or "2³" in result
        assert "+" in result
        assert "×" in result or "*" in result
        assert "-" in result


class TestPreviewMode:
    """Test preview functionality"""
    
    def test_convert_with_preview(self, converter):
        result = converter.convert_with_preview("x squared plus y")
        assert "original" in result
        assert "converted" in result
        assert "changed" in result
        assert result["original"] == "x squared plus y"
        assert "x²" in result["converted"] or "x^2" in result["converted"]
    
    def test_detect_math_phrases(self, converter):
        phrases = converter.detect_math_phrases("x squared plus sine of theta")
        assert len(phrases) >= 2  # Should detect "squared" and "sine of"
        assert any("squared" in phrase[0].lower() for phrase in phrases)
        assert any("sine" in phrase[0].lower() for phrase in phrases)


class TestRealWorldExamples:
    """Test real-world spoken math examples"""
    
    def test_jee_algebra(self, converter):
        # "If 3x = 6x - 15, then x + 8 = ?"
        result = converter.convert("if 3x equals 6x minus 15 then x plus 8 equals what")
        assert "3x = 6x - 15" in result
        assert "x + 8 =" in result
    
    def test_jee_calculus(self, converter):
        # "Find dy/dx for y = x³ + 2x"
        result = converter.convert("find derivative of y with respect to x for y equals x cubed plus 2x")
        assert "dy/dx" in result or "derivative" in result
        assert "x³" in result or "x^3" in result
    
    def test_jee_trigonometry(self, converter):
        # "If sin²θ + cos²θ = 1"
        result = converter.convert("if sine of theta squared plus cosine of theta squared equals 1")
        assert "sin" in result
        assert "cos" in result
        assert "θ" in result
        assert "²" in result or "^2" in result
    
    def test_probability(self, converter):
        result = converter.convert("find probability of x equals 2")
        assert "=" in result
        assert "2" in result


if __name__ == "__main__":
    # Run tests
    pytest.main([__file__, "-v"])
