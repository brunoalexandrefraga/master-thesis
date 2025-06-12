Starting from the equation in [[Transfer function for the linear transient behavior analysis]] and applying the step gotten in [[Phase of the frequency step in s-domain]], it results in
$$
\begin{split}
\theta_e&=\frac{s^2}{s^2+2\zeta\omega_ns+\omega_n^2}\frac{\Delta\omega}{s^2}\implies\\
&=\frac{\Delta\omega}{s^2+2\zeta\omega_ns+\omega_n^2}
\end{split}
$$
#### For $\zeta<1$
Applying the inverse Laplace transformation, for $\zeta<1$, following the result
$$
\begin{split}
\theta_e(t)&=\mathcal{L}^{-1}\left\{\frac{\Delta\omega}{s^2+2\zeta\omega_ns+\omega_n^2}\right\}\implies\\
&=\mathcal{L}^{-1}\left\{\frac{1}{s^2+2\zeta\omega_ns+\omega_n^2}\right\}\Delta\omega\implies\\
\end{split}
$$
For the first try, one can try to get the roots of denominator, that is
$$
\begin{split}
s^2+2\zeta\omega_ns+\omega_n^2=0
\end{split}
$$
solving with Bhaskara's formula, $a=1$, $b=2\zeta\omega_n$ and $c=\omega_n^2$,
$$
\begin{split}
\Delta&=b^2-4ac\implies\\
&=\left(2\zeta\omega_n\right)^2-4\cdot1\cdot\omega_n^2\implies\\
&=4\zeta^2\omega_n^2-4\omega_n^2\implies\\
&=4\omega_n^2\left(\zeta^2-1\right)\implies\\
\end{split}
$$
Thus, the roots are
$$
\begin{split}
s&=\frac{-b\pm\sqrt{\Delta}}{2a}\implies\\
&=\frac{-2\zeta\omega_n\pm\sqrt{4\omega_n^2\left(\zeta^2-1\right)}}{2}\implies\\
&=-\zeta\omega_n\pm\omega_n\sqrt{\zeta^2-1}\implies\\
\end{split}
$$
As $\zeta<1\implies\zeta^2<1$,  $\zeta^2-1<0$. So, to perform the transformation more practical, one can handle the denominator as
$$
\begin{split}
\left(s+\zeta\omega_n\right)^2&=s^2+2\zeta\omega_ns+\left(\zeta\omega_n\right)^2\implies\\
s^2+2\zeta\omega_ns+\omega_n^2&=\left(s+\zeta\omega_n\right)^2-\left(\zeta\omega_n\right)^2+\omega_n^2\implies\\
s^2+2\zeta\omega_ns+\omega_n^2&=\left(s+\zeta\omega_n\right)^2+\omega_n^2\left(1-\zeta^2\right)
\end{split}
$$
And the main function results in
$$
\begin{split}
\theta_e&=\frac{\Delta\omega}{\left(s+\zeta\omega_n\right)^2+\omega_n^2\left(1-\zeta^2\right)}
\end{split}
$$
By the result gotten in [[Demonstration of the Laplace transformation of e to the at times sin of bt]],
$$
e^{-at}\sin\left(bt\right)=\mathcal{L}^{-1}\left\{\frac{b}{\left(s-a\right)^2+b^2}\right\}
$$
To fit the equation of $\theta_e$, one do $a=\zeta\omega_n$ and $b=\omega_n^2\left(1-\zeta^2\right)$,
$$
\begin{split}
\theta_e(s)&=\frac{\Delta\omega}{\left(s+\zeta\omega_n\right)^2+\omega_n^2\left(1-\zeta^2\right)}\implies\\
&=\frac{\Delta\omega}{\omega_n^2\left(1-\zeta^2\right)}\frac{\omega_n^2\left(1-\zeta^2\right)}{\left(s+\zeta\omega_n\right)^2+\omega_n^2\left(1-\zeta^2\right)}
\end{split}
$$
Applying the transformation results
$$
\begin{split}
\theta_e(t)&=\frac{\Delta\omega}{\omega_n}\frac{\sin\left(\omega_n\sqrt{1-\zeta^2}t\right)}{\sqrt{1-\zeta^2}}e^{-\zeta\omega_nt}
\end{split}
$$
#### For $\zeta=1$
$$
\begin{split}
\theta_e(s)&=\frac{\Delta\omega}{s^2+2\zeta\omega_ns+\omega_n^2}\implies\\
&=\frac{\Delta\omega}{s^2+2\omega_ns+\omega_n^2}\implies\\
&=\frac{\Delta\omega}{\left(s+\omega_n\right)^2}\implies\\
\end{split}
$$
Using the expression gotten in [[Demonstration of the Laplace transformation of t to the n times e to the at]]
$$
\frac{n!}{(s-a)^{n+1}}=t^ne^{at}
$$
The equation above has $n=1$ and $a=-\omega_n$. Transforming, results in
$$
\begin{split}
\theta_e(t)&=\mathcal{L}^{-1}\left\{\frac{1}{\left(s+\omega_n\right)^2}\right\}\Delta\omega\implies\\
&=t^ne^{at}\Delta\omega
\end{split}
$$
#### For $\zeta>1$
As it was already gotten, the roots of denominator are
$$
\begin{split}
s&=-\zeta\omega_n+\omega_n\sqrt{\zeta^2-1}\implies\\
&=-\omega_n\left(\zeta+\sqrt{\zeta^2-1}\right)\implies\\
\end{split}
$$
That is,
$$
s_1=-\omega_n\left(\zeta+\sqrt{\zeta^2-1}\right)
$$
and
$$
s_2=-\omega_n\left(\zeta-\sqrt{\zeta^2-1}\right)
$$
Two real roots. Now it's intended the result
$$
\begin{split}
\theta_e(s)=\frac{\Delta\omega}{\left(s-s_1\right)\left(s-s_2\right)}=\frac{A}{s-s_1}+\frac{B}{s-s_2}\implies\\
\Delta\omega=\left(s-s_1\right)\left(s-s_2\right)\left(\frac{A}{s-s_1}+\frac{B}{s-s_2}\right)\implies\\
\Delta\omega=A\left(s-s_2\right)+B\left(s-s_1\right)
\end{split}
$$
If $s=s_1$,
$$
\begin{split}
\Delta\omega&=A\left(s_1-s_2\right)\implies\\
A&=\frac{\Delta\omega}{s_1-s_2}
\end{split}
$$
If $s=s_2$,
$$
\begin{split}
\Delta\omega&=A\left(s_2-s_2\right)+B\left(s_2-s_1\right)\implies\\
B&=\frac{\Delta\omega}{s_2-s_1}
\end{split}
$$
Resulting in the relation $A=-B$. It's already known that, as it was gotten in [[Demonstration of the Laplace transformation of e to the at]]
$$
\mathcal{L}^{-1}\left\{\frac{A}{s-s_1}\right\}=Ae^{s_1t}
$$
and
$$
\mathcal{L}^{-1}\left\{\frac{B}{s-s_2}\right\}=Be^{s_2t}
$$
So the transformation of $\theta_e(s)$ is
$$
\begin{split}
\theta_e(t)&=Ae^{s_1t}+Be^{s_2t}\implies\\
&=A\left(e^{s_1t}-e^{s_2t}\right)\implies\\
&=\frac{\Delta\omega}{s_1-s_2}\left(e^{s_1t}-e^{s_2t}\right)\implies\\
&=\frac{\Delta\omega}{2\omega_n\sqrt{\zeta^2-1}}\left[e^{\left(-\omega_n\zeta+\omega_n\sqrt{\zeta^2-1}\right)t}-e^{\left(-\omega_n\zeta-\omega_n\sqrt{\zeta^2-1}\right)t}\right]\implies\\
&=\frac{\Delta\omega}{2\omega_n\sqrt{\zeta^2-1}}\left[e^{-\omega_nt\zeta+\omega_nt\sqrt{\zeta^2-1}}-e^{-\omega_nt\zeta-\omega_nt\sqrt{\zeta^2-1}}\right]\implies\\
&=\frac{\Delta\omega}{2\omega_n\sqrt{\zeta^2-1}}\left[e^{\omega_nt\sqrt{\zeta^2-1}}-e^{-\omega_nt\sqrt{\zeta^2-1}}\right]e^{-\omega_nt\zeta}
\end{split}
$$

