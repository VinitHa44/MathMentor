# Practice Problems: Matrices and Determinants (20 Problems)

## Problem 1: Matrix Addition
**Question:** If A = [1 2; 3 4] and B = [5 6; 7 8], find A + B

**Solution:**
A + B = [1+5  2+6; 3+7  4+8]
= [6  8; 10  12]

**Answer:** [6 8; 10 12]

---

## Problem 2: Matrix Multiplication
**Question:** Find AB where A = [1 2; 3 4] and B = [2 0; 1 3]

**Solution:**
AB = [1×2+2×1  1×0+2×3; 3×2+3×1  3×0+4×3]
= [4  6; 9  12]

**Answer:** [4 6; 9 12]

---

## Problem 3: Determinant 2×2
**Question:** Find |A| where A = [3 4; 1 2]

**Solution:**
|A| = 3×2 - 4×1 = 6 - 4 = 2

**Answer:** 2

---

## Problem 4: Determinant 3×3
**Question:** Find determinant of [1 2 3; 0 1 4; 5 6 0]

**Solution:**
Expanding along first row:
= 1(1×0 - 4×6) - 2(0×0 - 4×5) + 3(0×6 - 1×5)
= 1(-24) - 2(-20) + 3(-5)
= -24 + 40 - 15
= 1

**Answer:** 1

---

## Problem 5: Transpose
**Question:** Find transpose of A = [1 2 3; 4 5 6]

**Solution:**
Aᵀ = [1 4; 2 5; 3 6]

**Answer:** [1 4; 2 5; 3 6]

---

## Problem 6: Inverse 2×2
**Question:** Find A⁻¹ where A = [2 3; 1 4]

**Solution:**
|A| = 8 - 3 = 5

A⁻¹ = (1/5)[4  -3; -1  2]
= [4/5  -3/5; -1/5  2/5]

**Answer:** [4/5  -3/5; -1/5  2/5]

---

## Problem 7: Cofactor Matrix
**Question:** Find cofactor of element a₁₂ in [1 2 3; 4 5 6; 7 8 9]

**Solution:**
Minor M₁₂ = |4 6; 7 9| = 36 - 42 = -6

Cofactor C₁₂ = (-1)^(1+2) × M₁₂ = -1 × (-6) = 6

**Answer:** 6

---

## Problem 8: Adjoint Matrix
**Question:** Find adjoint of A = [1 2; 3 4]

**Solution:**
Cofactors:
C₁₁ = 4, C₁₂ = -3
C₂₁ = -2, C₂₂ = 1

adj(A) = [C₁₁  C₂₁; C₁₂  C₂₂] = [4  -2; -3  1]

**Answer:** [4 -2; -3 1]

---

## Problem 9: Symmetric Matrix
**Question:** Check if A = [1 2 3; 2 4 5; 3 5 6] is symmetric

**Solution:**
Aᵀ = [1 2 3; 2 4 5; 3 5 6]

Aᵀ = A, so symmetric

**Answer:** Yes, symmetric

---

## Problem 10: System of Equations
**Question:** Solve using Cramer's rule: 2x + 3y = 7, x - y = 1

**Solution:**
D = |2 3; 1 -1| = -2 - 3 = -5

Dₓ = |7 3; 1 -1| = -7 - 3 = -10
Dᵧ = |2 7; 1 1| = 2 - 7 = -5

x = Dₓ/D = -10/-5 = 2
y = Dᵧ/D = -5/-5 = 1

**Answer:** x = 2, y = 1

---

## Problem 11: Singular Matrix
**Question:** For what value of k is [2 k; 4 6] singular?

**Solution:**
For singular: |A| = 0
2×6 - k×4 = 0
12 - 4k = 0
k = 3

**Answer:** k = 3

---

## Problem 12: Rank of Matrix
**Question:** Find rank of [1 2 3; 2 4 6; 3 6 9]

**Solution:**
All rows are proportional (R₂ = 2R₁, R₃ = 3R₁)

Rank = 1

**Answer:** 1

---

## Problem 13: Matrix Power
**Question:** If A = [1 1; 0 1], find A³

**Solution:**
A² = [1 1; 0 1][1 1; 0 1] = [1 2; 0 1]
A³ = A²·A = [1 2; 0 1][1 1; 0 1] = [1 3; 0 1]

**Answer:** [1 3; 0 1]

---

## Problem 14: Trace
**Question:** Find trace of [3 1 2; 0 4 5; 6 7 8]

**Solution:**
Trace = sum of diagonal elements
= 3 + 4 + 8 = 15

**Answer:** 15

---

## Problem 15: Orthogonal Matrix
**Question:** Check if A = [cos(θ) -sin(θ); sin(θ) cos(θ)] is orthogonal

**Solution:**
Aᵀ = [cos(θ) sin(θ); -sin(θ) cos(θ)]

AᵀA = [cos²(θ)+sin²(θ)  0; 0  cos²(θ)+sin²(θ)]
= [1 0; 0 1] = I

A is orthogonal ✓

**Answer:** Yes, orthogonal

---

## Problem 16: Eigenvalues
**Question:** Find eigenvalues of [2 1; 1 2]

**Solution:**
|A - λI| = 0
|2-λ  1; 1  2-λ| = 0
(2-λ)² - 1 = 0
λ² - 4λ + 3 = 0
(λ-3)(λ-1) = 0

λ = 3 or λ = 1

**Answer:** λ = 1, 3

---

## Problem 17: Idempotent Matrix
**Question:** Verify that A = [1 0; 0 0] is idempotent

**Solution:**
A² = [1 0; 0 0][1 0; 0 0] = [1 0; 0 0] = A

A² = A, so idempotent ✓

**Answer:** Yes, idempotent

---

## Problem 18: Determinant Property
**Question:** If |A| = 5 for 3×3 matrix, find |2A|

**Solution:**
|kA| = kⁿ|A| for n×n matrix

|2A| = 2³ × 5 = 8 × 5 = 40

**Answer:** 40

---

## Problem 19: Inverse Property
**Question:** If A = [2 1; 1 1] and B = A⁻¹, find B

**Solution:**
|A| = 2 - 1 = 1

A⁻¹ = (1/1)[1  -1; -1  2] = [1  -1; -1  2]

**Answer:** [1 -1; -1 2]

---

## Problem 20: Homogeneous System
**Question:** For what value of k does system kx + 2y = 0, 3x + ky = 0 have non-trivial solution?

**Solution:**
For non-trivial solution: |A| = 0

|k  2; 3  k| = 0
k² - 6 = 0
k = ±√6

**Answer:** k = ±√6