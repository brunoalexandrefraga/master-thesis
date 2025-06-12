
The general equation of a Integer-N, generic PLL can be obtained as
$$
\frac{\theta_o}{\theta_R}=\frac{K_\theta F(s)\frac{K_\text{VCO}}{s}\frac{1}{N}}{1+K_\theta F(s)\frac{K_\text{VCO}}{s}\frac{1}{N}}
$$
For a first-order loop filter, $F(s)=\left(R+\frac{1}{sC_1}\right)$, ignoring $C_2$. That is
$$
\begin{split}
\frac{\theta_o}{\theta_R}&=\frac{K_\theta\left(R+\frac{1}{sC_1}\right)\frac{K_\text{VCO}}{s}\frac{1}{N}}{1+K_\theta\left(R+\frac{1}{sC_1}\right)\frac{K_\text{VCO}}{s}\frac{1}{N}}\implies\\
\frac{\theta_o}{\theta_R}&=\frac{K_\theta\frac{\left(sC_1R+1\right)}{sC_1}\frac{K_\text{VCO}}{s}\frac{1}{N}}{1+K_\theta\frac{\left(sC_1R+1\right)}{sC_1}\frac{K_\text{VCO}}{s}\frac{1}{N}}\implies\\
\frac{\theta_o}{\theta_R}&=\frac{K_\theta\frac{\left(sC_1R+1\right)}{sC_1}\frac{K_\text{VCO}}{s}\frac{1}{N}}{1+K_\theta\frac{\left(sC_1R+1\right)}{sC_1}\frac{K_\text{VCO}}{s}\frac{1}{N}}\implies\\
\frac{\theta_o}{\theta_R}&=\frac{K_\theta\frac{\left(sC_1R+1\right)}{C_1}\frac{K_\text{VCO}}{N}}{s^2+K_\theta\frac{\left(sC_1R+1\right)}{C_1}\frac{K_\text{VCO}}{N}}\implies\\
\frac{\theta_o}{\theta_R}&=\frac{\frac{K_\theta K_\text{VCO}}{NC_1}\left(sC_1R+1\right)}{s^2+\frac{K_\theta K_\text{VCO}}{N}Rs+\frac{K_\theta K_\text{VCO}}{NC_1}}
\end{split}
$$
