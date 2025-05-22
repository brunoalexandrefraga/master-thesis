$$
\begin{split}
\frac{\varphi_\text{no}(s)}{\varphi_\text{nI}(s)}&=\frac{\frac{F(s)K_\text{VCO}K_\theta}{Ns}}{1+\frac{F(s)K_\text{VCO}K_\theta}{Ns}}\cdot N\cdot\frac{s}{s}\implies\\
&=\frac{F(s)K_\text{VCO}K_\theta}{s+\frac{F(s)K_\text{VCO}K_\theta}{N}}
\end{split}
$$
as the PSD output noise, $\varphi_\text{no}$, is obtained before the divider, the function could be multiplied by $N$ (i.e. divided by $N^{-1}$).
## Example
For a PLL with a second-order loop filter,
$$
\begin{split}
\frac{\varphi_\text{no}(s)}{\varphi_\text{nI}(s)}&=\frac{\frac{IK_\text{VCO}}{2\pi\cdot C_1}\left(1+RC_1s\right)}{s^2+\frac{IK_\text{VCO}}{2\pi\cdot N}Rs+\frac{IK_\text{VCO}}{2\pi\cdot NC_1}}
\end{split}
$$