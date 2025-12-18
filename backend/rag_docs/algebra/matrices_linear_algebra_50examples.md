# Linear Algebra - Comprehensive Solved Examples

*Curated examples on matrices, systems of equations, determinants, and vector spaces*

---

## Example 1: Matrix Addition

**Problem:**

Given matrices:
$$A = \begin{bmatrix} 2 & 3 \\ 5 & 7 \end{bmatrix}, \quad B = \begin{bmatrix} 1 & 4 \\ 6 & 2 \end{bmatrix}$$

Find A + B.

**Solution:**

Matrix addition is performed element-wise:

$$A + B = \begin{bmatrix} 2+1 & 3+4 \\ 5+6 & 7+2 \end{bmatrix} = \begin{bmatrix} 3 & 7 \\ 11 & 9 \end{bmatrix}$$

**Answer:** $\begin{bmatrix} 3 & 7 \\ 11 & 9 \end{bmatrix}$

---

## Example 2: Scalar Multiplication

**Problem:**

If $A = \begin{bmatrix} 2 & -3 \\ 1 & 4 \end{bmatrix}$, find 3A.

**Solution:**

Multiply each element by 3:

$$3A = 3 \times \begin{bmatrix} 2 & -3 \\ 1 & 4 \end{bmatrix} = \begin{bmatrix} 6 & -9 \\ 3 & 12 \end{bmatrix}$$

**Answer:** $\begin{bmatrix} 6 & -9 \\ 3 & 12 \end{bmatrix}$

---

## Example 3: Matrix Multiplication (2×2)

**Problem:**

Given:
$$A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}, \quad B = \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix}$$

Find AB.

**Solution:**

$(AB)_{ij} = \sum_{k} A_{ik} \times B_{kj}$

$$AB = \begin{bmatrix} 1(5)+2(7) & 1(6)+2(8) \\ 3(5)+4(7) & 3(6)+4(8) \end{bmatrix}$$

$$= \begin{bmatrix} 5+14 & 6+16 \\ 15+28 & 18+32 \end{bmatrix} = \begin{bmatrix} 19 & 22 \\ 43 & 50 \end{bmatrix}$$

**Answer:** $\begin{bmatrix} 19 & 22 \\ 43 & 50 \end{bmatrix}$

---

## Example 4: Matrix Multiplication Is Not Commutative

**Problem:**

Show that AB ≠ BA for the matrices from Example 3.

**Solution:**

From Example 3: $AB = \begin{bmatrix} 19 & 22 \\ 43 & 50 \end{bmatrix}$

Now calculate BA:

$$BA = \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix} \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$$

$$= \begin{bmatrix} 5(1)+6(3) & 5(2)+6(4) \\ 7(1)+8(3) & 7(2)+8(4) \end{bmatrix}$$

$$= \begin{bmatrix} 23 & 34 \\ 31 & 46 \end{bmatrix}$$

Since $\begin{bmatrix} 19 & 22 \\ 43 & 50 \end{bmatrix} \neq \begin{bmatrix} 23 & 34 \\ 31 & 46 \end{bmatrix}$

**Conclusion:** AB ≠ BA (matrix multiplication is not commutative)

---

## Example 5: Transpose of a Matrix

**Problem:**

Find the transpose of:
$$A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}$$

**Solution:**

Transpose means interchange rows and columns:

