# MOSFET CS output voltage by a voltage divisor

In triode region, the output voltage of the MOSFET can be described as:

$$
V_{o}=V_{DD}-R_{D}\frac{1}{2}\mu_{n}C_\mathrm{ox}\frac{W}{L}\bigg[2(V_{i}-V_\mathrm{TH})V_{o}-{V_{o}}^{2}\bigg]
$$ 

In deep triode region,

$$
V_{o}<<2(V_{i}-V_{TH})
$$

Thus,

$$
\begin{split}
V_{o}&=V_{DD}-R_{D}\frac{1}{2}\mu_{n}C_\mathrm{ox}\frac{W}{L}\bigg[2(V_{i}-V_\mathrm{TH})V_{o}\bigg]\implies\\
&=V_{DD}-R_{D}\mu_{n}C_\mathrm{ox}\frac{W}{L}(V_{i}-V_\mathrm{TH})V_{o}\implies\\
V_\mathrm{DD}&=V_{o}+R_{D}\mu_{n}C_\mathrm{ox}\frac{W}{L}(V_{i}-V_\mathrm{TH})V_{o}
\end{split}
$$

As it's known:

$$
g_{on}=\mu_{n}C_{ox}\frac{W}{L}(V_{i}-V_{TH})
$$

and

$$R_{on}=g_{on}^{-1}$$

Thus

$$
V_{o}=\frac{V_{DD}}{1+\frac{R_{o}}{R_{on}}}=V_{DD}\frac{R_{on}}{R_{on}+R_{o}}
$$