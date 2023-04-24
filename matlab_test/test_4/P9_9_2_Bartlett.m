% 设置参数
wp1 = 0.35*pi;
ws1 = 0.2*pi;
wp2 = 0.65*pi;
ws2 = 0.8*pi;
Rp = 1; % 通带最大衰减（dB）
As = 60; % 阻带最小衰减（dB）

% 计算滤波器阶数
delta_w1 = wp1 - ws1;
delta_w2 = ws2 - wp2;
delta_w = min(delta_w1, delta_w2);
M = ceil((As - 7.95)/(14.36*delta_w)+1);

% 构建Bartlett窗
w = bartlett(M+1);

% 计算理想的频率响应
n = 0: M;
h_ideal = (wp2/pi)*sinc(wp2*(n-M/2)/pi) - (wp1/pi)*sinc(wp1*(n-M/2)/pi);

% 应用窗函数
h = h_ideal .* w';

% 频域响应分析
[H, w] = freqz(h, 1);

% 绘制幅度响应曲线
figure;
plot(w/pi, 20*log10(abs(H)));
hold on;
plot([0, wp1/pi, wp1/pi, wp2/pi, wp2/pi, 1], [-As, -As, -Rp, -Rp, -As, -As], 'r');
hold off;
grid on;
title('Bartlett窗设计低通滤波器');
xlabel('归一化频率');
ylabel('幅度(dB)');
ylim([-80, 5]);