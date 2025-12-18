# Three-Dimensional Geometry

## Coordinate System

Point P in 3D space: P(x, y, z)

## Distance Formula

Distance between points A(x₁,y₁,z₁) and B(x₂,y₂,z₂):

d = √[(x₂-x₁)² + (y₂-y₁)² + (z₂-z₁)²]

Distance from origin: d = √(x² + y² + z²)

## Section Formula

Point dividing line from A to B in ratio m:n:

**Internal:**
x = (mx₂ + nx₁)/(m+n)
y = (my₂ + ny₁)/(m+n)
z = (mz₂ + nz₁)/(m+n)

**External:**
x = (mx₂ - nx₁)/(m-n)
y = (my₂ - ny₁)/(m-n)
z = (mz₂ - nz₁)/(m-n)

**Midpoint:**
((x₁+x₂)/2, (y₁+y₂)/2, (z₁+z₂)/2)

## Direction Cosines

If a line makes angles α, β, γ with x, y, z axes:

Direction cosines: l = cos(α), m = cos(β), n = cos(γ)

**Fundamental relation:**
l² + m² + n² = 1

## Direction Ratios

If direction cosines are l, m, n, then direction ratios are proportional: a, b, c

Relation: l = a/√(a²+b²+c²), m = b/√(a²+b²+c²), n = c/√(a²+b²+c²)

Direction ratios of line joining (x₁,y₁,z₁) and (x₂,y₂,z₂):
a = x₂-x₁, b = y₂-y₁, c = z₂-z₁

## Angle Between Two Lines

If direction cosines are (l₁,m₁,n₁) and (l₂,m₂,n₂):

cos(θ) = l₁l₂ + m₁m₂ + n₁n₂

If direction ratios are (a₁,b₁,c₁) and (a₂,b₂,c₂):

cos(θ) = (a₁a₂ + b₁b₂ + c₁c₂)/[√(a₁²+b₁²+c₁²)·√(a₂²+b₂²+c₂²)]

### Perpendicular Lines:
a₁a₂ + b₁b₂ + c₁c₂ = 0

### Parallel Lines:
a₁/a₂ = b₁/b₂ = c₁/c₂

## Equation of a Line

### Cartesian Form (Symmetric form):
(x - x₁)/a = (y - y₁)/b = (z - z₁)/c

Where (x₁,y₁,z₁) is a point and a,b,c are direction ratios

### Two-Point Form:
(x - x₁)/(x₂ - x₁) = (y - y₁)/(y₂ - y₁) = (z - z₁)/(z₂ - z₁)

### Vector Form:
**r** = **a** + λ**b**

Where **a** is position vector of point and **b** is direction vector

### General Form (Intersection of two planes):
A₁x + B₁y + C₁z + D₁ = 0
A₂x + B₂y + C₂z + D₂ = 0

## Equation of a Plane

### General Form:
Ax + By + Cz + D = 0

Normal vector: **n** = A**i** + B**j** + C**k**

### Normal Form:
lx + my + nz = p

Where (l,m,n) are direction cosines of normal and p is perpendicular distance from origin

### Intercept Form:
x/a + y/b + z/c = 1

Where a, b, c are x, y, z intercepts

### Point-Normal Form:
A(x - x₁) + B(y - y₁) + C(z - z₁) = 0

Plane through (x₁,y₁,z₁) with normal (A,B,C)

### Three-Point Form:
Plane through points (x₁,y₁,z₁), (x₂,y₂,z₂), (x₃,y₃,z₃):

|x-x₁   y-y₁   z-z₁|
|x₂-x₁  y₂-y₁  z₂-z₁| = 0
|x₃-x₁  y₃-y₁  z₃-z₁|

### Vector Form:
**r**·**n** = d

Or: (**r** - **a**)·**n** = 0

## Distance from Point to Plane

Distance from (x₁,y₁,z₁) to plane Ax + By + Cz + D = 0:

d = |Ax₁ + By₁ + Cz₁ + D|/√(A² + B² + C²)

## Distance Between Parallel Planes

For Ax + By + Cz + D₁ = 0 and Ax + By + Cz + D₂ = 0:

d = |D₂ - D₁|/√(A² + B² + C²)

## Angle Between Two Planes

If normal vectors are **n₁** = (A₁,B₁,C₁) and **n₂** = (A₂,B₂,C₂):

