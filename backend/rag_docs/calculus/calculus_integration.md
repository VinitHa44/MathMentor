# Integration

## Definition

Integration is the reverse process of differentiation.

If F'(x) = f(x), then:
∫f(x)dx = F(x) + C

Where C is the constant of integration.

## Standard Integrals

### Algebraic Functions

∫xⁿ dx = x^(n+1)/(n+1) + C, for n ≠ -1

∫(1/x) dx = ln|x| + C

∫dx = x + C

∫k dx = kx + C, where k is constant

∫√x dx = (2/3)x^(3/2) + C

∫(1/√x) dx = 2√x + C

### Trigonometric Functions

∫sin(x) dx = -cos(x) + C

∫cos(x) dx = sin(x) + C

∫tan(x) dx = -ln|cos(x)| + C = ln|sec(x)| + C

∫cot(x) dx = ln|sin(x)| + C

∫sec(x) dx = ln|sec(x) + tan(x)| + C

∫cosec(x) dx = ln|cosec(x) - cot(x)| + C

∫sec²(x) dx = tan(x) + C

∫cosec²(x) dx = -cot(x) + C

∫sec(x)·tan(x) dx = sec(x) + C

∫cosec(x)·cot(x) dx = -cosec(x) + C

### Exponential Functions

∫eˣ dx = eˣ + C

∫aˣ dx = aˣ/ln(a) + C

∫e^(ax) dx = e^(ax)/a + C

### Inverse Trigonometric Forms

∫1/√(1-x²) dx = sin⁻¹(x) + C

∫-1/√(1-x²) dx = cos⁻¹(x) + C

∫1/(1+x²) dx = tan⁻¹(x) + C

∫-1/(1+x²) dx = cot⁻¹(x) + C

∫1/(x√(x²-1)) dx = sec⁻¹(x) + C

∫-1/(x√(x²-1)) dx = cosec⁻¹(x) + C

## Properties of Indefinite Integrals

∫[f(x) + g(x)] dx = ∫f(x) dx + ∫g(x) dx

∫k·f(x) dx = k·∫f(x) dx, where k is constant

d/dx[∫f(x) dx] = f(x)

∫[d/dx(f(x))] dx = f(x) + C

## Methods of Integration

### Substitution Method

For ∫f(g(x))·g'(x) dx:

Put u = g(x), then du = g'(x)dx

∫f(g(x))·g'(x) dx = ∫f(u) du

### Integration by Parts

∫u·v dx = u·∫v dx - ∫[du/dx·∫v dx] dx

Short form: ∫u dv = uv - ∫v du

**ILATE Rule for choosing u:**
- I = Inverse trigonometric
- L = Logarithmic
- A = Algebraic
- T = Trigonometric
- E = Exponential

Choose u in this priority order.

### Partial Fractions

For rational functions P(x)/Q(x) where degree(P) < degree(Q):

Decompose into simpler fractions based on factors of Q(x).

**Types:**

1. Linear factors: A/(x-a)
2. Repeated linear: A/(x-a) + B/(x-a)²
3. Quadratic: (Ax+B)/(x²+bx+c)
4. Repeated quadratic: similar expansion

## Special Integrals

### Form: ∫1/(ax²+bx+c) dx

Complete the square:
ax²+bx+c = a[(x+b/2a)² + (c/a - b²/4a²)]

Then use standard forms.

### Form: ∫1/√(ax²+bx+c) dx

Complete square and use:
∫1/√(x²+a²) dx = ln|x + √(x²+a²)| + C
∫1/√(x²-a²) dx = ln|x + √(x²-a²)| + C
∫1/√(a²-x²) dx = sin⁻¹(x/a) + C

### Form: ∫√(ax²+bx+c) dx

Complete square and use standard formulas or substitution.

### Form: ∫(px+q)/(ax²+bx+c) dx

