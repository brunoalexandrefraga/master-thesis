# Cycle Slipping

Cycle slipping is an undesired phenomenon in Phase-Locked Loops (PLLs) that occurs when the phase error between the reference input and the feedback output exceeds the linear range of the system, typically that of the Phase Detector (PD) or Phase-Frequency Detector (PFD).

Cycle slipping occurs when the PLL is unable to maintain phase lock, and the phase error grows beyond $2\pi$, resulting in a temporary loss of synchronization. The loop then slips by one or more full cycles before attempting to reacquire lock.

This phenomenon is particularly critical in high-speed systems, as it can lead to increased phase noise, jitter, or even failure to maintain a stable lock.
