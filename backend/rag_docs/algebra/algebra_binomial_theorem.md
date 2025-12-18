# Binomial Theorem

## Basic Binomial Theorem

### For Positive Integer n

(x + y)ⁿ = ⁿC₀xⁿy⁰ + ⁿC₁xⁿ⁻¹y¹ + ⁿC₂xⁿ⁻²y² + ... + ⁿCₙx⁰yⁿ

General term (r+1)th term:
Tᵣ₊₁ = ⁿCᵣ × xⁿ⁻ʳ × yʳ

Where r = 0, 1, 2, ..., n

### Number of Terms
In the expansion of (x + y)ⁿ: n + 1 terms

## Special Cases

### (1 + x)ⁿ
(1 + x)ⁿ = ⁿC₀ + ⁿC₁x + ⁿC₂x² + ... + ⁿCₙxⁿ

### (1 - x)ⁿ
(1 - x)ⁿ = ⁿC₀ - ⁿC₁x + ⁿC₂x² - ... + (-1)ⁿ × ⁿCₙxⁿ

### (x - y)ⁿ
Replace y with -y in the general formula

## Middle Terms

### When n is even
Middle term = (n/2 + 1)th term
Only one middle term

### When n is odd
Middle terms = (n+1)/2 th and (n+3)/2 th terms
Two middle terms

## Greatest Term

To find the greatest term in (x + y)ⁿ:

Compare consecutive terms using ratio:
Tᵣ₊₁/Tᵣ = [(n-r+1)/r] × (y/x)

Greatest term occurs when:
Tᵣ₊₁/Tᵣ ≥ 1 and Tᵣ₊₂/Tᵣ₊₁ < 1

## Properties and Identities

### Sum of Binomial Coefficients

ⁿC₀ + ⁿC₁ + ⁿC₂ + ... + ⁿCₙ = 2ⁿ

Put x = 1 in (1 + x)ⁿ

### Sum of Coefficients with Alternating Signs

ⁿC₀ - ⁿC₁ + ⁿC₂ - ... + (-1)ⁿ × ⁿCₙ = 0

Put x = -1 in (1 + x)ⁿ

### Sum of Even-Placed Coefficients

ⁿC₀ + ⁿC₂ + ⁿC₄ + ... = 2ⁿ⁻¹

### Sum of Odd-Placed Coefficients

ⁿC₁ + ⁿC₃ + ⁿC₅ + ... = 2ⁿ⁻¹

## Summations Involving Binomial Coefficients

Σ(r × ⁿCᵣ) from r=0 to n = n × 2ⁿ⁻¹

Σ(r² × ⁿCᵣ) from r=0 to n = n(n+1) × 2ⁿ⁻²

Σ(ⁿCᵣ)² from r=0 to n = ²ⁿCₙ

Σ(ⁿCᵣ/r+1) from r=0 to n = (2ⁿ⁺¹ - 1)/(n+1)

## Finding Particular Terms

### Term Independent of x

In expansion of (x + a/xᵏ)ⁿ or similar:
Set power of x = 0 and solve for r

### Term Containing xᵖ

Set power of x = p and solve for r

### Coefficient of xᵖ

Find the term containing xᵖ, then extract coefficient

## Multinomial Theorem

(x₁ + x₂ + ... + xₘ)ⁿ

General term:
[n! / (r₁! × r₂! × ... × rₘ!)] × x₁ʳ¹ × x₂ʳ² × ... × xₘʳᵐ

Where r₁ + r₂ + ... + rₘ = n

Number of terms = ⁿ⁺ᵐ⁻¹Cₘ₋₁

## Binomial Theorem for Rational Index

### For any rational n (not necessarily positive integer)

(1 + x)ⁿ = 1 + nx + [n(n-1)/2!]x² + [n(n-1)(n-2)/3!]x³ + ...

Valid when |x| < 1

General term:
Tᵣ₊₁ = [n(n-1)(n-2)...(n-r+1)/r!] × xʳ

This series has infinite terms when n is not a positive integer.

## Important Expansions (for |x| < 1)

### (1 + x)⁻¹
(1 + x)⁻¹ = 1 - x + x² - x³ + x⁴ - ...

### (1 - x)⁻¹
(1 - x)⁻¹ = 1 + x + x² + x³ + x⁴ + ...

### (1 + x)⁻²
(1 + x)⁻² = 1 - 2x + 3x² - 4x³ + 5x⁴ - ...

### (1 - x)⁻²
(1 - x)⁻² = 1 + 2x + 3x² + 4x³ + 5x⁴ + ...

### (1 + x)¹/²
(1 + x)¹/² = 1 + x/2 - x²/8 + x³/16 - 5x⁴/128 + ...

### (1 - x)¹/²
(1 - x)¹/² = 1 - x/2 - x²/8 - x³/16 - 5x⁴/128 - ...

## Approximations

For small x (|x| << 1):

(1 + x)ⁿ ≈ 1 + nx

(1 + x)ⁿ ≈ 1 + nx + [n(n-1)/2]x² (better approximation)

## Greatest Binomial Coefficient

For (x + y)ⁿ:

### If n is even:
Greatest coefficient = ⁿCₙ/₂

### If n is odd:
Greatest coefficients = ⁿC₍ₙ₋₁₎/₂ = ⁿC₍ₙ₊₁₎/₂

## Applications

### Finding Remainder

To find remainder when 2ⁿ is divided by m:
Express 2ⁿ as (1+1)ⁿ or suitable form

### Divisibility Problems

Use binomial expansion to prove divisibility

Example: Prove 2²ⁿ - 1 is divisible by 3:
2²ⁿ - 1 = (2²)ⁿ - 1 = (4)ⁿ - 1 = (3+1)ⁿ - 1

### Finding Digits

Last digit of aⁿ can be found using binomial expansion

## Pascal's Triangle

```
                1
              1   1
            1   2   1
          1   3   3   1
        1   4   6   4   1
      1   5  10  10   5   1
```

Properties:
- Each number is sum of two numbers above it
- nth row contains binomial coefficients ⁿC₀, ⁿC₁, ..., ⁿCₙ
- Sum of nth row = 2ⁿ

## Common Mistakes to Avoid

- Confusing (r+1)th term with rth term
- Wrong application for negative or fractional indices
- Not checking convergence condition |x| < 1 for infinite series
- Miscalculating middle term position
- Forgetting to simplify binomial coefficients