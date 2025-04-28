📌 **ID:** 2025/04/28 09:01  
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
The general equation of a Integer-N, generic PLL can be obtained as
$$
\frac{\theta_o}{\theta_R}=\frac{K_\theta F(s)\frac{K_\text{VCO}}{s}\frac{1}{N}}{1+K_\theta F(s)\frac{K_\text{VCO}}{s}\frac{1}{N}}
$$
For a first-order loop filter, $F(s)=\left(R+\frac{1}{sC_1}\right)$, ignoring $C_2$. That is
$$
\begin{split}
\frac{\theta_o}{\theta_R}&=\frac{K_\theta\left(R+\frac{1}{sC_1}\right)\frac{K_\text{VCO}}{s}\frac{1}{N}}{1+K_\theta\left(R+\frac{1}{sC_1}\right)\frac{K_\text{VCO}}{s}\frac{1}{N}}\implies\\
\frac{\theta_o}{\theta_R}&=\frac{K_\theta\frac{\left(sC_1R+1\right)}{sC_1}\frac{K_\text{VCO}}{s}\frac{1}{N}}{1+K_\theta\frac{\left(sC_1R+1\right)}{sC_1}\frac{K_\text{VCO}}{s}\frac{1}{N}}\implies\\
\frac{\theta_o}{\theta_R}&=\frac{K_\theta\frac{\left(sC_1R+1\right)}{sC_1}\frac{K_\text{VCO}}{s}\frac{1}{N}}{1+K_\theta\frac{\left(sC_1R+1\right)}{sC_1}\frac{K_\text{VCO}}{s}\frac{1}{N}}\implies\\
\frac{\theta_o}{\theta_R}&=\frac{K_\theta\frac{\left(sC_1R+1\right)}{C_1}\frac{K_\text{VCO}}{N}}{s^2+K_\theta\frac{\left(sC_1R+1\right)}{C_1}\frac{K_\text{VCO}}{N}}\implies\\
\frac{\theta_o}{\theta_R}&=\frac{\frac{K_\theta K_\text{VCO}}{NC_1}\left(sC_1R+1\right)}{s^2+\frac{K_\theta K_\text{VCO}}{N}Rs+\frac{K_\theta K_\text{VCO}}{NC_1}}
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
