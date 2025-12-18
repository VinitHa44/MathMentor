# Limits

## Definition

lim(x→a) f(x) = L means that f(x) can be made arbitrarily close to L by taking x sufficiently close to a.

## Left and Right Hand Limits

### Left Hand Limit (LHL)
lim(x→a⁻) f(x) = value approached as x approaches a from left

### Right Hand Limit (RHL)
lim(x→a⁺) f(x) = value approached as x approaches a from right

### Existence of Limit
lim(x→a) f(x) exists if and only if:
lim(x→a⁻) f(x) = lim(x→a⁺) f(x)

## Fundamental Theorems on Limits

If lim(x→a) f(x) = l and lim(x→a) g(x) = m, then:

lim(x→a) [f(x) + g(x)] = l + m

lim(x→a) [f(x) - g(x)] = l - m

lim(x→a) [f(x) · g(x)] = l · m

lim(x→a) [f(x) / g(x)] = l/m, provided m ≠ 0

lim(x→a) [c · f(x)] = c · l, where c is constant

lim(x→a) [f(x)]ⁿ = lⁿ

## Standard Limits (Must Remember)

### Trigonometric Limits

lim(x→0) sin(x)/x = 1

lim(x→0) tan(x)/x = 1

lim(x→0) (1 - cos(x))/x = 0

lim(x→0) (1 - cos(x))/x² = 1/2

lim(x→0) sin⁻¹(x)/x = 1

lim(x→0) tan⁻¹(x)/x = 1

lim(x→0) sin(ax)/sin(bx) = a/b

lim(x→0) tan(ax)/tan(bx) = a/b

lim(x→0) sin(ax)/bx = a/b

### Exponential and Logarithmic Limits

lim(x→0) (eˣ - 1)/x = 1

lim(x→0) (aˣ - 1)/x = ln(a)

lim(x→0) ln(1 + x)/x = 1

lim(x→0) (eˣ - e⁻ˣ)/x = 2

lim(x→∞) (1 + 1/x)ˣ = e

lim(x→0) (1 + x)^(1/x) = e

lim(x→a) [xⁿ - aⁿ]/[x - a] = n·aⁿ⁻¹

### Algebraic Limits

lim(x→∞) (xⁿ/eˣ) = 0, for any n

lim(x→∞) (ln(x)/xⁿ) = 0, for any n > 0

## Indeterminate Forms

Common indeterminate forms:
- 0/0
- ∞/∞
- 0 × ∞
- ∞ - ∞
- 0⁰
- 1^∞
- ∞⁰

## L'Hôpital's Rule

If lim(x→a) f(x)/g(x) gives 0/0 or ∞/∞ form, then:

lim(x→a) f(x)/g(x) = lim(x→a) f'(x)/g'(x)

Provided the limit on right exists.

Can be applied repeatedly if needed.

## Algebraic Method for 0/0 Form

### Factorization
Factor numerator and denominator, cancel common factors

### Rationalization
Multiply by conjugate for expressions with radicals

Example: For √(a+x) - √a, multiply by [√(a+x) + √a]

## Expansion Method

Use standard expansions when x → 0:

eˣ = 1 + x + x²/2! + x³/3! + ...

ln(1 + x) = x - x²/2 + x³/3 - x⁴/4 + ...

sin(x) = x - x³/3! + x⁵/5! - ...

cos(x) = 1 - x²/2! + x⁴/4! - ...

tan(x) = x + x³/3 + 2x⁵/15 + ...

(1 + x)ⁿ = 1 + nx + n(n-1)x²/2! + ...

## Sandwich Theorem (Squeeze Theorem)

If f(x) ≤ g(x) ≤ h(x) for all x near a, and:
lim(x→a) f(x) = lim(x→a) h(x) = L

Then: lim(x→a) g(x) = L

Useful for proving: lim(x→0) x·sin(1/x) = 0

## Limits at Infinity

When x → ∞ for rational functions P(x)/Q(x):

Compare degrees:
- deg(P) < deg(Q): limit = 0
- deg(P) = deg(Q): limit = ratio of leading coefficients
- deg(P) > deg(Q): limit = ±∞

## Special Techniques

### For 1^∞ Form

lim[f(x)]^g(x) = e^[lim g(x)·(f(x)-1)]

When f(x) → 1 and g(x) → ∞

### For 0^0 or ∞^0 Forms

Let y = [f(x)]^g(x)

Take ln: ln(y) = g(x)·ln(f(x))

Find lim ln(y), then lim y = e^[lim ln(y)]

### For ∞ - ∞ Form

Combine into single fraction or use conjugate

## Continuity and Limits

f(x) is continuous at x = a if:
lim(x→a) f(x) = f(a)

This requires:
1. lim(x→a) f(x) exists
2. f(a) is defined
3. Both are equal

## Useful Substitutions

For lim(x→0) forms:
- Put x = 0 + h where h → 0
- Use sin(x) ≈ x, tan(x) ≈ x for small x

For lim(x→∞) forms:
- Put x = 1/h where h → 0
- Divide numerator and denominator by highest power

## Common Mistakes to Avoid

- Directly substituting value before checking form
- Applying L'Hôpital's rule when form is not indeterminate
- Not checking if limit exists before evaluating
- Wrong simplification in algebraic manipulations
- Forgetting domain restrictions
- Not checking left and right hand limits separately

## Important Results

lim(x→0) (sin x)/(x) = 1 (in radians, not degrees)

lim(x→0) [√(x+a) - √a]/x = 1/(2√a)

lim(n→∞) [1 + 1/n + 1/n² + ... + 1/nⁿ] = e

For very large x:
sin(1/x) ≈ 1/x
tan(1/x) ≈ 1/x
e^(1/x) ≈ 1 + 1/x