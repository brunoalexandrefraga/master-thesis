📌 **ID:** 2025/04/29 16:18  
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
Starting from the note [[Generic output signal of a synthesizer with random fluctuations in the phase of the output]], if it was analyzed for small phase fluctuation,
$$
\begin{split}
v_o(t)&=V_0\bigg\{\cos\left(\omega_\text{LO}t\right)\cos\left[\varphi_p\sin\left(\omega_m t\right)\right]-\sin\left(\omega_\text{LO}t\right)\sin\left[\varphi_p\sin\left(\omega_m t\right)\right]\bigg\}\implies\\
&=V_0\bigg[\cos\left(\omega_\text{LO}t\right)-\varphi_p\sin\left(\omega_m t\right)\sin\left(\omega_\text{LO}t\right)\bigg]
\end{split}
$$
It's possible to approximate due to the Taylor approximation ([[Inner Sine (of sine) Expansion Taylor Approximation]])
$$
\sin[\varphi_p \sin(\omega_m t)] \approx \varphi_p \sin(\omega_m t)
$$
and ([[Inner Sine (of cosine) Expansion Taylor Approximation]])
$$
\cos[\varphi_p \sin(\omega_m t)] \approx 1
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
