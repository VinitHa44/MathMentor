# Practice Problems: Derivatives (20 Problems)

## Problem 1: Power Rule
**Question:** Find dy/dx if y = x⁵ + 3x³ - 2x + 7

**Solution:**
dy/dx = 5x⁴ + 9x² - 2

**Answer:** 5x⁴ + 9x² - 2

---

## Problem 2: Product Rule
**Question:** Find derivative of f(x) = x²·sin(x)

**Solution:**
f'(x) = 2x·sin(x) + x²·cos(x)

**Answer:** 2x·sin(x) + x²·cos(x)

---

## Problem 3: Quotient Rule
**Question:** Differentiate y = (x² + 1)/(x - 1)

**Solution:**
dy/dx = [(2x)(x-1) - (x²+1)(1)]/(x-1)²
= [2x² - 2x - x² - 1]/(x-1)²
= (x² - 2x - 1)/(x-1)²

**Answer:** (x² - 2x - 1)/(x-1)²

---

## Problem 4: Chain Rule
**Question:** Find dy/dx if y = sin(x³)

**Solution:**
dy/dx = cos(x³)·3x² = 3x²·cos(x³)

**Answer:** 3x²·cos(x³)

---

## Problem 5: Logarithmic Differentiation
**Question:** Differentiate y = xˣ

**Solution:**
ln(y) = x·ln(x)
(1/y)·dy/dx = ln(x) + x·(1/x) = ln(x) + 1
dy/dx = y(ln(x) + 1) = xˣ(ln(x) + 1)

**Answer:** xˣ(ln(x) + 1)

---

## Problem 6: Implicit Differentiation
**Question:** Find dy/dx if x² + y² = 25

**Solution:**
2x + 2y·dy/dx = 0
dy/dx = -x/y

**Answer:** -x/y

---

## Problem 7: Parametric Form
**Question:** If x = a·cos(t), y = b·sin(t), find dy/dx

**Solution:**
dx/dt = -a·sin(t)
dy/dt = b·cos(t)

dy/dx = (dy/dt)/(dx/dt) = [b·cos(t)]/[-a·sin(t)] = -(b/a)·cot(t)

**Answer:** -(b/a)·cot(t)

---

## Problem 8: Inverse Function
**Question:** Find derivative of y = sin⁻¹(x)

**Solution:**
sin(y) = x
cos(y)·dy/dx = 1
dy/dx = 1/cos(y) = 1/√(1-sin²(y)) = 1/√(1-x²)

**Answer:** 1/√(1-x²)

---

## Problem 9: Second Derivative
**Question:** If y = eˣ·sin(x), find d²y/dx²

**Solution:**
dy/dx = eˣ·sin(x) + eˣ·cos(x) = eˣ(sin(x) + cos(x))

d²y/dx² = eˣ(sin(x) + cos(x)) + eˣ(cos(x) - sin(x))
= eˣ(2cos(x)) = 2eˣ·cos(x)

**Answer:** 2eˣ·cos(x)

---

## Problem 10: Exponential Chain
**Question:** Differentiate f(x) = e^(x²+3x)

**Solution:**
f'(x) = e^(x²+3x)·(2x + 3)

**Answer:** (2x + 3)·e^(x²+3x)

---

## Problem 11: Trigonometric Product
**Question:** Find d/dx[x·tan(x)]

**Solution:**
= tan(x) + x·sec²(x)

**Answer:** tan(x) + x·sec²(x)

---

## Problem 12: Composite Exponential
**Question:** Differentiate y = (x² + 1)^(3x)

**Solution:**
Take ln: ln(y) = 3x·ln(x² + 1)

(1/y)·dy/dx = 3·ln(x² + 1) + 3x·[2x/(x²+1)]

dy/dx = (x²+1)^(3x)·[3ln(x²+1) + 6x²/(x²+1)]

**Answer:** (x²+1)^(3x)·[3ln(x²+1) + 6x²/(x²+1)]

---

## Problem 13: Rational Power
**Question:** Find dy/dx if y = √[(x-1)/(x+1)]

**Solution:**
y = [(x-1)/(x+1)]^(1/2)

dy/dx = (1/2)·[(x-1)/(x+1)]^(-1/2)·[(x+1) - (x-1)]/(x+1)²

= (1/2)·√[(x+1)/(x-1)]·[2/(x+1)²]

= 1/[(x+1)^(3/2)·√(x-1)]

**Answer:** 1/[(x+1)^(3/2)·√(x-1)]

---

## Problem 14: Logarithmic Form
**Question:** Differentiate y = ln(x + √(x² + 1))

**Solution:**
dy/dx = [1 + x/√(x²+1)]/(x + √(x²+1))

= [√(x²+1) + x]/[(x + √(x²+1))·√(x²+1)]

= 1/√(x²+1)

**Answer:** 1/√(x²+1)

---

## Problem 15: Multiple Chain
**Question:** Find dy/dx if y = cos(sin(x²))

**Solution:**
dy/dx = -sin(sin(x²))·cos(x²)·2x

**Answer:** -2x·cos(x²)·sin(sin(x²))

---

## Problem 16: Tangent Line
**Question:** Find equation of tangent to y = x² at point (2, 4)

**Solution:**
dy/dx = 2x
At x = 2: slope = 4

Equation: y - 4 = 4(x - 2)
y = 4x - 4

**Answer:** y = 4x - 4

---

## Problem 17: Related Rates
**Question:** If radius of circle increases at 2 cm/s, find rate of area increase when r = 5 cm

**Solution:**
A = πr²
dA/dt = 2πr·dr/dt

At r = 5, dr/dt = 2:
dA/dt = 2π(5)(2) = 20π cm²/s

**Answer:** 20π cm²/s

---

## Problem 18: Mean Value Theorem
**Question:** Verify MVT for f(x) = x² on [1, 3]

**Solution:**
f(3) = 9, f(1) = 1
[f(3) - f(1)]/(3-1) = 8/2 = 4

f'(x) = 2x
f'(c) = 4 → c = 2

Since 1 < 2 < 3, MVT verified with c = 2

**Answer:** c = 2

---

## Problem 19: Higher Derivative
**Question:** Find 5th derivative of f(x) = x⁵ + 2x⁴ - 3x² + x

**Solution:**
f'(x) = 5x⁴ + 8x³ - 6x + 1
f''(x) = 20x³ + 24x² - 6
f'''(x) = 60x² + 48x
f⁽⁴⁾(x) = 120x + 48
f⁽⁵⁾(x) = 120

**Answer:** 120

---

## Problem 20: Implicit Complex
**Question:** Find dy/dx if x³ + y³ = 3xy

**Solution:**
3x² + 3y²·dy/dx = 3y + 3x·dy/dx
3y²·dy/dx - 3x·dy/dx = 3y - 3x²
dy/dx(y² - x) = y - x²
dy/dx = (y - x²)/(y² - x)

**Answer:** (y - x²)/(y² - x)