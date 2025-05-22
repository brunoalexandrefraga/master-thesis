The below equation presents the continuous-time analysis in the Laplace domain ($s$ domain) of the open loop PLL, $G_\text{OL}$. As we're considering the PFD a sampling element, the transfer function analyzed uses a [[Hold function]].
$$
G_\text{OL}(s)=F(s)\cdot K_\theta\cdot\frac{K_\text{VCO}}{N\cdot s}\left(\frac{1-e^{-sT}}{s}\right)
$$
For a simple [[First-order loop filter of a PLL]], with one resistor $R_1$ and two capacitors $C_1$ and $C_2$ (and ignoring $C_2$ for simplicity)
$$
G_\text{OL}(s)=\left(R_1+\frac{1}{sC_1}\right)\cdot K_\theta\cdot\frac{K_\text{VCO}}{N\cdot s}\left(\frac{1-e^{-sT}}{s}\right)
$$
It's known that
$$
C_1=\frac{IK_\text{VCO}}{2\pi N\omega_n^2}
$$
and
$$
R_1=\frac{4\pi\zeta N\omega_n}{IK_\text{VCO}}
$$
Substituting the component's values in the equation, and remembering that $K_\theta=I/2\pi$. From this point on, the development is entirely algebraic, and therefore the equation results in, 
$$
\begin{split}
G_\text{OL}(s)&=\left(\frac{4\pi\zeta N\omega_n}{IK_\text{VCO}}+\frac{1}{s}\frac{2\pi N\omega_n^2}{IK_\text{VCO}}\right)\cdot \frac{I}{2\pi}\cdot\frac{K_\text{VCO}}{N\cdot s}\left(\frac{1-e^{-sT}}{s}\right)\implies\\
&=\left(\frac{2\zeta \omega_n}{1}+\frac{\omega_n^2}{s}\right)\cdot\frac{1}{s}\cdot\left(\frac{1-e^{-sT}}{s}\right)\implies\\
&=\omega_n^2\left(\frac{2\zeta}{\omega_n}+\frac{1}{s}\right)\cdot\frac{1}{s}\cdot\left(\frac{1-e^{-sT}}{s}\right)\implies\\
&=\omega_n^2\left(\frac{2\zeta}{\omega_n}s+1\right)\cdot\frac{1}{s^2}\cdot\left(\frac{1-e^{-sT}}{s}\right)
\end{split}
$$