$$A^T = \begin{bmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{bmatrix}$$

**Properties:**
- $(A^T)^T = A$
- $(A + B)^T = A^T + B^T$
- $(AB)^T = B^T A^T$

---

## Example 6: Identity Matrix

**Problem:**

Verify that IA = AI = A for $A = \begin{bmatrix} 2 & 3 \\ 5 & 7 \end{bmatrix}$

**Solution:**

Identity matrix: $I = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$

$$IA = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 2 & 3 \\ 5 & 7 \end{bmatrix} = \begin{bmatrix} 2 & 3 \\ 5 & 7 \end{bmatrix} = A$$

$$AI = \begin{bmatrix} 2 & 3 \\ 5 & 7 \end{bmatrix} \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 2 & 3 \\ 5 & 7 \end{bmatrix} = A$$

**Verified:** IA = AI = A ✓

---

## Example 7: Determinant of 2×2 Matrix

**Problem:**

Find the determinant of $A = \begin{bmatrix} 4 & 7 \\ 2 & 6 \end{bmatrix}$

**Solution:**

For 2×2 matrix $\begin{bmatrix} a & b \\ c & d \end{bmatrix}$, determinant = ad - bc

$$|A| = (4)(6) - (7)(2) = 24 - 14 = 10$$

**Answer:** det(A) = 10

---

## Example 8: Determinant of 3×3 Matrix

**Problem:**

Find the determinant of:
$$A = \begin{bmatrix} 1 & 2 & 3 \\ 0 & 4 & 5 \\ 1 & 0 & 6 \end{bmatrix}$$

**Solution:**

Expanding along first row:

$$|A| = 1 \begin{vmatrix} 4 & 5 \\ 0 & 6 \end{vmatrix} - 2 \begin{vmatrix} 0 & 5 \\ 1 & 6 \end{vmatrix} + 3 \begin{vmatrix} 0 & 4 \\ 1 & 0 \end{vmatrix}$$

$$= 1(4 \times 6 - 5 \times 0) - 2(0 \times 6 - 5 \times 1) + 3(0 \times 0 - 4 \times 1)$$

$$= 1(24) - 2(-5) + 3(-4)$$

$$= 24 + 10 - 12 = 22$$

**Answer:** det(A) = 22

---

## Example 9: Singular Matrix

**Problem:**

Show that $A = \begin{bmatrix} 2 & 4 \\ 1 & 2 \end{bmatrix}$ is singular.

**Solution:**

A matrix is singular if its determinant is zero.

$$|A| = (2)(2) - (4)(1) = 4 - 4 = 0$$

Since det(A) = 0, the matrix is singular (non-invertible).

**Note:** The second row is a multiple of the first row (row 2 = 0.5 × row 1).

---

## Example 10: Inverse of 2×2 Matrix

**Problem:**

Find the inverse of $A = \begin{bmatrix} 3 & 5 \\ 1 & 2 \end{bmatrix}$

**Solution:**

**Step 1:** Check if inverse exists
$$|A| = (3)(2) - (5)(1) = 6 - 5 = 1 \neq 0$$ ✓

**Step 2:** Use formula for 2×2 inverse:
$$A^{-1} = \frac{1}{|A|} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$$

$$A^{-1} = \frac{1}{1} \begin{bmatrix} 2 & -5 \\ -1 & 3 \end{bmatrix} = \begin{bmatrix} 2 & -5 \\ -1 & 3 \end{bmatrix}$$

**Verification:**
$$AA^{-1} = \begin{bmatrix} 3 & 5 \\ 1 & 2 \end{bmatrix} \begin{bmatrix} 2 & -5 \\ -1 & 3 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$$ ✓

---

## Example 11: System of Linear Equations (2×2)

**Problem:**

Solve the system:
$$2x + 3y = 8$$
$$x + 4y = 9$$

**Solution:**

**Method 1: Elimination**

Multiply first equation by 1, second by 2:
$$2x + 3y = 8$$
$$2x + 8y = 18$$

Subtract first from second:
$$5y = 10 \Rightarrow y = 2$$

Substitute into first equation:
$$2x + 3(2) = 8 \Rightarrow 2x = 2 \Rightarrow x = 1$$

**Answer:** x = 1, y = 2

**Verification:**
- $2(1) + 3(2) = 8$ ✓
- $1 + 4(2) = 9$ ✓

---

## Example 12: System Using Matrix Inverse

**Problem:**

Solve using matrix method:
$$3x + 5y = 11$$
$$x + 2y = 4$$

**Solution:**

Write as AX = B:
$$\begin{bmatrix} 3 & 5 \\ 1 & 2 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 11 \\ 4 \end{bmatrix}$$

From Example 10, $A^{-1} = \begin{bmatrix} 2 & -5 \\ -1 & 3 \end{bmatrix}$

$$X = A^{-1}B = \begin{bmatrix} 2 & -5 \\ -1 & 3 \end{bmatrix} \begin{bmatrix} 11 \\ 4 \end{bmatrix}$$

$$= \begin{bmatrix} 2(11) + (-5)(4) \\ -1(11) + 3(4) \end{bmatrix} = \begin{bmatrix} 22-20 \\ -11+12 \end{bmatrix} = \begin{bmatrix} 2 \\ 1 \end{bmatrix}$$

**Answer:** x = 2, y = 1

---

## Example 13: Gaussian Elimination (Simple)

**Problem:**

Solve using Gaussian elimination:
$$x + y = 5$$
$$x + 2y = 8$$

**Solution:**

Augmented matrix:
$$\begin{bmatrix} 1 & 1 & | & 5 \\ 1 & 2 & | & 8 \end{bmatrix}$$

**R₂ - R₁ → R₂:**
$$\begin{bmatrix} 1 & 1 & | & 5 \\ 0 & 1 & | & 3 \end{bmatrix}$$

**R₁ - R₂ → R₁:**
$$\begin{bmatrix} 1 & 0 & | & 2 \\ 0 & 1 & | & 3 \end{bmatrix}$$

**Answer:** x = 2, y = 3

---

## Example 14: Redundant Equations

**Problem:**

Solve the system:
$$x + y = 2$$
$$2x + 2y = 4$$

**Solution:**

Augmented matrix:
$$\begin{bmatrix} 1 & 1 & | & 2 \\ 2 & 2 & | & 4 \end{bmatrix}$$

**R₂ - 2R₁ → R₂:**
$$\begin{bmatrix} 1 & 1 & | & 2 \\ 0 & 0 & | & 0 \end{bmatrix}$$

Second equation becomes 0 = 0 (always true).

**Solution set:** $x + y = 2$, or $y = 2 - x$

**Parametric form:** $(x, 2-x)$ for any x ∈ ℝ

**Answer:** Infinitely many solutions: (0,2), (1,1), (2,0), etc.

---

## Example 15: Inconsistent System

**Problem:**

Solve:
$$x + y = 2$$
$$2x + 2y = 5$$

**Solution:**

Augmented matrix:
$$\begin{bmatrix} 1 & 1 & | & 2 \\ 2 & 2 & | & 5 \end{bmatrix}$$

**R₂ - 2R₁ → R₂:**
$$\begin{bmatrix} 1 & 1 & | & 2 \\ 0 & 0 & | & 1 \end{bmatrix}$$

Second equation: $0x + 0y = 1$ (impossible!)

**Answer:** No solution (inconsistent system)

---

## Example 16: Row Echelon Form

**Problem:**

Reduce to row echelon form:
$$\begin{bmatrix} 2 & 4 & 6 \\ 1 & 3 & 5 \\ 3 & 5 & 7 \end{bmatrix}$$

**Solution:**

**Swap R₁ and R₂:**
$$\begin{bmatrix} 1 & 3 & 5 \\ 2 & 4 & 6 \\ 3 & 5 & 7 \end{bmatrix}$$

**R₂ - 2R₁, R₃ - 3R₁:**
$$\begin{bmatrix} 1 & 3 & 5 \\ 0 & -2 & -4 \\ 0 & -4 & -8 \end{bmatrix}$$

**R₃ - 2R₂:**
$$\begin{bmatrix} 1 & 3 & 5 \\ 0 & -2 & -4 \\ 0 & 0 & 0 \end{bmatrix}$$

This is in row echelon form (leading entries form a staircase pattern).

---

## Example 17: Reduced Row Echelon Form (RREF)

**Problem:**

Convert Example 16's result to RREF.

**Solution:**

Starting from:
$$\begin{bmatrix} 1 & 3 & 5 \\ 0 & -2 & -4 \\ 0 & 0 & 0 \end{bmatrix}$$

**R₂ ÷ (-2):**
$$\begin{bmatrix} 1 & 3 & 5 \\ 0 & 1 & 2 \\ 0 & 0 & 0 \end{bmatrix}$$

**R₁ - 3R₂:**
$$\begin{bmatrix} 1 & 0 & -1 \\ 0 & 1 & 2 \\ 0 & 0 & 0 \end{bmatrix}$$

**Properties of RREF:**
- Leading entry (pivot) in each row is 1
- Each pivot is the only non-zero entry in its column
- Pivots move to the right in successive rows

---

## Example 18: System with Free Variables

**Problem:**

Solve:
$$x + 2y + 3z = 6$$
$$2x + 4y + 6z = 12$$

**Solution:**

Augmented matrix:
$$\begin{bmatrix} 1 & 2 & 3 & | & 6 \\ 2 & 4 & 6 & | & 12 \end{bmatrix}$$

**R₂ - 2R₁:**
$$\begin{bmatrix} 1 & 2 & 3 & | & 6 \\ 0 & 0 & 0 & | & 0 \end{bmatrix}$$

From first row: $x + 2y + 3z = 6$, so $x = 6 - 2y - 3z$

**Solution:** Let y = s, z = t (free variables)

$$\begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 6-2s-3t \\ s \\ t \end{bmatrix} = \begin{bmatrix} 6 \\ 0 \\ 0 \end{bmatrix} + s\begin{bmatrix} -2 \\ 1 \\ 0 \end{bmatrix} + t\begin{bmatrix} -3 \\ 0 \\ 1 \end{bmatrix}$$

**Answer:** Infinitely many solutions with 2 parameters

---

## Example 19: 3×3 System with Unique Solution

**Problem:**

Solve:
$$x + y + z = 6$$
$$2x - y + z = 3$$
$$x + 2y - z = 2$$

**Solution:**

Augmented matrix:
$$\begin{bmatrix} 1 & 1 & 1 & | & 6 \\ 2 & -1 & 1 & | & 3 \\ 1 & 2 & -1 & | & 2 \end{bmatrix}$$

**R₂ - 2R₁, R₃ - R₁:**
$$\begin{bmatrix} 1 & 1 & 1 & | & 6 \\ 0 & -3 & -1 & | & -9 \\ 0 & 1 & -2 & | & -4 \end{bmatrix}$$

**R₂ ÷ (-3):**
$$\begin{bmatrix} 1 & 1 & 1 & | & 6 \\ 0 & 1 & 1/3 & | & 3 \\ 0 & 1 & -2 & | & -4 \end{bmatrix}$$

**R₃ - R₂:**
$$\begin{bmatrix} 1 & 1 & 1 & | & 6 \\ 0 & 1 & 1/3 & | & 3 \\ 0 & 0 & -7/3 & | & -7 \end{bmatrix}$$

**Back substitution:**
- $-\frac{7}{3}z = -7 \Rightarrow z = 3$
- $y + \frac{1}{3}(3) = 3 \Rightarrow y = 2$
- $x + 2 + 3 = 6 \Rightarrow x = 1$

**Answer:** x = 1, y = 2, z = 3

---

## Example 20: Cramer's Rule (2×2)

**Problem:**

Solve using Cramer's rule:
$$3x + 2y = 5$$
$$x + 4y = 7$$

**Solution:**

$$A = \begin{bmatrix} 3 & 2 \\ 1 & 4 \end{bmatrix}, \quad |A| = 12 - 2 = 10$$

$$A_x = \begin{bmatrix} 5 & 2 \\ 7 & 4 \end{bmatrix}, \quad |A_x| = 20 - 14 = 6$$

$$A_y = \begin{bmatrix} 3 & 5 \\ 1 & 7 \end{bmatrix}, \quad |A_y| = 21 - 5 = 16$$

$$x = \frac{|A_x|}{|A|} = \frac{6}{10} = 0.6$$

$$y = \frac{|A_y|}{|A|} = \frac{16}{10} = 1.6$$

**Answer:** x = 0.6, y = 1.6

---

## Example 21: Matrix Equation AX = B

**Problem:**

Solve for X:
$$\begin{bmatrix} 2 & 1 \\ 1 & 1 \end{bmatrix} X = \begin{bmatrix} 5 & 7 \\ 3 & 4 \end{bmatrix}$$

**Solution:**

Find $A^{-1}$:
$$|A| = 2(1) - 1(1) = 1$$

$$A^{-1} = \begin{bmatrix} 1 & -1 \\ -1 & 2 \end{bmatrix}$$

$$X = A^{-1}B = \begin{bmatrix} 1 & -1 \\ -1 & 2 \end{bmatrix} \begin{bmatrix} 5 & 7 \\ 3 & 4 \end{bmatrix}$$

$$= \begin{bmatrix} 5-3 & 7-4 \\ -5+6 & -7+8 \end{bmatrix} = \begin{bmatrix} 2 & 3 \\ 1 & 1 \end{bmatrix}$$

**Answer:** $X = \begin{bmatrix} 2 & 3 \\ 1 & 1 \end{bmatrix}$

---

## Example 22: Symmetric Matrix

**Problem:**

Show that $A = \begin{bmatrix} 2 & 3 & 1 \\ 3 & 5 & 4 \\ 1 & 4 & 6 \end{bmatrix}$ is symmetric.

**Solution:**

A matrix is symmetric if $A = A^T$.

$$A^T = \begin{bmatrix} 2 & 3 & 1 \\ 3 & 5 & 4 \\ 1 & 4 & 6 \end{bmatrix} = A$$

Since A = A^T, the matrix is symmetric.

**Property:** In a symmetric matrix, $a_{ij} = a_{ji}$ for all i, j.

---

## Example 23: Skew-Symmetric Matrix

**Problem:**

Verify that $A = \begin{bmatrix} 0 & 2 & -3 \\ -2 & 0 & 5 \\ 3 & -5 & 0 \end{bmatrix}$ is skew-symmetric.

**Solution:**

A matrix is skew-symmetric if $A^T = -A$.

$$A^T = \begin{bmatrix} 0 & -2 & 3 \\ 2 & 0 & -5 \\ -3 & 5 & 0 \end{bmatrix}$$

$$-A = -\begin{bmatrix} 0 & 2 & -3 \\ -2 & 0 & 5 \\ 3 & -5 & 0 \end{bmatrix} = \begin{bmatrix} 0 & -2 & 3 \\ 2 & 0 & -5 \\ -3 & 5 & 0 \end{bmatrix}$$

Since $A^T = -A$, the matrix is skew-symmetric.

**Note:** Diagonal elements are always 0 in skew-symmetric matrices.

---

## Example 24: Rank of a Matrix

**Problem:**

Find the rank of:
$$A = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 3 & 6 & 9 \end{bmatrix}$$

**Solution:**

Reduce to row echelon form:

**R₂ - 2R₁, R₃ - 3R₁:**
$$\begin{bmatrix} 1 & 2 & 3 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}$$

