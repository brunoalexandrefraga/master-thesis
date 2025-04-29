📌 **ID:** 2025/04/29 16:08  
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
The output signal of a synthesizer can be described as
$$
v_o(t)=V_0\cos\left[\omega_\text{LO}t+\varphi_n\left(t\right)\right]
$$
Here, $\omega_\text{LO}\cdot t$ is the desired phase of the output and $\varphi_n\left(t\right)$ are random fluctuations in the phase of the output. The phase fluctuation at this time is assumed to have a sinusoidal form as shown in [[Phase fluctuation equation]]
$$
\varphi_n(t)=\varphi_p\sin\left(\omega_m t\right)
$$
where $\varphi_p$ is the peak phase fluctuation, and $\omega_m$ is the offset frequency from the carrier. Substituting this equation in the $v_o$ equation, it follows
$$
\begin{split}
v_o(t)&=V_0\cos\left[\omega_\text{LO}t+\varphi_p\sin\left(\omega_m t\right)\right]\implies\\
&=V_0\bigg\{\cos\left(\omega_\text{LO}t\right)\cos\left[\varphi_p\sin\left(\omega_m t\right)\right]-\sin\left(\omega_\text{LO}t\right)\sin\left[\varphi_p\sin\left(\omega_m t\right)\right]\bigg\}
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
