# Practice Problems: Limits (20 Problems)

## Problem 1: Basic Limit
**Question:** Find lim(x→2) (x² - 4)/(x - 2)

**Solution:**
Factor: (x² - 4)/(x - 2) = (x+2)(x-2)/(x-2) = x + 2

lim(x→2) (x + 2) = 4

**Answer:** 4

---

## Problem 2: Standard Form
**Question:** Find lim(x→0) sin(5x)/x

**Solution:**
= 5 × lim(x→0) sin(5x)/(5x) = 5 × 1 = 5

**Answer:** 5

---

## Problem 3: L'Hôpital's Rule
**Question:** Find lim(x→0) (eˣ - 1 - x)/x²

**Solution:**
0/0 form, apply L'Hôpital:
= lim(x→0) (eˣ - 1)/(2x)

Still 0/0, apply again:
= lim(x→0) eˣ/2 = 1/2

**Answer:** 1/2

---

## Problem 4: Rationalization
**Question:** Find lim(x→0) (√(1+x) - 1)/x

**Solution:**
Multiply by conjugate:
= lim(x→0) [(√(1+x) - 1)(√(1+x) + 1)]/[x(√(1+x) + 1)]
= lim(x→0) (1+x-1)/[x(√(1+x) + 1)]
= lim(x→0) 1/(√(1+x) + 1)
= 1/2

**Answer:** 1/2

---

## Problem 5: Exponential Limit
**Question:** Find lim(x→∞) (1 + 2/x)ˣ

**Solution:**
Let y = (1 + 2/x)ˣ = [(1 + 2/x)^(x/2)]²

lim(t→∞) (1 + 2/t)^t = e²

So limit = e²

**Answer:** e²

---

## Problem 6: Trigonometric Limit
**Question:** Find lim(x→0) (1 - cos(4x))/x²

**Solution:**
= lim(x→0) [2sin²(2x)]/x²
= 2 × lim(x→0) [sin(2x)/(2x)]² × 4
= 2 × 1 × 4 = 8

**Answer:** 8

---

## Problem 7: Indeterminate Form
**Question:** Find lim(x→1) (xᵐ - 1)/(xⁿ - 1)

**Solution:**
Using L'Hôpital or direct formula:
= lim(x→1) (m·xᵐ⁻¹)/(n·xⁿ⁻¹)
= m/n

**Answer:** m/n

---

## Problem 8: Infinity Form
**Question:** Find lim(x→∞) (3x² + 2x + 1)/(2x² - x + 5)

**Solution:**
Divide by x²:
= lim(x→∞) (3 + 2/x + 1/x²)/(2 - 1/x + 5/x²)
= 3/2

**Answer:** 3/2

---

## Problem 9: Sandwich Theorem
**Question:** Find lim(x→0) x²·sin(1/x)

**Solution:**
-1 ≤ sin(1/x) ≤ 1
-x² ≤ x²·sin(1/x) ≤ x²

As x→0, both -x² and x² → 0
By sandwich theorem, limit = 0

**Answer:** 0

---

## Problem 10: Logarithmic Limit
**Question:** Find lim(x→0) ln(1 + 3x)/x

**Solution:**
= 3 × lim(x→0) ln(1 + 3x)/(3x)
= 3 × 1 = 3

**Answer:** 3

---

## Problem 11: Factorization
**Question:** Find lim(x→3) (x³ - 27)/(x - 3)

**Solution:**
= lim(x→3) (x-3)(x² + 3x + 9)/(x-3)
= lim(x→3) (x² + 3x + 9)
= 9 + 9 + 9 = 27

**Answer:** 27

---

## Problem 12: One-Sided Limit
**Question:** Find lim(x→0⁺) x·ln(x)

**Solution:**
= lim(x→0⁺) ln(x)/(1/x)

∞/∞ form, L'Hôpital:
= lim(x→0⁺) (1/x)/(-1/x²)
= lim(x→0⁺) -x = 0

**Answer:** 0

---

## Problem 13: Complex Limit
**Question:** Find lim(x→0) (tan x - sin x)/x³

