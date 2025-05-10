For $\zeta<1$, the transfer function of phase error was demonstrated in [[Time-domain of transfer function of phase error and phase reference in linear transient behavior analysis]],
$$
\begin{split}
\theta_e(t)&=\frac{\Delta\omega}{\omega_n}\frac{\sin\left(\omega_n\sqrt{1-\zeta^2}t\right)}{\sqrt{1-\zeta^2}}e^{-\zeta\omega_nt}
\end{split}
$$
To get the maximum value, it's done as follows
$$
\begin{split}
\frac{d\theta_e}{dt}&=\frac{\Delta\omega}{\omega_n\sqrt{1-\zeta^2}}\frac{dE}{dt}
\end{split}
$$
where $E(t)=\sin\left(\omega_n\sqrt{1-\zeta^2}t\right)e^{-\zeta\omega_nt}$. Calling $u=\sin\left(\omega_n\sqrt{1-\zeta^2}t\right)$ and $v=e^{-\zeta\omega_nt}$,
$$
\begin{split}
\frac{dE}{dt}&=u'v+v'u
\end{split}
$$
calculating the $u$ and $v$ derivatives,
$$
u'=\omega_n\sqrt{1-\zeta^2}\cos\left(\omega_n\sqrt{1-\zeta^2}t\right)
$$
and
$$
v'=-\zeta\omega_ne^{-\zeta\omega_nt}
$$
So that the equation results in
$$
\begin{split}
\frac{dE}{dt}&=\omega_n\sqrt{1-\zeta^2}\cos\left(\omega_n\sqrt{1-\zeta^2}t\right)e^{-\zeta\omega_nt}-\zeta\omega_ne^{-\zeta\omega_nt}\sin\left(\omega_n\sqrt{1-\zeta^2}t\right)\implies\\
&=e^{-\zeta\omega_nt}\omega_n\left[\sqrt{1-\zeta^2}\cos\left(\omega_n\sqrt{1-\zeta^2}t\right)-\zeta\sin\left(\omega_n\sqrt{1-\zeta^2}t\right)\right]
\end{split}
$$
The final result of the derivative is
$$
\begin{split}
\frac{d\theta_e}{dt}&=\frac{\Delta\omega}{\omega_n\sqrt{1-\zeta^2}}e^{-\zeta\omega_nt}\omega_n\left[\sqrt{1-\zeta^2}\cos\left(\omega_n\sqrt{1-\zeta^2}t\right)-\zeta\sin\left(\omega_n\sqrt{1-\zeta^2}t\right)\right]\implies\\
&=\frac{\Delta\omega}{\sqrt{1-\zeta^2}}e^{-\zeta\omega_nt}\left[\sqrt{1-\zeta^2}\cos\left(\omega_n\sqrt{1-\zeta^2}t\right)-\zeta\sin\left(\omega_n\sqrt{1-\zeta^2}t\right)\right]\implies\\
&=\Delta\omega\cdot e^{-\zeta\omega_nt}\left[\cos\left(\omega_n\sqrt{1-\zeta^2}t\right)-\frac{\zeta}{\sqrt{1-\zeta^2}}\sin\left(\omega_n\sqrt{1-\zeta^2}t\right)\right]
\end{split}
$$
To get the $t$ of the maximum value, $t_m$, it's done
$$
\begin{split}
\Delta\omega\cdot e^{-\zeta\omega_nt_m}\left[\cos\left(\omega_n\sqrt{1-\zeta^2}t_m\right)-\frac{\zeta}{\sqrt{1-\zeta^2}}\sin\left(\omega_n\sqrt{1-\zeta^2}t_m\right)\right]&=0\implies\\
\cos\left(\omega_n\sqrt{1-\zeta^2}t_m\right)=\frac{\zeta}{\sqrt{1-\zeta^2}}\sin\left(\omega_n\sqrt{1-\zeta^2}t_m\right)\implies\\
\frac{\cos\left(\omega_n\sqrt{1-\zeta^2}t_m\right)}{\sin\left(\omega_n\sqrt{1-\zeta^2}t_m\right)}=\frac{\zeta}{\sqrt{1-\zeta^2}}\implies\\
\tan\left(\omega_n\sqrt{1-\zeta^2}t_m\right)=\frac{\sqrt{1-\zeta^2}}{\zeta}\implies\\
t_m=\frac{1}{\omega_n\sqrt{1-\zeta^2}}\tan^{-1}\left(\frac{\sqrt{1-\zeta^2}}{\zeta}\right)
\end{split}
$$