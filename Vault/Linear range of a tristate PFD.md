# **Linear range of a tristate PFD**

The linearity limit of a Phase Frequency Detector (PFD) corresponds to the phase error range in which its output remains approximately proportional to the input phase difference. Outside this range, the PFD exhibits nonlinear behavior, potentially leading to [[Cycle slipping]].

For a typical tristate PFD (used with charge pumps), the linear range is:

$$
∣\phi_e∣\le2\pi
$$

This limit arises from the **functional behavior** of the topology rather than an analytical expression. The PFD measures the time difference between clock edges. When the phase error exceeds one full cycle ($2\pi$), it loses the ability to distinguish between multiples of $2\pi$, causing slips.

To estimate this range:

- Simulate the PFD (with or without the charge pump) under varying phase offsets.
    
- Identify the region where the output (e.g., pulse width or current) changes linearly with phase error.
    

For digital clocked PFDs, the practical linear range is empirically found to be around $\pm2\pi$ radians.