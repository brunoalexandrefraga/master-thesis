
As it was discussed in [[Simplified open-loop transfer function from continuous-time (s domain) to discrete-time (z domain)]] (and the results wasn't gotten correctly yet), the open-loop transfer function in the z domain of a simple Integer-N PLL can be expressed as
$$
G_\text{OL}(z)=K\left[\frac{z-\alpha}{\left(z-1\right)^2}\right]
$$
The closed-loop transfer function is
$$
\begin{split}
G(z)&=\frac{G_\text{OL}(z)}{1+G_\text{OL}(z)}\implies\\
&=\frac{K\left(z-\alpha\right)}{\left(z-1\right)^2+K\left(z-\alpha\right)}\implies\\
&=\frac{K\left(z-\alpha\right)}{z^2-2z+1+Kz-K\alpha}\implies\\
&=\frac{K\left(z-\alpha\right)}{z^2\left(K-2\right)z+\left(1-K\alpha\right)}
\end{split}
$$



