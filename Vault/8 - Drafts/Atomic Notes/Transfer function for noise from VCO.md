$$
\begin{split}
\frac{\varphi_\text{no}(s)}{\varphi_\text{nII}(s)}&=\frac{\frac{F(s)K_\text{VCO}K_\theta}{Ns}}{1+\frac{F(s)K_\text{VCO}K_\theta}{Ns}}\cdot N\cdot\frac{s}{K_\text{VCO}}\frac{1}{K_\theta}\frac{1}{F(s)}             \frac{s}{s}\implies\\
&=\frac{s}{s+\frac{F(s)K_\text{VCO}K_\theta}{N}}
\end{split}
$$
as the PSD output noise, $\varphi_\text{no}$, is obtained before the divider and after the VCO, the function could be multiplied by $N$ (i.e. divided by $N^{-1}$) and by the inverse transfer functions of VCO, loop filter and PFD/CP. 