# Practice Problems: Integration (20 Problems)

## Problem 1: Power Rule
**Question:** Find ∫(3x² + 2x - 5)dx

**Solution:**
= 3(x³/3) + 2(x²/2) - 5x + C
= x³ + x² - 5x + C

**Answer:** x³ + x² - 5x + C

---

## Problem 2: Substitution
**Question:** Find ∫2x·cos(x²)dx

**Solution:**
Let u = x², du = 2x·dx

= ∫cos(u)du
= sin(u) + C
= sin(x²) + C

**Answer:** sin(x²) + C

---

## Problem 3: By Parts
**Question:** Find ∫x·eˣdx

**Solution:**
u = x, dv = eˣdx
du = dx, v = eˣ

= x·eˣ - ∫eˣdx
= x·eˣ - eˣ + C
= eˣ(x - 1) + C

**Answer:** eˣ(x - 1) + C

---

## Problem 4: Definite Integral
**Question:** Evaluate ∫₀¹ x²dx

**Solution:**
= [x³/3]₀¹
= 1/3 - 0
= 1/3

**Answer:** 1/3

---

## Problem 5: Trigonometric
**Question:** Find ∫sin²(x)dx

**Solution:**
Use: sin²(x) = (1 - cos(2x))/2

= ∫(1 - cos(2x))/2 dx
= (1/2)[x - sin(2x)/2] + C
= x/2 - sin(2x)/4 + C

**Answer:** x/2 - sin(2x)/4 + C

---

## Problem 6: Partial Fractions
**Question:** Find ∫dx/(x² - 1)

**Solution:**
1/(x² - 1) = 1/[(x-1)(x+1)]
= A/(x-1) + B/(x+1)

1 = A(x+1) + B(x-1)
x = 1: 1 = 2A → A = 1/2
x = -1: 1 = -2B → B = -1/2

= (1/2)∫[1/(x-1) - 1/(x+1)]dx
= (1/2)[ln|x-1| - ln|x+1|] + C
= (1/2)ln|(x-1)/(x+1)| + C

**Answer:** (1/2)ln|(x-1)/(x+1)| + C

---

## Problem 7: Exponential
**Question:** Find ∫e²ˣ·cos(x)dx

**Solution:**
Let I = ∫e²ˣ·cos(x)dx

By parts twice:
I = e²ˣ·cos(x)/2 + (1/2)∫e²ˣ·sin(x)dx
= e²ˣ·cos(x)/2 + e²ˣ·sin(x)/4 - (1/4)I

(5/4)I = e²ˣ[2cos(x) + sin(x)]/4
I = e²ˣ[2cos(x) + sin(x)]/5 + C

**Answer:** e²ˣ[2cos(x) + sin(x)]/5 + C

---

## Problem 8: Rational Function
**Question:** Find ∫(2x + 3)/(x² + 3x + 2)dx

**Solution:**
2x + 3 = A(d/dx)(x² + 3x + 2) + B
= A(2x + 3) + B

A = 1, B = 0

= ∫(2x + 3)/(x² + 3x + 2)dx
= ln|x² + 3x + 2| + C

**Answer:** ln|x² + 3x + 2| + C

---

## Problem 9: Square Root
**Question:** Find ∫dx/√(1 - x²)

**Solution:**
Standard integral:
= sin⁻¹(x) + C

**Answer:** sin⁻¹(x) + C

---

## Problem 10: Properties
**Question:** Evaluate ∫₀^π x·sin(x)dx

**Solution:**
By parts: u = x, dv = sin(x)dx
= -x·cos(x)|₀^π + ∫cos(x)dx
= -x·cos(x) + sin(x)|₀^π
= [-π·(-1) + 0] - [0 + 0]
= π

**Answer:** π

---

## Problem 11: Substitution Complex
**Question:** Find ∫tan(x)dx

**Solution:**
= ∫sin(x)/cos(x)dx

Let u = cos(x), du = -sin(x)dx

