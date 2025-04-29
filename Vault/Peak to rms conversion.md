### Conversion from Peak Voltage to RMS for a Sinusoidal Waveform

Given a sinusoidal voltage:

$$
v(t) = V_p \cdot \sin(\omega t)
$$

We want to compute the RMS value over one period \( T \):

$$
V_{\text{RMS}} = \sqrt{\frac{1}{T} \int_0^T v^2(t)\, dt}
$$

#### Step 1: Square the signal

$$
v^2(t) = V_p^2 \cdot \sin^2(\omega t)
$$

#### Step 2: Use trigonometric identity

$$
\sin^2(\omega t) = \frac{1 - \cos(2\omega t)}{2}
$$

So,

$$
v^2(t) = V_p^2 \cdot \frac{1 - \cos(2\omega t)}{2}
$$

#### Step 3: Integrate over one period \( T = \frac{2\pi}{\omega} \)

$$
V_{\text{RMS}} = \sqrt{ \frac{1}{T} \int_0^T \frac{V_p^2}{2} (1 - \cos(2\omega t)) \, dt }
$$

Pull out constants:

$$
V_{\text{RMS}} = \sqrt{ \frac{V_p^2}{2T} \int_0^T (1 - \cos(2\omega t)) \, dt }
$$

Now compute the integral:

- $\int_0^T 1\, dt = T$
- $\int_0^T \cos(2\omega t) \, dt = 0$ (since it's one full period)

So:

$$
\int_0^T (1 - \cos(2\omega t)) \, dt = T
$$

Then:

$$
V_{\text{RMS}} = \sqrt{ \frac{V_p^2}{2T} \cdot T } = \sqrt{ \frac{V_p^2}{2} } = \frac{V_p}{\sqrt{2}}
$$

### Final Result:

$$
V_{\text{RMS}} = \frac{V_p}{\sqrt{2}} \approx 0.707 \cdot V_p
$$
