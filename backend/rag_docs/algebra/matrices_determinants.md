# Matrices and Determinants

## Matrix Definition

A matrix is a rectangular array of numbers arranged in rows and columns.

Order: m × n (m rows, n columns)

A = [aᵢⱼ]ₘₓₙ where aᵢⱼ is element in ith row and jth column

## Types of Matrices

### Row Matrix
Matrix with only one row: 1 × n

### Column Matrix
Matrix with only one column: m × 1

### Square Matrix
Number of rows = number of columns: n × n

### Diagonal Matrix
Square matrix with all non-diagonal elements zero
aᵢⱼ = 0 for i ≠ j

### Scalar Matrix
Diagonal matrix with all diagonal elements equal
aᵢᵢ = k for all i

### Identity Matrix (I)
Scalar matrix with diagonal elements = 1

### Zero Matrix (O)
All elements are zero

### Triangular Matrix

**Upper triangular:** aᵢⱼ = 0 for i > j
**Lower triangular:** aᵢⱼ = 0 for i < j

### Symmetric Matrix
A = Aᵀ (transpose equals original)
aᵢⱼ = aⱼᵢ

### Skew-Symmetric Matrix
A = -Aᵀ
aᵢⱼ = -aⱼᵢ
Diagonal elements must be zero

## Matrix Operations

### Equality
A = B if and only if aᵢⱼ = bᵢⱼ for all i,j

### Addition
(A + B)ᵢⱼ = aᵢⱼ + bᵢⱼ
Only for matrices of same order

Properties:
- A + B = B + A (commutative)
- (A + B) + C = A + (B + C) (associative)
- A + O = A

### Scalar Multiplication
(kA)ᵢⱼ = k·aᵢⱼ

Properties:
- k(A + B) = kA + kB
- (k + m)A = kA + mA
- k(mA) = (km)A

### Matrix Multiplication
C = AB where cᵢⱼ = Σₖ(aᵢₖ·bₖⱼ)

**Condition:** Number of columns in A = Number of rows in B

Properties:
- Generally AB ≠ BA (not commutative)
- (AB)C = A(BC) (associative)
- A(B + C) = AB + AC (distributive)
- IA = AI = A

### Transpose
(Aᵀ)ᵢⱼ = aⱼᵢ (rows become columns)

Properties:
- (Aᵀ)ᵀ = A
- (A + B)ᵀ = Aᵀ + Bᵀ
- (kA)ᵀ = kAᵀ
- (AB)ᵀ = BᵀAᵀ

## Determinant of a Matrix

Determinant exists only for square matrices.

### For 2×2 matrix:
|a  b|
|c  d| = ad - bc

### For 3×3 matrix:
|a₁  b₁  c₁|
|a₂  b₂  c₂| = a₁(b₂c₃ - b₃c₂) - b₁(a₂c₃ - a₃c₂) + c₁(a₂b₃ - a₃b₂)
|a₃  b₃  c₃|

## Properties of Determinants

|A| = |Aᵀ|

If two rows (or columns) are identical, |A| = 0

If all elements of a row (or column) are zero, |A| = 0

Interchanging two rows (or columns) changes sign: |A| → -|A|

Multiplying a row (or column) by k multiplies determinant by k

If A is n×n: |kA| = kⁿ|A|

Adding multiple of one row to another doesn't change determinant

|AB| = |A|·|B|

|Aⁿ| = |A|ⁿ

|A⁻¹| = 1/|A|

## Cofactor and Adjoint

### Minor (Mᵢⱼ)
Determinant after removing ith row and jth column

### Cofactor (Cᵢⱼ)
Cᵢⱼ = (-1)^(i+j) × Mᵢⱼ

### Adjoint (adj A)
Transpose of cofactor matrix
(adj A)ᵢⱼ = Cⱼᵢ

Properties:
- A(adj A) = (adj A)A = |A|·I
- |adj A| = |A|ⁿ⁻¹ for n×n matrix
- adj(AB) = (adj B)(adj A)
- adj(Aᵀ) = (adj A)ᵀ

## Inverse of a Matrix

A⁻¹ = (adj A)/|A|

**Condition:** |A| ≠ 0 (matrix must be non-singular)

### Properties:
- AA⁻¹ = A⁻¹A = I
- (A⁻¹)⁻¹ = A
- (AB)⁻¹ = B⁻¹A⁻¹
- (Aᵀ)⁻¹ = (A⁻¹)ᵀ
- |A⁻¹| = 1/|A|
- (kA)⁻¹ = (1/k)A⁻¹

## Rank of a Matrix

Rank = Maximum number of linearly independent rows (or columns)

Also = Order of largest non-zero minor

Properties:
- rank(A) ≤ min(m,n) for m×n matrix
- rank(A) = rank(Aᵀ)
- rank(AB) ≤ min(rank(A), rank(B))

## System of Linear Equations

For system AX = B:

### Cramer's Rule (when |A| ≠ 0):
xᵢ = |Aᵢ|/|A|

Where Aᵢ is matrix with ith column replaced by B

### Matrix Method:
If |A| ≠ 0: X = A⁻¹B (unique solution)

### Consistency Conditions:

**|A| ≠ 0:** Unique solution exists

**|A| = 0 and (adj A)B ≠ 0:** No solution (inconsistent)

**|A| = 0 and (adj A)B = 0:** Infinite solutions (consistent)

## Homogeneous System (AX = 0)

Always has trivial solution X = 0

**Non-trivial solution exists if and only if |A| = 0**

## Eigenvalues and Eigenvectors

For square matrix A:

If AX = λX for non-zero vector X, then:
- λ is eigenvalue
- X is eigenvector

**Characteristic equation:**
|A - λI| = 0

Sum of eigenvalues = Trace(A) = Sum of diagonal elements

Product of eigenvalues = |A|

## Cayley-Hamilton Theorem

Every square matrix satisfies its own characteristic equation.

If characteristic equation is λⁿ + c₁λⁿ⁻¹ + ... + cₙ = 0, then:
Aⁿ + c₁Aⁿ⁻¹ + ... + cₙI = O

## Special Matrix Results

### For 2×2 matrix:
If A² = I, then A = ±I or A² - (trace)A + |A|I = O

### Orthogonal Matrix:
AAᵀ = AᵀA = I
|A| = ±1

### Idempotent Matrix:
A² = A

### Nilpotent Matrix:
Aᵏ = O for some positive integer k

### Involutory Matrix:
A² = I

## Differentiation and Integration

d/dx[A] = [d/dx(aᵢⱼ)]

∫A dx = [∫aᵢⱼ dx]

## Common Mistakes to Avoid

- Assuming matrix multiplication is commutative
- Wrong order in matrix multiplication
- Forgetting to check if inverse exists
- Sign errors in cofactor calculation
- Incorrect expansion of determinants
- Not verifying dimensions in matrix operations
- Confusing adjoint with transpose

## Important Results

|kA| = kⁿ|A| for n×n matrix

If A is orthogonal: A⁻¹ = Aᵀ

For symmetric matrix: All eigenvalues are real

For skew-symmetric matrix: All eigenvalues are purely imaginary or zero

If A is singular: At least one eigenvalue is zero

Trace(A + B) = Trace(A) + Trace(B)

Trace(AB) = Trace(BA)