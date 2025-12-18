# Practice Problems: Applications of Derivatives (20 Problems)

## Problem 1: Rate of Change
**Question:** If radius of circle increases at 2 cm/s, find rate of increase of area when r = 5 cm

**Solution:**
A = πr²
dA/dt = 2πr·dr/dt

At r = 5, dr/dt = 2:
dA/dt = 2π(5)(2) = 20π cm²/s

**Answer:** 20π cm²/s

---

## Problem 2: Tangent Equation
**Question:** Find equation of tangent to y = x³ at x = 2

**Solution:**
At x = 2: y = 8

dy/dx = 3x² = 12 at x = 2

Tangent: y - 8 = 12(x - 2)
y = 12x - 16

**Answer:** y = 12x - 16

---

## Problem 3: Normal Equation
**Question:** Find equation of normal to y = x² + 3x + 1 at (1, 5)

**Solution:**
dy/dx = 2x + 3 = 5 at x = 1

Slope of normal = -1/5

Normal: y - 5 = (-1/5)(x - 1)
5y - 25 = -x + 1
x + 5y = 26

**Answer:** x + 5y = 26

---

## Problem 4: Increasing Function
**Question:** Find intervals where f(x) = x³ - 3x² + 4 is increasing

**Solution:**
f'(x) = 3x² - 6x = 3x(x - 2)

f'(x) > 0 when x < 0 or x > 2

**Answer:** (-∞, 0) ∪ (2, ∞)

---

## Problem 5: Critical Points
**Question:** Find critical points of f(x) = x³ - 6x² + 9x + 1

**Solution:**
f'(x) = 3x² - 12x + 9 = 3(x² - 4x + 3)
= 3(x - 1)(x - 3)

Critical points: x = 1, 3

**Answer:** x = 1, 3

---

## Problem 6: Local Maximum
**Question:** Find local maximum of f(x) = x³ - 3x² + 2

**Solution:**
f'(x) = 3x² - 6x = 3x(x - 2)
f''(x) = 6x - 6

At x = 0: f''(0) = -6 < 0 → local maximum
f(0) = 2

**Answer:** Local maximum at x = 0, value = 2

---

## Problem 7: Local Minimum
**Question:** Find local minimum of f(x) = x³ - 3x² + 2

**Solution:**
Critical points: x = 0, 2

At x = 2: f''(2) = 6 > 0 → local minimum
f(2) = 8 - 12 + 2 = -2

**Answer:** Local minimum at x = 2, value = -2

---

## Problem 8: Absolute Extrema
**Question:** Find absolute maximum and minimum of f(x) = x³ - 3x on [-2, 3]

**Solution:**
f'(x) = 3x² - 3 = 3(x² - 1)
Critical points: x = ±1

Check values:
f(-2) = -8 + 6 = -2
f(-1) = -1 + 3 = 2
f(1) = 1 - 3 = -2
f(3) = 27 - 9 = 18

**Answer:** Max = 18 at x = 3, Min = -2 at x = -2, 1

---

## Problem 9: Point of Inflection
**Question:** Find point of inflection of f(x) = x³ - 3x + 2

**Solution:**
f'(x) = 3x² - 3
f''(x) = 6x

f''(x) = 0 at x = 0

Check sign change: f''(x) changes from negative to positive

Point of inflection: (0, f(0)) = (0, 2)

**Answer:** (0, 2)

---

## Problem 10: Related Rates - Ladder
**Question:** 5m ladder against wall slides down at 2 m/s. How fast is top moving when bottom is 3m from wall?

**Solution:**
x² + y² = 25

At x = 3: y = 4

Differentiate: 2x·dx/dt + 2y·dy/dt = 0

3(2) + 4·dy/dt = 0
dy/dt = -3/2 m/s

**Answer:** -3/2 m/s (moving down)

---

## Problem 11: Optimization - Rectangle
**Question:** Find dimensions of rectangle with perimeter 20 and maximum area

**Solution:**
Perimeter: 2l + 2w = 20 → l + w = 10

Area: A = lw = l(10 - l) = 10l - l²

