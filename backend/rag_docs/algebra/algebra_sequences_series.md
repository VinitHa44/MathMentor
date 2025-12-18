# Sequences and Series

## Arithmetic Progression (AP)

### Definition
A sequence where the difference between consecutive terms is constant.

### General Form
a, a+d, a+2d, a+3d, ...

Where:
- a = first term
- d = common difference

### nth Term Formula
aₙ = a + (n-1)d

### Sum of n Terms
Sₙ = n/2 × [2a + (n-1)d]

Alternative form:
Sₙ = n/2 × (first term + last term)
Sₙ = n/2 × (a + l)

Where l = last term = a + (n-1)d

### Properties
- If a, b, c are in AP: 2b = a + c
- Three numbers in AP: a-d, a, a+d
- Four numbers in AP: a-3d, a-d, a+d, a+3d

### Sum of First n Natural Numbers
Sum = 1 + 2 + 3 + ... + n = n(n+1)/2

### Sum of First n Odd Numbers
Sum = 1 + 3 + 5 + ... + (2n-1) = n²

### Sum of First n Even Numbers
Sum = 2 + 4 + 6 + ... + 2n = n(n+1)

## Geometric Progression (GP)

### Definition
A sequence where the ratio between consecutive terms is constant.

### General Form
a, ar, ar², ar³, ...

Where:
- a = first term
- r = common ratio

### nth Term Formula
aₙ = a × r^(n-1)

### Sum of n Terms

When r ≠ 1:
Sₙ = a(1 - rⁿ)/(1 - r)

Alternative form:
Sₙ = a(rⁿ - 1)/(r - 1)

When r = 1:
Sₙ = na

### Sum to Infinity

When |r| < 1:
S∞ = a/(1 - r)

When |r| ≥ 1: Sum does not exist (diverges)

### Properties
- If a, b, c are in GP: b² = ac
- Three numbers in GP: a/r, a, ar
- Four numbers in GP: a/r³, a/r, ar, ar³

## Harmonic Progression (HP)

### Definition
A sequence is in HP if the reciprocals of its terms are in AP.

### General Form
If 1/a, 1/(a+d), 1/(a+2d), ... are in AP, then a, a+d, a+2d, ... are in HP

### nth Term
If aₙ is the nth term of HP:
1/aₙ = 1/a + (n-1)d

Where d is the common difference of corresponding AP.

### Harmonic Mean
For two numbers a and b:
HM = 2ab/(a + b)

### Properties
- If a, b, c are in HP: b = 2ac/(a + c)
- No simple formula for sum of HP

## Arithmetic-Geometric Progression (AGP)

### Definition
A sequence where each term is the product of corresponding terms of an AP and a GP.

### General Form
a, (a+d)r, (a+2d)r², (a+3d)r³, ...

### Sum of n Terms
Sₙ = a/(1-r) + [dr(1-rⁿ⁻¹)]/[(1-r)²] - [a + (n-1)d]rⁿ/(1-r)

When |r| < 1, as n → ∞:
S∞ = a/(1-r) + dr/(1-r)²

## Special Summations

### Sum of Squares of First n Natural Numbers
1² + 2² + 3² + ... + n² = n(n+1)(2n+1)/6

### Sum of Cubes of First n Natural Numbers
1³ + 2³ + 3³ + ... + n³ = [n(n+1)/2]²

### Sum of Fourth Powers
1⁴ + 2⁴ + 3⁴ + ... + n⁴ = n(n+1)(2n+1)(3n²+3n-1)/30

## Arithmetic Mean (AM)

For n numbers a₁, a₂, ..., aₙ:
AM = (a₁ + a₂ + ... + aₙ)/n

### AM between two numbers a and b:
AM = (a + b)/2

### n Arithmetic Means between a and b:
If A₁, A₂, ..., Aₙ are n AMs between a and b:
Common difference d = (b - a)/(n + 1)

## Geometric Mean (GM)

For n numbers a₁, a₂, ..., aₙ:
GM = (a₁ × a₂ × ... × aₙ)^(1/n)

### GM between two numbers a and b:
GM = √(ab)

### n Geometric Means between a and b:
If G₁, G₂, ..., Gₙ are n GMs between a and b:
Common ratio r = (b/a)^(1/(n+1))

## Harmonic Mean (HM)

For n numbers a₁, a₂, ..., aₙ:
HM = n / (1/a₁ + 1/a₂ + ... + 1/aₙ)

### HM between two numbers a and b:
HM = 2ab/(a + b)

## Relationship Between AM, GM, HM

For positive numbers:

AM ≥ GM ≥ HM

Equality holds when all numbers are equal.

For two numbers a and b:
GM² = AM × HM

## Method of Differences

For series of the form Σ[f(n) - f(n+1)]:
Sum = f(1) - f(n+1)

Useful for:
- Σ 1/(n(n+1)) = Σ [1/n - 1/(n+1)]
- Σ 1/(n(n+2)) = 1/2 × Σ [1/n - 1/(n+2)]

## Sigma Notation Properties

- Σc = nc (where c is constant)
- Σ(aₙ ± bₙ) = Σaₙ ± Σbₙ
- Σ(c × aₙ) = c × Σaₙ
- Σaₙ from i=m to n = Σaₙ from i=1 to n - Σaₙ from i=1 to m-1