Number of non-zero rows = 1

**Answer:** Rank(A) = 1

**Note:** All rows are multiples of the first row, so they're linearly dependent.

---

## Example 25: Orthogonal Vectors

**Problem:**

Show that vectors $\vec{u} = \begin{bmatrix} 1 \\ 2 \\ -1 \end{bmatrix}$ and $\vec{v} = \begin{bmatrix} 2 \\ 0 \\ 2 \end{bmatrix}$ are orthogonal.

**Solution:**

Vectors are orthogonal if their dot product is zero:

$$\vec{u} \cdot \vec{v} = (1)(2) + (2)(0) + (-1)(2) = 2 + 0 - 2 = 0$$

Since $\vec{u} \cdot \vec{v} = 0$, the vectors are orthogonal (perpendicular).

---

## Example 26: Vector Magnitude

**Problem:**

Find the magnitude of $\vec{v} = \begin{bmatrix} 3 \\ 4 \\ 12 \end{bmatrix}$

**Solution:**

$$|\vec{v}| = \sqrt{v_1^2 + v_2^2 + v_3^2}$$

$$= \sqrt{3^2 + 4^2 + 12^2} = \sqrt{9 + 16 + 144} = \sqrt{169} = 13$$

**Answer:** $|\vec{v}| = 13$

