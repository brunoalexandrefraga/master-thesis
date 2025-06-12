Now it's important to get the poles from the equation gotten in [[Simplified closed-loop transfer function for discrete-time PLL system analysis]].
$$
\begin{split}
G(z)&=\frac{K\left(z-\alpha\right)}{z^2\left(K-2\right)z+\left(1-K\alpha\right)}
\end{split}
$$
To analyse the poles in the equation, it's done
$$
z^2+\left(K-2\right)z+(1-\alpha K)=0
$$
To use the Bhaskara's formula, it's used the form $az^2+bz+c$, where $a=1$, $b=(K-2)$ and $c=1-\alpha K$, this way it's gotten,
$$
\begin{split}
\Delta&=b^2-4ac\implies\\
&=\left(K-2\right)^2-4\cdot1\cdot\left(1-\alpha K\right)
\end{split}
$$
That way, the poles are
$$
\begin{split}
z&=\frac{-\left(K-2\right)\pm\sqrt{\left(K-2\right)^2-4\left(1-\alpha K\right)}}{2\cdot1}\implies\\
&=1-\frac{K}{2}\pm\frac{1}{2}\sqrt{\left(K-2\right)^2-4\left(1-\alpha K\right)}
\end{split}
$$