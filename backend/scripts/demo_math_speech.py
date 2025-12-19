"""
Demo script for Math Speech Converter
Shows conversion examples from spoken math to notation
"""

from utils.math_speech_converter import MathSpeechConverter


def print_conversion(converter, spoken_text):
    """Print before/after conversion"""
    result = converter.convert_with_preview(spoken_text)
    print(f"\n{'='*70}")
    print(f"🎤 SPOKEN: {result['original']}")
    print(f"📝 NOTATION: {result['converted']}")
    if result['changed']:
        print(f"✅ Conversion applied")
    else:
        print(f"ℹ️  No math notation detected")
    print(f"{'='*70}")


def main():
    """Run demonstration"""
    converter = MathSpeechConverter()
    
    print("\n" + "="*70)
    print("🧮 MATH SPEECH CONVERTER DEMONSTRATION")
    print("="*70)
    print("\nConverting spoken math to mathematical notation...")
    
    # Examples from the requirements
    examples = [
        # Basic powers
        "2 raised to 3",
        "2 to the power 3",
        "2 upto 3",
        "x squared",
        "x cubed",
        
        # Trigonometry
        "sine of theta",
        "cosine of x",
        "tangent of 45",
        
        # Calculus
        "derivative of x cubed",
        "integral of x squared",
        "limit as x approaches 0 of sine x",
        
        # Complex expressions
        "2 raised to 3 equals 8",
        "x squared plus 5x minus 3 equals 0",
        "square root of 16 equals 4",
        
        # JEE-style problems
        "if 3x equals 6x minus 15 then x plus 8 equals what",
        "find derivative of x cubed plus 2x with respect to x",
        "sine of theta squared plus cosine of theta squared equals 1",
        
        # Edge cases
        "2 times 3 plus 4 divided by 2",
        "x raised to the power of n minus 1",
        "absolute value of x minus 5 equals 3",
    ]
    
    for example in examples:
        print_conversion(converter, example)
    
    # Show phrase detection
    print("\n" + "="*70)
    print("🔍 MATH PHRASE DETECTION")
    print("="*70)
    
    test_text = "x squared plus sine of theta equals 5"
    phrases = converter.detect_math_phrases(test_text)
    
    print(f"\n📝 Input: {test_text}")
    print(f"\n🎯 Detected Math Phrases:")
    for phrase, notation in phrases:
        print(f"   • '{phrase}' → '{notation}'")
    
    # Interactive mode
    print("\n" + "="*70)
    print("🎮 INTERACTIVE MODE")
    print("="*70)
    print("\nTry your own spoken math expressions!")
    print("(Type 'quit' to exit)\n")
    
    while True:
        try:
            user_input = input("🎤 Speak math > ")
            if user_input.lower() in ['quit', 'exit', 'q']:
                break
            
            result = converter.convert(user_input)
            print(f"📝 Notation > {result}\n")
            
        except KeyboardInterrupt:
            break
    
    print("\n👋 Thanks for using Math Speech Converter!")


if __name__ == "__main__":
    main()