Write px+q = A(d/dx(ax²+bx+c)) + B
= A(2ax+b) + B

Then integrate separately.

### Form: ∫(px+q)/√(ax²+bx+c) dx

Similar decomposition as above.

## Trigonometric Integrals

### ∫sinⁿ(x)·cosᵐ(x) dx

**If n is odd:** Put cos(x) = t
**If m is odd:** Put sin(x) = t
**If both even:** Use reduction formulas or half-angle identities

### ∫tanⁿ(x)·secᵐ(x) dx

**If n is odd:** Put sec(x) = t
**If m is even:** Put tan(x) = t

### Product of sines/cosines

Use: 2sin(A)cos(B) = sin(A+B) + sin(A-B)
2cos(A)cos(B) = cos(A+B) + cos(A-B)
2sin(A)sin(B) = cos(A-B) - cos(A+B)

## Reduction Formulas

For ∫sinⁿ(x) dx:
Iₙ = [-cos(x)·sinⁿ⁻¹(x)]/n + [(n-1)/n]·Iₙ₋₂

For ∫cosⁿ(x) dx:
Iₙ = [sin(x)·cosⁿ⁻¹(x)]/n + [(n-1)/n]·Iₙ₋₂

## Definite Integrals

∫ₐᵇ f(x) dx = F(b) - F(a)

Where F'(x) = f(x)

## Properties of Definite Integrals

∫ₐᵇ f(x) dx = -∫ᵇₐ f(x) dx

∫ₐᵃ f(x) dx = 0

∫ₐᵇ f(x) dx = ∫ₐᶜ f(x) dx + ∫ᶜᵇ f(x) dx

∫ₐᵇ f(x) dx = ∫ₐᵇ f(t) dt (dummy variable)

∫ₐᵇ f(x) dx = ∫ₐᵇ f(a+b-x) dx (King's Property)

∫₀ᵃ f(x) dx = ∫₀ᵃ f(a-x) dx

∫₋ₐᵃ f(x) dx = 2∫₀ᵃ f(x) dx, if f is even
∫₋ₐᵃ f(x) dx = 0, if f is odd

∫₀²ᵃ f(x) dx = ∫₀ᵃ f(x) dx + ∫₀ᵃ f(2a-x) dx

If f(2a-x) = f(x):
∫₀²ᵃ f(x) dx = 2∫₀ᵃ f(x) dx

If f(2a-x) = -f(x):
∫₀²ᵃ f(x) dx = 0

## Leibniz Rule

For differentiation under integral sign:

d/dx[∫ₐ₍ₓ₎^b₍ₓ₎ f(t,x) dt] = f(b(x),x)·b'(x) - f(a(x),x)·a'(x) + ∫ₐ₍ₓ₎^b₍ₓ₎ ∂f/∂x dt

## Walli's Formula

∫₀^(π/2) sinⁿ(x) dx = ∫₀^(π/2) cosⁿ(x) dx

= [(n-1)/n]·[(n-3)/(n-2)]·...·(1/2 or 2/3)·(π/2 or 1)

**If n is even:** ends with π/2
**If n is odd:** ends with 1

## Gamma Function

Γ(n) = ∫₀^∞ e^(-x)·x^(n-1) dx

Properties:
- Γ(n+1) = n·Γ(n)
- Γ(n) = (n-1)!, for positive integers
- Γ(1/2) = √π

## Important Results

∫e^x[f(x) + f'(x)] dx = e^x·f(x) + C

∫[f'(x)/f(x)] dx = ln|f(x)| + C

∫tan(x) dx = -ln|cos(x)| + C

∫sec(x) dx = ln|sec(x) + tan(x)| + C

## Common Mistakes to Avoid

- Forgetting constant of integration in indefinite integrals
- Wrong limits substitution in definite integrals
- Not checking continuity in definite integral range
- Incorrect application of integration by parts
- Wrong choice of substitution
- Sign errors in partial fractions