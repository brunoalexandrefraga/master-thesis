%% Fechar figuras abertas
close all;

%% Extração dos dados do Simulink
dataset1 = out.ScopeData1;
dataset2 = out.ScopeData2;
dataset3 = out.ScopeData3;

% Sinal de corrente do charge pump
icp_ts = dataset2{1}.Values;
t_icp  = icp_ts.Time;
i_cp   = icp_ts.Data;

% Sinais UP e DOWN
up_ts   = dataset3{1}.Values;
down_ts = dataset3{2}.Values;

t_up   = up_ts.Time;
d_up   = up_ts.Data;
t_down = down_ts.Time;
d_down = down_ts.Data;

%% Detectar pulsos UP
up_rising  = find(diff(d_up) > 0.5);
up_falling = find(diff(d_up) < -0.5);

n_up_pulses = min(length(up_rising), length(up_falling));
t_up_start = t_up(up_rising(1:n_up_pulses) + 1);
t_up_end   = t_up(up_falling(1:n_up_pulses) + 1);
pulse_width_up = t_up_end - t_up_start;

%% Detectar pulsos DOWN
down_rising  = find(diff(d_down) > 0.5);
down_falling = find(diff(d_down) < -0.5);

n_down_pulses = min(length(down_rising), length(down_falling));
t_down_start = t_down(down_rising(1:n_down_pulses) + 1);
t_down_end   = t_down(down_falling(1:n_down_pulses) + 1);
pulse_width_down = t_down_end - t_down_start;

%% Garantir pareamento final
num_pulses = min([length(pulse_width_up), length(pulse_width_down)]);
pulse_width_up   = pulse_width_up(1:num_pulses);
pulse_width_down = pulse_width_down(1:num_pulses);

t_error = 0.5 * (t_up_start(1:num_pulses) + t_up_end(1:num_pulses));
delta_t = pulse_width_up - pulse_width_down;

%% Conversão para erro de fase em π rad
f_ref = 10e6;  % <<< ajuste conforme a frequência do seu sinal de referência
T = 1 / f_ref;

phase_error_pi = 2 * delta_t / T;  % em unidades de π rad

%% Plotar erro de fase (em múltiplos de π rad)
figure;
plot(t_error, phase_error_pi);
xlabel('Tempo (s)');
ylabel('Erro de fase (π rad)');
title('Erro de fase via pulsos UP e DOWN (em π rad)');
grid on;
yticks_vals = -2:1:2;
yticks(yticks_vals);
yticklabels({'-2\pi', '-\pi', '0', '\pi', '2\pi'});

%% Corrente média do Charge Pump com base nos pulsos UP e DOWN
I_ref = 1e-3;  % <<< Defina o valor da corrente ideal (em ampères)
T = 1 / f_ref;   % Período do sinal de referência

% Cálculo da corrente média por ciclo
i_cp_avg_by_pulse = I_ref * (pulse_width_up - pulse_width_down) / T;

% Tempo de referência: centro do pulso
t_cp_avg = t_error;  % mesmo tempo dos pulsos já alinhados

%% Plotar corrente média do CP baseada nos pulsos
figure;
plot(t_cp_avg, i_cp_avg_by_pulse);
xlabel('Tempo (s)');
ylabel('Corrente média (A)');
title('Corrente média do Charge Pump com base nos pulsos UP/DOWN');
grid on;

%% Plotar corrente média do CP em função do erro de fase
figure;
plot(phase_error_pi, i_cp_avg_by_pulse);
xlabel('Erro de fase (π rad)');
ylabel('Corrente média (A)');
title('Corrente média do CP vs Erro de fase');
grid on;

%% NOVA SEÇÃO: Cálculo do erro de fase via sinais de ref e fb (correto)
% Sinais de entrada
ref_ts = dataset1{1}.Values;
fb_ts  = dataset1{2}.Values;

t_ref = ref_ts.Time;
d_ref = ref_ts.Data;
t_fb  = fb_ts.Time;
d_fb  = fb_ts.Data;

% Detectar bordas de subida
ref_rising = find(diff(d_ref) > 0.5) + 1;  % +1 pois diff remove um ponto
fb_rising  = find(diff(d_fb)  > 0.5) + 1;

% Inicializar variáveis
i_ref = 1;
i_fb  = 1;
t_phase_err = [];
phase_err_rad = [];
last_time = -Inf;  % Inicializa com -Inf para garantir que a 1ª comparação ocorra

% Loop até acabar um dos vetores
while i_ref <= length(ref_rising) && i_fb <= length(fb_rising)
    tr = t_ref(ref_rising(i_ref));
    tf = t_fb(fb_rising(i_fb));

    % Garante que as bordas ainda não foram usadas (devem estar após last_time)
    if tr <= last_time
        i_ref = i_ref + 1;
        continue;
    end
    if tf <= last_time
        i_fb = i_fb + 1;
        continue;
    end

    % Bordas praticamente simultâneas (considera empate se diferença < 1ps)
    if abs(tr - tf) < 1e-12
        t_phase_err(end+1) = tr;
        phase_err_rad(end+1) = 0;
        last_time = tr;  % ou tf, são praticamente iguais
        i_ref = i_ref + 1;
        i_fb  = i_fb + 1;
        continue;
    end

    % Cálculo do erro de fase
    delta_t = tf - tr;
    t_phase_err(end+1) = min(tr, tf);
    last_time = max(tr, tf);  % Atualiza para evitar reutilização
    phase_err_rad(end+1) = 2 * pi * delta_t / T;

    if tr < tf
        % REF subiu antes -> erro de fase positivo (fb atrasado)
        i_ref = i_ref + 1;
    else
        % FB subiu antes -> erro de fase negativo (fb adiantado)
        i_fb = i_fb + 1;
    end
end

% Plotar o erro de fase
figure;
plot(t_phase_err, phase_err_rad / pi);
xlabel('Tempo (s)');
ylabel('Erro de fase (π rad)');
title('Erro de Fase: REF vs FB');
grid on;
ylim([-2 2]);  % Ajuste conforme necessário
yticks(-2:1:2);
yticklabels({'-2\pi','-\pi','0','\pi','2\pi'});
