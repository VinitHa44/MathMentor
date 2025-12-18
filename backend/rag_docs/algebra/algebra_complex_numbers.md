# Complex Numbers

## Definition

A complex number is of the form:
z = x + iy

Where:
- x = real part = Re(z)
- y = imaginary part = Im(z)
- i = √(-1) is the imaginary unit
- i² = -1

## Powers of i

i¹ = i
i² = -1
i³ = -i
i⁴ = 1

General pattern:
i⁴ⁿ = 1
i⁴ⁿ⁺¹ = i
i⁴ⁿ⁺² = -1
i⁴ⁿ⁺³ = -i

## Equality of Complex Numbers

z₁ = z₂ if and only if:
- Re(z₁) = Re(z₂)
- Im(z₁) = Im(z₂)

## Conjugate of Complex Number

If z = x + iy, then conjugate:
z̄ = x - iy

### Properties of Conjugate

z + z̄ = 2Re(z)
z - z̄ = 2i·Im(z)
z·z̄ = x² + y² = |z|²
(z̄) = z
(z₁ + z₂) = z̄₁ + z̄₂
(z₁ - z₂) = z̄₁ - z̄₂
(z₁·z₂) = z̄₁·z̄₂
(z₁/z₂) = z̄₁/z̄₂

If z̄ = z, then z is purely real
If z̄ = -z, then z is purely imaginary

## Modulus (Absolute Value)

For z = x + iy:
|z| = √(x² + y²)

### Properties of Modulus

|z| ≥ 0, equality holds only when z = 0
|z| = |z̄|
|z₁·z₂| = |z₁|·|z₂|
|z₁/z₂| = |z₁|/|z₂|
|zⁿ| = |z|ⁿ
|z₁ + z₂| ≤ |z₁| + |z₂| (Triangle Inequality)
|z₁ - z₂| ≥ ||z₁| - |z₂||
-|z| ≤ Re(z) ≤ |z|
-|z| ≤ Im(z) ≤ |z|

## Argument (Amplitude)

For z = x + iy (z ≠ 0):
arg(z) = θ where tan(θ) = y/x

### Principal Argument
-π < arg(z) ≤ π

### Properties of Argument

arg(z₁·z₂) = arg(z₁) + arg(z₂)
arg(z₁/z₂) = arg(z₁) - arg(z₂)
arg(zⁿ) = n·arg(z)
arg(z̄) = -arg(z)
arg(-z) = π + arg(z) if arg(z) < 0
arg(-z) = arg(z) - π if arg(z) > 0

## Polar Form

z = r(cos θ + i sin θ)

Where:
- r = |z| = modulus
- θ = arg(z) = argument

Short form:
z = r·cis(θ)

### Euler's Formula
e^(iθ) = cos θ + i sin θ

Therefore:
z = r·e^(iθ)

## Operations in Polar Form

If z₁ = r₁·cis(θ₁) and z₂ = r₂·cis(θ₂):

### Multiplication
z₁·z₂ = r₁r₂·cis(θ₁ + θ₂)

### Division
z₁/z₂ = (r₁/r₂)·cis(θ₁ - θ₂)

### Power (De Moivre's Theorem)
zⁿ = rⁿ·cis(nθ)

Or: (cos θ + i sin θ)ⁿ = cos(nθ) + i sin(nθ)

## Roots of Complex Numbers

### nth roots of unity
The equation zⁿ = 1 has n roots:

zₖ = e^(2πik/n) = cos(2πk/n) + i sin(2πk/n)

Where k = 0, 1, 2, ..., n-1

### Properties of nth roots of unity

Sum of all nth roots = 0
Product of all nth roots = (-1)^(n-1)

If ω is a primitive nth root of unity:
1 + ω + ω² + ... + ω^(n-1) = 0

### Cube roots of unity
The roots of z³ = 1:

1, ω, ω²

Where ω = (-1 + i√3)/2 and ω² = (-1 - i√3)/2

Properties:
- 1 + ω + ω² = 0
- ω³ = 1
- ω² = ω̄

### Square roots of complex number
If z = x + iy, then √z = ±(α + iβ) where:

α = √[(|z| + x)/2]
β = √[(|z| - x)/2]

Sign of β is same as sign of y.

## Geometric Representation

### Distance Formula
Distance between z₁ and z₂:
|z₁ - z₂|

### Section Formula
If z divides the join of z₁ and z₂ in ratio m:n:

z = (mz₂ + nz₁)/(m + n)

### Collinearity
Three points z₁, z₂, z₃ are collinear if:

|z₁ - z₂| + |z₂ - z₃| = |z₁ - z₃|

Or: Im[(z₃ - z₁)/(z₂ - z₁)] = 0

## Equations and Loci

### Circle
|z - z₀| = r represents circle with center z₀ and radius r

### Perpendicular Bisector
|z - z₁| = |z - z₂| represents perpendicular bisector of segment joining z₁ and z₂

### Apollonius Circle
|z - z₁|/|z - z₂| = k (k ≠ 1) represents a circle

### Half-plane
arg[(z - z₁)/(z - z₂)] = α represents a ray from z₁ through z₂

## Rotation

Rotation of z about origin by angle θ:
w = z·e^(iθ)

Rotation of z about point z₀ by angle θ:
w = z₀ + (z - z₀)·e^(iθ)

## Important Identities

### Triangle Inequality
|z₁ + z₂ + z₃| ≤ |z₁| + |z₂| + |z₃|

### Ptolemy's Inequality
|z₁ - z₃|·|z₂ - z₄| ≤ |z₁ - z₂|·|z₃ - z₄| + |z₂ - z₃|·|z₁ - z₄|

## Quadratic Equations with Complex Coefficients

For az² + bz + c = 0:

z = [-b ± √(b² - 4ac)]/(2a)

If coefficients are real and one root is α + iβ, the other root is α - iβ (complex conjugate)

## Useful Results

If |z| = 1:
- 1/z = z̄
- Re(z) = (z + z̄)/2
- Im(z) = (z - z̄)/(2i)

If z lies on unit circle:
z = e^(iθ) = cos θ + i sin θ

## Common Mistakes to Avoid

- Confusing Re(z₁z₂) with Re(z₁)·Re(z₂)
- Wrong sign in conjugate operations
- Not considering principal value of argument
- Forgetting domain restrictions in argument calculations
- Incorrect application of De Moivre's theorem