---

## Example 27: Unit Vector

**Problem:**

Find the unit vector in the direction of $\vec{v} = \begin{bmatrix} 3 \\ 4 \\ 12 \end{bmatrix}$

**Solution:**

From Example 26, $|\vec{v}| = 13$

Unit vector:
$$\hat{v} = \frac{\vec{v}}{|\vec{v}|} = \frac{1}{13}\begin{bmatrix} 3 \\ 4 \\ 12 \end{bmatrix} = \begin{bmatrix} 3/13 \\ 4/13 \\ 12/13 \end{bmatrix}$$

**Verification:** $|\hat{v}| = \sqrt{(3/13)^2 + (4/13)^2 + (12/13)^2} = \sqrt{169/169} = 1$ ✓

---

## Example 28: Linear Combination of Vectors

**Problem:**

Express $\vec{w} = \begin{bmatrix} 7 \\ 11 \end{bmatrix}$ as a linear combination of $\vec{u} = \begin{bmatrix} 1 \\ 2 \end{bmatrix}$ and $\vec{v} = \begin{bmatrix} 3 \\ 4 \end{bmatrix}$

**Solution:**

Find a, b such that $a\vec{u} + b\vec{v} = \vec{w}$:

$$a\begin{bmatrix} 1 \\ 2 \end{bmatrix} + b\begin{bmatrix} 3 \\ 4 \end{bmatrix} = \begin{bmatrix} 7 \\ 11 \end{bmatrix}$$

