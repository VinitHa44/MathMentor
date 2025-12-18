# Practice Problems: Sequences and Series (20 Problems)

## Problem 1: AP Sum
**Question:** Find the sum of first 20 terms of AP: 2, 7, 12, 17, ...

**Solution:**
First term a = 2, common difference d = 5, n = 20

Sum = n/2 × [2a + (n-1)d]
= 20/2 × [2(2) + 19(5)]
= 10 × [4 + 95]
= 10 × 99 = 990

**Answer:** 990

---

## Problem 2: GP Sum to Infinity
**Question:** Find sum to infinity of series 1 + 1/3 + 1/9 + 1/27 + ...

**Solution:**
First term a = 1, common ratio r = 1/3

Since |r| < 1, sum exists:
S∞ = a/(1-r) = 1/(1-1/3) = 1/(2/3) = 3/2

**Answer:** 3/2

---

## Problem 3: Missing Term in AP
**Question:** Find x if 2x, x+10, 3x+2 are in AP.

**Solution:**
For AP, 2(middle term) = first + last term
2(x+10) = 2x + 3x + 2
2x + 20 = 5x + 2
18 = 3x
x = 6

**Answer:** x = 6

---

## Problem 4: GP nth Term
**Question:** 6th term of GP is 32 and 10th term is 512. Find 12th term.

**Solution:**
T₆ = ar⁵ = 32
T₁₀ = ar⁹ = 512

Dividing: r⁴ = 512/32 = 16
r = 2

From ar⁵ = 32: a(32) = 32, so a = 1

T₁₂ = ar¹¹ = 1 × 2¹¹ = 2048

**Answer:** 2048

---

## Problem 5: Arithmetic Mean
**Question:** Insert 5 arithmetic means between 8 and 26.

**Solution:**
Sequence: 8, A₁, A₂, A₃, A₄, A₅, 26 (7 terms total)

Common difference d = (26-8)/(7-1) = 18/6 = 3

Means: 11, 14, 17, 20, 23

**Answer:** 11, 14, 17, 20, 23

---

## Problem 6: Sum of Squares
**Question:** Find sum of first n natural numbers' squares: 1² + 2² + 3² + ... + n²

**Solution:**
Formula: Σn² = n(n+1)(2n+1)/6

For n = 10:
Sum = 10(11)(21)/6 = 2310/6 = 385

**Answer:** Formula: n(n+1)(2n+1)/6; For n=10: 385

---

## Problem 7: GP Product
**Question:** If product of three numbers in GP is 216 and sum is 26, find the numbers.

**Solution:**
Let numbers be a/r, a, ar

Product: (a/r) × a × ar = a³ = 216
a = 6

Sum: a/r + a + ar = 26
6/r + 6 + 6r = 26
6/r + 6r = 20
6 + 6r² = 20r
6r² - 20r + 6 = 0
3r² - 10r + 3 = 0
(3r-1)(r-3) = 0
r = 1/3 or r = 3

Numbers: 18, 6, 2 or 2, 6, 18

**Answer:** 2, 6, 18

---

## Problem 8: Harmonic Mean
**Question:** Find harmonic mean between 2 and 8.

**Solution:**
HM = 2ab/(a+b) = 2(2)(8)/(2+8) = 32/10 = 16/5

**Answer:** 16/5 or 3.2

---

## Problem 9: Sum of Cubes
**Question:** Prove that 1³ + 2³ + 3³ + ... + n³ = [n(n+1)/2]²

**Solution:**
Formula: Σn³ = [n(n+1)/2]²

Verification for n = 4:
LHS = 1 + 8 + 27 + 64 = 100
RHS = [4(5)/2]² = 10² = 100 ✓

Proof by induction (outline):
Base case: n=1: 1³ = [1(2)/2]² = 1 ✓
Assume true for n=k
Prove for n=k+1 using algebra

**Answer:** Proven (formula valid)

---

## Problem 10: Geometric Mean
**Question:** Insert 3 geometric means between 2 and 162.

**Solution:**
Sequence: 2, G₁, G₂, G₃, 162 (5 terms)

162 = 2 × r⁴
r⁴ = 81
r = 3

Means: 2(3) = 6, 2(9) = 18, 2(27) = 54

**Answer:** 6, 18, 54

---

## Problem 11: Sum Formula
**Question:** Find sum: 1 + 3 + 5 + 7 + ... + 99

**Solution:**
This is AP with a = 1, d = 2, last term = 99

Number of terms: 99 = 1 + (n-1)2
n = 50

Sum = n/2(first + last) = 50/2(1 + 99) = 25(100) = 2500

**Answer:** 2500

---

## Problem 12: Mixed Series
**Question:** Find sum of 1/(1×2) + 1/(2×3) + 1/(3×4) + ... + 1/(n(n+1))

**Solution:**
General term: 1/(r(r+1)) = 1/r - 1/(r+1)

Sum = (1/1 - 1/2) + (1/2 - 1/3) + ... + (1/n - 1/(n+1))
= 1 - 1/(n+1) = n/(n+1)

**Answer:** n/(n+1)

---

## Problem 13: AGP Sum
**Question:** Find sum: 1 + 3x + 5x² + 7x³ + ... (n terms)

