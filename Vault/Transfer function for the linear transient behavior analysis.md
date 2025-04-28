📌 **ID:** 2025/04/28 09:37  
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
As what was done in [[PLL transfer function of control vontage going into the VCO]], one can start from the equation gotten in [[General equation for closed-loop PLL]] and get the relation between the phase error, $\theta_e$, and the input phase reference, $\theta_R$.
$$
\begin{split}
\frac{\theta_e}{\theta_R}&=\frac{\frac{K_\theta K_\text{VCO}}{NC_1}\left(sC_1R+1\right)}{s^2+\frac{K_\theta K_\text{VCO}}{N}Rs+\frac{K_\theta K_\text{VCO}}{NC_1}}\cdot\frac{Ns}{K_\text{VCO}K_\theta}\left(R+\frac{1}{sC_1}\right)^{-1}\implies\\
&=\frac{s^2}{s^2+\frac{K_\theta K_\text{VCO}}{N}Rs+\frac{K_\theta K_\text{VCO}}{NC_1}}\implies\\
&=\frac{s^2}{s^2+2\zeta\omega_ns+\omega_n^2}
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