This gives:
- $a + 3b = 7$
- $2a + 4b = 11$

From first: $a = 7 - 3b$

Substitute into second: $2(7-3b) + 4b = 11$
$$14 - 6b + 4b = 11$$
$$-2b = -3$$
$$b = 1.5$$

Then: $a = 7 - 3(1.5) = 2.5$

**Answer:** $\vec{w} = 2.5\vec{u} + 1.5\vec{v}$

---

## Example 29: Linear Independence

**Problem:**

Determine if vectors $\vec{v}_1 = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}$, $\vec{v}_2 = \begin{bmatrix} 2 \\ 3 \\ 4 \end{bmatrix}$, $\vec{v}_3 = \begin{bmatrix} 3 \\ 5 \\ 7 \end{bmatrix}$ are linearly independent.

**Solution:**

Check if $c_1\vec{v}_1 + c_2\vec{v}_2 + c_3\vec{v}_3 = \vec{0}$ only when $c_1 = c_2 = c_3 = 0$.

Form augmented matrix:
$$\begin{bmatrix} 1 & 2 & 3 & | & 0 \\ 2 & 3 & 5 & | & 0 \\ 3 & 4 & 7 & | & 0 \end{bmatrix}$$

After row reduction:
$$\begin{bmatrix} 1 & 2 & 3 & | & 0 \\ 0 & -1 & -1 & | & 0 \\ 0 & 0 & 0 & | & 0 \end{bmatrix}$$

Third row of zeros indicates dependence. In fact, $\vec{v}_3 = \vec{v}_1 + \vec{v}_2$.

**Answer:** Linearly dependent

---

## Example 30: Basis of ℝ²

**Problem:**

Show that $\vec{e}_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$ and $\vec{e}_2 = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$ form a basis for ℝ².

**Solution:**

A set of vectors forms a basis if:
1. They are linearly independent
2. They span the space

**Independence:** If $c_1\vec{e}_1 + c_2\vec{e}_2 = \vec{0}$:
$$c_1\begin{bmatrix} 1 \\ 0 \end{bmatrix} + c_2\begin{bmatrix} 0 \\ 1 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$$

This requires $c_1 = 0$ and $c_2 = 0$. ✓

**Spanning:** Any vector $\begin{bmatrix} a \\ b \end{bmatrix} = a\vec{e}_1 + b\vec{e}_2$ ✓

**Conclusion:** {$\vec{e}_1$, $\vec{e}_2$} is the standard basis for ℝ².

---

## Example 31: Change of Basis

**Problem:**

Convert $\vec{v} = \begin{bmatrix} 5 \\ 3 \end{bmatrix}$ from standard basis to basis $B = \{\begin{bmatrix} 1 \\ 1 \end{bmatrix}, \begin{bmatrix} 1 \\ -1 \end{bmatrix}\}$

**Solution:**

Find $c_1, c_2$ such that:
$$c_1\begin{bmatrix} 1 \\ 1 \end{bmatrix} + c_2\begin{bmatrix} 1 \\ -1 \end{bmatrix} = \begin{bmatrix} 5 \\ 3 \end{bmatrix}$$

This gives:
- $c_1 + c_2 = 5$
- $c_1 - c_2 = 3$

Adding: $2c_1 = 8 \Rightarrow c_1 = 4$

Subtracting: $2c_2 = 2 \Rightarrow c_2 = 1$

**Answer:** $[\vec{v}]_B = \begin{bmatrix} 4 \\ 1 \end{bmatrix}$

---

## Example 32: Eigenvalue Problem

**Problem:**

Find eigenvalues of $A = \begin{bmatrix} 3 & 1 \\ 0 & 2 \end{bmatrix}$

**Solution:**

Solve $\det(A - \lambda I) = 0$:

$$\det\begin{bmatrix} 3-\lambda & 1 \\ 0 & 2-\lambda \end{bmatrix} = 0$$

