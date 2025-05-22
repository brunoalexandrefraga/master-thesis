# Discrete-Time Analysis for PLL
The preceding linear, continuous-time analysis of the synthesizer is not valid under all conditions. If the loop bandwidth is increased so that it becomes a significant fraction of the reference frequency, the previous analyses become increasingly inaccurate.

For this reason, it is sometimes necessary to treat the synthesizer system as the discrete-time control system that it truly is.

The closed-loop gain of the system can also be determined as
$$
G(z)=\frac{K\left(z-\alpha\right)}{z^2\left(K-2\right)z+\left(1-K\alpha\right)}

$$
The relationship becomes,
$$
\frac{\omega}{\omega_n}\ge2\pi\zeta
$$
So, for instance, in the case of $\zeta = 0.707$, this ratio must be greater than $4.4$. Therefore, for a reference frequency of $40\;\text{MHz}$, if the loop natural frequency is set any higher than $9.1\;\text{MHz}$, the loop will go unstable. A ratio often quoted as being ‘‘safe’’ is 10:1.
# Transient Behavior of PLL


# Phase Noise and Timing Jitter in PLL
Synthesizer noise performance is usually classified in terms of phase noise, and the phase noise is a measure of how much the output diverges from an ideal impulse function in the frequency domain.

Phase noise is often quoted in units of $\text{dBc}/\text{Hz}$, while timing jitter is often quoted in units of picoseconds.

