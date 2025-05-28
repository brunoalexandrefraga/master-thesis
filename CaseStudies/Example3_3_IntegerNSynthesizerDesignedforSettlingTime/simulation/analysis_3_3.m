% analyze_settling_time.m

t = out.vco_ctrl_data.time;
y = out.vco_ctrl_data.signals.values;

% Valor final: média dos últimos 1% da simulação
N = length(y);
y_final = 1.457;

t_init = 350e-6;

% Faixa de tolerância
tol = 0.01 * abs(y_final);
y_upper = y_final + tol;
y_lower = y_final - tol;

% Encontrar o tempo em que o sinal entra e permanece na faixa
settling_index = NaN;
for i = 1:N
    if all(y(i:end) <= y_upper & y(i:end) >= y_lower)
        settling_index = i;
        break;
    end
end

if isnan(settling_index)
    disp('O sinal nunca entrou e permaneceu dentro da faixa de ±1%.');
else
    settling_instant = t(settling_index);
    fprintf('Settling instant (99%%): %.6f s\n', settling_instant);

    settling_time = settling_instant - t_init;
    fprintf('Settling time (99%%): %.3f us\n', settling_time * 1e6);
end
