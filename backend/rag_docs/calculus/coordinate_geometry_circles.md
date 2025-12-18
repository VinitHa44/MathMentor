# Coordinate Geometry - Circles

## Standard Equation of Circle

### Centre at origin, radius r:
x² + y² = r²

### Centre at (h,k), radius r:
(x - h)² + (y - k)² = r²

## General Equation of Circle

x² + y² + 2gx + 2fy + c = 0

Where:
- Centre = (-g, -f)
- Radius = √(g² + f² - c)

**Condition for circle to exist:**
g² + f² - c > 0

## Diameter Form

Equation of circle with (x₁,y₁) and (x₂,y₂) as ends of diameter:

(x - x₁)(x - x₂) + (y - y₁)(y - y₂) = 0

## Parametric Equations

For circle x² + y² = r²:

x = r·cos(θ)
y = r·sin(θ)

For circle (x-h)² + (y-k)² = r²:

x = h + r·cos(θ)
y = k + r·sin(θ)

## Position of Point

For point (x₁,y₁) and circle x² + y² + 2gx + 2fy + c = 0:

S₁ = x₁² + y₁² + 2gx₁ + 2fy₁ + c

- S₁ > 0: Point outside circle
- S₁ = 0: Point on circle
- S₁ < 0: Point inside circle

## Equation of Tangent

### Point form (at point (x₁,y₁) on circle):

For x² + y² = r²:
xx₁ + yy₁ = r²

For x² + y² + 2gx + 2fy + c = 0:
xx₁ + yy₁ + g(x + x₁) + f(y + y₁) + c = 0

### Slope form (tangent with slope m):

For x² + y² = r²:
y = mx ± r√(1 + m²)

For (x-h)² + (y-k)² = r²:
y - k = m(x - h) ± r√(1 + m²)

### Parametric form:

For x² + y² = r², tangent at (r·cos(θ), r·sin(θ)):
x·cos(θ) + y·sin(θ) = r

## Length of Tangent

Length of tangent from point (x₁,y₁) to circle x² + y² + 2gx + 2fy + c = 0:

L = √(x₁² + y₁² + 2gx₁ + 2fy₁ + c) = √S₁

## Pair of Tangents

Equation of pair of tangents from (x₁,y₁) to circle S = 0:

SS₁ = T²

Where:
- S = x² + y² + 2gx + 2fy + c
- S₁ = x₁² + y₁² + 2gx₁ + 2fy₁ + c
- T = xx₁ + yy₁ + g(x + x₁) + f(y + y₁) + c

## Chord of Contact

Equation of chord of contact from external point (x₁,y₁):

For x² + y² = r²:
xx₁ + yy₁ = r²

For general circle:
T = 0 (same as tangent equation)

## Equation of Normal

### At point (x₁,y₁) on circle with centre (h,k):

(y - y₁)/(x - x₁) = (y₁ - k)/(x₁ - h)

Or: (y - y₁)(x₁ - h) = (x - x₁)(y₁ - k)

### For x² + y² = r²:
y/x = y₁/x₁ (normal passes through origin)

## Equation of Chord

### Chord with midpoint (x₁,y₁):

For x² + y² = r²:
xx₁ + yy₁ = x₁² + y₁²

For general circle S = 0:
T = S₁

## Power of a Point

Power of point (x₁,y₁) with respect to circle:

P = S₁ = x₁² + y₁² + 2gx₁ + 2fy₁ + c

Also equals:
- Square of length of tangent
- Product of distances to circle along any line through point

## Radical Axis

Common chord (or locus of points with equal power) of two circles:

S₁ - S₂ = 0

Where S₁ and S₂ are equations of circles.

Properties:
- Perpendicular to line joining centres
- Every circle through intersection points has same radical axis

## Radical Centre

Point of intersection of three radical axes

Has equal power with respect to all three circles

## Family of Circles

### Through intersection of circle S = 0 and line L = 0:
S + λL = 0

### Through intersection of two circles S₁ = 0 and S₂ = 0:
S₁ + λS₂ = 0

## Orthogonal Circles

Two circles are orthogonal if tangents at intersection are perpendicular.

Condition: 2g₁g₂ + 2f₁f₂ = c₁ + c₂

Where circles are:
x² + y² + 2g₁x + 2f₁y + c₁ = 0
x² + y² + 2g₂x + 2f₂y + c₂ = 0

## Angle Between Two Circles

cos(θ) = (r₁² + r₂² - d²)/(2r₁r₂)

Where:
- r₁, r₂ = radii
- d = distance between centres

## Common Tangents

For two circles with radii r₁, r₂ and distance d between centres:

### Number of common tangents:
- d > r₁ + r₂: 4 tangents (2 direct, 2 transverse)
- d = r₁ + r₂: 3 tangents (external touch)
- |r₁ - r₂| < d < r₁ + r₂: 2 tangents (both direct)
- d = |r₁ - r₂|: 1 tangent (internal touch)
- d < |r₁ - r₂|: 0 tangents (one inside other)

### Length of direct common tangent:
L = √(d² - (r₁ - r₂)²)

### Length of transverse common tangent:
L = √(d² - (r₁ + r₂)²)

## Circle Through Three Points

Circle through (x₁,y₁), (x₂,y₂), (x₃,y₃):

|x² + y²   x   y   1|
|x₁² + y₁² x₁  y₁  1| = 0
|x₂² + y₂² x₂  y₂  1|
|x₃² + y₃² x₃  y₃  1|

## Director Circle

Locus of point of intersection of perpendicular tangents.

For circle x² + y² = r²:
Director circle: x² + y² = 2r²

## Pole and Polar

Polar of point (x₁,y₁) with respect to circle:
xx₁ + yy₁ = r² (for x² + y² = r²)

If polar passes through (x₂,y₂), then polar of (x₂,y₂) passes through (x₁,y₁).

## Important Results

### Circle touching both axes:
(x ± a)² + (y ± a)² = a²
Centre at (±a, ±a), radius = a

### Circle touching x-axis:
(x - h)² + (y - k)² = k²

### Circle touching y-axis:
(x - h)² + (y - k)² = h²

### Circle through origin:
c = 0 in general equation

## Limiting Points

For family S₁ + λS₂ = 0, limiting points satisfy:
- S₁ = 0
- S₂ = 0
- Points from which tangent lengths to both circles are equal

## Common Mistakes to Avoid

- Forgetting condition g² + f² - c > 0 for circle existence
- Sign errors in centre coordinates
- Wrong formula for tangent length
- Confusing chord of contact with chord with given midpoint
- Not checking if point is inside/outside before finding tangent
- Incorrect application of orthogonality condition