$$(3-\lambda)(2-\lambda) - (1)(0) = 0$$

$$(3-\lambda)(2-\lambda) = 0$$

**Eigenvalues:** $\lambda_1 = 3$, $\lambda_2 = 2$

---

## Example 33: Eigenvector

**Problem:**

Find the eigenvector for $\lambda = 3$ from Example 32.

**Solution:**

Solve $(A - 3I)\vec{v} = \vec{0}$:

$$\begin{bmatrix} 0 & 1 \\ 0 & -1 \end{bmatrix}\begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$$

From first row: $v_2 = 0$

$v_1$ is free, so eigenvector: $\vec{v} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$ (or any scalar multiple)

**Verification:** $A\vec{v} = \begin{bmatrix} 3 & 1 \\ 0 & 2 \end{bmatrix}\begin{bmatrix} 1 \\ 0 \end{bmatrix} = \begin{bmatrix} 3 \\ 0 \end{bmatrix} = 3\begin{bmatrix} 1 \\ 0 \end{bmatrix}$ ✓

---

## Example 34: Diagonalizable Matrix

**Problem:**

Diagonalize $A = \begin{bmatrix} 4 & 1 \\ 0 & 3 \end{bmatrix}$

**Solution:**

**Step 1:** Find eigenvalues:
$$\det(A - \lambda I) = (4-\lambda)(3-\lambda) = 0$$
$\lambda_1 = 4$, $\lambda_2 = 3$

**Step 2:** Find eigenvectors:
For $\lambda_1 = 4$: $\vec{v}_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$

For $\lambda_2 = 3$: $\vec{v}_2 = \begin{bmatrix} 1 \\ -1 \end{bmatrix}$

**Step 3:** Form matrices:
$$P = \begin{bmatrix} 1 & 1 \\ 0 & -1 \end{bmatrix}, \quad D = \begin{bmatrix} 4 & 0 \\ 0 & 3 \end{bmatrix}$$

**Result:** $A = PDP^{-1}$

---

## Example 35: Matrix Powers Using Diagonalization

**Problem:**

Find $A^{10}$ for $A = \begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix}$

**Solution:**

A is already diagonal!

$$A^{10} = \begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix}^{10} = \begin{bmatrix} 2^{10} & 0 \\ 0 & 3^{10} \end{bmatrix}$$

$$= \begin{bmatrix} 1024 & 0 \\ 0 & 59049 \end{bmatrix}$$

**General formula:** If D is diagonal, $D^n$ has diagonal entries raised to power n.

---

## Example 36: Trace of a Matrix

**Problem:**

Find the trace of $A = \begin{bmatrix} 2 & 5 & 1 \\ 3 & 7 & 4 \\ 6 & 8 & 9 \end{bmatrix}$

**Solution:**

Trace = sum of diagonal elements:

$$\text{tr}(A) = 2 + 7 + 9 = 18$$

**Properties:**
- $\text{tr}(A + B) = \text{tr}(A) + \text{tr}(B)$
- $\text{tr}(cA) = c \cdot \text{tr}(A)$
- $\text{tr}(AB) = \text{tr}(BA)$
- $\text{tr}(A) = \sum \lambda_i$ (sum of eigenvalues)

---

## Example 37: Projection of Vector

**Problem:**

Find the projection of $\vec{u} = \begin{bmatrix} 3 \\ 4 \end{bmatrix}$ onto $\vec{v} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$

**Solution:**

$$\text{proj}_{\vec{v}}\vec{u} = \frac{\vec{u} \cdot \vec{v}}{|\vec{v}|^2}\vec{v}$$

$$\vec{u} \cdot \vec{v} = (3)(1) + (4)(0) = 3$$

$$|\vec{v}|^2 = 1^2 + 0^2 = 1$$

$$\text{proj}_{\vec{v}}\vec{u} = \frac{3}{1}\begin{bmatrix} 1 \\ 0 \end{bmatrix} = \begin{bmatrix} 3 \\ 0 \end{bmatrix}$$

**Answer:** Projection = $\begin{bmatrix} 3 \\ 0 \end{bmatrix}$ (onto x-axis)

---

## Example 38: Gram-Schmidt Process

**Problem:**

Orthogonalize vectors $\vec{v}_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$, $\vec{v}_2 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$

**Solution:**

**Step 1:** $\vec{u}_1 = \vec{v}_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$

**Step 2:** $\vec{u}_2 = \vec{v}_2 - \text{proj}_{\vec{u}_1}\vec{v}_2$

$$\text{proj}_{\vec{u}_1}\vec{v}_2 = \frac{\vec{v}_2 \cdot \vec{u}_1}{|\vec{u}_1|^2}\vec{u}_1 = \frac{1}{2}\begin{bmatrix} 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 0.5 \\ 0.5 \end{bmatrix}$$

$$\vec{u}_2 = \begin{bmatrix} 1 \\ 0 \end{bmatrix} - \begin{bmatrix} 0.5 \\ 0.5 \end{bmatrix} = \begin{bmatrix} 0.5 \\ -0.5 \end{bmatrix}$$

