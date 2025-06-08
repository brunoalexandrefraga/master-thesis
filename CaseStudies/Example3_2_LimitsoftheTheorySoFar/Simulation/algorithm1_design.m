zeta = 0.707;
f_bw = 150e3;
omega_bw = 2 * pi * f_bw;

f_r = 10e6;
f_o = 50e6;
N = 5;
KVCO_lin = 10e6;
KVCO_ang = 2 * pi * KVCO_lin;
I = 1e-3;
Kphase = I / (2 * pi);
A0 = 1;
K = A0 * Kphase * KVCO_ang / N;

omega_n = omega_bw / sqrt(1 + 2 * zeta^2 + sqrt(4 * zeta^4 + 4 * zeta^2 + 2));
f_n = omega_n / (2 * pi);

% Parâmetros do PLL
C1 = K / omega_n^2;
C2 = C1 / 10;
R1 = 2 * zeta * omega_n / K;

N0 = 5;
fi = 10e6; % Hz


% Frequência absoluta para análise de resposta em frequência
omega_n_meas = sqrt(K / C1);
zeta_meas = R1 / 2 * sqrt(K * C1);

t_m = 1/(omega_n_meas*sqrt(1 - zeta_meas^2)) * atan(sqrt(1 - zeta_meas^2)/zeta_meas);
theta_e_m_n = sin(omega_n_meas * sqrt(1 - zeta_meas^2) * t_m) / sqrt(1 - zeta_meas^2) * exp(-zeta_meas * omega_n_meas * t_m);
fprintf('theta_e_m_n = %.4e rad\n', theta_e_m_n);
theta_e_m = 1.62435 * pi;
step_m_ang = theta_e_m * omega_n_meas / theta_e_m_n;
step_m_lin = step_m_ang / (2*pi);
fprintf('step_m_lin = %.4e Hz\n', step_m_lin);


step_f = step_m_lin * 1.00;



fprintf('Step frequency: %.6f s\n', step_f);
fr = fi + step_f;
fo = N0 * fr; % Hz
fvco = 50e6; % Hz
v_c = (fo - fvco) / KVCO_lin;
fprintf('Voltage control: %.6f s\n', v_c);