# Permutations and Combinations

## Fundamental Principles

### Multiplication Principle
If an event can occur in m ways and another independent event can occur in n ways, then both events together can occur in m × n ways.

### Addition Principle
If an event can occur in m ways or another event can occur in n ways (mutually exclusive), then either event can occur in m + n ways.

## Factorial

### Definition
n! (n factorial) = n × (n-1) × (n-2) × ... × 3 × 2 × 1

### Special Cases
- 0! = 1
- 1! = 1

### Properties
- n! = n × (n-1)!
- n!/(n-r)! = n × (n-1) × ... × (n-r+1)

## Permutations

### Definition
Arrangement of objects where order matters.

### Formula: Permutations of n distinct objects taken r at a time

ⁿPᵣ = n!/(n-r)!

Alternative notation: P(n,r)

### Special Cases

All n objects arranged:
ⁿPₙ = n!

No selection (r = 0):
ⁿP₀ = 1

### Permutations with Repetition

When objects are repeated:

If n objects with n₁ of type 1, n₂ of type 2, ..., nₖ of type k:

Number of permutations = n! / (n₁! × n₂! × ... × nₖ!)

Where n = n₁ + n₂ + ... + nₖ

### Circular Permutations

Number of ways to arrange n distinct objects in a circle:
(n-1)!

If clockwise and anticlockwise are considered same:
(n-1)!/2

### Permutations with Restrictions

#### Adjacent objects (always together)
- Treat them as one unit
- Arrange units: (n-k+1)! where k objects are together
- Arrange within group: k!
- Total = (n-k+1)! × k!

#### Non-adjacent objects (never together)
- First arrange other objects
- Then place restricted objects in gaps

## Combinations

### Definition
Selection of objects where order does not matter.

### Formula: Combinations of n distinct objects taken r at a time

ⁿCᵣ = n! / [r!(n-r)!]

Alternative notations: C(n,r) or (n choose r)

### Properties

ⁿCᵣ = ⁿCₙ₋ᵣ

ⁿCᵣ + ⁿCᵣ₋₁ = ⁿ⁺¹Cᵣ (Pascal's Identity)

ⁿC₀ = ⁿCₙ = 1

ⁿC₁ = ⁿCₙ₋₁ = n

If ⁿCₓ = ⁿCᵧ then either x = y or x + y = n

### Summation Formulas

ⁿC₀ + ⁿC₁ + ⁿC₂ + ... + ⁿCₙ = 2ⁿ

ⁿC₀ + ⁿC₂ + ⁿC₄ + ... = ⁿC₁ + ⁿC₃ + ⁿC₅ + ... = 2ⁿ⁻¹

### Relationship Between P and C

ⁿPᵣ = r! × ⁿCᵣ

## Selection Problems

### Selection from Identical Objects

Number of ways to distribute n identical objects into r groups:
ⁿ⁺ʳ⁻¹Cᵣ₋₁

### Selection with Repetition Allowed

Selecting r objects from n types (repetition allowed):
ⁿ⁺ʳ⁻¹Cᵣ

### Division into Groups

#### Dividing n distinct objects into groups

Equal groups (r groups of size k each where n = rk):
n! / [(k!)ʳ × r!]

Unequal groups (groups of size n₁, n₂, ..., nᵣ):
n! / (n₁! × n₂! × ... × nᵣ!)

## Derangements

Number of ways to arrange n objects so that no object is in its original position:

Dₙ = n! × [1 - 1/1! + 1/2! - 1/3! + ... + (-1)ⁿ/n!]

Approximate value: Dₙ ≈ n!/e

## Restricted Combinations

### At least/At most problems

At least r objects from n:
ⁿCᵣ + ⁿCᵣ₊₁ + ... + ⁿCₙ

### Selections from Two Groups

From group A (m objects) and group B (n objects):

Selecting r objects with at least one from each:
Total - (selections from A only) - (selections from B only)
= ᵐ⁺ⁿCᵣ - ᵐCᵣ - ⁿCᵣ

## Distribution Problems

### Distributing n identical objects into r distinct boxes

With no restrictions:
ⁿ⁺ʳ⁻¹Cᵣ₋₁

With each box having at least one object:
ⁿ⁻¹Cᵣ₋₁

### Distributing n distinct objects into r identical boxes

Use Stirling numbers of the second kind S(n,r)

## Multinomial Theorem

(x₁ + x₂ + ... + xₘ)ⁿ

Coefficient of x₁ʳ¹ × x₂ʳ² × ... × xₘʳᵐ where r₁ + r₂ + ... + rₘ = n:

n! / (r₁! × r₂! × ... × rₘ!)

## Important Identities

ⁿCᵣ × ʳCₖ = ⁿCₖ × ⁿ⁻ᵏCᵣ₋ₖ

r × ⁿCᵣ = n × ⁿ⁻¹Cᵣ₋₁

Σ(r × ⁿCᵣ) from r=0 to n = n × 2ⁿ⁻¹

Σ(ⁿCᵣ)² = ²ⁿCₙ

## Geometric Applications

### Number of diagonals in a polygon of n sides
n(n-3)/2

### Number of triangles formed by n points
ⁿC₃ (if no three points are collinear)

### Number of straight lines from n points
ⁿC₂ (if no three points are collinear)

## Common Mistakes to Avoid

- Confusing permutation and combination
- Forgetting to account for identical objects
- Not considering restrictions properly
- Using wrong formula for circular arrangements
- Overcounting in division problems