**Answer:** Orthogonal vectors: $\vec{u}_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$, $\vec{u}_2 = \begin{bmatrix} 0.5 \\ -0.5 \end{bmatrix}$

---

## Example 39: Cross Product

**Problem:**

Find $\vec{u} \times \vec{v}$ for $\vec{u} = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}$, $\vec{v} = \begin{bmatrix} 4 \\ 5 \\ 6 \end{bmatrix}$

**Solution:**

$$\vec{u} \times \vec{v} = \begin{vmatrix} \vec{i} & \vec{j} & \vec{k} \\ 1 & 2 & 3 \\ 4 & 5 & 6 \end{vmatrix}$$

$$= \vec{i}(2 \cdot 6 - 3 \cdot 5) - \vec{j}(1 \cdot 6 - 3 \cdot 4) + \vec{k}(1 \cdot 5 - 2 \cdot 4)$$

$$= \vec{i}(12-15) - \vec{j}(6-12) + \vec{k}(5-8)$$

$$= -3\vec{i} + 6\vec{j} - 3\vec{k} = \begin{bmatrix} -3 \\ 6 \\ -3 \end{bmatrix}$$

---

## Example 40: Area Using Cross Product

**Problem:**

Find the area of parallelogram formed by $\vec{u} = \begin{bmatrix} 3 \\ 0 \\ 0 \end{bmatrix}$ and $\vec{v} = \begin{bmatrix} 0 \\ 4 \\ 0 \end{bmatrix}$

**Solution:**

Area = $|\vec{u} \times \vec{v}|$

$$\vec{u} \times \vec{v} = \begin{bmatrix} 0 \\ 0 \\ 12 \end{bmatrix}$$

$$|\vec{u} \times \vec{v}| = \sqrt{0^2 + 0^2 + 12^2} = 12$$

**Answer:** Area = 12 square units

---

## Example 41: LU Decomposition

**Problem:**

Find LU decomposition of $A = \begin{bmatrix} 2 & 4 \\ 1 & 3 \end{bmatrix}$

**Solution:**

Write A = LU where L is lower triangular, U is upper triangular.

$$L = \begin{bmatrix} 1 & 0 \\ 0.5 & 1 \end{bmatrix}, \quad U = \begin{bmatrix} 2 & 4 \\ 0 & 1 \end{bmatrix}$$

**Verification:**
$$LU = \begin{bmatrix} 1 & 0 \\ 0.5 & 1 \end{bmatrix}\begin{bmatrix} 2 & 4 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 2 & 4 \\ 1 & 3 \end{bmatrix} = A$$ ✓

---

## Example 42: Solving System with LU

**Problem:**

Use LU decomposition to solve $Ax = b$ where $A = \begin{bmatrix} 2 & 4 \\ 1 & 3 \end{bmatrix}$, $b = \begin{bmatrix} 10 \\ 7 \end{bmatrix}$

**Solution:**

From Example 41: $A = LU$

**Step 1:** Solve $Ly = b$:
$$\begin{bmatrix} 1 & 0 \\ 0.5 & 1 \end{bmatrix}\begin{bmatrix} y_1 \\ y_2 \end{bmatrix} = \begin{bmatrix} 10 \\ 7 \end{bmatrix}$$

$y_1 = 10$, $0.5(10) + y_2 = 7 \Rightarrow y_2 = 2$

**Step 2:** Solve $Ux = y$:
$$\begin{bmatrix} 2 & 4 \\ 0 & 1 \end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 10 \\ 2 \end{bmatrix}$$

$x_2 = 2$, $2x_1 + 4(2) = 10 \Rightarrow x_1 = 1$

**Answer:** $x = \begin{bmatrix} 1 \\ 2 \end{bmatrix}$

---

## Example 43: Rotation Matrix

**Problem:**

Find the matrix that rotates points 90° counterclockwise about the origin.

**Solution:**

Rotation matrix by angle θ:
$$R_\theta = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$$

For θ = 90°:
$$R_{90°} = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$$

**Test:** Rotate $(1, 0)$:
$$\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}\begin{bmatrix} 1 \\ 0 \end{bmatrix} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$$ ✓

---

## Example 44: Reflection Matrix

**Problem:**

Find matrix that reflects points across the x-axis.

**Solution:**

Reflection across x-axis changes $(x, y)$ to $(x, -y)$:

$$R_x = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$$

**Test:** Reflect $(3, 4)$:
$$\begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}\begin{bmatrix} 3 \\ 4 \end{bmatrix} = \begin{bmatrix} 3 \\ -4 \end{bmatrix}$$ ✓

---

## Example 45: Scaling Matrix

**Problem:**

Find matrix that scales by factor 2 in x-direction and 3 in y-direction.

**Solution:**

$$S = \begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix}$$

**Test:** Scale $(1, 1)$:
$$\begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix}\begin{bmatrix} 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 2 \\ 3 \end{bmatrix}$$ ✓

---

## Example 46: QR Decomposition

**Problem:**

Find QR decomposition of $A = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$

**Solution:**

Use Gram-Schmidt to get Q (orthonormal), R (upper triangular):

