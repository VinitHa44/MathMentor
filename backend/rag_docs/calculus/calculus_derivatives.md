# Derivatives

## Definition

The derivative of f(x) at x = a is:

f'(a) = lim(h→0) [f(a+h) - f(a)]/h

Or equivalently:

f'(x) = lim(h→0) [f(x+h) - f(x)]/h

## Notations

f'(x), dy/dx, df/dx, Df(x), d/dx[f(x)]

## Fundamental Rules

### Constant Rule
d/dx[c] = 0, where c is constant

### Power Rule
d/dx[xⁿ] = n·xⁿ⁻¹

### Constant Multiple Rule
d/dx[c·f(x)] = c·f'(x)

### Sum/Difference Rule
d/dx[f(x) ± g(x)] = f'(x) ± g'(x)

## Product Rule

d/dx[f(x)·g(x)] = f'(x)·g(x) + f(x)·g'(x)

Short form: (uv)' = u'v + uv'

### For three functions:
d/dx[uvw] = u'vw + uv'w + uvw'

## Quotient Rule

d/dx[f(x)/g(x)] = [f'(x)·g(x) - f(x)·g'(x)]/[g(x)]²

Short form: (u/v)' = (u'v - uv')/v²

## Chain Rule

If y = f(g(x)), then:

dy/dx = f'(g(x))·g'(x)

Or: dy/dx = (dy/du)·(du/dx) where u = g(x)

## Standard Derivatives

### Algebraic Functions

d/dx[xⁿ] = n·xⁿ⁻¹

d/dx[√x] = 1/(2√x)

d/dx[1/x] = -1/x²

d/dx[c] = 0

### Trigonometric Functions

d/dx[sin(x)] = cos(x)

d/dx[cos(x)] = -sin(x)

d/dx[tan(x)] = sec²(x)

d/dx[cot(x)] = -cosec²(x)

d/dx[sec(x)] = sec(x)·tan(x)

d/dx[cosec(x)] = -cosec(x)·cot(x)

### Inverse Trigonometric Functions

d/dx[sin⁻¹(x)] = 1/√(1-x²), for |x| < 1

d/dx[cos⁻¹(x)] = -1/√(1-x²), for |x| < 1

d/dx[tan⁻¹(x)] = 1/(1+x²)

d/dx[cot⁻¹(x)] = -1/(1+x²)

d/dx[sec⁻¹(x)] = 1/(|x|√(x²-1)), for |x| > 1

d/dx[cosec⁻¹(x)] = -1/(|x|√(x²-1)), for |x| > 1

### Exponential Functions

d/dx[eˣ] = eˣ

d/dx[aˣ] = aˣ·ln(a)

d/dx[e^(f(x))] = e^(f(x))·f'(x)

### Logarithmic Functions

d/dx[ln(x)] = 1/x, for x > 0

d/dx[log_a(x)] = 1/(x·ln(a))

d/dx[ln|x|] = 1/x

d/dx[ln(f(x))] = f'(x)/f(x)

## Logarithmic Differentiation

For y = [f(x)]^g(x) or products/quotients of many functions:

1. Take ln of both sides: ln(y) = g(x)·ln(f(x))
2. Differentiate both sides: (1/y)·(dy/dx) = ...
3. Solve for dy/dx: dy/dx = y·[...]

Useful when:
- Variable in both base and exponent
- Product of many functions
- Quotient of many functions

## Implicit Differentiation

For equations where y is not explicitly expressed in terms of x:

1. Differentiate both sides with respect to x
2. Use chain rule: d/dx[f(y)] = f'(y)·(dy/dx)
3. Collect all dy/dx terms
4. Solve for dy/dx

## Parametric Differentiation

If x = f(t) and y = g(t), then:

dy/dx = (dy/dt)/(dx/dt)

Second derivative:

d²y/dx² = d/dx[dy/dx] = [d/dt(dy/dx)]/(dx/dt)

## Higher Order Derivatives

### Notation
f''(x), d²y/dx², D²f(x)

f'''(x), d³y/dx³, D³f(x)

fⁿ(x), dⁿy/dxⁿ, Dⁿf(x)

### Leibniz Theorem

nth derivative of product:

(uv)ⁿ = Σ(k=0 to n) [ⁿCₖ·u^(n-k)·v^k]

Where u^k means kth derivative of u.

## Derivatives of Special Functions

### Absolute Value
d/dx[|x|] = x/|x| = { 1 if x > 0; -1 if x < 0; undefined at x = 0 }

### Signum Function
sgn(x) = { 1 if x > 0; 0 if x = 0; -1 if x < 0 }
Not differentiable at x = 0

### Greatest Integer Function
[x] is not differentiable at integer points

## Derivative of Inverse Function

If y = f(x) and x = f⁻¹(y), then:

dx/dy = 1/(dy/dx)

Or: (f⁻¹)'(y) = 1/f'(x)

## Useful Derivative Formulas

d/dx[x^x] = x^x(1 + ln(x))

d/dx[x^(1/x)] = x^(1/x)·(1 - ln(x))/x²

d/dx[a^(x^n)] = a^(x^n)·x^(n-1)·n·ln(a)

d/dx[e^(x²)] = 2x·e^(x²)

d/dx[ln(ln(x))] = 1/(x·ln(x))

d/dx[√(1-x²)] = -x/√(1-x²)

## Mean Value Theorem (MVT)

If f is continuous on [a,b] and differentiable on (a,b), then there exists c in (a,b) such that:

f'(c) = [f(b) - f(a)]/(b - a)

## Rolle's Theorem

If f is continuous on [a,b], differentiable on (a,b), and f(a) = f(b), then there exists c in (a,b) such that:

f'(c) = 0

## L'Hôpital's Rule

For limits of form 0/0 or ∞/∞:

lim(x→a) f(x)/g(x) = lim(x→a) f'(x)/g'(x)

## Partial Derivatives

For z = f(x,y):

∂z/∂x = derivative treating y as constant

∂z/∂y = derivative treating x as constant

## Common Mistakes to Avoid

- Forgetting chain rule when differentiating composite functions
- Wrong application of product/quotient rule
- Not using logarithmic differentiation for complex expressions
- Sign errors in trigonometric derivatives
- Forgetting absolute value in domain restrictions
- Not checking differentiability at corner points

## Important Results

If f(x) is differentiable at x = a:
- f(x) is continuous at x = a
- But continuity doesn't imply differentiability

f'(x) = 0 at local maxima and minima (critical points)

If f'(x) > 0 on interval, f is increasing
If f'(x) < 0 on interval, f is decreasing