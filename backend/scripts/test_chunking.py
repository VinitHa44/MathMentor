"""
Test script for smart chunking implementation
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Direct import to avoid __init__ issues
from smart_chunker import SmartChunker

def test_chunker():
    """Test smart chunker on existing markdown files"""
    
    print("="*60)
    print("Testing Smart Chunker")
    print("="*60)
    print()
    
    chunker = SmartChunker()
    
    # Test files
    test_files = [
        ("algebra", "quadratic_equations_examples.md"),
        ("probability", "probability_examples.md"),
        ("calculus", "limits_derivatives_examples.md"),
        ("algebra", "matrices_linear_algebra_50examples.md"),
    ]
    
    total_chunks = 0
    
    for topic, filename in test_files:
        filepath = Path("rag_docs") / topic / filename
        
        if not filepath.exists():
            print(f"❌ File not found: {filepath}")
            continue
        
        print(f"\n{'='*60}")
        print(f"Processing: {filepath}")
        print(f"{'='*60}")
        
        # Chunk the file
        chunks = chunker.chunk_markdown_file(filepath, topic)
        
        print(f"Total chunks: {len(chunks)}")
        
        # Count by type
        by_type = {}
        for chunk in chunks:
            chunk_type = chunk['type']
            by_type[chunk_type] = by_type.get(chunk_type, 0) + 1
        
        print(f"\nBreakdown by type:")
        for chunk_type, count in sorted(by_type.items()):
            print(f"  {chunk_type}: {count}")
        
        # Show sample chunks
        print(f"\nSample chunks:")
        for chunk_type in ['formula', 'example', 'definition']:
            samples = [c for c in chunks if c['type'] == chunk_type]
            if samples:
                sample = samples[0]
                print(f"\n  [{chunk_type.upper()}]")
                print(f"  Text preview: {sample['text'][:150]}...")
                print(f"  Subtopic: {sample.get('subtopic', 'N/A')}")
                if 'pattern' in sample:
                    print(f"  Pattern: {sample['pattern']}")
        
        total_chunks += len(chunks)
    
    print(f"\n{'='*60}")
    print(f"TOTAL CHUNKS: {total_chunks}")
    print(f"{'='*60}")
    
    # Get overall statistics
    print("\nOverall Statistics:")
    all_chunks = []
    for topic, filename in test_files:
        filepath = Path("rag_docs") / topic / filename
        if filepath.exists():
            chunks = chunker.chunk_markdown_file(filepath, topic)
            all_chunks.extend(chunks)
    
    stats = chunker.get_chunk_stats(all_chunks)
    
    print(f"Total chunks: {stats['total']}")
    print(f"Average length: {stats['avg_length']} characters")
    print(f"\nBy type:")
    for chunk_type, count in stats['by_type'].items():
        percentage = (count / stats['total'] * 100) if stats['total'] > 0 else 0
        print(f"  {chunk_type}: {count} ({percentage:.1f}%)")
    print(f"\nBy topic:")
    for topic, count in stats['by_topic'].items():
        percentage = (count / stats['total'] * 100) if stats['total'] > 0 else 0
        print(f"  {topic}: {count} ({percentage:.1f}%)")

if __name__ == "__main__":
    test_chunker()
