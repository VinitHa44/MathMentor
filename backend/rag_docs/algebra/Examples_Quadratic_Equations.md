# Practice Problems: Quadratic Equations (20 Problems)

## Problem 1: Basic Roots
**Question:** Find the roots of the equation 2x² - 7x + 3 = 0

**Solution:**
Using quadratic formula: x = [7 ± √(49-24)]/4 = [7 ± 5]/4

Roots: x = 3 or x = 1/2

**Answer:** x = 3, 1/2

---

## Problem 2: Discriminant Nature
**Question:** For what values of k does x² + (k-5)x + 15 = 3k have no real roots?

**Solution:**
Rearrange: x² + (k-5)x + (15-3k) = 0

For no real roots: D < 0
(k-5)² - 4(15-3k) < 0
k² - 10k + 25 - 60 + 12k < 0
k² + 2k - 35 < 0
(k+7)(k-5) < 0

**Answer:** k ∈ (-7, 5)

---

## Problem 3: Sum and Product of Roots
**Question:** If α and β are roots of x² - 6x - 2 = 0, find the value of α⁴ + β⁴

**Solution:**
α + β = 6, αβ = -2

α² + β² = (α+β)² - 2αβ = 36 + 4 = 40

α⁴ + β⁴ = (α²+β²)² - 2(αβ)² = 1600 - 8 = 1592

**Answer:** 1592

---

## Problem 4: Formation of Equation
**Question:** If α, β are roots of x² + 2√2x - 1 = 0, find equation whose roots are α⁴ + β⁴ and (1/10)(α⁶ + β⁶)

**Solution:**
α + β = -2√2, αβ = -1

α² + β² = (α+β)² - 2αβ = 8 + 2 = 10

α⁴ + β⁴ = (α²+β²)² - 2(αβ)² = 100 - 2 = 98

For α⁶ + β⁶:
α³ + β³ = (α+β)³ - 3αβ(α+β) = -16√2 + 6√2 = -10√2

α⁶ + β⁶ = (α³+β³)² - 2(αβ)³ = 200 + 2 = 202

So (1/10)(α⁶+β⁶) = 20.2

Equation: -32x² + 134x - 2 = 0 or 32x² - 134x + 2 = 0

**Answer:** 32x² - 134x + 2 = 0

---

## Problem 5: Common Root
**Question:** Find value of b for which x² + bx - 1 = 0 and x² + x + b = 0 have one root in common

**Solution:**
Let α be common root.
α² + bα - 1 = 0 ... (1)
α² + α + b = 0 ... (2)

Subtracting: (b-1)α - (b+1) = 0
α = (b+1)/(b-1)

Substituting in (1):
[(b+1)/(b-1)]² + b[(b+1)/(b-1)] - 1 = 0

(b+1)² + b(b+1)(b-1) - (b-1)² = 0
b² + 2b + 1 + b³ - b - b² + 2b - 1 = 0
b³ + 3b = 0
b(b² + 3) = 0

b = 0 or b = ±i√3

**Answer:** b = -i√3

---

## Problem 6: Range of Roots
**Question:** Let S be set of all α such that αx² - x + α = 0 has two distinct real roots x₁, x₂ satisfying |x₁ - x₂| < 1. Find S.

**Solution:**
For distinct real roots: D > 0
1 - 4α² > 0
α² < 1/4
|α| < 1/2

Now, |x₁ - x₂| < 1
√D < 1
√(1 - 4α²) < 1
1 - 4α² < 1

This gives |x₁ - x₂| = √(1-4α²)/|α| < 1
√(1-4α²) < |α|
1 - 4α² < α²
1 < 5α²
α² > 1/5

So: 1/5 < α² < 1/4

**Answer:** S = (-1/2, -1/√5) ∪ (1/√5, 1/2)

---

## Problem 7: Maximum Value
**Question:** If 2x² + (a-5)x + 15 = 3a has no real roots, and α < a < β, find sum of integer values in (α, β).

**Solution:**
For no real roots:
(a-5)² - 4·2·(15-3a) < 0
a² - 10a + 25 - 120 + 24a < 0
a² + 14a - 95 < 0
(a+19)(a-5) < 0

So α = -19, β = 5
Integers: -18, -17, ..., 4

Sum = Σ(k=-18 to 4) k = 23 terms
Sum = 23×(-7) = -161

But calculating properly:
Sum = -18 + (-17) + ... + 4 = (23/2)(-18+4) = -161

**Answer:** Sum = -161 (needs verification with formula)

---