cos(θ) = (A₁A₂ + B₁B₂ + C₁C₂)/[√(A₁²+B₁²+C₁²)·√(A₂²+B₂²+C₂²)]

### Perpendicular Planes:
A₁A₂ + B₁B₂ + C₁C₂ = 0

### Parallel Planes:
A₁/A₂ = B₁/B₂ = C₁/C₂

## Angle Between Line and Plane

If line has direction ratios (a,b,c) and plane has normal (A,B,C):

sin(θ) = |aA + bB + cC|/[√(a²+b²+c²)·√(A²+B²+C²)]

### Line parallel to plane:
aA + bB + cC = 0

### Line perpendicular to plane:
a/A = b/B = c/C

## Distance from Point to Line

Distance from point P(x₁,y₁,z₁) to line **r** = **a** + λ**b**:

d = |(**a** - **p**) × **b**|/|**b**|

Where **p** is position vector of P

## Shortest Distance Between Skew Lines

For lines **r** = **a₁** + λ**b₁** and **r** = **a₂** + μ**b₂**:

d = |(**a₂** - **a₁**)·(**b₁** × **b₂**)|/|**b₁** × **b₂**|

In Cartesian form, if lines are:
(x-x₁)/a₁ = (y-y₁)/b₁ = (z-z₁)/c₁
(x-x₂)/a₂ = (y-y₂)/b₂ = (z-z₂)/c₂

d = |x₂-x₁  y₂-y₁  z₂-z₁|
    |a₁     b₁     c₁    |
    |a₂     b₂     c₂    |
    ÷ √[(b₁c₂-b₂c₁)² + (c₁a₂-c₂a₁)² + (a₁b₂-a₂b₁)²]

## Coplanar Lines

Two lines are coplanar if shortest distance = 0

Or if (**a₂** - **a₁**)·(**b₁** × **b₂**) = 0

## Condition for Intersection

Lines intersect if:
1. They are coplanar
2. The point of intersection satisfies both equations

## Family of Planes

### Through intersection of L₁ = 0 and L₂ = 0:
L₁ + λL₂ = 0

### Through line **r** = **a** + λ**b**:
(**r** - **a**)·**n** = 0 where **n** ⊥ **b**

## Plane Through Three Points

Equation: |x-x₁  y-y₁  z-z₁|
         |x₂-x₁ y₂-y₁ z₂-z₁| = 0
         |x₃-x₁ y₃-y₁ z₃-z₁|

## Image of a Point

Image of (x₁,y₁,z₁) in plane Ax + By + Cz + D = 0:

(x₂-x₁)/A = (y₂-y₁)/B = (z₂-z₁)/C = -2(Ax₁+By₁+Cz₁+D)/(A²+B²+C²)

## Foot of Perpendicular

From point (x₁,y₁,z₁) to plane Ax + By + Cz + D = 0:

(x-x₁)/A = (y-y₁)/B = (z-z₁)/C = -(Ax₁+By₁+Cz₁+D)/(A²+B²+C²)

## Equation of Sphere

### Centre at origin, radius r:
x² + y² + z² = r²

### Centre at (a,b,c), radius r:
(x-a)² + (y-b)² + (z-c)² = r²

### General Form:
x² + y² + z² + 2ux + 2vy + 2wz + d = 0

Centre: (-u, -v, -w)
Radius: √(u² + v² + w² - d)

## Plane Section of a Sphere

Intersection of plane and sphere is a circle

If plane passes through center: Great circle
Otherwise: Small circle

## Common Mistakes to Avoid

- Forgetting condition l² + m² + n² = 1 for direction cosines
- Sign errors in distance formulas
- Wrong application of shortest distance formula
- Not checking if lines are skew before finding shortest distance
- Confusing direction ratios with direction cosines
- Incorrect determinant expansion in three-point form

## Important Results

Line parallel to coordinate axes:
- Parallel to x-axis: b = 0, c = 0
- Parallel to y-axis: a = 0, c = 0
- Parallel to z-axis: a = 0, b = 0

Plane parallel to coordinate axes:
- Parallel to xy-plane: C = 0
- Parallel to yz-plane: A = 0
- Parallel to zx-plane: B = 0

Coordinate planes:
- xy-plane: z = 0
- yz-plane: x = 0
- zx-plane: y = 0