% --- Script para calcular o Settling Time (1%) ---

% Valor pretendido (valor final de referência)
target_value = 0.5;

% Margem de tolerância (1% do valor de referência)
tolerance = 0.01 * target_value;
upper_bound = target_value + tolerance;
lower_bound = target_value - tolerance;

% Acessando os dados da estrutura
time = out.vco_control_voltage.time;
signal = out.vco_control_voltage.signals.values;

% Determinar o instante a partir do qual o sinal permanece dentro da faixa
settling_instant = NaN;  % Inicializa como NaN caso não se estabilize

for i = 1:length(signal)
    if all(signal(i:end) >= lower_bound & signal(i:end) <= upper_bound)
        settling_instant = time(i);
        break;
    end
end

% Resultado
if isnan(settling_instant)
    fprintf('O sinal não se estabilizou dentro de 1%% da referência (%.2f).\n', target_value);
else
    settling_time = settling_instant - 10e-6;
    fprintf('Settling Time (1%%) = %.6f us\n', settling_time * 1e6);
end