## Problem 8: Complex Roots
**Question:** If 2 + i√3 is a root of x² + px + q = 0 where p, q are real, find (p, q).

**Solution:**
If 2 + i√3 is root, then 2 - i√3 is also root (complex conjugate)

Sum of roots: (2+i√3) + (2-i√3) = 4 = -p
So p = -4

Product of roots: (2+i√3)(2-i√3) = 4 + 3 = 7 = q

**Answer:** (p, q) = (-4, 7)

---

## Problem 9: Condition for Integer Roots
**Question:** If x² + px - 444p = 0 has integral roots where p is prime, find p.

**Solution:**
Let roots be α, β (integers)
α + β = -p
αβ = -444p

From αβ = -444p and α + β = -p:
If α = -p - β, then:
(-p - β)β = -444p
-pβ - β² = -444p
β² + pβ - 444p = 0

For integral β, discriminant must be perfect square:
D = p² + 4·444p = p² + 1776p = p(p + 1776)

For p = 37 (prime):
D = 37(1813) = 67081 = 259²

So β = (-37 ± 259)/2 = 111 or -148

Check: If β = 111, α = -148
Product: 111×(-148) = -16428 = -444×37 ✓

**Answer:** p = 37

---

## Problem 10: Inequality with Quadratic
**Question:** Find sum of all integral values of h for which x² + y² + xy + 1 ≥ h(x+y) holds ∀x,y ∈ R.

**Solution:**
Treat as quadratic in x:
x² + x(y-h) + (y² - hy + 1) ≥ 0 ∀x

For this: D ≤ 0
(y-h)² - 4(y² - hy + 1) ≤ 0
y² - 2hy + h² - 4y² + 4hy - 4 ≤ 0
-3y² + 2hy + h² - 4 ≤ 0
3y² - 2hy - h² + 4 ≥ 0 ∀y

For this: D ≤ 0
4h² - 12(-h² + 4) ≤ 0
4h² + 12h² - 48 ≤ 0
16h² ≤ 48
h² ≤ 3
-√3 ≤ h ≤ √3

Integers: -1, 0, 1

**Answer:** Sum = 0

---

## Problem 11: Relationship Between Roots
**Question:** If both roots of x² + px + q = 0 exceed k, what conditions must hold?

**Solution:**
Three conditions:
1. D ≥ 0: p² - 4q ≥ 0
2. Vertex x-coordinate > k: -p/(2) > k, so p < -2k
3. f(k) > 0: k² + pk + q > 0

**Answer:** D ≥ 0, -p/2 > k, f(k) > 0

---

## Problem 12: Symmetric Function
**Question:** If α, β are roots of x² - 6x - 2 = 0, find (a₁₀ - 2a₈)/(2a₉) where aₙ = αⁿ - βⁿ.

**Solution:**
α + β = 6, αβ = -2

Recurrence: aₙ = (α+β)aₙ₋₁ - αβ·aₙ₋₂ = 6aₙ₋₁ + 2aₙ₋₂

So: a₁₀ = 6a₉ + 2a₈

Therefore: (a₁₀ - 2a₈)/(2a₉) = (6a₉ + 2a₈ - 2a₈)/(2a₉) = 6a₉/(2a₉) = 3

**Answer:** 3

---

## Problem 13: Roots in AP
**Question:** If 2, 6 are roots of ax² + bx + 1 = 0, find equation whose roots are 1/(2a+b) and 1/(6a+b).

**Solution:**
From given equation:
2 + 6 = -b/a → b = -8a
2×6 = 1/a → a = 1/12, b = -2/3

2a + b = 1/6 - 2/3 = -1/2
6a + b = 1/2 - 2/3 = -1/6

New roots: 1/(-1/2) = -2 and 1/(-1/6) = -6

Equation: x² + 8x + 12 = 0

**Answer:** x² + 8x + 12 = 0

---

## Problem 14: Transformation of Roots
**Question:** If α, β are roots of px² + qx - r = 0 (p ≠ 0) and p, q, r are in AP, and 1/α + 1/β = 4, find |α - β|.

**Solution:**
1/α + 1/β = (α+β)/(αβ) = (-q/p)/(-r/p) = q/r = 4

Since p, q, r in AP: q = (p+r)/2

So: 2q = p + r and q/r = 4
From q = 4r and 2q = p + r:
8r = p + r
p = 7r

α + β = -q/p = -4r/(7r) = -4/7
αβ = -r/p = -r/(7r) = -1/7

|α - β| = √[(α+β)² - 4αβ] = √[16/49 + 4/7] = √[16/49 + 28/49] = √(44/49) = (2√11)/7

