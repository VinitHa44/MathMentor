# Applications of Derivatives

## Rate of Change

If y = f(x), then dy/dx represents rate of change of y with respect to x.

### Average Rate of Change:
[f(x₂) - f(x₁)]/(x₂ - x₁)

### Instantaneous Rate of Change:
dy/dx = f'(x)

## Related Rates

When two or more quantities are related and changing with time:

If x and y are related by y = f(x), and both vary with time t:
dy/dt = (dy/dx)·(dx/dt)

## Tangent and Normal

### Equation of Tangent

At point (x₁,y₁) on curve y = f(x):

y - y₁ = f'(x₁)(x - x₁)

### Equation of Normal

At point (x₁,y₁):

y - y₁ = -1/f'(x₁)·(x - x₁)

(provided f'(x₁) ≠ 0)

### Angle of Intersection

Angle between two curves at their point of intersection:

tan(θ) = |m₁ - m₂|/(1 + m₁m₂|)

Where m₁ and m₂ are slopes of tangents.

### Orthogonal Curves:
m₁·m₂ = -1

## Length of Tangent, Normal, Subtangent, Subnormal

At point P(x₁,y₁) on curve y = f(x):

### Length of Tangent:
y₁√(1 + 1/m²) = |y₁|√(1 + [1/f'(x₁)]²)

### Length of Normal:
|y₁|√(1 + m²) = |y₁|√(1 + [f'(x₁)]²)

### Length of Subtangent:
|y₁/m| = |y₁/f'(x₁)|

### Length of Subnormal:
|y₁·m| = |y₁·f'(x₁)|

Where m = f'(x₁)

## Increasing and Decreasing Functions

For function f(x) on interval I:

### Increasing:
f'(x) > 0 for all x in I
(or f'(x) ≥ 0 with equality at isolated points)

### Decreasing:
f'(x) < 0 for all x in I
(or f'(x) ≤ 0 with equality at isolated points)

### Strictly Increasing:
f'(x) > 0 for all x in I

### Strictly Decreasing:
f'(x) < 0 for all x in I

## Maxima and Minima

### Critical Points

Points where f'(x) = 0 or f'(x) does not exist

### Local Maximum

f(c) is local maximum if:
f(c) ≥ f(x) for all x in some neighborhood of c

### Local Minimum

f(c) is local minimum if:
f(c) ≤ f(x) for all x in some neighborhood of c

## First Derivative Test

For critical point c where f'(c) = 0:

**Local Maximum:**
- f'(x) > 0 for x < c (increasing)
- f'(x) < 0 for x > c (decreasing)

**Local Minimum:**
- f'(x) < 0 for x < c (decreasing)
- f'(x) > 0 for x > c (increasing)

**Neither:**
- f'(x) has same sign on both sides

## Second Derivative Test

For critical point c where f'(c) = 0:

**If f''(c) > 0:** Local minimum at x = c

**If f''(c) < 0:** Local maximum at x = c

**If f''(c) = 0:** Test fails, use first derivative test

## Global (Absolute) Maximum and Minimum

On closed interval [a,b]:

1. Find all critical points in (a,b)
2. Evaluate f at critical points and endpoints
3. Largest value = absolute maximum
4. Smallest value = absolute minimum

## Concavity

### Concave Up:
f''(x) > 0 on interval
(curve bends upward)

### Concave Down:
f''(x) < 0 on interval
(curve bends downward)

### Point of Inflection

Point where concavity changes
Occurs where f''(x) = 0 and f''(x) changes sign

## Curve Sketching

To sketch y = f(x):

1. **Domain and Range:** Find where function is defined
2. **Intercepts:** x-intercepts (y=0), y-intercept (x=0)
3. **Symmetry:** Even (f(-x) = f(x)) or Odd (f(-x) = -f(x))
4. **Asymptotes:**
   - Vertical: lim(x→a) f(x) = ±∞
   - Horizontal: lim(x→±∞) f(x) = L
   - Oblique: y = mx + c
5. **Critical Points:** Solve f'(x) = 0
6. **Increasing/Decreasing:** Check sign of f'(x)
7. **Local Extrema:** Using first or second derivative test
8. **Concavity:** Check sign of f''(x)
9. **Inflection Points:** Where f''(x) = 0 and changes sign

## Mean Value Theorem (MVT)

If f is continuous on [a,b] and differentiable on (a,b), then:

∃ c ∈ (a,b) such that: f'(c) = [f(b) - f(a)]/(b - a)

**Geometric interpretation:** Tangent at c is parallel to chord AB

## Rolle's Theorem

Special case of MVT:

If f is continuous on [a,b], differentiable on (a,b), and f(a) = f(b), then:

∃ c ∈ (a,b) such that: f'(c) = 0

## Approximations

### Linear Approximation:
f(x) ≈ f(a) + f'(a)(x - a)

For x close to a

### Differential:
dy = f'(x)dx

Approximates actual change Δy for small Δx

### Newton's Method (Root Finding):

Iterative formula:
xₙ₊₁ = xₙ - f(xₙ)/f'(xₙ)

Converges to root of f(x) = 0

## Optimization Problems

To find maximum or minimum value:

1. Identify quantity to be optimized
2. Express it as function of one variable
3. Find domain of function
4. Find critical points
5. Use appropriate test to identify max/min
6. Check endpoints if applicable

### Common Problems:
- Maximum area/volume
- Minimum cost/distance
- Optimal dimensions

## Inequalities Using Derivatives

To prove f(x) ≥ g(x):

1. Let h(x) = f(x) - g(x)
2. Find minimum of h(x)
3. If min(h(x)) ≥ 0, inequality holds

## Higher Order Derivatives

### nth Derivative Test:

If f'(c) = f''(c) = ... = f⁽ⁿ⁻¹⁾(c) = 0 and f⁽ⁿ⁾(c) ≠ 0:

**If n is even:**
- f⁽ⁿ⁾(c) > 0: local minimum
- f⁽ⁿ⁾(c) < 0: local maximum

**If n is odd:**
- Point of inflection (not extremum)

## Important Results

### For polynomial:
Maximum number of turning points = n - 1 (for degree n)

### For continuous function on [a,b]:
At least one point where f'(c) = [f(b)-f(a)]/(b-a)

### Extreme Value Theorem:
Continuous function on closed interval attains maximum and minimum

## Common Mistakes to Avoid

- Not checking domain before finding derivatives
- Forgetting to check endpoints in closed intervals
- Assuming f'(c) = 0 always gives extremum
- Not verifying that critical points are in domain
- Wrong application of optimization constraints
- Sign errors in derivative calculations
- Forgetting to check second derivative test applicability

## Parametric Form

For parametric equations x = f(t), y = g(t):

dy/dx = (dy/dt)/(dx/dt)

d²y/dx² = [d/dt(dy/dx)]/(dx/dt)

## Important Inequalities

**AM-GM Inequality (using calculus):**
For positive numbers a₁, a₂, ..., aₙ:
(a₁ + a₂ + ... + aₙ)/n ≥ (a₁·a₂·...·aₙ)^(1/n)

Can be proved using calculus optimization

## Special Techniques

### Lagrange Multipliers (basic):
For optimization with constraints, convert to single variable using constraint

### Implicit Differentiation:
For curves not explicitly y = f(x), differentiate both sides with respect to x

## Practical Applications

- Velocity and acceleration (motion)
- Marginal cost and revenue (economics)
- Population growth rates (biology)
- Reaction rates (chemistry)
- Electric current (physics)