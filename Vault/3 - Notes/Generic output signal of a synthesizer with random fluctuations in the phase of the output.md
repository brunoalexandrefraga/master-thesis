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