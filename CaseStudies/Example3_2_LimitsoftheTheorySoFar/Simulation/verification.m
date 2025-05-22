clc; clear; close all;

zeta = 0.707;
f_bw = 150e3;
omega_bw = 2*pi*f_bw;

omega_n = omega_bw / sqrt(1 + 2*zeta^2 + sqrt(4*zeta^4 + 4*zeta^2 + 2));
fprintf('omega_n = %.4e rad/s\n', omega_n);

t_m = 1/(omega_n*sqrt(1 - zeta^2)) * atan(sqrt(1 - zeta^2)/zeta);
fprintf('t_m = %.4e s\n', t_m);

theta_e_m_n = sin(omega_n * sqrt(1 - zeta^2) * t_m) / sqrt(1 - zeta^2) * exp(-zeta * omega_n * t_m);
fprintf('theta_e_m_n = %.4e rad\n', theta_e_m_n);

theta_e_m = 2 * pi;

step_m_ang = theta_e_m * omega_n / theta_e_m_n;
fprintf('step_m_ang = %.4e rad/s\n', step_m_ang);

step_m_lin = step_m_ang / (2*pi);
fprintf('step_m_lin = %.4e Hz\n', step_m_lin);

t_s = log(0.01 * sqrt(1 - zeta^2)) / (-zeta * omega_n);
fprintf('t_s = %.4e s\n', t_s);
