As it was seen in [[Transfer function of a CS stage in a feedback loop]], the presented transfer function have a canonical form of a first-order system with a single pole or the form of a low-pass filter. It's possible to rewrite the above equation as
$$
H(s)=\frac{K}{s\tau+1}
$$
where $K=g_mR_D$ and $\tau=R_DC_L$.
Substituting $s=j\omega$,
$$
H(s)=\frac{K}{j\omega\tau+1}
$$
The calculation of the
$$
\angle H(j\omega)=-\tan^{-1}\left(\omega\tau\right)
$$
That way,
$$
\lim_{\omega\to0}\left[\tan^{-1}(\omega\tau)\right]=0^\circ
$$
and
$$
\lim_{\omega\to\infty}\left[\tan^{-1}(\omega\tau)\right]=-90^\circ
$$
That way, $H(s)=-1$ cannot be achieved for a finite frequency.