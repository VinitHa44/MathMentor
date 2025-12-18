# Coordinate Geometry - Straight Lines

## Distance Formula

Distance between points (x₁,y₁) and (x₂,y₂):

d = √[(x₂-x₁)² + (y₂-y₁)²]

Distance from origin to (x,y): d = √(x² + y²)

## Section Formula

### Internal Division
Point dividing line segment from (x₁,y₁) to (x₂,y₂) in ratio m:n internally:

x = (mx₂ + nx₁)/(m+n)
y = (my₂ + ny₁)/(m+n)

### External Division
Point dividing in ratio m:n externally:

x = (mx₂ - nx₁)/(m-n)
y = (my₂ - ny₁)/(m-n)

### Midpoint (m=n=1)
x = (x₁+x₂)/2
y = (y₁+y₂)/2

## Slope of a Line

Slope (m) of line through (x₁,y₁) and (x₂,y₂):

m = (y₂-y₁)/(x₂-x₁) = tan(θ)

Where θ is angle with positive x-axis

### Special Cases:
- Horizontal line: m = 0
- Vertical line: m = undefined (∞)
- Line through origin with angle θ: m = tan(θ)

## Collinearity of Three Points

Points (x₁,y₁), (x₂,y₂), (x₃,y₃) are collinear if:

Slope method: (y₂-y₁)/(x₂-x₁) = (y₃-y₂)/(x₃-x₂)

Area method: (1/2)|x₁(y₂-y₃) + x₂(y₃-y₁) + x₃(y₁-y₂)| = 0

## Angle Between Two Lines

If slopes are m₁ and m₂:

tan(θ) = |(m₂-m₁)/(1+m₁m₂)|

### Parallel Lines:
m₁ = m₂

### Perpendicular Lines:
m₁ · m₂ = -1

## Equations of a Line

### Point-Slope Form
Line through (x₁,y₁) with slope m:

y - y₁ = m(x - x₁)

### Two-Point Form
Line through (x₁,y₁) and (x₂,y₂):

(y - y₁)/(y₂ - y₁) = (x - x₁)/(x₂ - x₁)

### Slope-Intercept Form
Line with slope m and y-intercept c:

y = mx + c

### Intercept Form
Line with x-intercept a and y-intercept b:

x/a + y/b = 1

### Normal Form
Line at perpendicular distance p from origin, normal at angle α:

x·cos(α) + y·sin(α) = p

### General Form
ax + by + c = 0

Slope: m = -a/b
x-intercept: -c/a
y-intercept: -c/b

### Parametric Form
Line through (x₁,y₁) in direction of angle θ:

x = x₁ + r·cos(θ)
y = y₁ + r·sin(θ)

Where r is parameter (distance from (x₁,y₁))

## Distance from Point to Line

Distance from point (x₀,y₀) to line ax + by + c = 0:

d = |ax₀ + by₀ + c| / √(a² + b²)

## Distance Between Parallel Lines

For parallel lines ax + by + c₁ = 0 and ax + by + c₂ = 0:

d = |c₂ - c₁| / √(a² + b²)

## Position of Point Relative to Line

For point (x₀,y₀) and line ax + by + c = 0:

Substitute point in equation:
- If ax₀ + by₀ + c > 0: point on one side
- If ax₀ + by₀ + c < 0: point on other side
- If ax₀ + by₀ + c = 0: point on line

## Family of Lines

### Through intersection of L₁ = 0 and L₂ = 0:
L₁ + λL₂ = 0, where λ is parameter

### Parallel to ax + by + c = 0:
ax + by + k = 0

### Perpendicular to ax + by + c = 0:
bx - ay + k = 0

## Equation of Bisectors

For lines L₁: a₁x + b₁y + c₁ = 0 and L₂: a₂x + b₂y + c₂ = 0:

Bisectors:
(a₁x + b₁y + c₁)/√(a₁² + b₁²) = ±(a₂x + b₂y + c₂)/√(a₂² + b₂²)

### Acute Angle Bisector:
Use positive sign if a₁a₂ + b₁b₂ < 0

### Obtuse Angle Bisector:
Use positive sign if a₁a₂ + b₁b₂ > 0

## Concurrent Lines

Three lines L₁ = 0, L₂ = 0, L₃ = 0 are concurrent if they meet at a point.

Condition using determinants:
|a₁  b₁  c₁|
|a₂  b₂  c₂| = 0
|a₃  b₃  c₃|

## Foot of Perpendicular

Foot of perpendicular from (x₁,y₁) to line ax + by + c = 0:

x = (b(bx₁ - ay₁) - ac) / (a² + b²)
y = (a(-bx₁ + ay₁) - bc) / (a² + b²)

## Image (Reflection) of a Point

Image of (x₁,y₁) in line ax + by + c = 0:

(x₂ - x₁)/a = (y₂ - y₁)/b = -2(ax₁ + by₁ + c)/(a² + b²)

## Area of Triangle

Area of triangle with vertices (x₁,y₁), (x₂,y₂), (x₃,y₃):

Area = (1/2)|x₁(y₂ - y₃) + x₂(y₃ - y₁) + x₃(y₁ - y₂)|

## Centroid of Triangle

Centroid of triangle with vertices (x₁,y₁), (x₂,y₂), (x₃,y₃):

G = ((x₁+x₂+x₃)/3, (y₁+y₂+y₃)/3)

## Orthocentre

Intersection point of altitudes

For triangle with vertices A, B, C:
Use slopes of sides and perpendicularity

## Circumcentre

Intersection point of perpendicular bisectors

Equidistant from all three vertices

## Incentre

Intersection point of angle bisectors

I = ((ax₁+bx₂+cx₃)/(a+b+c), (ay₁+by₂+cy₃)/(a+b+c))

Where a, b, c are sides opposite to vertices

## Shift of Origin

If origin shifted to (h,k):
New coordinates: X = x - h, Y = y - k
Old coordinates: x = X + h, y = Y + k

## Rotation of Axes

If axes rotated by angle θ:
x = X·cos(θ) - Y·sin(θ)
y = X·sin(θ) + Y·cos(θ)

## Locus Problems

To find locus:
1. Let point be (h,k)
2. Express given condition
3. Eliminate parameter if any
4. Replace (h,k) with (x,y)

## Important Results

### Equation of line parallel to x-axis:
y = k

### Equation of line parallel to y-axis:
x = k

### Lines through origin:
c = 0 in general form

### Diagonal of square:
Perpendicular lines with equal intercepts

## Common Mistakes to Avoid

- Sign errors in distance formula
- Wrong ratio in section formula (internal vs external)
- Not using absolute value in distance to line
- Confusing slope and angle
- Incorrect parametric representation
- Wrong identification of bisectors