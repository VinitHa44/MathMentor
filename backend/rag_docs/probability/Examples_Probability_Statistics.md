## Problem 1: Basic Probability
**Question:** A die is rolled. Find probability of getting an even number.

**Solution:**
Favorable outcomes: {2, 4, 6} = 3
Total outcomes: 6

P(even) = 3/6 = 1/2

**Answer:** 1/2

---

## Problem 2: Cards Problem
**Question:** Find probability of drawing a king or a heart from standard deck.

**Solution:**
P(King) = 4/52
P(Heart) = 13/52
P(King and Heart) = 1/52

P(King or Heart) = 4/52 + 13/52 - 1/52 = 16/52 = 4/13

**Answer:** 4/13

---

## Problem 3: Conditional Probability
**Question:** In a class, 18 play soccer, 12 play basketball, 8 play both. If a student plays soccer, what's probability they play basketball?

**Solution:**
P(Basketball|Soccer) = P(Both)/P(Soccer)
= (8/total)/(18/total) = 8/18 = 4/9

**Answer:** 4/9

---

## Problem 4: Independent Events
**Question:** Two dice rolled. Find probability that sum is 7.

**Solution:**
Favorable: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) = 6 outcomes
Total: 36

P(sum = 7) = 6/36 = 1/6

**Answer:** 1/6

---

## Problem 5: Complement Rule
**Question:** Probability of hitting target is 0.3. Find probability of missing at least once in 3 shots.

**Solution:**
P(miss at least once) = 1 - P(hit all three)
= 1 - (0.3)³
= 1 - 0.027 = 0.973

**Answer:** 0.973

---

## Problem 6: Bayes' Theorem
**Question:** Bag A has 3 red, 2 black. Bag B has 2 red, 3 black. One ball drawn randomly. If it's red, find probability it's from Bag A.

**Solution:**
P(A) = 1/2, P(B) = 1/2
P(Red|A) = 3/5, P(Red|B) = 2/5

P(A|Red) = [P(Red|A)·P(A)]/[P(Red|A)·P(A) + P(Red|B)·P(B)]
= [(3/5)·(1/2)]/[(3/5)·(1/2) + (2/5)·(1/2)]
= (3/10)/[(3/10) + (2/10)]
= (3/10)/(5/10) = 3/5

**Answer:** 3/5

---

## Problem 7: Binomial Probability
**Question:** Coin tossed 5 times. Find probability of exactly 3 heads.

**Solution:**
P(X = 3) = ⁵C₃·(1/2)³·(1/2)²
= 10·(1/2)⁵
= 10/32 = 5/16

**Answer:** 5/16

---

## Problem 8: Expected Value
**Question:** Die rolled. Win ₹10 if even, lose ₹5 if odd. Find expected value.

**Solution:**
E(X) = 10·(1/2) + (-5)·(1/2)
= 5 - 2.5 = 2.5

**Answer:** ₹2.5

---

## Problem 9: Total Probability
**Question:** 3 machines produce 50%, 30%, 20% of items. Defect rates are 2%, 3%, 4%. Find probability of defect.

**Solution:**
P(Defect) = 0.5·0.02 + 0.3·0.03 + 0.2·0.04
= 0.01 + 0.009 + 0.008
= 0.027

**Answer:** 0.027 or 2.7%

---

## Problem 10: Mutually Exclusive
**Question:** P(A) = 0.4, P(B) = 0.5, P(A∪B) = 0.7. Find P(A∩B).

**Solution:**
P(A∪B) = P(A) + P(B) - P(A∩B)
0.7 = 0.4 + 0.5 - P(A∩B)
P(A∩B) = 0.2

**Answer:** 0.2

---

## Problem 11: At Least Problems
**Question:** 4 coins tossed. Find probability of at least 2 heads.

**Solution:**
P(at least 2 heads) = P(2H) + P(3H) + P(4H)
= ⁴C₂(1/2)⁴ + ⁴C₃(1/2)⁴ + ⁴C₄(1/2)⁴
= (6 + 4 + 1)/16 = 11/16

**Answer:** 11/16

---

## Problem 12: Variance
**Question:** Random variable X has values 1, 2, 3 with probabilities 0.2, 0.5, 0.3. Find variance.

**Solution:**
E(X) = 1(0.2) + 2(0.5) + 3(0.3) = 2.1

E(X²) = 1²(0.2) + 2²(0.5) + 3²(0.3)
= 0.2 + 2 + 2.7 = 4.9

Var(X) = E(X²) - [E(X)]²
= 4.9 - (2.1)² = 4.9 - 4.41 = 0.49

**Answer:** 0.49

---

## Problem 13: Selection Problem
**Question:** From 5 men and 4 women, 3 selected randomly. Find probability exactly 2 are men.

**Solution:**
Total ways: ⁹C₃ = 84

Ways (2M, 1W): ⁵C₂·⁴C₁ = 10·4 = 40

Probability = 40/84 = 10/21

**Answer:** 10/21

---

## Problem 14: Consecutive Events
**Question:** 2 cards drawn without replacement. Find probability both are aces.

**Solution:**
P(1st ace) = 4/52
P(2nd ace | 1st ace) = 3/51

P(both aces) = (4/52)·(3/51) = 12/2652 = 1/221

**Answer:** 1/221

---

## Problem 15: Odds
**Question:** If odds in favor of event are 3:2, find probability of event.

**Solution:**
Odds 3:2 means P(A):P(A') = 3:2

P(A) = 3/(3+2) = 3/5

**Answer:** 3/5

---

## Problem 16: Poisson Distribution
**Question:** Average 3 calls per hour. Find probability of exactly 5 calls in next hour.

**Solution:**
λ = 3, x = 5

P(X = 5) = (e⁻³·3⁵)/5!
= (e⁻³·243)/120
≈ 0.1008

**Answer:** ≈ 0.101 or 10.1%

---

## Problem 17: Geometric Probability
**Question:** Coin tossed until first head. Find probability it takes exactly 4 tosses.

**Solution:**
Need: TTT H

P = (1/2)³·(1/2) = 1/16

**Answer:** 1/16

---

## Problem 18: Hypergeometric
**Question:** Bag has 6 red, 4 blue balls. 3 drawn without replacement. Find probability of 2 red, 1 blue.

**Solution:**
P = [⁶C₂·⁴C₁]/[¹⁰C₃]
= (15·4)/120
= 60/120 = 1/2

**Answer:** 1/2

---

## Problem 19: Mean and SD
**Question:** Data: 2, 4, 6, 8, 10. Find mean and standard deviation.

**Solution:**
Mean = (2+4+6+8+10)/5 = 30/5 = 6

Variance = [(2-6)² + (4-6)² + (6-6)² + (8-6)² + (10-6)²]/5
= [16 + 4 + 0 + 4 + 16]/5 = 40/5 = 8

SD = √8 = 2√2 ≈ 2.83

**Answer:** Mean = 6, SD = 2√2

---

## Problem 20: False Positive
**Question:** Test 99% accurate for disease affecting 1% population. Person tests positive. Find actual probability they have disease.

**Solution:**
P(D) = 0.01, P(D') = 0.99
P(+|D) = 0.99, P(+|D') = 0.01

P(D|+) = [P(+|D)·P(D)]/[P(+|D)·P(D) + P(+|D')·P(D')]
= [0.99·0.01]/[0.99·0.01 + 0.01·0.99]
= 0.0099/(0.0099 + 0.0099) = 0.5

**Answer:** 50% (counterintuitive!)