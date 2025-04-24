📌 **ID:** 2025/04/24 09:21  
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
The below equation presents the continuous-time analysis in the Laplace domain ($s$ domain) of the open loop PLL, $G_\text{OL}$. As we're considering the PFD a sampling element, the transfer function analyzed uses a [[Hold function]].
$$
\begin{split}
G_\text{OL}(s)=F(s)\cdot K_\theta\cdot\frac{K_\text{VCO}}{N\cdot s}\left(\frac{1-e^{-sT}}{s}\right)\implies\\
G_\text{OL}(s)=F(s)\cdot K_\theta\cdot\frac{K_\text{VCO}}{N\cdot s}\left(\frac{1-e^{-sT}}{s}\right)
\end{split}
$$

$$
H(s) = \frac{\theta_{out}(s)}{\theta_{ref}(s)} = \frac{K_{PD} \cdot K_{VCO}}{s + K_{PD} \cdot K_{VCO}}
$$

> You may include diagrams, links to supporting notes, or intermediate results.

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