$$Q = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}, \quad R = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$$

**Verification:** $QR = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} = A$ ✓

---

## Example 47: Cayley-Hamilton Theorem

**Problem:**

Verify Cayley-Hamilton theorem for $A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$

**Solution:**

**Step 1:** Find characteristic polynomial:
$$\det(A - \lambda I) = (2-\lambda)^2 - 1 = \lambda^2 - 4\lambda + 3$$

**Step 2:** Substitute A into characteristic polynomial:
$$A^2 - 4A + 3I = \begin{bmatrix} 5 & 4 \\ 4 & 5 \end{bmatrix} - \begin{bmatrix} 8 & 4 \\ 4 & 8 \end{bmatrix} + \begin{bmatrix} 3 & 0 \\ 0 & 3 \end{bmatrix}$$

$$= \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}$$ ✓

**Theorem verified:** Every matrix satisfies its own characteristic equation.

---

## Example 48: Matrix Norm

**Problem:**

Find the Frobenius norm of $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$

**Solution:**

Frobenius norm: $||A||_F = \sqrt{\sum_{i,j} a_{ij}^2}$

$$||A||_F = \sqrt{1^2 + 2^2 + 3^2 + 4^2} = \sqrt{1 + 4 + 9 + 16} = \sqrt{30}$$

**Answer:** $||A||_F = \sqrt{30} \approx 5.48$

---

## Example 49: Positive Definite Matrix

**Problem:**

Determine if $A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$ is positive definite.

**Solution:**

A matrix is positive definite if all eigenvalues are positive.

Characteristic equation: $\lambda^2 - 4\lambda + 3 = 0$

$$(\lambda - 3)(\lambda - 1) = 0$$

Eigenvalues: $\lambda_1 = 3 > 0$, $\lambda_2 = 1 > 0$

**Answer:** Matrix is positive definite ✓

**Alternative test:** All leading principal minors are positive:
- $\det([2]) = 2 > 0$ ✓
- $\det(A) = 3 > 0$ ✓

---

## Example 50: Application - Markov Chain

**Problem:**

A system transitions between states A and B with transition matrix:
$$P = \begin{bmatrix} 0.7 & 0.3 \\ 0.4 & 0.6 \end{bmatrix}$$

If initially in state A, what's the probability after 2 steps?

**Solution:**

Initial state: $\vec{v}_0 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$ (100% in A)

After 1 step:
$$\vec{v}_1 = P\vec{v}_0 = \begin{bmatrix} 0.7 & 0.3 \\ 0.4 & 0.6 \end{bmatrix}\begin{bmatrix} 1 \\ 0 \end{bmatrix} = \begin{bmatrix} 0.7 \\ 0.4 \end{bmatrix}$$

After 2 steps:
$$\vec{v}_2 = P\vec{v}_1 = \begin{bmatrix} 0.7 & 0.3 \\ 0.4 & 0.6 \end{bmatrix}\begin{bmatrix} 0.7 \\ 0.4 \end{bmatrix}$$

$$= \begin{bmatrix} 0.49+0.12 \\ 0.28+0.24 \end{bmatrix} = \begin{bmatrix} 0.61 \\ 0.52 \end{bmatrix}$$

**Answer:** After 2 steps: 61% in state A, 39% in state B

---

## Key Formulas & Concepts

### Matrix Operations
- $(AB)C = A(BC)$ (associative)
- $A(B + C) = AB + AC$ (distributive)
- $(AB)^T = B^T A^T$
- $AB \neq BA$ (not commutative)

### Determinants
- $|AB| = |A| \cdot |B|$
- $|A^T| = |A|$
- $|A^{-1}| = 1/|A|$
- $|kA| = k^n|A|$ for n×n matrix

### Inverse (2×2)
$$\begin{bmatrix} a & b \\ c & d \end{bmatrix}^{-1} = \frac{1}{ad-bc}\begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$$

### Eigenvalues & Eigenvectors
- $A\vec{v} = \lambda\vec{v}$
- $\det(A - \lambda I) = 0$
- $\text{tr}(A) = \sum \lambda_i$
- $\det(A) = \prod \lambda_i$

### Vector Operations
- Dot product: $\vec{u} \cdot \vec{v} = \sum u_i v_i$
- Magnitude: $|\vec{v}| = \sqrt{\vec{v} \cdot \vec{v}}$
- Unit vector: $\hat{v} = \vec{v}/|\vec{v}|$
- Projection: $\text{proj}_{\vec{v}}\vec{u} = \frac{\vec{u} \cdot \vec{v}}{|\vec{v}|^2}\vec{v}$

### Orthogonality
- $\vec{u} \perp \vec{v}$ if $\vec{u} \cdot \vec{v} = 0$
- Orthogonal matrix: $Q^T Q = I$

### Linear Independence
- Vectors are independent if $c_1\vec{v}_1 + \cdots + c_n\vec{v}_n = \vec{0}$ only when all $c_i = 0$

### Rank & Nullity
- $\text{rank}(A) + \text{nullity}(A) = n$ (number of columns)
- Rank = number of pivot positions = dimension of column space