**Solution:**
tan x - sin x = sin x/cos x - sin x = sin x(1 - cos x)/cos x

= lim(x→0) [sin x·2sin²(x/2)]/(cos x·x³)
= lim(x→0) [sin x/x]·[2sin²(x/2)]/(x²/4)·[1/cos x]·[1/(4)]
= 1 × 2/4 × 1 × 1/4 = 1/8

Or using series: tan x ≈ x + x³/3, sin x ≈ x
tan x - sin x ≈ x³/3
Limit = 1/3... (check calculation)

Correct answer using L'Hôpital repeatedly: 1/2

**Answer:** 1/2

---

## Problem 14: Parametric Form
**Question:** Find lim(h→0) [f(x+h) + f(x-h) - 2f(x)]/h²

**Solution:**
This is related to second derivative.
Using Taylor expansion:
f(x+h) ≈ f(x) + f'(x)h + f''(x)h²/2
f(x-h) ≈ f(x) - f'(x)h + f''(x)h²/2

Sum: f(x+h) + f(x-h) ≈ 2f(x) + f''(x)h²

Limit = f''(x)

**Answer:** f''(x)

---

## Problem 15: Absolute Value
**Question:** Find lim(x→0) |x|/x

**Solution:**
Left limit: lim(x→0⁻) -x/x = -1
Right limit: lim(x→0⁺) x/x = 1

Since LHL ≠ RHL, limit does not exist

**Answer:** Does not exist

---

## Problem 16: Multiple Variable
**Question:** Find lim(x→a) (xⁿ - aⁿ)/(x - a)

**Solution:**
Factor: (xⁿ - aⁿ) = (x-a)(xⁿ⁻¹ + xⁿ⁻²a + ... + aⁿ⁻¹)

= lim(x→a) (xⁿ⁻¹ + xⁿ⁻²a + ... + aⁿ⁻¹)
= aⁿ⁻¹ + aⁿ⁻¹ + ... + aⁿ⁻¹ (n terms)
= n·aⁿ⁻¹

**Answer:** n·aⁿ⁻¹

---

## Problem 17: Exponential Comparison
**Question:** Find lim(x→0) (aˣ - bˣ)/x

**Solution:**
= lim(x→0) [(aˣ - 1) - (bˣ - 1)]/x
= lim(x→0) (aˣ - 1)/x - lim(x→0) (bˣ - 1)/x
= ln(a) - ln(b)
= ln(a/b)

**Answer:** ln(a/b)

---

## Problem 18: Trigonometric Product
**Question:** Find lim(x→0) (sin(ax)·sin(bx))/x²

**Solution:**
= lim(x→0) [sin(ax)/x]·[sin(bx)/x]·x²/x²
= lim(x→0) [sin(ax)/(ax)]·a·[sin(bx)/(bx)]·b
= 1·a·1·b = ab

**Answer:** ab

---

## Problem 19: Composite Function
**Question:** Find lim(x→0) [ln(1 + x²)]/sin²(x)

**Solution:**
= lim(x→0) [ln(1 + x²)/x²]·[x²/sin²(x)]
= 1·1 = 1

**Answer:** 1

---

## Problem 20: Power Tower
**Question:** Find lim(n→∞) [1 + 1/n + 1/n² + ... + 1/nⁿ]

**Solution:**
= lim(n→∞) Σ(k=0 to n) (1/n)ᵏ
= lim(n→∞) [1 - (1/n)ⁿ⁺¹]/[1 - 1/n]
= lim(n→∞) [1 - (1/n)ⁿ⁺¹]/[(n-1)/n]
= lim(n→∞) n/(n-1) = 1/(1-0) = 1

Actually: = 1 + 1 + 0 + ... = 2 (first two terms dominate)

More carefully: = 1/(1-0) · n/(n-1) → 1 as n→∞

Actually sum = (1-(1/n)ⁿ⁺¹)/(1-1/n) × n/(n) = n/(n-1) → 1

Correct: Each term → 0 except first two → answer involves more care

**Answer:** n/(n-1) → 1