As what was done in [[PLL transfer function of control vontage going into the VCO]], one can start from the equation gotten in [[General equation for closed-loop PLL]] and get the relation between the phase error, $\theta_e$, and the input phase reference, $\theta_R$.
$$
\begin{split}
\frac{\theta_e}{\theta_R}&=\frac{\frac{K_\theta K_\text{VCO}}{NC_1}\left(sC_1R+1\right)}{s^2+\frac{K_\theta K_\text{VCO}}{N}Rs+\frac{K_\theta K_\text{VCO}}{NC_1}}\cdot\frac{Ns}{K_\text{VCO}K_\theta}\left(R+\frac{1}{sC_1}\right)^{-1}\implies\\
&=\frac{s^2}{s^2+\frac{K_\theta K_\text{VCO}}{N}Rs+\frac{K_\theta K_\text{VCO}}{NC_1}}\implies\\
&=\frac{s^2}{s^2+2\zeta\omega_ns+\omega_n^2}
\end{split}
$$