**Answer:** (2√11)/7

---

## Problem 15: Parametric Equation
**Question:** Let Pₙ = αⁿ + βⁿ where α, β are roots of some quadratic. If P₁₀ = 123, P₉ = 76, P₈ = 47, P₁ = 1, find equation with roots 1/α, 1/β.

**Solution:**
Recurrence: Pₙ = (α+β)Pₙ₋₁ - αβ·Pₙ₋₂

123 = (α+β)·76 - αβ·47
76 = (α+β)·47 - αβ·P₇

Also: P₁ = α + β = 1

From first equation:
123 = 76 - 47αβ
αβ = (76-123)/(-47) = 47/47 = -1

Equation with α, β: x² - x - 1 = 0

For roots 1/α, 1/β:
If y = 1/x, then x = 1/y
Substituting: 1/y² - 1/y - 1 = 0
Multiply by y²: 1 - y - y² = 0
y² + y - 1 = 0

**Answer:** x² + x - 1 = 0

---

## Problem 16: Cubic Reduction
**Question:** If α is root of 2x(2x+1) = 1, find the other root.

**Solution:**
4x² + 2x - 1 = 0

Product of roots: αβ = -1/4
If α is one root and β is other:
β = (-1/4)/α = -1/(4α)

**Answer:** -1/(4α)

---

## Problem 17: Absolute Value Equation
**Question:** Find sum of squares of roots of |x-2|² + |x-2| - 2 = 0 and x² - 2|x-3| - 5 = 0.

**Solution:**
First equation: Let y = |x-2|
y² + y - 2 = 0
(y+2)(y-1) = 0
y = 1 (y = -2 rejected)

|x-2| = 1
x = 3 or x = 1

Sum of squares: 9 + 1 = 10

Second equation: Two cases
Case 1: x ≥ 3: x² - 2(x-3) - 5 = 0
x² - 2x + 6 - 5 = 0
x² - 2x + 1 = 0
x = 1 (rejected as x ≥ 3)

Case 2: x < 3: x² + 2(x-3) - 5 = 0
x² + 2x - 11 = 0
x = (-2 ± √48)/2 = -1 ± 2√3

Sum of squares: (-1+2√3)² + (-1-2√3)² = (1-4√3+12) + (1+4√3+12) = 26

Total: 10 + 26 = 36

**Answer:** 36

---

## Problem 18: Exponential Quadratic
**Question:** Find sum of solutions of 8²ˣ - 16·8ˣ + 48 = 0.

**Solution:**
Let y = 8ˣ
y² - 16y + 48 = 0
(y-4)(y-12) = 0
y = 4 or y = 12

8ˣ = 4: x = log₈(4) = log₈(2²) = (2/3)
8ˣ = 12: x = log₈(12) = log₈(12)

Sum = (2/3) + log₈(12) = (2/3) + [log(12)/log(8)]
= (2/3) + [log(12)/(3log(2))]

Actually, we need numerical value.
8ˣ = 4 → 2³ˣ = 2² → x = 2/3
8ˣ = 12 → x = log(12)/log(8) ≈ 1.196

Sum ≈ 0.667 + 1.196 = 1.863

**Answer:** (2/3) + log₈(12)

---

## Problem 19: Location of Roots
**Question:** If both roots of x² + (p+2)x + (2p+9) = 0 are negative, find interval for p.

**Solution:**
Three conditions:
1. D ≥ 0: (p+2)² - 4(2p+9) ≥ 0
   p² + 4p + 4 - 8p - 36 ≥ 0
   p² - 4p - 32 ≥ 0
   (p-8)(p+4) ≥ 0
   p ≤ -4 or p ≥ 8

2. Sum < 0: -(p+2) < 0 → p > -2

3. Product > 0: 2p + 9 > 0 → p > -9/2

Intersection: p ≥ 8

**Answer:** p ∈ [8, ∞)

---

## Problem 20: Complex Solutions
**Question:** For equation (9/x - 9/√x + 2)(2/x - 7/√x + 3) = 0, find number of solutions.

**Solution:**
Either 9/x - 9/√x + 2 = 0 or 2/x - 7/√x + 3 = 0

First: Let y = 1/√x
9y² - 9y + 2 = 0
y = (9 ± √(81-72))/18 = (9 ± 3)/18
y = 2/3 or y = 1/3

Both positive, so 2 solutions for x.

Second: 2y² - 7y + 3 = 0
(2y-1)(y-3) = 0
y = 1/2 or y = 3

Both positive, so 2 more solutions.

Total: 4 solutions

**Answer:** 4