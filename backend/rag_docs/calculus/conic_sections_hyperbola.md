# Conic Sections - Hyperbola

## Definition

Locus of points where absolute difference of distances from two fixed points (foci) is constant.

## Standard Equation (center at origin, transverse axis along x-axis)

x²/a² - y²/b² = 1

- Foci: (±ae, 0) where e = √(1 + b²/a²)
- Vertices: (±a, 0)
- Center: (0, 0)
- Transverse axis: 2a (along x-axis)
- Conjugate axis: 2b (along y-axis)
- Eccentricity: e = √(1 + b²/a²), e > 1
- Latus rectum: 2b²/a
- Directrices: x = ±a/e

### Relationship:
b² = a²(e² - 1)
c² = a² + b² where c = ae

## Conjugate Hyperbola

x²/a² - y²/b² = -1

Or: -x²/a² + y²/b² = 1

- Transverse axis along y-axis
- Vertices: (0, ±b)
- Foci: (0, ±be') where e' = √(1 + a²/b²)

### Important: 
For hyperbola and its conjugate, e and e' satisfy:
1/e² + 1/e'² = 1

## If transverse axis along y-axis

y²/a² - x²/b² = 1

- Foci: (0, ±ae)
- Vertices: (0, ±a)
- Directrices: y = ±a/e

## General Hyperbola (center at (h,k))

(x-h)²/a² - (y-k)²/b² = 1

## Parametric Equations

For x²/a² - y²/b² = 1:

x = a·sec(θ)
y = b·tan(θ)

Point on hyperbola: (a·sec(θ), b·tan(θ))

Alternative form:
x = a·cosh(t)
y = b·sinh(t)

## Asymptotes

Lines that hyperbola approaches but never touches.

For x²/a² - y²/b² = 1:

Equations: x²/a² - y²/b² = 0

Or: y = ±(b/a)x

### Properties:
- Pass through center
- Slope = ±b/a
- Distance from center to asymptote = ab/√(a²+b²)
- Hyperbola lies between asymptotes
- Product of perpendiculars from any point on hyperbola to asymptotes = constant = a²b²/(a²+b²)

## Rectangular Hyperbola

Special case when a = b, making e = √2

Equation: x² - y² = a²

Asymptotes: x = 0 and y = 0 (coordinate axes)

### Standard form: xy = c²
- Asymptotes: x = 0, y = 0
- Parametric form: x = ct, y = c/t
- Eccentricity: e = √2

## Focal Property

For any point P on hyperbola with foci F₁ and F₂:
|PF₁ - PF₂| = 2a

## Tangent to Hyperbola

**At point (x₁,y₁):**
xx₁/a² - yy₁/b² = 1

**At parameter θ:**
(x·sec(θ))/a - (y·tan(θ))/b = 1

**With slope m:**
y = mx ± √(a²m² - b²)

Condition: m² > b²/a² (for real tangents)

Point of contact: (±a²m/√(a²m²-b²), ±b²/√(a²m²-b²))

**For xy = c²:**
At point (ct, c/t): x/t + ty = 2c

With slope m: y = mx + c/m

## Normal to Hyperbola

**At point (x₁,y₁):**
(a²x)/x₁ + (b²y)/y₁ = a² + b²

**At parameter θ:**
ax·cos(θ) + by·cot(θ) = a² + b²

**For xy = c²:**
At (ct, c/t): tx³ - t³y = c(t⁴ - 1)

## Chord of Contact

From external point (x₁,y₁):
xx₁/a² - yy₁/b² = 1

## Equation of Chord

Chord with midpoint (x₁,y₁):
xx₁/a² - yy₁/b² = (x₁²/a² - y₁²/b²)

Or: T = S₁

## Director Circle

Locus of intersection of perpendicular tangents:
x² + y² = a² - b²

**Note:** Exists only when a² > b²

## Auxiliary Circle

Circle with radius equal to semi-transverse axis:
x² + y² = a²

## Position of Point

For point (x₁,y₁) and hyperbola x²/a² - y²/b² = 1:

- If x₁²/a² - y₁²/b² > 1: outside
- If x₁²/a² - y₁²/b² = 1: on hyperbola
- If x₁²/a² - y₁²/b² < 1: inside (between branches)

## Angle Between Asymptotes

For x²/a² - y²/b² = 1:

tan(θ) = 2ab/(a² - b²)

If θ = 90° (rectangular hyperbola): a = b

## Important Properties

### General:
- Difference of focal distances is constant (= 2a)
- Tangent at any point bisects angle between focal radii
- Product of perpendiculars from foci to any tangent = b²
- Tangent at endpoints of latus rectum pass through vertices

### For Rectangular Hyperbola xy = c²:
- Tangent at (ct, c/t) meets axes at (2ct, 0) and (0, 2c/t)
- Area of triangle formed by tangent and axes = 2c²
- Normal at (ct, c/t) passes through origin

## Length of Latus Rectum

For x²/a² - y²/b² = 1:
Length = 2b²/a

For xy = c²:
Length = c√2

## Focal Chord

Chord passing through focus

For focal chord with parameters θ₁ and θ₂:
tan(θ₁/2)·tan(θ₂/2) = (e-1)/(e+1)

## Conjugate Diameters

Two diameters are conjugate if each bisects chords parallel to the other.

For diameters y = m₁x and y = m₂x:
m₁m₂ = b²/a²

## Important Formulas

Distance between foci: 2ae

Distance between directrices: 2a/e

Distance between vertices: 2a

Eccentricity: e = (distance between foci)/(distance between vertices)

## Common Mistakes to Avoid

- Confusing with ellipse (sign in equation)
- Wrong eccentricity formula (+ instead of -)
- Forgetting that e > 1 for hyperbola
- Not checking domain for tangent with slope m
- Sign errors in conjugate hyperbola
- Confusing transverse and conjugate axes
- Incorrect asymptote equations

## Special Cases

**Equilateral/Rectangular Hyperbola:**
- a = b
- e = √2
- Asymptotes are perpendicular
- Standard form: xy = c²

**When b → 0:**
Hyperbola degenerates into two lines (asymptotes coincide with transverse axis)

## Areas

Area between hyperbola and latus rectum: (2/3)ab(e²-1)

For rectangular hyperbola xy = c²:
Area between curve and line joining points (ct₁, c/t₁) and (ct₂, c/t₂):
Area = (c²/2)|ln(t₁/t₂) - (t₁-t₂)(t₁+t₂)/(2t₁t₂)|

## Comparison with Other Conics

| Property | Parabola | Ellipse | Hyperbola |
|----------|----------|---------|-----------|
| e value | e = 1 | 0 < e < 1 | e > 1 |
| Foci | 1 | 2 | 2 |
| Directrix | 1 | 2 | 2 |
| Branches | 1 | 1 closed | 2 open |
| Asymptotes | 1 (at ∞) | None | 2 |