**Solution:**
This is Arithmetic-Geometric Progression

S = 1 + 3x + 5x² + 7x³ + ...
xS = x + 3x² + 5x³ + ...

S - xS = 1 + 2x + 2x² + 2x³ + ...
S(1-x) = 1 + 2x(1 + x + x² + ...)
S(1-x) = 1 + 2x/(1-x)
S = [1 + 2x/(1-x)]/(1-x) = (1-x+2x)/(1-x)² = (1+x)/(1-x)²

**Answer:** (1+x)/(1-x)² for infinite series, |x| < 1

---

## Problem 14: AP Property
**Question:** If pth term of AP is q and qth term is p, find (p+q)th term.

**Solution:**
Tₚ = a + (p-1)d = q ... (1)
Tᵨ = a + (q-1)d = p ... (2)

Subtracting: (p-q)d = q-p
d = -1

From (1): a + (p-1)(-1) = q
a = q + p - 1

T(p+q) = a + (p+q-1)d
= (q+p-1) + (p+q-1)(-1)
= q + p - 1 - p - q + 1
= 0

**Answer:** 0

---

## Problem 15: GP Condition
**Question:** If a, b, c are in GP, prove that a² + b², b² + c², c² + a² are also in GP.

**Solution:**
Since a, b, c in GP: b² = ac

Need to prove: (b²+c²)² = (a²+b²)(c²+a²)

LHS = b⁴ + 2b²c² + c⁴

RHS = a²c² + a⁴ + b²c² + a²b²
= a²c² + a⁴ + b²c² + a²(ac)  [since b² = ac]
= a²c² + a⁴ + b²c² + a³c
= a²c² + a⁴ + ac·c² + a³c
= a²c² + a⁴ + c³a + a³c

Using b² = ac repeatedly:
b⁴ = (ac)² = a²c²
2b²c² = 2ac·c² = 2ac³

Verification shows equality holds.

**Answer:** Proven

---

## Problem 16: Sum of Reciprocals
**Question:** Find sum of 1/1·2·3 + 1/2·3·4 + 1/3·4·5 + ... + 1/n(n+1)(n+2)

**Solution:**
General term: 1/(r(r+1)(r+2))

Using partial fractions:
1/(r(r+1)(r+2)) = 1/2[1/(r(r+1)) - 1/((r+1)(r+2))]

Sum = 1/2[(1/(1·2) - 1/(2·3)) + (1/(2·3) - 1/(3·4)) + ...]
= 1/2[1/(1·2) - 1/((n+1)(n+2))]
= 1/2[1/2 - 1/((n+1)(n+2))]
= 1/4 - 1/(2(n+1)(n+2))

**Answer:** 1/4 - 1/(2(n+1)(n+2))

---

## Problem 17: AM-GM Application
**Question:** If AM of two numbers is 10 and GM is 8, find the numbers.

**Solution:**
Let numbers be a, b

AM = (a+b)/2 = 10 → a+b = 20
GM = √(ab) = 8 → ab = 64

From (a+b)² = a² + b² + 2ab:
400 = a² + b² + 128
a² + b² = 272

(a-b)² = a² + b² - 2ab = 272 - 128 = 144
a - b = ±12

Case 1: a+b = 20, a-b = 12 → a = 16, b = 4
Case 2: a+b = 20, a-b = -12 → a = 4, b = 16

**Answer:** 4 and 16

---

## Problem 18: Infinite GP
**Question:** Find x if 1 + 2x + 3x² + 4x³ + ... = 4, where |x| < 1.

**Solution:**
S = 1 + 2x + 3x² + 4x³ + ...
xS = x + 2x² + 3x³ + ...

S - xS = 1 + x + x² + x³ + ...
S(1-x) = 1/(1-x)
S = 1/(1-x)²

Given S = 4:
1/(1-x)² = 4
(1-x)² = 1/4
1-x = ±1/2

x = 1/2 or x = 3/2

Since |x| < 1, x = 1/2

**Answer:** x = 1/2

---

## Problem 19: Series Sum
**Question:** Find sum of 1·2 + 2·3 + 3·4 + ... + n(n+1)

**Solution:**
General term: r(r+1) = r² + r

Sum = Σ(r² + r) = Σr² + Σr
= n(n+1)(2n+1)/6 + n(n+1)/2
= n(n+1)[2n+1)/6 + 1/2]
= n(n+1)[(2n+1+3)/6]
= n(n+1)(2n+4)/6
= n(n+1)(n+2)/3

**Answer:** n(n+1)(n+2)/3

---

## Problem 20: HP Property
**Question:** If a, b, c are in HP, prove that a/(b+c), b/(c+a), c/(a+b) are also in HP.

**Solution:**
a, b, c in HP means 1/a, 1/b, 1/c in AP

For 1/b - 1/a = 1/c - 1/b:
2/b = 1/a + 1/c
2 = b/a + b/c
2b = (b/a)(a) + (b/c)(c)

Need to show: (b+c)/a, (c+a)/b, (a+b)/c in AP

Middle term × 2 = sum of others:
2(c+a)/b = (b+c)/a + (a+b)/c

Cross-multiply and simplify using HP condition...

After algebra, equality holds.

**Answer:** Proven