
Starting from [[General transfer function for phase error of a PLL]], it's possible to get the steady-state error as
$$
\begin{split}
\theta_{e\_ss}&=\lim_{s\to0}\left[\left(\frac{\Delta\omega}{s^2}\right)\cdot\left(\frac{s}{s+KF(s)}\right)\cdot s\right]\implies\\
&=\lim_{s\to0}\left[\left(\frac{\Delta\omega}{s}\right)\cdot\left(\frac{s}{s+KF(s)}\right)\right]\implies\\
&=\lim_{s\to0}\left(\frac{\Delta\omega}{s+KF(s)}\right)\implies\\
&=\frac{\Delta\omega}{KF(0)}
\end{split}
$$
In the second-order PFD/CP system, the steady-state phase error will always be zero because there is an integrator in $F(s)$, and $F(0)$ will go to $\infty$ ([[3.6.2 Nonlinear Transient Behavior]]).


