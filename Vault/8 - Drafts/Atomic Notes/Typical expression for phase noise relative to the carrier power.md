📌 **ID:** 2025/04/29 16:49  
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
A spectrum analyzer measures the phase noise power in dBm/Hz, but often phase noise is reported relative to the carrier power as
$$
\varphi_n^2\left(\Delta\omega\right)=\frac{N\left(\omega_\text{LO}+\Delta\omega\right)}{P_c\left(\omega_\text{LO}\right)}
$$
where $N$ is the noise power in a 1-Hz bandwidth, and $P_c$ is the power of the carrier or $\text{LO}$ (Local Oscillator) tone at the frequency at which the synthesizer is operating. In  this form, phase noise has units of $rad^2/Hz$.
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
