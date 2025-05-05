The goal here is to get the value of the normalized settling time for the natural frequency of the response of PLL phase error. As the first step, it's started with the note [[Time-domain of transfer function of phase error and phase reference in linear transient behavior analysis]], where, for $\zeta<1$,
$$
\theta_e(t) = \frac{\Delta\omega}{\omega_n} \cdot \frac{1}{\sqrt{1-\zeta^2}} e^{-\zeta\omega_n t} \sin\left(\omega_n \sqrt{1-\zeta^2} \, t\right)
$$
Analyzing the response generically (no specific response, such as impulse or step, and normalized for $\omega_n$), the phase error transfer function can be rewritten as
$$
\theta_e(t) = \frac{1}{\sqrt{1-\zeta^2}} e^{-\zeta\omega_n t} \sin\left(\omega_n \sqrt{1-\zeta^2} \, t\right)
$$
That way, it's possible to establish that the settling time is referred to the response better than 99% complete. Then the answer equation could be
$$
∣\theta_e(t)−\theta_f​∣\;\le\;0.01\;\cdot∣\theta_f​∣
$$
How it's being analyzed the phase error response, the final value should be null, i.e. $\theta_f=0$.
$$
\left|\theta_e(t)\right|\le0.01
$$
Calculating the modulus,
$$
\left|\theta_e(t)\right|=\frac{1}{\sqrt{1-\zeta^2}}e^{-\zeta\omega_nt}
$$
Thus the equation is
$$
\begin{split}
\frac{1}{\sqrt{1-\zeta^2}}e^{-\zeta\omega_nt_s}\le0.01\implies\\
e^{-\zeta\omega_nt_s}\le0.01\sqrt{1-\zeta^2}\implies\\
-\zeta\omega_nt_s\le\ln\left(0.01\sqrt{1-\zeta^2}\right)\implies\\
t_s\ge\frac{-\ln\left(0.01\sqrt{1-\zeta^2}\right)}{\zeta}\frac{1}{\omega_n}
\end{split}
$$