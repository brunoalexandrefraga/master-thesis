# Demonstration - $cos[ϕₚ·sin(ωₘt)] ≈ 1$ (via Taylor series)

## Step 1: Definition of Taylor Series

The Taylor series of a function $f(x)$ around $x = 0$ (Maclaurin series) is:

$$
f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!} x^n
$$

For $f(x) = \cos(x)$, the derivatives are:

- $f(x) = \cos(x)$  
- $f'(x) = -\sin(x)$  
- $f''(x) = -\cos(x)$  
- $f^{(3)}(x) = \sin(x)$  
- $f^{(4)}(x) = \cos(x)$, and so on.

Evaluating at $x = 0$:

- $\cos(0) = 1$  
- $-\sin(0) = 0$  
- $-\cos(0) = -1$  
- $\sin(0) = 0$  
- $\cos(0) = 1$

So the Taylor series becomes:

$$
\cos(x) = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n)!} x^{2n} = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots
$$

---

## Step 2: Apply to $\cos[\varphi_p \sin(\omega_m t)]$

Let $x = \varphi_p \sin(\omega_m t)$. Then:

$$
\cos[\varphi_p \sin(\omega_m t)] = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n)!} \left(\varphi_p \sin(\omega_m t)\right)^{2n}
$$

Expanding the first few terms:

$$
= 1 - \frac{1}{2} \left(\varphi_p \sin(\omega_m t)\right)^2 + \frac{1}{24} \left(\varphi_p \sin(\omega_m t)\right)^4 - \cdots
$$

$$
= 1 - \frac{\varphi_p^2}{2} \sin^2(\omega_m t) + \frac{\varphi_p^4}{24} \sin^4(\omega_m t) - \cdots
$$

---

## Step 3: Approximate for small $\varphi_p$

If $\varphi_p \ll 1$, then $\varphi_p^2, \varphi_p^4, \dots$ are very small and can be neglected.

Keeping only the leading constant term:

$$
\cos[\varphi_p \sin(\omega_m t)] \approx 1
$$

---

## ✅ Conclusion

We have shown, starting from the Taylor series definition, that:

$$
\cos[\varphi_p \sin(\omega_m t)] \approx 1
\quad \text{(when } \varphi_p \ll 1 \text{)}
$$

This is part of the **narrowband phase modulation** approximation.

---

## Tags

`#phase-modulation` `#taylor-series` `#approximations` `#narrowband`
