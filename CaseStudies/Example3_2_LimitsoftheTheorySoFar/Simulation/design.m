zeta = 0.707;
f_bw = 150e3;
omega_bw = 2*pi*f_bw;

f_r = 10e6;
f_o = 50e6;
N = 5;
KVCO = 10e6;
I = 1e-3;
Kphase = I / (2 * pi);
%A0 = 6.257;
A0 = 6.258;
K = A0 * Kphase * KVCO / N;

omega_n = omega_bw / sqrt(1 + 2 * zeta^2 + sqrt(4 * zeta^4 + 4 * zeta^2 + 2));
f_n = omega_n/2/pi;

% Parâmetros do PLL
C1 = K / omega_n^2;
C2 = C1 / 10;
R1 = 2 * zeta * omega_n / K;

N0 = 5;
fi = 10e6; % Hz
step_f_m = 502.16e3;
%step_f = step_f_m + step_f_m * 0.7084;
%step_f = step_f_m + step_f_m * 0.62575;
%step_f = step_f_m + step_f_m * 0.6257;
step_f = 816.27e3;
fprintf('Step frequency: %.6f s\n', step_f);
fr = fi + step_f;
fo = N0 * fr; % Hz
fvco = 50e6; % Hz
Kvco = 10e6; % Hz/V
v_c = (fo - fvco) / Kvco;
fprintf('Voltage control: %.6f s\n', v_c);