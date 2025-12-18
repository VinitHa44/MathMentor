## Problem 1: Basic Permutation
**Question:** In how many ways can 5 boys and 3 girls sit in a row?

**Solution:**
Total persons = 8
Number of arrangements = 8! = 40320

**Answer:** 40,320

---

## Problem 2: Circular Arrangement
**Question:** In how many ways can 6 people sit around a circular table?

**Solution:**
Circular arrangements = (n-1)! = (6-1)! = 5! = 120

**Answer:** 120

---

## Problem 3: Combinations
**Question:** From 10 students, how many committees of 4 can be formed?

**Solution:**
¹⁰C₄ = 10!/(4!×6!) = (10×9×8×7)/(4×3×2×1) = 5040/24 = 210

**Answer:** 210

---

## Problem 4: Restricted Arrangement
**Question:** How many ways can 7 people sit in a row if 2 particular persons must sit together?

**Solution:**
Treat 2 persons as 1 unit
Units to arrange = 6
Arrangements = 6! × 2! = 720 × 2 = 1440

**Answer:** 1,440

---

## Problem 5: Selection with Condition
**Question:** From 6 men and 4 women, how many committees of 5 can be formed with at least 2 women?

**Solution:**
At least 2 women = 2W,3M or 3W,2M or 4W,1M

= ⁴C₂×⁶C₃ + ⁴C₃×⁶C₂ + ⁴C₄×⁶C₁
= 6×20 + 4×15 + 1×6
= 120 + 60 + 6 = 186

**Answer:** 186

---

## Problem 6: Word Arrangement
**Question:** How many distinct arrangements of letters in "MISSISSIPPI"?

**Solution:**
Total letters = 11
I appears 4 times, S appears 4 times, P appears 2 times, M appears 1 time

Arrangements = 11!/(4!×4!×2!) = 39,916,800/(24×24×2) = 34,650

**Answer:** 34,650

---

## Problem 7: Distribution
**Question:** In how many ways can 10 identical balls be distributed into 3 distinct boxes?

**Solution:**
Using stars and bars: ⁿ⁺ʳ⁻¹Cᵣ₋₁

= ¹⁰⁺³⁻¹C₃₋₁ = ¹²C₂ = 12×11/2 = 66

**Answer:** 66

---

## Problem 8: Digits Problem
**Question:** How many 4-digit numbers can be formed using digits 1,2,3,4,5 without repetition?

**Solution:**
⁵P₄ = 5!/(5-4)! = 5!/1! = 120

**Answer:** 120

---

## Problem 9: Selection from Groups
**Question:** From 5 consonants and 4 vowels, how many words of 3 consonants and 2 vowels can be formed?

**Solution:**
Selection: ⁵C₃ × ⁴C₂ = 10 × 6 = 60
Arrangements of 5 letters: 5! = 120

Total = 60 × 120 = 7,200

**Answer:** 7,200

---

## Problem 10: Derangement
**Question:** In how many ways can 4 letters be placed in 4 envelopes so that no letter is in correct envelope?

**Solution:**
Derangements D₄ = 4![1 - 1/1! + 1/2! - 1/3! + 1/4!]
= 24[1 - 1 + 0.5 - 0.167 + 0.042]
= 24 × 0.375 = 9

**Answer:** 9

---

## Problem 11: Diagonal Selection
**Question:** How many diagonals can be drawn in a polygon of 10 sides?

**Solution:**
Total line segments = ¹⁰C₂ = 45
Sides = 10
Diagonals = 45 - 10 = 35

**Answer:** 35

---

## Problem 12: Arrangement with Repetition
**Question:** How many 3-digit even numbers can be formed using 1,2,3,4,5 (repetition allowed)?

**Solution:**
Last digit must be 2 or 4 (2 choices)
First digit: 5 choices
Second digit: 5 choices

Total = 5 × 5 × 2 = 50

**Answer:** 50

---

## Problem 13: Division into Groups
**Question:** In how many ways can 12 students be divided into 3 groups of 4 each?

**Solution:**
= 12!/(4!×4!×4!×3!)

3! divides because groups are identical

= 479,001,600/(24×24×24×6) = 5,775

**Answer:** 5,775

---

## Problem 14: Handshake Problem
**Question:** 20 people meet, each shakes hands with every other once. How many handshakes?

**Solution:**
²⁰C₂ = 20×19/2 = 190

**Answer:** 190

---

## Problem 15: Arrangement of Books
**Question:** In how many ways can 4 math, 3 physics, and 2 chemistry books be arranged on shelf if books of same subject are together?

**Solution:**
Groups = 3
Arrangement of groups = 3! = 6

Within groups:
Math: 4! = 24
Physics: 3! = 6
Chemistry: 2! = 2

Total = 6 × 24 × 6 × 2 = 1,728

**Answer:** 1,728

---

## Problem 16: Selection with At Least One
**Question:** From 8 books, how many ways to select at least one book?

**Solution:**
Total ways = 2⁸ - 1 = 256 - 1 = 255

(Subtract 1 for selecting none)

**Answer:** 255

---

## Problem 17: Rank of Word
**Question:** What is rank of word "GIRL" in dictionary order of all arrangements?

**Solution:**
Alphabetical: G, I, L, R

Words before GIRL:
Starting with G, I before R: GI__
- GILR: 1
- GIRL: This is what we want

Words starting with G, before I:
None (G is first)

Actually, let's count systematically:
Before G: None
GI: GILR (1), GIRL (2)
GL: 2 more
GR: 2 more

Rank = 2

**Answer:** 2 (requires full enumeration for accuracy)

---

## Problem 18: Conditional Selection
**Question:** From 10 points where no 3 are collinear, how many triangles can be formed?

**Solution:**
¹⁰C₃ = 10!/(3!×7!) = (10×9×8)/(3×2×1) = 720/6 = 120

**Answer:** 120

---

## Problem 19: Distribution with Empty Allowed
**Question:** Number of ways to distribute 5 distinct balls into 3 distinct boxes (empty boxes allowed)?

**Solution:**
Each ball has 3 choices
Total = 3⁵ = 243

**Answer:** 243

---

## Problem 20: Necklace Problem
**Question:** In how many ways can 6 different beads form a necklace?

**Solution:**
Circular arrangement with reflection symmetry

= (6-1)!/2 = 5!/2 = 120/2 = 60

**Answer:** 60