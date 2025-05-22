clc; clear; close all;


N = 5;
A0 = 1;
KVCO = 10e6;
I = 1e-3;
Kphase = I / (2 * pi);

zeta = 0.707;
t_n = 10e-6;
f_n = 1 / t_n;
omega_n = 2 * pi * f_n;

% Exibir os valores calculados
fprintf('Frequência natural (f_n): %.3f Hz\n', f_n);
fprintf('Tempo natural (t_n): %.3g s\n', t_n);
fprintf('Fator de amortecimento (zeta): %.3f\n', zeta);


% Definição dos parâmetros do PLL
C1 = (Kphase * KVCO) / (N * omega_n^2);
C2 = C1 / 10;
R1 = (zeta * 4 * pi * N * omega_n) / (I * KVCO);


% Exibir os valores calculados
fprintf('C1: %.3g F\n', C1);
fprintf('C2: %.3g F\n', C2);
fprintf('R1: %.3g R\n', R1);


% Definição da variável Laplace
s = tf('s');


Fnum = s * C1 * R1 + 1;
Fden = s^2 * C1 * C2 * R1 + s * (C1+ C2);
F = Fnum / Fden;

K = A0 * Kphase * KVCO / N;

G = K * F / s;

Hnum = G;
Hden = 1 + G;
H = Hnum / Hden;




% Frequência absoluta para análise de resposta em frequência
omega_n_meas = sqrt(KVCO * Kphase / (N * (C1 + C2)));
f_n_meas = omega_n_meas / (2 * pi);
omega = logspace(log10(0.1 * omega_n_meas), log10(100 * omega_n_meas), 1000);

zeta_meas = (C1 * R1 / 2) * sqrt(KVCO * Kphase / (N * (C1 + C2)));
t_s_meas = 4 / (zeta_meas * omega_n_meas);

t_n_meas = 1 / f_n_meas;

% Exibir os valores calculados
fprintf('Frequência natural (f_n_meas): %.3f Hz\n', f_n_meas);
fprintf('Tempo natural (t_n_meas): %.3g s\n', t_n_meas);
fprintf('Fator de amortecimento (zeta_meas): %.3f\n', zeta_meas);
fprintf('Tempo de estabilização (t_s_meas): %.3g s\n', t_s_meas);

% Plotando resposta em frequência (Bode Plot)
figure;
bode(H, omega);
grid on;
title('Resposta em frequência do PLL closed-loop');
xlabel('Frequência (Hz)');

% Plotando resposta em frequência (Bode Plot)
figure;
bode(G, omega);
grid on;
title('Resposta em frequência do PLL open-loop');
xlabel('Frequência (Hz)');

% Plotando resposta ao impulso
figure;
impulse(H);
grid on;
title('Resposta ao Impulso');

% Plotando resposta ao degrau
figure;
step(H);
grid on;
title('Resposta ao Degrau');

% Plotando polos e zeros da malha aberta (G)
figure;
pzmap(G);
grid on;
title('Polos e Zeros da Malha Aberta (G)');

% Plotando polos e zeros da malha fechada (H)
figure;
pzmap(H);
grid on;
title('Polos e Zeros da Malha Fechada (H)');
