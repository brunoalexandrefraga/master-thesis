
Starting from the first analysis made in [[Transfer function for the linear transient behavior analysis]], it's known that
$$
\begin{split}
\frac{\theta_e}{\theta_R}&=\frac{K_\theta K_\text{VCO}N^{-1}s^{-1}F(s)}{1+K_\theta K_\text{VCO}N^{-1}s^{-1}F(s)}\cdot\frac{1}{F(s)}\cdot\frac{s}{K_\text{VCO}}\cdot N\cdot\frac{1}{K_\theta}\implies\\
&=\frac{s}{s+\frac{K_\theta K_\text{VCO}}{N}F(s)}
\end{split}
$$
calling $K=K_\theta K_\text{VCO}/N$,
$$
\frac{\theta_e}{\theta_R}=\frac{s}{s+KF(s)}
$$
