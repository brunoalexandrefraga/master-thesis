clc; clear; close all;


N = 5;
A0 = 1;
KVCO = 10e6;
I = 1e-3;
Kphase = I / (2 * pi);

zeta = 0.707;
f_bw = 150e3;
omega_bw = 2*pi*f_bw;
omega_n = omega_bw / sqrt(1 + 2*zeta^2 + sqrt(4*zeta^4 + 4*zeta^2 + 2));


% Definição dos parâmetros do PLL
C1 = (Kphase * KVCO) / (N * omega_n^2);
C2 = C1 / 10;
R1 = (zeta * 4 * pi * N * omega_n) / (I * KVCO);


% Exibir os valores calculados
fprintf('C1: %.3g F\n', C1);
fprintf('C2: %.3g F\n', C2);
fprintf('R1: %.3g R\n', R1);


% % Definição da variável Laplace
% s = tf('s');
% 
% Fnum = s * C1 * R1 + 1;
% Fden = s^2 * C1 * C2 * R1 + s * (C1+ C2);
% F = Fnum / Fden;
% 
% K = A0 * Kphase * KVCO / N;
% 
% G = K * F / s;
% 
% Hnum = G;
% Hden = 1 + G;
% H = Hnum / Hden;




% Frequência absoluta para análise de resposta em frequência
omega_n_meas = sqrt(KVCO * Kphase / (N * (C1 + C2)));
zeta_meas = (C1 * R1 / 2) * sqrt(KVCO * Kphase / (N * (C1 + C2)));


t_m = 1/(omega_n_meas*sqrt(1 - zeta_meas^2)) * atan(sqrt(1 - zeta_meas^2)/zeta_meas);
fprintf('t_m = %.4e s\n', t_m);

theta_e_m_n = sin(omega_n_meas * sqrt(1 - zeta_meas^2) * t_m) / sqrt(1 - zeta_meas^2) * exp(-zeta_meas * omega_n_meas * t_m);
fprintf('theta_e_m_n = %.4e rad\n', theta_e_m_n);

theta_e_m = 2 * pi;

step_m_ang = theta_e_m * omega_n_meas / theta_e_m_n;
fprintf('step_m_ang = %.4e rad/s\n', step_m_ang);

step_m_lin = step_m_ang / (2*pi);
fprintf('step_m_lin = %.4e Hz\n', step_m_lin);

t_s = log(0.01 * sqrt(1 - zeta_meas^2)) / (-zeta_meas * omega_n_meas);
fprintf('t_s = %.4e s\n', t_s);









% omega = logspace(log10(0.1 * omega_n_meas), log10(100 * omega_n_meas), 1000);
% 
% % Plotando resposta em frequência (Bode Plot)
% figure;
% bode(H, omega);
% grid on;
% title('Resposta em frequência do PLL closed-loop');
% xlabel('Frequência (Hz)');
% 
% % Plotando resposta em frequência (Bode Plot)
% figure;
% bode(G, omega);
% grid on;
% title('Resposta em frequência do PLL open-loop');
% xlabel('Frequência (Hz)');
% 
% % Plotando resposta ao impulso
% figure;
% impulse(H);
% grid on;
% title('Resposta ao Impulso');
% 
% % Plotando resposta ao degrau
% figure;
% step(H);
% grid on;
% title('Resposta ao Degrau');
% 
% % Plotando polos e zeros da malha aberta (G)
% figure;
% pzmap(G);
% grid on;
% title('Polos e Zeros da Malha Aberta (G)');
% 
% % Plotando polos e zeros da malha fechada (H)
% figure;
% pzmap(H);
% grid on;
% title('Polos e Zeros da Malha Fechada (H)');
