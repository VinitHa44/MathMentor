# Calculus: Limits and Derivatives - Solved Examples

*Curated from NCERT Class 11 Mathematics*

---

## Example 1: Limits of Polynomial Functions

**Problem:** Find the limits:

(i) $\lim_{x \to 1} [x^3 - x^2 + 1]$

(ii) $\lim_{x \to 3} [x(x + 1)]$

(iii) $\lim_{x \to -1} [1 + x + x^2 + ... + x^{10}]$

**Solution:**

The required limits are all limits of polynomial functions. Hence the limits are the values of the function at the prescribed points.

(i) $\lim_{x \to 1} [x^3 - x^2 + 1] = 1^3 - 1^2 + 1 = 1$

(ii) $\lim_{x \to 3} [x(x + 1)] = 3(3 + 1) = 3 \times 4 = 12$

(iii) $\lim_{x \to -1} [1 + x + x^2 + ... + x^{10}]$
     $= 1 + (-1) + (-1)^2 + ... + (-1)^{10}$
     $= 1 - 1 + 1 - 1 + ... + 1 = 1$

---

## Example 2: Factorization Method for Limits

**Problem:** Find $\lim_{x \to 1} \frac{x^{15} - 1}{x^{10} - 1}$

**Solution:**

We have:
$$\lim_{x \to 1} \frac{x^{15} - 1}{x^{10} - 1}$$

Since both numerator and denominator approach 0 as x → 1, we use factorization:

Using the identity: $x^n - 1 = (x - 1)(x^{n-1} + x^{n-2} + ... + x + 1)$

$$= \lim_{x \to 1} \frac{(x-1)(x^{14} + x^{13} + ... + x + 1)}{(x-1)(x^9 + x^8 + ... + x + 1)}$$

Canceling (x - 1):

$$= \lim_{x \to 1} \frac{x^{14} + x^{13} + ... + x + 1}{x^9 + x^8 + ... + x + 1}$$

Substituting x = 1:

$$= \frac{1 + 1 + ... + 1 \text{ (15 times)}}{1 + 1 + ... + 1 \text{ (10 times)}} = \frac{15}{10} = \frac{3}{2}$$

---

## Example 3: Rationalization Method

**Problem:** Find $\lim_{x \to 0} \frac{\sqrt{1+x} - 1}{x}$

**Solution:**

Direct substitution gives 0/0 form. We rationalize the numerator:

$$\lim_{x \to 0} \frac{\sqrt{1+x} - 1}{x} \times \frac{\sqrt{1+x} + 1}{\sqrt{1+x} + 1}$$

$$= \lim_{x \to 0} \frac{(1+x) - 1}{x(\sqrt{1+x} + 1)}$$

$$= \lim_{x \to 0} \frac{x}{x(\sqrt{1+x} + 1)}$$

$$= \lim_{x \to 0} \frac{1}{\sqrt{1+x} + 1}$$

Substituting x = 0:

$$= \frac{1}{\sqrt{1} + 1} = \frac{1}{2}$$

---

## Example 4: Derivative Using First Principles

**Problem:** Find the derivative of $f(x) = x^2$ from first principles.

**Solution:**

By definition:
$$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$

For $f(x) = x^2$:

$$f'(x) = \lim_{h \to 0} \frac{(x+h)^2 - x^2}{h}$$

$$= \lim_{h \to 0} \frac{x^2 + 2xh + h^2 - x^2}{h}$$

$$= \lim_{h \to 0} \frac{2xh + h^2}{h}$$

$$= \lim_{h \to 0} \frac{h(2x + h)}{h}$$

$$= \lim_{h \to 0} (2x + h)$$

$$= 2x$$

Therefore, $\frac{d}{dx}(x^2) = 2x$

---

## Example 5: Derivative of a Constant

**Problem:** Find the derivative of $f(x) = 5$ (a constant function).

**Solution:**

Using first principles:
$$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$

Since f(x) = 5 for all x:

$$f'(x) = \lim_{h \to 0} \frac{5 - 5}{h} = \lim_{h \to 0} \frac{0}{h} = 0$$

**Conclusion:** The derivative of any constant is zero.

---

## Example 6: Power Rule Application

**Problem:** Find the derivative of $f(x) = x^4 + 3x^3 - 5x + 2$

**Solution:**

Using the power rule and sum rule:

$$f'(x) = \frac{d}{dx}(x^4) + \frac{d}{dx}(3x^3) - \frac{d}{dx}(5x) + \frac{d}{dx}(2)$$

$$= 4x^3 + 3 \cdot 3x^2 - 5 + 0$$

$$= 4x^3 + 9x^2 - 5$$

---

## Example 7: Product Rule

**Problem:** Find the derivative of $f(x) = (x^2 + 1)(x^3 - 2)$

**Solution:**

Using the product rule: $(uv)' = u'v + uv'$

Let $u = x^2 + 1$ and $v = x^3 - 2$

Then: $u' = 2x$ and $v' = 3x^2$

$$f'(x) = (2x)(x^3 - 2) + (x^2 + 1)(3x^2)$$

$$= 2x^4 - 4x + 3x^4 + 3x^2$$

$$= 5x^4 + 3x^2 - 4x$$

---

## Key Formulas

### Limits
- $\lim_{x \to a} k = k$ (constant)
- $\lim_{x \to a} x = a$
- $\lim_{x \to a} [f(x) \pm g(x)] = \lim_{x \to a} f(x) \pm \lim_{x \to a} g(x)$

### Derivatives
- $\frac{d}{dx}(c) = 0$ (constant)
- $\frac{d}{dx}(x^n) = nx^{n-1}$ (power rule)
- $\frac{d}{dx}[f(x) \pm g(x)] = f'(x) \pm g'(x)$ (sum/difference rule)
- $\frac{d}{dx}[f(x) \cdot g(x)] = f'(x)g(x) + f(x)g'(x)$ (product rule)
