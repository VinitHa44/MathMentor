# Practice Problems: Binomial Theorem (20 Problems)

## Problem 1: Specific Term
**Question:** Find 6th term in expansion of (2x - 3y)¹⁰

**Solution:**
T₆ = T₅₊₁ = ¹⁰C₅(2x)⁵(-3y)⁵
= 252 × 32x⁵ × (-243)y⁵
= 252 × 32 × (-243) × x⁵y⁵
= -1,959,552x⁵y⁵

**Answer:** -1,959,552x⁵y⁵

---

## Problem 2: Middle Term
**Question:** Find middle term in expansion of (x + 2)⁸

**Solution:**
n = 8 (even), middle term = (8/2 + 1)th = 5th term

T₅ = ⁸C₄ × x⁴ × 2⁴
= 70 × 16x⁴
= 1120x⁴

**Answer:** 1120x⁴

---

## Problem 3: Coefficient Sum
**Question:** Find sum of all coefficients in (2x + 3y)⁷

**Solution:**
Put x = 1, y = 1:
Sum = (2 + 3)⁷ = 5⁷ = 78,125

**Answer:** 78,125

---

## Problem 4: Independent Term
**Question:** Find term independent of x in (x² - 1/x)⁹

**Solution:**
General term: Tᵣ₊₁ = ⁹Cᵣ(x²)⁹⁻ʳ(-1/x)ʳ
= ⁹Cᵣ × x¹⁸⁻²ʳ × (-1)ʳ × x⁻ʳ
= ⁹Cᵣ × (-1)ʳ × x¹⁸⁻³ʳ

For x⁰: 18 - 3r = 0, r = 6

T₇ = ⁹C₆ × (-1)⁶ = 84 × 1 = 84

**Answer:** 84

---

## Problem 5: Ratio of Coefficients
**Question:** If ratio of 5th term to 3rd term in (a+b)ⁿ is 5:3, find n.

**Solution:**
T₅/T₃ = [ⁿC₄aⁿ⁻⁴b⁴]/[ⁿC₂aⁿ⁻²b²] = 5/3

ⁿC₄/ⁿC₂ × b²/a² = 5/3

For a = b:
ⁿC₄/ⁿC₂ = 5/3

[n!/(4!(n-4)!)]/[n!/(2!(n-2)!)] = 5/3
[(n-2)!×2!]/[(n-4)!×4!] = 5/3
[(n-2)(n-3)]/12 = 5/3
(n-2)(n-3) = 20
n² - 5n + 6 = 20
n² - 5n - 14 = 0
(n-7)(n+2) = 0

n = 7 (n > 0)

**Answer:** n = 7

---

## Problem 6: Greatest Coefficient
**Question:** Find greatest coefficient in (1+x)¹⁰

**Solution:**
n = 10 (even)
Greatest coefficient = ¹⁰C₅ = 252

**Answer:** 252

---

## Problem 7: Binomial Expansion
**Question:** Find coefficient of x⁷ in (1+x)¹⁰ + (1+x)¹¹

**Solution:**
Coefficient = ¹⁰C₇ + ¹¹C₇
= ¹⁰C₃ + ¹¹C₄ 
= 120 + 330 = 450

**Answer:** 450

---

## Problem 8: Sum with Alternating Signs
**Question:** Find value of ⁵C₀ - ⁵C₁ + ⁵C₂ - ⁵C₃ + ⁵C₄ - ⁵C₅

**Solution:**
Put x = -1 in (1+x)⁵:
(1-1)⁵ = 0

**Answer:** 0

---

## Problem 9: Specific Power
**Question:** Find coefficient of x⁵⁰ in (1+x)¹⁰⁰⁰

**Solution:**
¹⁰⁰⁰C₅₀

**Answer:** ¹⁰⁰⁰C₅₀ (exact numeric value too large)

---

## Problem 10: Greatest Term
**Question:** Find numerically greatest term in expansion of (2 + 3x)⁹ when x = 3/2

**Solution:**
For greatest term, compare ratio:
Tᵣ₊₁/Tᵣ = [(9-r+1)/r] × (3x/2)

At x = 3/2: = [(10-r)/r] × (9/4)

Set ≥ 1: (10-r)(9/4) ≥ r
90 - 9r ≥ 4r
90 ≥ 13r
r ≤ 6.9

So r = 6 gives greatest term (T₇)

T₇ = ⁹C₆ × 2³ × (3×3/2)⁶
= 84 × 8 × (9/2)⁶

**Answer:** T₇ is greatest (exact value requires calculation)

---

