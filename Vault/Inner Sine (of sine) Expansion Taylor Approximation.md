# Demonstration - $\sin[ϕₚ·sin(ωₘt)] ≈ ϕₚ·\sin(ωₘt)$ (via Taylor series)

## Step 1: Definition of Taylor Series

The Taylor series of a function $f(x)$ around $x = 0$ (Maclaurin series) is:

$$
f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!} x^n
$$

For $f(x) = \sin(x)$, the derivatives are:

- $f(x) = \sin(x)$  
- $f'(x) = \cos(x)$  
- $f''(x) = -\sin(x)$  
- $f^{(3)}(x) = -\cos(x)$  
- $f^{(4)}(x) = \sin(x)$, and so on.

Evaluating at $x = 0$:

- $\sin(0) = 0$  
- $\cos(0) = 1$  
- $-\sin(0) = 0$  
- $-\cos(0) = -1$

So the Taylor series becomes:

$$
\sin(x) = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)!} x^{2n+1} = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots
$$

---

## Step 2: Apply to $\sin[\varphi_p \sin(\omega_m t)]$

Let $x = \varphi_p \sin(\omega_m t)$. Then:

$$
\sin[\varphi_p \sin(\omega_m t)] = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)!} \left(\varphi_p \sin(\omega_m t)\right)^{2n+1}
$$

Expanding the first few terms:

$$
= \varphi_p \sin(\omega_m t) - \frac{1}{6} \left(\varphi_p \sin(\omega_m t)\right)^3 + \frac{1}{120} \left(\varphi_p \sin(\omega_m t)\right)^5 - \cdots
$$

$$
= \varphi_p \sin(\omega_m t) - \frac{\varphi_p^3}{6} \sin^3(\omega_m t) + \frac{\varphi_p^5}{120} \sin^5(\omega_m t) - \cdots
$$

---

## Step 3: Approximate for small $\varphi_p$

If $\varphi_p \ll 1$, then $\varphi_p^3, \varphi_p^5, \dots$ are very small and can be neglected.

Keeping only the first-order term:

$$
\sin[\varphi_p \sin(\omega_m t)] \approx \varphi_p \sin(\omega_m t)
$$

---

## ✅ Conclusion

We have shown, starting from the formal Taylor series definition, that:

$$
\sin[\varphi_p \sin(\omega_m t)] \approx \varphi_p \sin(\omega_m t)
\quad \text{(when } \varphi_p \ll 1 \text{)}
$$