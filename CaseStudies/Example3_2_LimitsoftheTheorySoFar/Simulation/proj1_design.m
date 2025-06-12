phase_errors = linspace(-2*pi, 2*pi, 1000);
T_clk = 100e-9; % período do clock (10 MHz)
delay_time = (phase_errors / (2*pi)) * T_clk;