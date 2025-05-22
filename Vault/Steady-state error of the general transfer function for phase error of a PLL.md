📌 **ID:** 2025/04/29 12:17  
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
Starting from [[General transfer function for phase error of a PLL]], it's possible to get the steady-state error as
$$
\begin{split}
\theta_{e\_ss}&=\lim_{s\to0}\left[\left(\frac{\Delta\omega}{s^2}\right)\cdot\left(\frac{s}{s+KF(s)}\right)\cdot s\right]\implies\\
&=\lim_{s\to0}\left[\left(\frac{\Delta\omega}{s}\right)\cdot\left(\frac{s}{s+KF(s)}\right)\right]\implies\\
&=\lim_{s\to0}\left(\frac{\Delta\omega}{s+KF(s)}\right)\implies\\
&=\frac{\Delta\omega}{KF(0)}
\end{split}
$$
In the second-order PFD/CP system, the steady-state phase error will always be zero because there is an integrator in $F(s)$, and $F(0)$ will go to $\infty$ ([[3.6.2 Nonlinear Transient Behavior]]).



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
