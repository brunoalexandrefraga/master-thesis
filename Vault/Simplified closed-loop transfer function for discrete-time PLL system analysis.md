📌 **ID:** 2025/04/25 18:12  
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
As it was discussed in [[Simplified open-loop transfer function from continuous-time (s domain) to discrete-time (z domain)]] (and the results wasn't gotten correctly yet), the open-loop transfer function in the z domain of a simple Integer-N PLL can be expressed as
$$
G_\text{OL}(z)=K\left[\frac{z-\alpha}{\left(z-1\right)^2}\right]
$$
The closed-loop transfer function is
$$
\begin{split}
G(z)&=\frac{G_\text{OL}(z)}{1+G_\text{OL}(z)}\implies\\
&=\frac{K\left(z-\alpha\right)}{\left(z-1\right)^2+K\left(z-\alpha\right)}\implies\\
&=\frac{K\left(z-\alpha\right)}{z^2-2z+1+Kz-K\alpha}\implies\\
&=\frac{K\left(z-\alpha\right)}{z^2\left(K-2\right)z+\left(1-K\alpha\right)}
\end{split}
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
