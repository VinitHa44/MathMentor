# Vectors

## Vector Definition

A vector has both magnitude and direction.

Notation: **a**, →a, or bold **a**

Position vector of point P(x,y,z): **r** = x**i** + y**j** + z**k**

## Unit Vectors

Vector with magnitude 1

**i**, **j**, **k** are unit vectors along x, y, z axes

For vector **a**: Unit vector â = **a**/|**a**|

## Magnitude of a Vector

For **a** = a₁**i** + a₂**j** + a₃**k**:

|**a**| = √(a₁² + a₂² + a₃²)

## Direction Cosines and Ratios

### Direction Cosines (l, m, n):
If vector makes angles α, β, γ with axes:

l = cos(α), m = cos(β), n = cos(γ)

l² + m² + n² = 1

### Direction Ratios (a, b, c):
Proportional to direction cosines

If direction ratios are a, b, c:
l = a/√(a²+b²+c²), m = b/√(a²+b²+c²), n = c/√(a²+b²+c²)

## Vector Operations

### Addition
**a** + **b** = (a₁+b₁)**i** + (a₂+b₂)**j** + (a₃+b₃)**k**

Properties:
- **a** + **b** = **b** + **a** (commutative)
- (**a** + **b**) + **c** = **a** + (**b** + **c**) (associative)
- **a** + **0** = **a**
- **a** + (-**a**) = **0**

### Scalar Multiplication
k**a** = ka₁**i** + ka₂**j** + ka₃**k**

Properties:
- k(**a** + **b**) = k**a** + k**b**
- (k + m)**a** = k**a** + m**a**
- k(m**a**) = (km)**a**
- 1·**a** = **a**

### Subtraction
**a** - **b** = (a₁-b₁)**i** + (a₂-b₂)**j** + (a₃-b₃)**k**

## Position Vector

Vector from origin to point P(x,y,z): **OP** = x**i** + y**j** + z**k**

Vector from A(x₁,y₁,z₁) to B(x₂,y₂,z₂):
**AB** = (x₂-x₁)**i** + (y₂-y₁)**j** + (z₂-z₁)**k**

## Section Formula

Point dividing line from **a** to **b** in ratio m:n:

**Internal:** **r** = (m**b** + n**a**)/(m+n)

**External:** **r** = (m**b** - n**a**)/(m-n)

**Midpoint:** **r** = (**a** + **b**)/2

## Scalar (Dot) Product

**a**·**b** = |**a**||**b**|cos(θ)

In component form:
**a**·**b** = a₁b₁ + a₂b₂ + a₃b₃

### Properties:
- **a**·**b** = **b**·**a** (commutative)
- **a**·(**b** + **c**) = **a**·**b** + **a**·**c** (distributive)
- k(**a**·**b**) = (k**a**)·**b** = **a**·(k**b**)
- **a**·**a** = |**a**|²
- **i**·**i** = **j**·**j** = **k**·**k** = 1
- **i**·**j** = **j**·**k** = **k**·**i** = 0

### Angle Between Vectors:
cos(θ) = (**a**·**b**)/(|**a**||**b**|)

### Perpendicular Vectors:
**a** ⊥ **b** if and only if **a**·**b** = 0

### Projection:
Projection of **a** on **b** = (**a**·**b**)/|**b**|

## Vector (Cross) Product

**a** × **b** = |**a**||**b**|sin(θ)**n̂**

Where **n̂** is unit vector perpendicular to both **a** and **b** (right-hand rule)

In component form:
**a** × **b** = |**i**  **j**  **k**|
              |a₁  a₂  a₃|
              |b₁  b₂  b₃|

= (a₂b₃-a₃b₂)**i** + (a₃b₁-a₁b₃)**j** + (a₁b₂-a₂b₁)**k**

