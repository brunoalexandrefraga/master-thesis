📌 **ID:** 2025/04/30 11:14  
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
As what was obtained in [[DSB phase noise PSD to carrier ratio]] and [[SSB phase noise PSD to carrier ratio]], it's possible to get the rms jitter as
$$
\varphi_\text{rms}\left(\Delta\omega\right)=\sqrt{10^\frac{\text{PN}_\text{DSB}\left(\Delta\omega\right)}{10}}=\sqrt{2}\cdot\sqrt{10^\frac{\text{PN}_\text{SSB}\left(\Delta\omega\right)}{10}}
$$
And it's measured in $\text{rad}/\sqrt{\text{Hz}}$. If it's desired to measure the rms jitter in deg, it can use the following relation
$$
\varphi_\text{rms}\left(\Delta f\right)=\frac{180^\circ}{\pi}\sqrt{10^\frac{\text{PN}_\text{DSB}\left(\Delta f\right)}{10}}=\frac{180^\circ\sqrt{2}}{\pi}\cdot\sqrt{10^\frac{\text{PN}_\text{SSB}\left(\Delta f\right)}{10}}
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
