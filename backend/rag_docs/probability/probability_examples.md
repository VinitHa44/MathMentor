## Example 1: Events and Set Operations

**Problem:**

Consider the experiment of rolling a die. Let A be the event 'getting a prime number', B be the event 'getting an odd number'. Write the sets representing the events:
- (i) A or B
- (ii) A and B
- (iii) A but not B
- (iv) not A

**Solution:**

Sample space: S = {1, 2, 3, 4, 5, 6}

Event A (prime numbers) = {2, 3, 5}

Event B (odd numbers) = {1, 3, 5}

**(i) A or B** = A ∪ B = {1, 2, 3, 5}

**(ii) A and B** = A ∩ B = {3, 5}

**(iii) A but not B** = A – B = {2}

**(iv) not A** = A' = {1, 4, 6}

---

## Example 2: Mutually Exclusive Events

**Problem:**

Two dice are thrown and the sum of the numbers is noted. Consider the following events:
- A: 'the sum is even'
- B: 'the sum is a multiple of 3'
- C: 'the sum is less than 4'
- D: 'the sum is greater than 11'

Which pairs of these events are mutually exclusive?

**Solution:**

Sample space: S = {(x, y) : x, y = 1, 2, 3, 4, 5, 6}, total 36 outcomes.

**Event A** (sum is even):
A = {(1,1), (1,3), (1,5), (2,2), (2,4), (2,6), (3,1), (3,3), (3,5), (4,2), (4,4), (4,6), (5,1), (5,3), (5,5), (6,2), (6,4), (6,6)}

**Event B** (sum is multiple of 3):
B = {(1,2), (2,1), (1,5), (5,1), (3,3), (2,4), (4,2), (3,6), (6,3), (4,5), (5,4), (6,6)}

**Event C** (sum < 4):
C = {(1,1), (2,1), (1,2)}

**Event D** (sum > 11):
D = {(6,6)}

**Checking intersections:**

- A ∩ B = {(1,5), (2,4), (3,3), (4,2), (5,1), (6,6)} ≠ ∅ → **Not mutually exclusive**
- A ∩ C ≠ ∅ → **Not mutually exclusive**
- A ∩ D ≠ ∅ → **Not mutually exclusive**
- B ∩ C ≠ ∅ → **Not mutually exclusive**
- B ∩ D ≠ ∅ → **Not mutually exclusive**
- **C ∩ D = ∅** → **Mutually exclusive**

**Answer:** Only C and D are mutually exclusive events.

---

## Example 3: Mutually Exclusive and Exhaustive Events

**Problem:**

A coin is tossed three times. Consider the following events:
- A: 'No head appears'
- B: 'Exactly one head appears'
- C: 'At least two heads appear'

Do they form a set of mutually exclusive and exhaustive events?

**Solution:**

Sample space: S = {HHH, HHT, HTH, THH, HTT, THT, TTH, TTT}

Event A = {TTT}
Event B = {HTT, THT, TTH}
Event C = {HHT, HTH, THH, HHH}

**Checking exhaustiveness:**
A ∪ B ∪ C = {TTT, HTT, THT, TTH, HHT, HTH, THH, HHH} = S ✓

Therefore, A, B, and C are **exhaustive events**.

**Checking mutual exclusivity:**
- A ∩ B = ∅
- A ∩ C = ∅
- B ∩ C = ∅

All pairs are disjoint, so they are **mutually exclusive**.

**Answer:** Yes, A, B, and C form a set of mutually exclusive and exhaustive events.

---

## Example 4: Card Probability

**Problem:**

One card is drawn from a well-shuffled deck of 52 cards. If each outcome is equally likely, calculate the probability that the card will be:
- (i) a diamond
- (ii) not an ace
- (iii) a black card (club or spade)
- (iv) not a diamond
- (v) not a black card

**Solution:**

Total outcomes = 52

**(i) Probability of a diamond:**
Number of diamonds = 13
P(diamond) = 13/52 = 1/4

**(ii) Probability of not an ace:**
Number of aces = 4
Number of non-aces = 52 - 4 = 48
P(not ace) = 48/52 = 12/13

**(iii) Probability of a black card:**
Number of black cards (clubs + spades) = 13 + 13 = 26
P(black card) = 26/52 = 1/2

**(iv) Probability of not a diamond:**
Number of non-diamonds = 52 - 13 = 39
P(not diamond) = 39/52 = 3/4

**(v) Probability of not a black card:**
Number of non-black cards (hearts + diamonds) = 26
P(not black) = 26/52 = 1/2

---

## Example 5: Conditional Probability - Coins

**Problem:**

A bag contains 3 red balls and 5 black balls. A ball is drawn at random from the bag. What is the probability that the ball drawn is:
- (i) red?
- (ii) not red?

**Solution:**

Total number of balls = 3 + 5 = 8

**(i) Probability of drawing a red ball:**
Number of red balls = 3
P(red) = 3/8

**(ii) Probability of not drawing a red ball:**
Number of non-red balls = 5
P(not red) = 5/8

**Note:** P(red) + P(not red) = 3/8 + 5/8 = 1 ✓

---

## Example 6: Probability with OR

**Problem:**

In a class of 60 students, 30 opted for Mathematics, 32 opted for Biology, and 24 opted for both Mathematics and Biology. If one of these students is selected at random, find the probability that:
- (i) the student opted for Mathematics or Biology
- (ii) the student opted for exactly one of the two subjects

**Solution:**

Let M = students who opted for Mathematics = 30
Let B = students who opted for Biology = 32
M ∩ B = students who opted for both = 24
Total students n(S) = 60

**(i) Probability of Mathematics OR Biology:**
Using: n(M ∪ B) = n(M) + n(B) - n(M ∩ B)
n(M ∪ B) = 30 + 32 - 24 = 38

P(M ∪ B) = 38/60 = 19/30

**(ii) Probability of exactly one subject:**
Students with exactly one subject = (M only) + (B only)
M only = 30 - 24 = 6
B only = 32 - 24 = 8
Exactly one = 6 + 8 = 14

P(exactly one) = 14/60 = 7/30

---

## Key Formulas

### Basic Probability
- $P(A) = \frac{\text{Number of favorable outcomes}}{\text{Total number of outcomes}}$
- $0 \leq P(A) \leq 1$
- $P(S) = 1$ (certain event)
- $P(\emptyset) = 0$ (impossible event)

### Complement Rule
- $P(A') = 1 - P(A)$

### Addition Rule
- $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
- For mutually exclusive events: $P(A \cup B) = P(A) + P(B)$

### Properties
- **Mutually Exclusive:** $A \cap B = \emptyset$
- **Exhaustive:** $A_1 \cup A_2 \cup ... \cup A_n = S$
