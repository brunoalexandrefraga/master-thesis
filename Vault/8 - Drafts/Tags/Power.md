## 📌 Mathematical Definition of Power

The **average power** of a signal $x(t)$ is defined as:

$$
P = \lim_{T \to \infty} \frac{1}{2T} \int_{-T}^{T} |x(t)|^2 \, dt
$$

This represents the time-average of the instantaneous power of the signal. It is commonly used for signals with **finite power**, such as periodic signals or stationary random processes.

---

## ⚡ Power of a Sine Wave

Let the signal be:

$$
x(t) = A\sin(\omega t + \phi)
$$

Then the power is:

$$
P = \lim_{T \to \infty} \frac{1}{2T} \int_{-T}^{T} A^2 \sin^2(\omega t + \phi) \, dt
$$

Using the identity:

$$
\sin^2(\theta) = \frac{1 - \cos(2\theta)}{2}
$$

We get:

$$
P = \lim_{T \to \infty} \frac{1}{2T} \int_{-T}^{T} \frac{A^2}{2} \left[1 - \cos(2\omega t + 2\phi)\right] dt
$$

Since the integral of a cosine over a full period is zero, the result is:

$$
P = \frac{A^2}{2}
$$

---

## ⚡ Power of a Cosine Wave

Let the signal be:

$$
x(t) = A\cos(\omega t + \phi)
$$

Then the power is:

$$
P = \lim_{T \to \infty} \frac{1}{2T} \int_{-T}^{T} A^2 \cos^2(\omega t + \phi) \, dt
$$

Using the identity:

$$
\cos^2(\theta) = \frac{1 + \cos(2\theta)}{2}
$$

We get:

$$
P = \lim_{T \to \infty} \frac{1}{2T} \int_{-T}^{T} \frac{A^2}{2} \left[1 + \cos(2\omega t + 2\phi)\right] dt
$$

Again, the integral of the cosine term averages to zero:

$$
P = \frac{A^2}{2}
$$

---

## ✅ Summary

> For both sine and cosine waves, the average power is:

$$
P = \frac{A^2}{2}
$$
