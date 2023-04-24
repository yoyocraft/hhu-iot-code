% 设置参数
wp = 0.2 * pi; % 通带截止频率
ws = 0.3 * pi; % 阻带截止频率
Rp = 0.25; % 通带最大衰减量（单位：dB）
As = 50; % 阻带最小衰减量（单位：dB）

% 求出滤波器阶数N
delta_p = (10^(Rp/20)-1)/(10^(Rp/20)+1);
delta_s = 10^(-As/20);
delta_min = min(delta_p, delta_s);
delta_max = max(delta_p, delta_s);
delta = delta_min;
N = ceil((As-7.95)/(2.285*(ws-wp)));

% 求出截止频率wp和ws对应的归一化频率ωp和ωs
omega_p = wp / pi;
omega_s = ws / pi;

% 根据Rp和As计算出通带衰减量δp和阻带衰减量δs
delta_p = (10^(Rp/20)-1)/(10^(Rp/20)+1);
delta_s = 10^(-As/20);

% 选择Bartlett窗函数，并计算窗函数参数M
M = N - 1;
w = bartlett(M+1)';

% 计算滤波器系数h(n)
n = 0:M;
h = omega_p/pi * sinc(omega_p*(n-M/2)) .* w;

% 绘制滤波器幅频响应曲线，检查是否符合要求
[H,f] = freqz(h);
figure;
plot(f/pi,20*log10(abs(H)));
hold on;
plot([0 omega_p omega_p],[0 -Rp -As],'--r');
plot([omega_s omega_s 1],[0 -As -As],'--r');
axis([0 1 -60 5]);
grid on;
xlabel('Normalized Frequency (\times\pi rad/sample)');
ylabel('Magnitude (dB)');
title('Bartlett Window FIR Filter');