By the definition of $\sinh(x)$ as obtained in [[Demonstration of the definition of sinh of x]],

$$
\sinh(x)=\frac{e^{x}-e^{-x}}{2}
$$
Substituting with $x=\omega_nt\sqrt{\zeta^2-1}$,
$$
e^{\omega_nt\sqrt{\zeta^2-1}}-e^{-\omega_nt\sqrt{\zeta^2-1}}=2\sinh(\omega_nt\sqrt{\zeta^2-1})
$$
Resulting in
$$
\theta_e(t)=\frac{\Delta\omega}{\omega_n\sqrt{\zeta^2-1}}\sinh(\omega_nt\sqrt{\zeta^2-1})e^{-\omega_nt\zeta}
$$

### 3. Summary
|                  Caso                   | Solução para $$\theta_e(t)$$                                                                                                                   |
| :-------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------- |
|      $$\zeta < 1$$ (subamortecido)      | $$\theta_e(t) = \Delta\omega \cdot \frac{1}{\omega_n \sqrt{1-\zeta^2}} e^{-\zeta\omega_n t} \sin\left(\omega_n \sqrt{1-\zeta^2} \, t\right)$$  |
| $$\zeta = 1$$ (criticamento amortecido) | $$\theta_e(t) = \Delta\omega \cdot t \, e^{-\omega_n t}$$                                                                                      |
|     $$\zeta > 1$$ (superamortecido)     | $$\theta_e(t) = \Delta\omega \cdot \frac{1}{\omega_n \sqrt{\zeta^2-1}} e^{-\zeta\omega_n t} \sinh\left(\omega_n \sqrt{\zeta^2-1} \, t\right)$$ |
