The SSB phase noise [[Power Spectral Density (PSD)]] to carrier ratio, in units of dBc/Hz, is defined as
$$
\text{PN}_\text{SSB}\left(\Delta\omega\right)=10\log\left[\frac{N\left(\omega_\text{LO}+\Delta\omega\right)+N\left(\omega_\text{LO}-\Delta\omega\right)}{P_c\left(\omega_\text{LO}\right)}\right]
$$
Similar to what was done to the positive SSB in the [[Power of the phase fluctuation of a generic output signal of a synthesizer]],
$$
N(\omega_\text{LO}-\Delta\omega)=\frac{1}{2}\left(\frac{V_0\varphi_p}{2}\right)^2
$$
So, calculating [[Power of the signal carrier of a generic output signal of a synthesizer]],
$$
\begin{split}
\text{PN}_\text{SSB}\left(\Delta\omega\right)&=10\log\left[\frac{\frac{1}{2}\left(\frac{V_0\varphi_p}{2}\right)^2+\frac{1}{2}\left(\frac{V_0\varphi_p}{2}\right)^2}{\frac{1}{2}V_0^2}\right]\implies\\
&=10\log\left(\frac{\frac{V_0^2\varphi_p^2}{4}}{\frac{1}{2}V_0^2}\right)\implies\\
&=10\log\left(\frac{\varphi_p^2}{2}\right)
\end{split}
$$
As $\varphi_p$ is the peak value of, it's possible to express $\text{PN}_\text{SSB}$, using the relation gotten in [[Peak to rms conversion]], $\varphi_\text{rms}=\varphi_p/\sqrt{2}$, so it follows as
$$
\text{PN}_\text{SSB}\left(\Delta\omega\right)=10\log\left(\varphi_\text{rms}^ 2\right)
$$
where $\varphi_\text{rms}^2$ is the root mean squared phase noise PSD in units of $\text{rad}^2/\text{Hz}$.