= -∫du/u
= -ln|u| + C
= -ln|cos(x)| + C
= ln|sec(x)| + C

**Answer:** ln|sec(x)| + C

---

## Problem 12: King's Property
**Question:** Evaluate ∫₀^(π/2) sin(x)/(sin(x) + cos(x))dx

**Solution:**
Let I = ∫₀^(π/2) sin(x)/(sin(x) + cos(x))dx

By King's property (a+b-x):
I = ∫₀^(π/2) cos(x)/(sin(x) + cos(x))dx

2I = ∫₀^(π/2) [sin(x) + cos(x)]/(sin(x) + cos(x))dx
= ∫₀^(π/2) 1·dx = π/2

I = π/4

**Answer:** π/4

---

## Problem 13: Logarithmic
**Question:** Find ∫ln(x)dx

**Solution:**
By parts: u = ln(x), dv = dx
du = dx/x, v = x

= x·ln(x) - ∫x·(1/x)dx
= x·ln(x) - ∫dx
= x·ln(x) - x + C

**Answer:** x·ln(x) - x + C

---

## Problem 14: Area Under Curve
**Question:** Find area between y = x² and x-axis from x = 0 to x = 2

**Solution:**
Area = ∫₀² x²dx
= [x³/3]₀²
= 8/3

**Answer:** 8/3

---

## Problem 15: Even Function
**Question:** Evaluate ∫₋₂² x²·cos(x)dx

**Solution:**
f(x) = x²·cos(x)
f(-x) = (-x)²·cos(-x) = x²·cos(x) = f(x)

Function is even:
= 2∫₀² x²·cos(x)dx

By parts (twice):
= 2[x²·sin(x) + 2x·cos(x) - 2sin(x)]₀²
= 2[4sin(2) + 4cos(2) - 2sin(2)]
= 2[2sin(2) + 4cos(2)]
= 4sin(2) + 8cos(2)

**Answer:** 4sin(2) + 8cos(2)

---

## Problem 16: Reciprocal
**Question:** Find ∫dx/(x² + 4)

**Solution:**
= ∫dx/[4(x²/4 + 1)]
= (1/4)∫dx/(x²/4 + 1)

Let u = x/2, du = dx/2

= (1/2)∫du/(u² + 1)
= (1/2)tan⁻¹(u) + C
= (1/2)tan⁻¹(x/2) + C

**Answer:** (1/2)tan⁻¹(x/2) + C

---

## Problem 17: Product Integration
**Question:** Find ∫x²·sin(x)dx

**Solution:**
By parts: u = x², dv = sin(x)dx
= -x²·cos(x) + ∫2x·cos(x)dx

Again by parts:
= -x²·cos(x) + 2[x·sin(x) + cos(x)] + C
= -x²·cos(x) + 2x·sin(x) + 2cos(x) + C

**Answer:** -x²·cos(x) + 2x·sin(x) + 2cos(x) + C

---

## Problem 18: Special Form
**Question:** Find ∫eˣ[f(x) + f'(x)]dx

**Solution:**
This is standard result:
= eˣ·f(x) + C

**Answer:** eˣ·f(x) + C

---

## Problem 19: Odd Function
**Question:** Evaluate ∫₋₁¹ x³·sin(x)dx

**Solution:**
f(x) = x³·sin(x)
f(-x) = (-x)³·sin(-x) = -x³·(-sin(x)) = x³·sin(x)

Wait: f(-x) = -x³·sin(x) = -f(x)

Function is odd:
∫₋₁¹ f(x)dx = 0

**Answer:** 0

---

## Problem 20: Reduction Formula
**Question:** Find ∫sin³(x)dx

**Solution:**
= ∫sin²(x)·sin(x)dx
= ∫(1 - cos²(x))·sin(x)dx

Let u = cos(x), du = -sin(x)dx

= -∫(1 - u²)du
= -[u - u³/3] + C
= -cos(x) + cos³(x)/3 + C

**Answer:** -cos(x) + cos³(x)/3 + C 