Starting from [[Simplified open-loop transfer function for continuous-time PLL system analysis with Holder Function]], it's possible to discretize the function presented there. To do that, it's useful to separate that function in two parts,
$$
G_1(s)=\left(\frac{2\zeta}{\omega_n}s+1\right)\cdot\frac{1}{s^2}
$$
e
$$
G_2(s)=\left(\frac{1-e^{-sT}}{s}\right)
$$
To perform the discretization of that system, the bilinear transformation is used, where
$$
s=\frac{2}{T}\frac{1-z^{-1}}{1+z^{-1}}=\frac{2\left(1-z^{-1}\right)}{T\left(1+z^{-1}\right)}
$$
Substituting $s$ in $G_1(s)$ it results in
$$
\begin{split}
G_1(z)&=\left[\frac{2\zeta}{\omega_n}\frac{2\left(1-z^{-1}\right)}{T\left(1+z^{-1}\right)}+1\right]\cdot\left[\frac{T\left(1+z^{-1}\right)}{2\left(1-z^{-1}\right)}\right]^2\implies\\
&=\left[\frac{4\zeta\left(1-z^{-1}\right)+\omega_nT\left(1+z^{-1}\right)}{\omega_nT\left(1+z^{-1}\right)}\right]\cdot\frac{T^2\left(1+z^{-1}\right)^2}{4\left(1-z^{-1}\right)^2}\implies\\
&=\left[\frac{\frac{4\zeta}{\omega_nT}\left(1-z^{-1}\right)+\left(1+z^{-1}\right)}{\left(1+z^{-1}\right)}\right]\cdot\frac{T^2\left(1+z^{-1}\right)^2}{4\left(1-z^{-1}\right)^2}\implies\\
&=\frac{T^2}{4}\left[\frac{4\zeta}{\omega_nT}\left(1-z^{-1}\right)+\left(1+z^{-1}\right)\right]\cdot\frac{\left(1+z^{-1}\right)}{\left(1-z^{-1}\right)^2}
\end{split}
$$
It's named
$$
\begin{split}
Q(z)&=\left[\frac{4\zeta}{\omega_nT}\left(1-z^{-1}\right)+\left(1+z^{-1}\right)\right]\implies\\
&=\frac{4\zeta}{\omega_nT}-\frac{4\zeta}{\omega_nT}z^{-1}+1+z^{-1}\implies\\
&=A+Bz^{-1}
\end{split}
$$
where
$$
A=\frac{4\zeta}{\omega_nT}+1
$$
e
$$
B=-\frac{4\zeta}{\omega_nT}+1
$$
Thus, $G_1(z)$ results in
$$
G_1(z)=\frac{T^2}{4}\left(A+Bz^{-1}\right)\cdot\frac{\left(1+z^{-1}\right)}{\left(1-z^{-1}\right)^2}
$$
Multiplying the whole equation for $z^2/z^2$, it results
$$
\begin{split}
G_1(z)&=\frac{T^2}{4}\left(Az+B\right)\cdot\frac{\left(z+1\right)}{\left(z-1\right)^2}\implies\\
&=\frac{T^2}{4}A\left(z+\frac{B}{A}\right)\cdot\frac{\left(z+1\right)}{\left(z-1\right)^2}\implies\\
\end{split}
$$
So, it's called $G_{OL_1}$ the equation $G_{OL}$ without $G_1$, then
$$
G_{OL_1}(z)=\frac{\omega_n^2T^2}{4}A\left(z+\frac{B}{A}\right)\cdot\frac{\left(z+1\right)}{\left(z-1\right)^2}\implies\\
$$
Substituting $A$ and $B$, it results
$$
\begin{split}
G_{OL_1}(z)&=\frac{\omega_n^2T^2}{4}\left(1+\frac{4\zeta}{\omega_nT}\right)\left(z+\frac{-\frac{4\zeta}{\omega_nT}+1}{\frac{4\zeta}{\omega_nT}+1}\right)\cdot\frac{\left(z+1\right)}{\left(z-1\right)^2}\implies\\
&=\frac{\omega_n^2T^2}{4}\left(1+\frac{4\zeta}{\omega_nT}\right)\left(z+\frac{-4\zeta+\omega_nT}{4\zeta+\omega_nT}\right)\cdot\frac{\left(z+1\right)}{\left(z-1\right)^2}\implies\\
&=\frac{\omega_n^2T^2}{4}\left(1+\frac{4\zeta}{\omega_nT}\right)\left(z-\frac{4\zeta-\omega_nT}{4\zeta+\omega_nT}\right)\cdot\frac{\left(z+1\right)}{\left(z-1\right)^2}\implies\\
&=\frac{\omega_n^2T^2}{2}\left(1+\frac{4\zeta}{\omega_nT}\right)\left[\frac{z-\frac{4\zeta-\omega_nT}{4\zeta+\omega_nT}}{\left(z-1\right)^2}\right]\frac{\left(z+1\right)}{2}\implies\\
\end{split}
$$
Performing the bilinear transformation for $G_2(s)$, it results
$$
\begin{split}
G_2(z)&=\left[\frac{1-e^{-\frac{2\left(1-z^{-1}\right)}{T\left(1+z^{-1}\right)}T}}{\frac{2\left(1-z^{-1}\right)}{T\left(1+z^{-1}\right)}}\right]\implies\\
&=\frac{T\left(1+z^{-1}\right)}{2\left(1-z^{-1}\right)}\left[1-e^{-\frac{2\left(1-z^{-1}\right)}{T\left(1+z^{-1}\right)}T}\right]\implies\\
\end{split}
$$

I don't know what to do now.









The final transformation is
$$
\begin{split}
G_\text{OL}(z)&=\frac{\omega_n^2T^2}{2}\left(1+\frac{4\zeta}{\omega_nT}\right)\cdot\left[z-\frac{4\zeta-\omega_nT}{4\zeta+\omega_nT}\right]\frac{1}{\left(z-1\right)^2}\implies\\
&=K\left[\frac{z-\alpha}{\left(z-1\right)^2}\right]
\end{split}
$$
where,
$$
K=\frac{\omega_n^2T}{2}\left(1+\frac{4\zeta}{\omega_nT}\right)
$$
and
$$
\alpha=\frac{4\zeta-\omega_nT}{4\zeta+\omega_nT}
$$


