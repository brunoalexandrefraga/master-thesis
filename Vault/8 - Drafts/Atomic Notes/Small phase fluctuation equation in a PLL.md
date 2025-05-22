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