dA/dl = 10 - 2l = 0
l = 5, w = 5

**Answer:** 5 × 5 (square)

---

## Problem 12: Approximation
**Question:** Using differentials, approximate √26

**Solution:**
f(x) = √x, x = 25, dx = 1

f'(x) = 1/(2√x)

√26 ≈ √25 + f'(25)·1
≈ 5 + 1/10 = 5.1

**Answer:** ≈ 5.1

---

## Problem 13: Angle of Intersection
**Question:** Find angle between curves y = x² and y = 4 - x² at intersection

**Solution:**
Intersection: x² = 4 - x²
x = ±√2

At x = √2:
Curve 1: dy/dx = 2x = 2√2
Curve 2: dy/dx = -2x = -2√2

tan(θ) = |m₁ - m₂|/|1 + m₁m₂|
= |2√2 + 2√2|/|1 - 8|
= 4√2/7

**Answer:** tan⁻¹(4√2/7)

---

## Problem 14: Mean Value Theorem
**Question:** Verify MVT for f(x) = x² - 4x on [1, 4]

**Solution:**
f(4) = 0, f(1) = -3

[f(4) - f(1)]/(4 - 1) = 3/3 = 1

f'(x) = 2x - 4 = 1
x = 5/2 ∈ (1, 4) ✓

**Answer:** c = 5/2

---

## Problem 15: Rolle's Theorem
**Question:** Verify Rolle's theorem for f(x) = x² - 5x + 6 on [2, 3]

**Solution:**
f(2) = 4 - 10 + 6 = 0
f(3) = 9 - 15 + 6 = 0

f'(x) = 2x - 5 = 0
x = 5/2 ∈ (2, 3) ✓

**Answer:** c = 5/2

---

## Problem 16: Optimization - Cylinder
**Question:** Find dimensions of cylinder with volume 100π and minimum surface area

**Solution:**
V = πr²h = 100π → h = 100/r²

S = 2πr² + 2πrh = 2πr² + 200π/r

dS/dr = 4πr - 200π/r² = 0
4r³ = 200
r³ = 50
r = ∛50

h = 100/50 = 2∛50

**Answer:** r = ∛50, h = 2∛50

---

## Problem 17: Maximum Distance
**Question:** Find point on y = x² closest to (0, 2)

**Solution:**
Distance squared: D² = x² + (x² - 2)²
= x² + x⁴ - 4x² + 4
= x⁴ - 3x² + 4

d(D²)/dx = 4x³ - 6x = 2x(2x² - 3) = 0
x = 0 or x = ±√(3/2)

Check: x = 0 gives D² = 4
x = √(3/2) gives smaller D²

**Answer:** (±√(3/2), 3/2)

---

## Problem 18: Related Rates - Cone
**Question:** Water pours into cone (r = h/2) at 3 cm³/s. Find rate of height increase when h = 6 cm

**Solution:**
V = (1/3)πr²h = (1/3)π(h/2)²h = πh³/12

dV/dt = πh²/4·dh/dt = 3

At h = 6:
π(36)/4·dh/dt = 3
dh/dt = 12/(36π) = 1/(3π) cm/s

**Answer:** 1/(3π) cm/s

---

## Problem 19: Concavity
**Question:** Find intervals where f(x) = x⁴ - 4x³ is concave up

**Solution:**
f'(x) = 4x³ - 12x²
f''(x) = 12x² - 24x = 12x(x - 2)

f''(x) > 0 when x < 0 or x > 2

**Answer:** (-∞, 0) ∪ (2, ∞)

---

## Problem 20: Optimization - Box
**Question:** Square sheet metal 12×12 cm. Cut squares from corners and fold to make box. Find maximum volume.

**Solution:**
Let x = side of cut square
V = x(12-2x)²

dV/dx = (12-2x)² + x·2(12-2x)(-2)
= (12-2x)[(12-2x) - 4x]
= (12-2x)(12-6x)

dV/dx = 0: x = 2 or x = 6

Check: x = 2 gives V = 2(8)² = 128 cm³

**Answer:** x = 2 cm, Max volume = 128 cm³