 
Starting from the equation gotten in [[General equation for closed-loop PLL]], it's possible to determine the transfer function with the $\theta_R$ as the reference and $v_C$ as the output
$$
\begin{split}
\frac{v_C}{\theta_R}&=\frac{\frac{K_\theta K_\text{VCO}}{NC_1}\left(sC_1R+1\right)}{s^2+\frac{K_\theta K_\text{VCO}}{N}Rs+\frac{K_\theta K_\text{VCO}}{NC_1}}\cdot\frac{Ns}{K_\text{VCO}}\implies\\
\frac{v_C}{\theta_R}&=\frac{\frac{K_\theta}{C_1}s\left(sC_1R+1\right)}{s^2+\frac{K_\theta K_\text{VCO}}{N}Rs+\frac{K_\theta K_\text{VCO}}{NC_1}}\implies\\
\end{split}
$$

