# Conic Sections - Parabola and Ellipse

## Parabola

### Definition
Locus of points equidistant from a fixed point (focus) and a fixed line (directrix).

### Standard Equation (vertex at origin, axis along x-axis):
y² = 4ax

- Focus: F(a, 0)
- Directrix: x = -a
- Axis: y = 0 (x-axis)
- Vertex: (0, 0)
- Latus rectum: 4a
- Eccentricity: e = 1

### Other Standard Forms:

**y² = -4ax** (opens left)
- Focus: (-a, 0)
- Directrix: x = a

**x² = 4ay** (opens up)
- Focus: (0, a)
- Directrix: y = -a

**x² = -4ay** (opens down)
- Focus: (0, -a)
- Directrix: y = a

### General Parabola (vertex at (h,k)):

**(y-k)² = 4a(x-h)** (horizontal axis)
**(x-h)² = 4a(y-k)** (vertical axis)

### Parametric Equations

For y² = 4ax:
x = at²
y = 2at

Point on parabola: (at², 2at)

### Focal Chord

Chord passing through focus

For focal chord with endpoints t₁ and t₂:
t₁·t₂ = -1

Length of focal chord: a(t₁ - t₂)² = 4a + (y₁-y₂)²/(4a)

### Latus Rectum

Focal chord perpendicular to axis
Length = 4a
Endpoints: (a, 2a) and (a, -2a) for y² = 4ax

### Tangent to Parabola

**At point (x₁,y₁):**
yy₁ = 2a(x + x₁)

**At parameter t:**
ty = x + at²

**With slope m:**
y = mx + a/m

Point of contact: (a/m², 2a/m)

### Normal to Parabola

**At point (x₁,y₁):**
y - y₁ = -(y₁/2a)(x - x₁)

**At parameter t:**
y + tx = 2at + at³

**With slope m:**
y = mx - 2am - am³

### Chord of Contact

From external point (x₁,y₁):
yy₁ = 2a(x + x₁)

### Equation of Chord

Chord with midpoint (x₁,y₁):
yy₁ - 2a(x + x₁) = y₁² - 4ax₁

### Important Properties

- Tangent at vertex is perpendicular to axis
- Normal at any point passes through axis
- Point of intersection of tangents at t₁ and t₂: (at₁t₂, a(t₁+t₂))
- Tangents at endpoints of focal chord are perpendicular
- All normals to parabola pass through some point on axis

## Ellipse

### Definition
Locus of points where sum of distances from two fixed points (foci) is constant.

### Standard Equation (center at origin, major axis along x-axis):
x²/a² + y²/b² = 1, where a > b

- Foci: (±ae, 0) where e = √(1 - b²/a²)
- Vertices: (±a, 0)
- Co-vertices: (0, ±b)
- Major axis: 2a (along x-axis)
- Minor axis: 2b (along y-axis)
- Center: (0, 0)
- Eccentricity: e = √(1 - b²/a²), 0 < e < 1
- Latus rectum: 2b²/a
- Directrices: x = ±a/e

### Relationship:
b² = a²(1 - e²)
a² = b² + c² where c = ae

### If major axis along y-axis:
x²/b² + y²/a² = 1, where a > b

- Foci: (0, ±ae)
- Vertices: (0, ±a)
- Directrices: y = ±a/e

### General Ellipse (center at (h,k)):
(x-h)²/a² + (y-k)²/b² = 1

### Parametric Equations

For x²/a² + y²/b² = 1:
x = a·cos(θ)
y = b·sin(θ)

Point on ellipse: (a·cos(θ), b·sin(θ))

### Focal Property

For any point P on ellipse with foci F₁ and F₂:
PF₁ + PF₂ = 2a

### Tangent to Ellipse

**At point (x₁,y₁):**
xx₁/a² + yy₁/b² = 1

**At parameter θ:**
(x·cos(θ))/a + (y·sin(θ))/b = 1

**With slope m:**
y = mx ± √(a²m² + b²)

Point of contact: (±a²m/√(a²m²+b²), ∓b²/√(a²m²+b²))

### Normal to Ellipse

**At point (x₁,y₁):**
(a²x)/x₁ - (b²y)/y₁ = a² - b²

**At parameter θ:**
ax·sec(θ) - by·cosec(θ) = a² - b²

### Chord of Contact

From external point (x₁,y₁):
xx₁/a² + yy₁/b² = 1

### Equation of Chord

Chord with midpoint (x₁,y₁):
xx₁/a² + yy₁/b² = (x₁²/a² + y₁²/b²)

Or: T = S₁ where T is tangent equation at (x₁,y₁) and S₁ is value of S at (x₁,y₁)

### Director Circle

Locus of intersection of perpendicular tangents:
x² + y² = a² + b²

### Auxiliary Circle

Circle with radius equal to semi-major axis:
x² + y² = a²

### Eccentric Angle

For point P(x,y) on ellipse:
Eccentric angle θ is such that:
x = a·cos(θ), y = b·sin(θ)

### Important Properties

- Sum of focal distances is constant (= 2a)
- Tangent at any point makes equal angles with focal radii
- Normal at any point bisects angle between focal radii
- Product of perpendiculars from foci to any tangent = b²
- Tangent at endpoints of latus rectum pass through vertices

## Position of Point

For point (x₁,y₁):

**Parabola y² = 4ax:**
- If y₁² - 4ax₁ > 0: outside
- If y₁² - 4ax₁ = 0: on parabola
- If y₁² - 4ax₁ < 0: inside

**Ellipse x²/a² + y²/b² = 1:**
- If x₁²/a² + y₁²/b² > 1: outside
- If x₁²/a² + y₁²/b² = 1: on ellipse
- If x₁²/a² + y₁²/b² < 1: inside

## Common Mistakes to Avoid

- Confusing a and b in ellipse equations
- Wrong sign in eccentricity formula
- Not checking which axis is major
- Forgetting condition t₁t₂ = -1 for focal chord
- Incorrect parametric substitution
- Sign errors in tangent/normal equations

## Important Results

**Parabola:**
- Area enclosed between parabola and latus rectum = (8/3)a²
- Length of focal chord = 4a·cosec²(θ/2)

**Ellipse:**
- Area = πab
- Length of latus rectum = 2b²/a
- Distance between foci = 2ae
- Distance between directrices = 2a/e