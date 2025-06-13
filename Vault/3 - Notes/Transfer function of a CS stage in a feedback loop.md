```tikz
\usepackage{circuitikz}

\begin{document}
\begin{circuitikz}[american]
    % Transistor NMOS M1
    \ctikzset{tripoles/mos style/arrows}
    \draw (1,-2) node[nmos] (M1) {$M_1$};
    \draw (M1.S) -- ++(0,-0.5) node[ground]{};
    \draw (M1.G) -- ++(0,-1.27) node[ground]{};

    % Conexão dreno ao resistor
    \draw (M1.D) to[R=$R_D$] ++(0,2) node[vcc](VCC){$V_{CC}$};

    % Carga capacitiva CL
    \draw (M1.D) -- ++(1.5,0) to[C=$C_L$] ++(0,-2.04) node[ground]{};

    % Linha de realimentação até o gate
    \draw (M1.D) ++(1.5,0) -- ++(1.5,0) -- (4,-4.5) -- (-1,-4.5) -- (-1,-2) -- (M1.G);

    % Caixa tracejada
    \draw[dashed] (-0.5,-4) rectangle (3.6,2);

    % Rótulo -H(s)
    \node at (-1.2, 1.8) {$-H(s)$};
\end{circuitikz}
\end{document}
```

$$
\begin{split}
H(s)&=\frac{V_o}{V_i}=g_m\left(\frac{R_D}{sR_DC_L+1}\right)\implies\\
&=\frac{g_mR_D}{sR_DC_L+1}
\end{split}
$$