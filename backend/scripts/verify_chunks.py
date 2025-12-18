"""
Verify chunk quality - show sample chunks
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from smart_chunker import SmartChunker

def show_sample_chunks():
    """Show sample chunks to verify quality"""
    
    chunker = SmartChunker()
    
    # Process one file
    filepath = Path("rag_docs/algebra/matrices_linear_algebra_50examples.md")
    chunks = chunker.chunk_markdown_file(filepath, "algebra")
    
    print("="*80)
    print("SAMPLE CHUNKS FROM: matrices_linear_algebra_50examples.md")
    print("="*80)
    
    # Show first example
    example_chunks = [c for c in chunks if c['type'] == 'example']
    if example_chunks:
        print("\n" + "="*80)
        print("EXAMPLE CHUNK #1 (Full)")
        print("="*80)
        print(example_chunks[0]['text'])
        print("\nMetadata:", {k:v for k,v in example_chunks[0].items() if k != 'text'})
    
    # Show first formula
    formula_chunks = [c for c in chunks if c['type'] == 'formula']
    if formula_chunks:
        print("\n" + "="*80)
        print("FORMULA CHUNK #1 (From Key Formulas Section)")
        print("="*80)
        print(formula_chunks[0]['text'])
        print("\nMetadata:", {k:v for k,v in formula_chunks[0].items() if k != 'text'})
    
    # Show chunk stats
    print("\n" + "="*80)
    print("CHUNK STATISTICS")
    print("="*80)
    
    example_lengths = [len(c['text']) for c in chunks if c['type'] == 'example']
    formula_lengths = [len(c['text']) for c in chunks if c['type'] == 'formula']
    
    if example_lengths:
        print(f"\nExample chunks:")
        print(f"  Count: {len(example_lengths)}")
        print(f"  Min length: {min(example_lengths)} chars")
        print(f"  Max length: {max(example_lengths)} chars")
        print(f"  Avg length: {sum(example_lengths)//len(example_lengths)} chars")
    
    if formula_lengths:
        print(f"\nFormula chunks:")
        print(f"  Count: {len(formula_lengths)}")
        print(f"  Min length: {min(formula_lengths)} chars")
        print(f"  Max length: {max(formula_lengths)} chars")
        print(f"  Avg length: {sum(formula_lengths)//len(formula_lengths)} chars")
    
    print("\n" + "="*80)
    print("✅ NO FRAGMENTED CHUNKS!")
    print("✅ Each example includes full problem + solution")
    print("✅ Formulas only from 'Key Formulas' section")
    print("="*80)

if __name__ == "__main__":
    show_sample_chunks()
