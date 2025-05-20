clc; clear; close all;


N = 5;
A0 = 1;
KVCO = 10e6;
I = 1e-3;
Kphase = I / (2 * pi);

fref = 10e6;

zeta = 0.707;
f_n = fref / 10;
f_bw = f_n * sqrt(1 + 2*zeta^2 + sqrt(4*zeta^4 + 4*zeta^2 + 2));
omega_bw = 2 *pi * f_bw;
omega_n = 2 * pi * f_n;