### Properties:
- **a** × **b** = -**b** × **a** (anti-commutative)
- **a** × (**b** + **c**) = **a** × **b** + **a** × **c** (distributive)
- k(**a** × **b**) = (k**a**) × **b** = **a** × (k**b**)
- **a** × **a** = **0**
- **i** × **j** = **k**, **j** × **k** = **i**, **k** × **i** = **j**
- **j** × **i** = -**k**, **k** × **j** = -**i**, **i** × **k** = -**j**

### Parallel Vectors:
**a** ∥ **b** if and only if **a** × **b** = **0**

### Area of Parallelogram:
Area = |**a** × **b**|

### Area of Triangle:
Area = (1/2)|**a** × **b**|

## Scalar Triple Product

[**a** **b** **c**] = **a**·(**b** × **c**)

= |a₁  a₂  a₃|
  |b₁  b₂  b₃|
  |c₁  c₂  c₃|

### Properties:
- [**a** **b** **c**] = [**b** **c** **a**] = [**c** **a** **b**] (cyclic)
- [**a** **b** **c**] = -[**b** **a** **c**] (anti-cyclic)
- [**a** **b** **c**] = 0 if vectors are coplanar

### Volume of Parallelepiped:
V = |[**a** **b** **c**]|

### Volume of Tetrahedron:
V = (1/6)|[**a** **b** **c**]|

## Vector Triple Product

**a** × (**b** × **c**) = (**a**·**c**)**b** - (**a**·**b**)**c**

(**a** × **b**) × **c** = (**a**·**c**)**b** - (**b**·**c**)**a**

**Note:** Vector triple product is not associative

## Coplanar Vectors

Vectors are coplanar if [**a** **b** **c**] = 0

Or if one vector can be expressed as linear combination of others:
**c** = λ**a** + μ**b**

## Collinear Vectors

Vectors are collinear if **a** = k**b** for some scalar k

Or if **a** × **b** = **0**

## Linear Independence

Vectors **a**, **b**, **c** are linearly independent if:
λ**a** + μ**b** + ν**c** = **0** implies λ = μ = ν = 0

Equivalently: [**a** **b** **c**] ≠ 0

## Reciprocal System of Vectors

For non-coplanar vectors **a**, **b**, **c**:

**a**' = (**b** × **c**)/[**a** **b** **c**]
**b**' = (**c** × **a**)/[**a** **b** **c**]
**c**' = (**a** × **b**)/[**a** **b** **c**]

Properties:
- **a**·**a**' = **b**·**b**' = **c**·**c**' = 1
- **a**·**b**' = **a**·**c**' = 0 (and similar)
- [**a**' **b**' **c**'] = 1/[**a** **b** **c**]

## Important Vector Identities

(**a** × **b**)² = |**a**|²|**b**|² - (**a**·**b**)² (Lagrange's identity)

**a** × (**b** × **c**) + **b** × (**c** × **a**) + **c** × (**a** × **b**) = **0** (Jacobi identity)

(**a** × **b**)·(**c** × **d**) = (**a**·**c**)(**b**·**d**) - (**a**·**d**)(**b**·**c**)

## Application: Lines and Planes

### Vector equation of line:
**r** = **a** + λ**b**

Where **a** is position vector of a point and **b** is direction vector

### Vector equation of plane:
**r**·**n** = d

Where **n** is normal to plane

## Common Mistakes to Avoid

- Confusing dot and cross product
- Wrong order in cross product (not commutative)
- Forgetting right-hand rule for cross product
- Sign errors in scalar triple product
- Not checking if vectors are coplanar before solving
- Incorrect application of vector triple product formula
- Confusing magnitude with components

## Important Results

|**a** + **b**|² = |**a**|² + |**b**|² + 2**a**·**b**

|**a** - **b**|² = |**a**|² + |**b**|² - 2**a**·**b**

|**a** + **b**|² + |**a** - **b**|² = 2(|**a**|² + |**b**|²)

If **a** ⊥ **b**: |**a** + **b**|² = |**a**|² + |**b**|²

For unit vectors: |**â** + **b̂**| = 2cos(θ/2) where θ is angle between them