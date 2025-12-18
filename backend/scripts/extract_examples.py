"""
Extract solved examples from PDFs and create markdown files
"""

import re
from pathlib import Path
from typing import List, Dict

try:
    import fitz  # PyMuPDF
    HAS_PYMUPDF = True
except ImportError:
    HAS_PYMUPDF = False
    print("Warning: PyMuPDF not installed. Install with: pip install pymupdf")

def extract_pdf_text(pdf_path: Path) -> str:
    """Extract text from PDF"""
    if not HAS_PYMUPDF:
        return ""
    
    doc = fitz.open(str(pdf_path))
    text = ""
    
    for page in doc:
        blocks = page.get_text("blocks")
        blocks = sorted(blocks, key=lambda b: (b[1], b[0]))
        
        for block in blocks:
            if len(block) >= 5:
                block_text = block[4].strip()
                if block_text:
                    text += block_text + "\n\n"
    
    doc.close()
    return text

def find_examples(text: str) -> List[Dict[str, str]]:
    """
    Find solved examples in text
    Looks for patterns like "Example 1", "EXAMPLE", "Ex.", etc.
    """
    examples = []
    
    # Split text into sections
    lines = text.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Check if this line starts an example
        example_match = re.match(r'(Example|EXAMPLE|Ex\.?|E\s*X\s*A\s*M\s*P\s*L\s*E)\s*[\d\.]+', line, re.IGNORECASE)
        
        if example_match:
            # Found an example, collect content until next example or solution ends
            example_num = line
            content_lines = []
            i += 1
            
            # Collect lines until we hit next example or clear break
            while i < len(lines):
                current = lines[i].strip()
                
                # Stop if we hit another example
                if re.match(r'(Example|EXAMPLE|Ex\.?)\s*[\d\.]+', current, re.IGNORECASE):
                    break
                
                # Stop if we hit chapter markers or similar
                if re.match(r'^(Chapter|\d+\.\d+|EXERCISE|MISCELLANEOUS)', current, re.IGNORECASE):
                    break
                
                # Include this line
                content_lines.append(lines[i])
                i += 1
                
                # Stop after reasonable length (avoid capturing too much)
                if len(content_lines) > 100:
                    break
            
            # Clean and store example
            content = '\n'.join(content_lines).strip()
            
            if len(content) > 50:  # Only keep substantial examples
                examples.append({
                    'title': example_num,
                    'content': content
                })
        else:
            i += 1
    
    return examples

def create_markdown(examples: List[Dict[str, str]], topic: str, source_file: str) -> str:
    """
    Create markdown content from examples
    """
    md_content = f"# {topic.title()} - Solved Examples\n\n"
    md_content += f"*Source: {source_file}*\n\n"
    md_content += "---\n\n"
    
    for idx, example in enumerate(examples, 1):
        md_content += f"## {example['title']}\n\n"
        
        # Split content into problem and solution if possible
        content = example['content']
        
        # Try to identify solution section
        solution_match = re.search(r'(Solution|SOLUTION|Sol\.?|Answer)', content, re.IGNORECASE)
        
        if solution_match:
            problem = content[:solution_match.start()].strip()
            solution = content[solution_match.start():].strip()
            
            if problem:
                md_content += f"**Problem:**\n\n{problem}\n\n"
            
            md_content += f"**{solution}**\n\n"
        else:
            md_content += f"{content}\n\n"
        
        md_content += "---\n\n"
    
    return md_content

def process_pdf(pdf_path: Path, output_dir: Path):
    """
    Process a single PDF and create markdown file
    """
    print(f"\n📄 Processing: {pdf_path.name}")
    
    # Extract text
    print("   Extracting text...")
    text = extract_pdf_text(pdf_path)
    
    if not text:
        print("   ❌ No text extracted")
        return
    
    print(f"   ✅ Extracted {len(text)} characters")
    
    # Find examples
    print("   🔍 Finding examples...")
    examples = find_examples(text)
    
    if not examples:
        print("   ⚠️  No examples found")
        return
    
    print(f"   ✅ Found {len(examples)} examples")
    
    # Create markdown
    topic = pdf_path.parent.name
    md_content = create_markdown(examples, topic, pdf_path.name)
    
    # Save markdown
    output_file = output_dir / f"{pdf_path.stem}_examples.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    print(f"   ✅ Saved to: {output_file.name}")
    print(f"   📊 {len(examples)} examples extracted")

def main():
    """Main function"""
    print("="*80)
    print("PDF to Markdown Examples Converter")
    print("="*80)
    
    if not HAS_PYMUPDF:
        print("\n❌ PyMuPDF is required. Install with: pip install pymupdf")
        return
    
    # Directories
    rag_docs = Path("rag_docs")
    output_dir = Path("rag_docs_markdown")
    output_dir.mkdir(exist_ok=True)
    
    # Find all PDFs
    pdf_files = list(rag_docs.glob("**/*.pdf"))
    
    if not pdf_files:
        print("\n⚠️  No PDF files found in rag_docs/")
        return
    
    print(f"\nFound {len(pdf_files)} PDF(s) to process\n")
    
    # Process each PDF
    for pdf_file in pdf_files:
        try:
            process_pdf(pdf_file, output_dir)
        except Exception as e:
            print(f"   ❌ Error: {e}")
    
    print("\n" + "="*80)
    print("✅ Processing complete!")
    print(f"📁 Markdown files saved to: {output_dir}")
    print("="*80)

if __name__ == "__main__":
    main()
