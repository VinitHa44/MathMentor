# Practice Problems: Complex Numbers (20 Problems)

## Problem 1: Basic Operations
**Question:** Find (3 + 4i) + (2 - 5i)

**Solution:**
= (3 + 2) + (4 - 5)i
= 5 - i

**Answer:** 5 - i

---

## Problem 2: Multiplication
**Question:** Find (2 + 3i)(1 - 2i)

**Solution:**
= 2(1) + 2(-2i) + 3i(1) + 3i(-2i)
= 2 - 4i + 3i - 6i²
= 2 - i - 6(-1)
= 2 - i + 6 = 8 - i

**Answer:** 8 - i

---

## Problem 3: Modulus
**Question:** Find |3 - 4i|

**Solution:**
|z| = √(3² + (-4)²)
= √(9 + 16)
= √25 = 5

**Answer:** 5

---

## Problem 4: Conjugate
**Question:** If z = 5 + 12i, find z·z̄

**Solution:**
z̄ = 5 - 12i
z·z̄ = (5 + 12i)(5 - 12i)
= 25 - (12i)²
= 25 - 144(-1)
= 25 + 144 = 169

Or simply: z·z̄ = |z|² = 169

**Answer:** 169

---

## Problem 5: Division
**Question:** Find (3 + 4i)/(1 + 2i)

**Solution:**
Multiply by conjugate:
= (3 + 4i)(1 - 2i)/[(1 + 2i)(1 - 2i)]
= (3 - 6i + 4i - 8i²)/(1 - 4i²)
= (3 - 2i + 8)/(1 + 4)
= (11 - 2i)/5 = 11/5 - 2i/5

**Answer:** 11/5 - 2i/5

---

## Problem 6: Argument
**Question:** Find argument of z = -1 + i

**Solution:**
tan(θ) = y/x = 1/(-1) = -1

Since z is in 2nd quadrant:
θ = π - π/4 = 3π/4

**Answer:** 3π/4

---

## Problem 7: Polar Form
**Question:** Express z = 1 + i√3 in polar form

**Solution:**
r = |z| = √(1² + (√3)²) = √4 = 2
θ = tan⁻¹(√3/1) = π/3

z = 2(cos(π/3) + i·sin(π/3))
Or: z = 2·e^(iπ/3)

**Answer:** 2(cos(π/3) + i·sin(π/3))

---

## Problem 8: De Moivre's Theorem
**Question:** Find (1 + i)⁸

**Solution:**
1 + i = √2(cos(π/4) + i·sin(π/4))

(1 + i)⁸ = (√2)⁸(cos(8π/4) + i·sin(8π/4))
= 16(cos(2π) + i·sin(2π))
= 16(1 + 0)
= 16

**Answer:** 16

---

## Problem 9: Cube Roots of Unity
**Question:** Find sum of all cube roots of unity

**Solution:**
Roots: 1, ω, ω²
where ω = e^(2πi/3) = (-1 + i√3)/2

Sum = 1 + ω + ω² = 0

**Answer:** 0

---

## Problem 10: Powers of i
**Question:** Find i⁴⁷

**Solution:**
i⁴⁷ = i⁴⁸⁻¹ = i⁴⁸·i⁻¹
= (i⁴)¹²·(1/i)
= 1¹²·(-i)
= -i

Or: 47 = 4(11) + 3, so i⁴⁷ = i³ = -i

**Answer:** -i

---

## Problem 11: Quadratic with Complex Roots
**Question:** If 2 + 3i is root of x² + px + q = 0 (p, q real), find p and q.

**Solution:**
Other root = 2 - 3i (conjugate)

Sum: (2 + 3i) + (2 - 3i) = 4 = -p
So p = -4

Product: (2 + 3i)(2 - 3i) = 4 + 9 = 13 = q

**Answer:** p = -4, q = 13

---

## Problem 12: Real Part
**Question:** If z = (1 + 2i)/(3 - i), find Re(z)

**Solution:**
z = (1 + 2i)(3 + i)/[(3 - i)(3 + i)]
= (3 + i + 6i + 2i²)/(9 + 1)
= (3 + 7i - 2)/10
= (1 + 7i)/10

Re(z) = 1/10

**Answer:** 1/10

---

## Problem 13: Square Root
**Question:** Find square root of 3 + 4i

**Solution:**
Let √(3 + 4i) = a + bi

Then: (a + bi)² = 3 + 4i
a² - b² + 2abi = 3 + 4i

a² - b² = 3 ... (1)
2ab = 4 → ab = 2 ... (2)

|3 + 4i| = 5, so a² + b² = 5 ... (3)

From (1) and (3):
2a² = 8 → a = ±2
b = ±1

**Answer:** ±(2 + i)

---

## Problem 14: Equation with Modulus
**Question:** Solve |z - 3| = |z - 3i|

**Solution:**
This represents perpendicular bisector of segment joining 3 and 3i.

Let z = x + iy:
√[(x-3)² + y²] = √[x² + (y-3)²]
(x-3)² + y² = x² + (y-3)²
x² - 6x + 9 + y² = x² + y² - 6y + 9
-6x = -6y
y = x

**Answer:** y = x (line through origin at 45°)

---

## Problem 15: nth Roots
**Question:** Find all 4th roots of 16

**Solution:**
16 = 16(cos(0) + i·sin(0))

4th roots: 16^(1/4)[cos(2πk/4) + i·sin(2πk/4)] for k = 0,1,2,3

k=0: 2(cos(0) + i·sin(0)) = 2
k=1: 2(cos(π/2) + i·sin(π/2)) = 2i
k=2: 2(cos(π) + i·sin(π)) = -2
k=3: 2(cos(3π/2) + i·sin(3π/2)) = -2i

**Answer:** 2, 2i, -2, -2i

---

## Problem 16: Complex Equation
**Question:** If z² + |z| = 0, find z

**Solution:**
Let z = x + iy
x² - y² + 2xyi + √(x² + y²) = 0

Equating real: x² - y² + √(x² + y²) = 0 ... (1)
Equating imaginary: 2xy = 0 ... (2)

From (2): x = 0 or y = 0

If x = 0: -y² + |y| = 0 → |y|(1 - |y|) = 0 → y = 0 or y = ±1
If y = 0: x² + |x| = 0 → |x|(|x| + 1) = 0 → x = 0

**Answer:** z = 0, i, -i

---

## Problem 17: Rotation
**Question:** Rotate z = 1 + i by 90° counterclockwise about origin

**Solution:**
Multiply by e^(iπ/2) = i

z' = i(1 + i) = i + i² = i - 1 = -1 + i

**Answer:** -1 + i

---

## Problem 18: Circle Equation
**Question:** Find locus of z if |z - 2 - 3i| = 5

**Solution:**
This is circle with center (2, 3) and radius 5

In Cartesian: (x - 2)² + (y - 3)² = 25

**Answer:** Circle centered at (2,3), radius 5

---

## Problem 19: Complex Product
**Question:** If z₁ = 2 + 3i and z₂ = 1 - i, find |z₁·z₂|

**Solution:**
|z₁·z₂| = |z₁|·|z₂|

|z₁| = √(4 + 9) = √13
|z₂| = √(1 + 1) = √2

|z₁·z₂| = √13·√2 = √26

**Answer:** √26

---

## Problem 20: Amplitude Addition
**Question:** If arg(z) = π/4 and |z| = 2, find z

**Solution:**
z = r(cos(θ) + i·sin(θ))
= 2(cos(π/4) + i·sin(π/4))
= 2(1/√2 + i/√2)
= √2 + i√2
= √2(1 + i)

**Answer:** √2(1 + i) or √2 + i√2