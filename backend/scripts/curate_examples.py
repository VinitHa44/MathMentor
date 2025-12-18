"""
Curate and clean extracted examples to create high-quality markdown files
"""

import re
from pathlib import Path

def clean_math_notation(text: str) -> str:
    """Clean up mathematical notation"""
    # Add spaces around operators
    text = re.sub(r'([a-zA-Z0-9)])\s*([=<>≤≥≠±+\-×÷])\s*([a-zA-Z0-9(])', r'\1 \2 \3', text)
    
    # Fix fractions
    text = re.sub(r'(\d+)\s*/\s*(\d+)', r'\1/\2', text)
    
    # Clean up excessive whitespace
    text = re.sub(r' +', ' ', text)
    text = re.sub(r'\n\n\n+', '\n\n', text)
    
    return text

def curate_markdown_file(input_file: Path, output_file: Path, max_examples: int = 10):
    """
    Curate markdown file - select best examples and clean format
    """
    print(f"\n📝 Curating: {input_file.name}")
    
    # Read original file
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split into sections
    sections = content.split('---')
    
    # Header
    header = sections[0] if sections else ""
    
    # Examples
    examples = sections[1:] if len(sections) > 1 else []
    
    # Filter and clean examples
    curated_examples = []
    
    for i, example in enumerate(examples[:max_examples]):
        # Clean up the example text
        example = clean_math_notation(example)
        
        # Skip if too short or empty
        if len(example.strip()) < 100:
            continue
        
        # Skip if it's mostly table data (lots of consecutive pipes or numbers)
        if example.count('|') > 20 or re.search(r'\d+\s+\d+\s+\d+\s+\d+', example):
            continue
        
        curated_examples.append(example)
    
    # Rebuild markdown
    new_content = header + "\n"
    
    for i, example in enumerate(curated_examples, 1):
        new_content += f"\n---\n{example}\n"
    
    # Save curated version
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"   ✅ Saved {len(curated_examples)} curated examples to: {output_file.name}")

def main():
    """Main function"""
    print("="*80)
    print("Markdown Examples Curator")
    print("="*80)
    
    # Directories
    input_dir = Path("rag_docs_markdown")
    output_dir = Path("rag_docs")
    
    if not input_dir.exists():
        print(f"\n❌ Directory not found: {input_dir}")
        return
    
    # Process each markdown file
    md_files = list(input_dir.glob("*.md"))
    
    if not md_files:
        print(f"\n⚠️  No markdown files found in {input_dir}")
        return
    
    print(f"\nFound {len(md_files)} markdown file(s)\n")
    
    for md_file in md_files:
        # Create output in respective topic folders
        if 'linear_algebra' in md_file.name:
            topic_dir = output_dir / 'algebra'
        elif 'prob' in md_file.name.lower():
            topic_dir = output_dir / 'probability'
        elif 'stat' in md_file.name.lower():
            topic_dir = output_dir / 'probability'
        elif 'calculus' in md_file.name or 'limit' in md_file.name or 'deriv' in md_file.name:
            topic_dir = output_dir / 'calculus'
        else:
            topic_dir = output_dir
        
        topic_dir.mkdir(parents=True, exist_ok=True)
        
        output_file = topic_dir / md_file.name
        
        try:
            curate_markdown_file(md_file, output_file, max_examples=10)
        except Exception as e:
            print(f"   ❌ Error: {e}")
    
    print("\n" + "="*80)
    print("✅ Curation complete!")
    print(f"📁 Curated markdown files saved to rag_docs/*/")
    print("="*80)

if __name__ == "__main__":
    main()
