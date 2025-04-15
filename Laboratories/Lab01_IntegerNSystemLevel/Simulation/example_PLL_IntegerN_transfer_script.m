clc; clear; close all;

% Definição dos parâmetros do PLL
C1 = 200e-9;
C2 = 20e-9;
Cs = C1 * C2 / (C1 + C2);
N = 5;
R = 200;
KVCO = 10e6;
I = 1e-3;
Kphase = I / (2 * pi);

% Definição da variável Laplace
s = tf('s');

% Função de transferência do PLL (nova equação)
num = KVCO * Kphase * (1 + s * C1 * R);
den = s^2 * N * (C1 + C2) * (1 + s * Cs * R) + KVCO * Kphase * (1 + s * C1 * R);
H = num / den;

zeta = (C1 * R / 2) * sqrt(KVCO * Kphase / (N * (C1 + C2)));



% Frequência absoluta para análise de resposta em frequência
omega_n = sqrt(KVCO * Kphase / (N * (C1 + C2)));
omega = logspace(log10(0.1 * omega_n), log10(100 * omega_n), 1000);

% Cálculo do tempo de estabilização
t_s = 4 / (zeta * omega_n);

% Exibir os valores calculados
fprintf('Frequência natural (omega_n): %.2f Hz\n', omega_n);
fprintf('Fator de amortecimento (zeta): %.2f\n', zeta);
fprintf('Tempo de estabilização (t_s): %.6f s\n', t_s);

% Plotando resposta em frequência (Bode Plot)
figure;
bode(H, omega);
grid on;
title('Resposta em frequência do PLL');
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



