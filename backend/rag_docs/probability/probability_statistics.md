# Probability and Statistics

## Basic Probability

### Sample Space
Set of all possible outcomes, denoted by S or Ω

### Event
A subset of sample space

### Probability Definition
For equally likely outcomes:

P(A) = n(A)/n(S) = (Number of favorable outcomes)/(Total number of outcomes)

Where 0 ≤ P(A) ≤ 1

## Axiomatic Approach

For any event A:
- 0 ≤ P(A) ≤ 1
- P(S) = 1 (certainty)
- P(∅) = 0 (impossible event)

For mutually exclusive events A₁, A₂, ...:
P(A₁ ∪ A₂ ∪ ...) = P(A₁) + P(A₂) + ...

## Complementary Events

P(A') = 1 - P(A)

Where A' is "not A"

## Addition Theorems

### For any two events:
P(A ∪ B) = P(A) + P(B) - P(A ∩ B)

### For mutually exclusive events:
P(A ∪ B) = P(A) + P(B)
Since P(A ∩ B) = 0

### For three events:
P(A ∪ B ∪ C) = P(A) + P(B) + P(C) - P(A ∩ B) - P(B ∩ C) - P(A ∩ C) + P(A ∩ B ∩ C)

## Conditional Probability

Probability of A given B has occurred:

P(A|B) = P(A ∩ B) / P(B), where P(B) ≠ 0

### Properties
P(S|B) = 1
P(A'|B) = 1 - P(A|B)
P(A ∪ B|C) = P(A|C) + P(B|C) - P(A ∩ B|C)

## Multiplication Theorem

### General case:
P(A ∩ B) = P(A) · P(B|A) = P(B) · P(A|B)

### For independent events:
P(A ∩ B) = P(A) · P(B)

### For three events:
P(A ∩ B ∩ C) = P(A) · P(B|A) · P(C|A ∩ B)

## Independent Events

Events A and B are independent if:
P(A ∩ B) = P(A) · P(B)

Equivalently:
- P(A|B) = P(A)
- P(B|A) = P(B)

### Pairwise vs Mutually Independent

Three events A, B, C are mutually independent if:
- P(A ∩ B) = P(A)·P(B)
- P(B ∩ C) = P(B)·P(C)
- P(A ∩ C) = P(A)·P(C)
- P(A ∩ B ∩ C) = P(A)·P(B)·P(C)

## Law of Total Probability

If B₁, B₂, ..., Bₙ partition the sample space, then:

P(A) = P(A|B₁)·P(B₁) + P(A|B₂)·P(B₂) + ... + P(A|Bₙ)·P(Bₙ)

Or: P(A) = Σ P(A|Bᵢ)·P(Bᵢ)

## Bayes' Theorem

If B₁, B₂, ..., Bₙ partition the sample space:

P(Bᵢ|A) = [P(A|Bᵢ)·P(Bᵢ)] / [Σ P(A|Bⱼ)·P(Bⱼ)]

For two events:
P(B|A) = [P(A|B)·P(B)] / P(A)

## Random Variables

### Definition
A function that assigns a real number to each outcome in sample space.

### Types
- Discrete: Takes countable values
- Continuous: Takes any value in an interval

## Probability Distribution

### Discrete Random Variable
P(X = xᵢ) = pᵢ where Σ pᵢ = 1

### Probability Mass Function (PMF)
Lists all possible values and their probabilities

### Cumulative Distribution Function (CDF)
F(x) = P(X ≤ x)

## Expectation (Mean)

### Discrete:
E(X) = μ = Σ xᵢ·P(X = xᵢ)

### Properties:
E(aX + b) = a·E(X) + b
E(X + Y) = E(X) + E(Y)
E(XY) = E(X)·E(Y), if X and Y are independent

## Variance

Var(X) = σ² = E[(X - μ)²] = E(X²) - [E(X)]²

Standard Deviation: σ = √Var(X)

### Properties:
Var(aX + b) = a²·Var(X)
Var(X + Y) = Var(X) + Var(Y), if X and Y are independent

## Binomial Distribution

For n independent trials with success probability p:

P(X = r) = ⁿCᵣ · pʳ · (1-p)ⁿ⁻ʳ

Where r = 0, 1, 2, ..., n

Mean: μ = np
Variance: σ² = np(1-p)

## Poisson Distribution

For rare events:

P(X = r) = (e^(-λ) · λʳ) / r!

Where λ is the average rate

Mean: μ = λ
Variance: σ² = λ

## Normal Distribution

Probability Density Function:

f(x) = [1/(σ√(2π))] · e^[-(x-μ)²/(2σ²)]

Mean: μ
Variance: σ²

Standard Normal: μ = 0, σ = 1

## Statistics

### Mean (Average)
Mean = (x₁ + x₂ + ... + xₙ)/n = Σxᵢ/n

For grouped data:
Mean = Σfᵢxᵢ/Σfᵢ

### Median
Middle value when data is arranged in order

For n values:
- If n is odd: Median = (n+1)/2 th value
- If n is even: Median = average of n/2 and (n/2 + 1) th values

### Mode
Most frequently occurring value

### Range
Range = Maximum value - Minimum value

### Variance
s² = Σ(xᵢ - x̄)²/n = [Σxᵢ² - (Σxᵢ)²/n]/n

### Standard Deviation
s = √(variance)

### Coefficient of Variation
CV = (s/x̄) × 100%

## Important Formulas

### For Permutations and Probability
P(at least one) = 1 - P(none)
P(exactly one) = P(first only) + P(second only) + ...

### Odds
If P(A) = p, then:
Odds in favor = p/(1-p)
Odds against = (1-p)/p

### Probability with Replacement
Events remain independent
Total outcomes = n^r for r selections from n items

### Probability without Replacement
Events are dependent
Use conditional probability

## Common Probability Problems

### Card Problems
- Total cards = 52
- Suits = 4 (13 each)
- Face cards = 12
- Aces = 4

### Dice Problems
- Single die: 6 outcomes
- Two dice: 36 outcomes
- Sum formulas important

### Coin Problems
- Single coin: 2 outcomes
- n coins: 2ⁿ outcomes

## Hypergeometric Distribution

Sampling without replacement:

P(X = r) = [ᴷCᵣ · ᴺ⁻ᴷCₙ₋ᵣ] / [ᴺCₙ]

Where:
- N = population size
- K = successes in population
- n = sample size
- r = successes in sample

## Common Mistakes to Avoid

- Confusing P(A|B) with P(B|A)
- Not checking if events are independent
- Wrong application of addition vs multiplication
- Forgetting to check if events are mutually exclusive
- Incorrect use of complement rule
- Not considering order in probability calculations