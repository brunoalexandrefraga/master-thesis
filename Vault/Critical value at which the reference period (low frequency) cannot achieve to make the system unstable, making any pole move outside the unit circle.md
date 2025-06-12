# Critical value at which the reference period (low frequency) cannot achieve to make the system unstable, making any pole move outside the unit circle

Using the value of $K$ and $\alpha$ defined in [[Simplified open-loop transfer function from continuous-time (s domain) to discrete-time (z domain)]] as 
$$
K=\frac{\omega_n^2T^2}{2}\left(1+\frac{4\zeta}{\omega_nT}\right)
$$
and
$$
\alpha=\frac{4\zeta-\omega_nT}{4\zeta+\omega_nT}
$$
Starting from the results gotten in [[Critical value of the negative pole of simple closed-loop PLL transfer function]], the equation becomes
First, computing,
$$
\begin{split}
1+\alpha&=1+\frac{4\zeta-\omega_nT}{4\zeta+\omega_nT}\implies\\
&=\frac{\left(4\zeta+\omega_nT\right)+\left(4\zeta-\omega_nT\right)}{4\zeta+\omega_nT}\implies\\
&=\frac{8\zeta}{4\zeta+\omega_nT}\implies\\
\end{split}
$$
Treating of the term between parenthesis of $K$,
$$
1+\frac{4\zeta}{\omega_nT}=\frac{\omega_nT+4\zeta}{\omega_nT}
$$
Thus, $K$ can be expressed as
$$
\begin{split}
K&=\frac{\omega_n^2T^2}{2}\left(1+\frac{4\zeta}{\omega_nT}\right)\implies\\
&=\frac{\omega_n^2T^2}{2}\frac{\left(\omega_nT+4\zeta\right)}{\omega_nT}\implies\\
&=\frac{\omega_nT\left(\omega_nT+4\zeta\right)}{2}\implies\\
\end{split}
$$
Multiplying the expression, it results in
$$
\begin{split}
K\left(1+\alpha\right)&=\frac{\omega_nT\left(\omega_nT+4\zeta\right)}{2}\frac{8\zeta}{\left(4\zeta+\omega_nT\right)}\implies\\
&=4\zeta\omega_nT
\end{split}
$$
Therefore, the equation results in
$$
\begin{split}
K\left(1+\alpha\right)&=4\implies\\
4\zeta\omega_nT&=4\implies\\
T=\frac{1}{\omega_n\zeta}
\end{split}
$$