## Problem 11: Even Coefficient Sum
**Question:** Find sum of coefficients of even powers of x in (1+x+x²+x³)⁵

**Solution:**
Let P(x) = (1+x+x²+x³)⁵
P(1) = sum of all coefficients = 4⁵ = 1024
P(-1) = sum with alternating signs

Even terms sum = [P(1) + P(-1)]/2
P(-1) = (1-1+1-1)⁵ = 0

Sum = (1024 + 0)/2 = 512

**Answer:** 512

---

## Problem 12: Multinomial
**Question:** Find coefficient of x²y³z in (x+y+z)⁶

**Solution:**
Coefficient = 6!/(2!×3!×1!) = 720/(2×6×1) = 60

**Answer:** 60

---

## Problem 13: Pascal's Triangle
**Question:** What is 4th element in 7th row of Pascal's triangle? (0-indexed)

**Solution:**
7th row (n=7), 4th element (r=4):
⁷C₄ = 7!/(4!×3!) = 35

**Answer:** 35

---

## Problem 14: Divisibility
**Question:** Find remainder when 2²⁰ is divided by 17.

**Solution:**
2²⁰ = (2⁴)⁵ = 16⁵
= (17-1)⁵
= ⁵C₀(17)⁵ - ⁵C₁(17)⁴ + ... - ⁵C₅

All terms divisible by 17 except last:
Remainder = (-1)⁵ = -1 ≡ 16 (mod 17)

**Answer:** 16

---

## Problem 15: Approximation
**Question:** Using binomial theorem, find approximate value of (1.01)⁵

**Solution:**
(1 + 0.01)⁵ ≈ 1 + 5(0.01) + 10(0.01)²
≈ 1 + 0.05 + 0.001
≈ 1.051

**Answer:** ≈ 1.051

---

## Problem 16: Rational Index
**Question:** Find first three terms of (1+x)⁻²

**Solution:**
Using general binomial:
(1+x)⁻² = 1 + (-2)x + [(-2)(-3)/2!]x²
= 1 - 2x + 3x²

**Answer:** 1 - 2x + 3x²

---

## Problem 17: Coefficient Relation
**Question:** If coefficients of x⁷ and x⁸ in (2+x/3)ⁿ are equal, find n.

**Solution:**
ⁿC₇(2)ⁿ⁻⁷(1/3)⁷ = ⁿC₈(2)ⁿ⁻⁸(1/3)⁸

ⁿC₇ × 2ⁿ⁻⁷/(3⁷) = ⁿC₈ × 2ⁿ⁻⁸/(3⁸)

ⁿC₇ × 2 × 3 = ⁿC₈
6 × ⁿC₇ = ⁿC₈

6 = ⁿC₈/ⁿC₇ = (n-7)/8

48 = n - 7
n = 55

**Answer:** n = 55

---

## Problem 18: Sum of Products
**Question:** Find ⁿC₀² + ⁿC₁² + ⁿC₂² + ... + ⁿCₙ²

**Solution:**
This equals coefficient of xⁿ in:
(1+x)ⁿ × (1+x)ⁿ = (1+x)²ⁿ

Coefficient of xⁿ in (1+x)²ⁿ = ²ⁿCₙ

**Answer:** ²ⁿCₙ

---

## Problem 19: Alternating Sum
**Question:** Prove ⁿC₁ - 2·ⁿC₂ + 3·ⁿC₃ - ... + (-1)ⁿ⁻¹n·ⁿCₙ = 0

**Solution:**
Consider (1-x)ⁿ = Σ(-1)ʳ ⁿCᵣxʳ

Differentiate:
n(1-x)ⁿ⁻¹(-1) = Σ(-1)ʳ r·ⁿCᵣxʳ⁻¹

Put x = 1:
0 = Σ(-1)ʳ r·ⁿCᵣ

**Answer:** Proven

---

## Problem 20: Complex Application
**Question:** Find coefficient of x⁴ in expansion of (1+x-2x²)⁵

**Solution:**
(1+x-2x²)⁵ = [(1+x)(1-2x)]⁵
= (1+x)⁵(1-2x)⁵

Coefficient of x⁴:
= ⁵C₀×coeff of x⁴ in (1-2x)⁵ + ⁵C₁×coeff of x³ in (1-2x)⁵ + ...

= 1×⁵C₄(-2)⁴ + 5×⁵C₃(-2)³ + 10×⁵C₂(-2)² + 10×⁵C₁(-2)¹ + 5×⁵C₀
= 80 - 400 + 400 - 100 + 5
= -15

**Answer:** -15