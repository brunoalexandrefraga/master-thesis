📌 **ID:** 2025/04/29 10:40  
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
Starting from the first analysis made in [[Transfer function for the linear transient behavior analysis]], it's known that
$$
\begin{split}
\frac{\theta_e}{\theta_R}&=\frac{K_\theta K_\text{VCO}N^{-1}s^{-1}F(s)}{1+K_\theta K_\text{VCO}N^{-1}s^{-1}F(s)}\cdot\frac{1}{F(s)}\cdot\frac{s}{K_\text{VCO}}\cdot N\cdot\frac{1}{K_\theta}\implies\\
&=\frac{s}{s+\frac{K_\theta K_\text{VCO}}{N}F(s)}
\end{split}
$$
calling $K=K_\theta K_\text{VCO}/N$,
$$
\frac{\theta_e}{\theta_R}=\frac{s}{s+KF(s)}
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
