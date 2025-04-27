📌 **ID:** 2025/04/27 15:20  
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
From the poles gotten in [[Poles of the simplified closed-loop transfer function for discrete-time PLL system analysis]] it's important to find out the critical conditions that make the system unstable. To find out these conditions, it's needed to find out the relationship that leads to, i.e. the negative pole achieve the critical value of instability, or the pole goes out from the unit circle.
$$
1-\frac{K}{2}-\frac{1}{2}\sqrt{\left(K-2\right)^2-4\left(1-\alpha K\right)}=-1
$$
As was discussed, [[Positive pole of the transfer function of a simple PLL will never leave the unit circle]].
Solving this equation, it's gotten
$$
\begin{split}
-\frac{K}{2}-\frac{1}{2}\sqrt{\left(K-2\right)^2-4\left(1-\alpha K\right)}=-2\implies\\
-\frac{1}{2}\sqrt{\left(K-2\right)^2-4\left(1-\alpha K\right)}=\frac{K}{2}-2\implies\\
\sqrt{\left(K-2\right)^2-4\left(1-\alpha K\right)}=4-K\implies\\
\left(K-2\right)^2-4\left(1-\alpha K\right)=\left(4-K\right)^2\implies\\
K^2-4K+4-4+4\alpha K-16+8K-K^2=0\implies\\
4\alpha K-16+4K=0\implies\\
K\left(1+\alpha\right)=4
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
