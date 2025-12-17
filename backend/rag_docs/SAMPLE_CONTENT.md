# Sample Math PDFs for RAG Knowledge Base

## Algebra

### Quadratic Formulas
```
Standard Form: ax² + bx + c = 0

Quadratic Formula:
x = (-b ± √(b² - 4ac)) / 2a

Discriminant (Δ):
Δ = b² - 4ac

If Δ > 0: Two distinct real roots
If Δ = 0: One repeated real root
If Δ < 0: Two complex roots

Factoring Form:
ax² + bx + c = a(x - x₁)(x - x₂)

Example:
x² + 5x + 6 = 0
a = 1, b = 5, c = 6
Δ = 25 - 24 = 1
x = (-5 ± 1) / 2
x = -2 or x = -3

Verification:
(-2)² + 5(-2) + 6 = 4 - 10 + 6 = 0 ✓
(-3)² + 5(-3) + 6 = 9 - 15 + 6 = 0 ✓

Common Mistakes:
1. Forgetting the ± sign
2. Wrong sign for -b
3. Not checking discriminant first
4. Calculation errors with negatives
```

Save this as: `rag_docs/algebra/quadratic_formulas.txt` (then convert to PDF)

### Linear Equations
```
Standard Form: ax + b = 0

Solution:
x = -b / a

System of Linear Equations:
ax + by = c
dx + ey = f

Elimination Method:
1. Multiply equations to match coefficients
2. Add or subtract to eliminate one variable
3. Solve for remaining variable
4. Substitute back

Substitution Method:
1. Solve one equation for one variable
2. Substitute into other equation
3. Solve for remaining variable
4. Substitute back

Example:
2x + 3y = 8
x - y = 1

From second: x = y + 1
Substitute: 2(y + 1) + 3y = 8
2y + 2 + 3y = 8
5y = 6
y = 6/5
x = 1 + 6/5 = 11/5

Common Mistakes:
1. Sign errors when subtracting equations
2. Not simplifying before elimination
3. Forgetting to substitute back
```

## Calculus

### Derivatives Rules
```
Basic Rules:

Power Rule:
d/dx[xⁿ] = nxⁿ⁻¹

Constant Rule:
d/dx[c] = 0

Sum Rule:
d/dx[f(x) + g(x)] = f'(x) + g'(x)

Product Rule:
d/dx[f(x)g(x)] = f'(x)g(x) + f(x)g'(x)

Quotient Rule:
d/dx[f(x)/g(x)] = [f'(x)g(x) - f(x)g'(x)] / [g(x)]²

Chain Rule:
d/dx[f(g(x))] = f'(g(x))·g'(x)

Common Functions:
d/dx[sin x] = cos x
d/dx[cos x] = -sin x
d/dx[eˣ] = eˣ
d/dx[ln x] = 1/x

Example:
f(x) = x² sin x

Using product rule:
f'(x) = 2x·sin x + x²·cos x

Domain Constraints:
- For ln x: x > 0
- For √x: x ≥ 0
- For 1/x: x ≠ 0

Common Mistakes:
1. Forgetting chain rule for composite functions
2. Sign errors in quotient rule
3. Not simplifying before differentiating
```

## Probability

### Basic Probability
```
Definitions:

Probability of Event A:
P(A) = (Number of favorable outcomes) / (Total number of outcomes)

Range: 0 ≤ P(A) ≤ 1

Complement:
P(A') = 1 - P(A)

Addition Rule (Mutually Exclusive):
P(A or B) = P(A) + P(B)

Addition Rule (General):
P(A or B) = P(A) + P(B) - P(A and B)

Multiplication Rule (Independent):
P(A and B) = P(A) × P(B)

Conditional Probability:
P(A|B) = P(A and B) / P(B)

Bayes' Theorem:
P(A|B) = [P(B|A) × P(A)] / P(B)

Example:
Two dice rolled. Find P(sum = 7)
Favorable outcomes: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) = 6
Total outcomes: 6 × 6 = 36
P(sum = 7) = 6/36 = 1/6

Common Mistakes:
1. Adding probabilities when events not mutually exclusive
2. Multiplying when events not independent
3. Forgetting to check conditions
```

## How to Create PDFs

### Method 1: Text to PDF (Simple)
1. Copy content above into a `.txt` file
2. Open in any editor
3. Print to PDF (Save as PDF)

### Method 2: LaTeX (Professional)
```latex
\documentclass{article}
\usepackage{amsmath}
\begin{document}

\section{Quadratic Formulas}
Standard Form: $ax^2 + bx + c = 0$

Quadratic Formula:
$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

\end{document}
```

Compile: `pdflatex formulas.tex`

### Method 3: Word/Google Docs
1. Create formatted document
2. Add formulas using equation editor
3. File → Download/Save as PDF

### Method 4: Screenshots (Quick)
1. Take screenshot of formula sheet
2. Save as image
3. Insert image into Word/Docs
4. Save as PDF

## Recommended Structure

Create 2-3 PDFs per topic (8-12 total):

**Algebra** (3 PDFs):
- `quadratic_equations.pdf` - Formulas, discriminant, examples
- `linear_systems.pdf` - Elimination, substitution, matrices
- `polynomial_basics.pdf` - Factoring, roots, remainder theorem

**Calculus** (3 PDFs):
- `derivatives_rules.pdf` - Power, product, quotient, chain
- `integration_basics.pdf` - Fundamental theorem, u-substitution
- `limits_continuity.pdf` - Limit laws, L'Hospital's rule

**Probability** (2 PDFs):
- `probability_axioms.pdf` - Basic rules, conditional, Bayes
- `distributions.pdf` - Binomial, normal, expected value

**Linear Algebra** (2 PDFs):
- `matrices_operations.pdf` - Addition, multiplication, inverse
- `vectors_basics.pdf` - Dot product, cross product, projection

## Quick Start (5 minutes)

1. Copy the sample content above
2. Paste into Google Docs (3 separate docs for algebra, calculus, probability)
3. Format with headings
4. File → Download → PDF
5. Save to appropriate folders
6. Run `python scripts/build_rag_index.py`

Done! Your RAG system now has knowledge.
