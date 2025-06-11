% Parâmetros de entrada
theta_e_meas = 0.5149;       % Valor medido de theta_e_m_n
% Função a ser anulada
f = @(zeta) (sin(omega_n_meas * sqrt(1 - zeta.^2) * t_m) ./ sqrt(1 - zeta.^2)) ...
            .* exp(-zeta * omega_n_meas * t_m) - theta_e_meas;

% Resolver numericamente: intervalo (0, 1) para sistema subamortecido
zeta_initial_guess = 0.5;
zeta_meas = fzero(f, [0.001, 0.999]);

% Exibir resultado
fprintf('zeta_meas = %.6f\n', zeta_meas);
