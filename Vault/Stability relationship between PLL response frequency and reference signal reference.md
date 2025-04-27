📌 **ID:** 2025/04/27 16:48  
🔗 **Linked Notes:** [[Integer-N PLL]], [[Phase-Locked Loop]], [[Transfer Function]]  
🏷️ **Tags:** #PLL #circuit-design #control-theory

---

## ✍️ Core Idea  
A clear sentence that summarizes the central insight or purpose of the note.  
> *Example:* The transfer function of a basic Integer-N PLL can be expressed as a first-order system.

---

## 🧩 Development

### 1. Context  
Brief description of the system, circuit, or problem being analyzed.  
> *Example:* Linearized model of an Integer-N PLL for frequency-domain analysis.

### 2. Derivation / Analysis  
As was gotten in [[Critical value at which the reference period (low frequency) cannot achieve to make the system unstable, making any pole move outside the unit circle]],
$$
\begin{split}
T&=\frac{1}{\omega_n\zeta}\implies\\
\end{split}
$$
Where $T$ is the period of the reference signal of angular frequency $\omega$. This way, it's also true that
$$
T=\frac{2\pi}{\omega}
$$
So,
$$
\frac{2\pi}{\omega}=\frac{1}{\omega_n\zeta}
$$
The relationship becomes,
$$
\frac{\omega}{\omega_n}\ge2\pi\zeta
$$

### 3. Example (optional)  
Include a practical case, numerical example, or simulation result to reinforce understanding.

---

## 🔁 Connections  
- [[Loop Filter Design]]  
- [[Phase Noise in Integer-N PLLs]]  
- [[Design of CMOS Phase-Locked Loops - From Circuit Level to Architecture Level (Razavi)]]

---

## 💡 Personal Reflections  
Write down insights, questions, possible variations, or connections with your dissertation.

---

## 📚 References  
- [[CMOS VLSI Design - A Circuits and Systems Perspective]]
- [[2.2 Integer-N PLL Synthesizers]] 
