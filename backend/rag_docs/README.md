# Place your math PDFs here in organized folders

## Folder Structure

```
rag_docs/
├── algebra/
│   ├── formulas.pdf
│   ├── examples.pdf
│
├── calculus/
│   ├── limits.pdf
│   ├── derivatives.pdf
│
├── probability/
│   ├── basics.pdf
│   ├── conditional.pdf
│
├── linear_algebra/
│   ├── matrices.pdf
│   ├── vectors.pdf
```

## Adding Documents

1. Download or create PDFs with:
   - Math formulas & identities
   - Solved examples
   - Common mistakes
   - Solution templates

2. Organize by topic (algebra, calculus, probability, linear_algebra)

3. Name files descriptively (e.g., `quadratic_formulas.pdf`)

4. Run the RAG indexing script to process all PDFs

## Sample Content to Include

- NCERT formulas
- JEE solved examples
- Common mistake patterns
- Step-by-step solution templates
- Domain constraints (e.g., x > 0 for √x)

## Free Resources

- Khan Academy content (save as PDF)
- OpenStax textbooks
- NCERT PDFs (freely available)
- Your own notes/formulas

## Processing

After adding PDFs, restart the backend or call:
```python
rag_service.process_pdf_directory(force_rebuild=True)
```
