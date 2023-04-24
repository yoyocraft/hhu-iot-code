% 设计数字FIR低通滤波器
% 技术指标：下阻带边缘：w1s=0.2π，As=60dB;
% 下通带边缘：w1p=0.35π, Rp=1dB;
% 上阻带边缘：w2s=0.8π，As=60dB;
% 上通带边缘：w2p=0.65π, Rp=1dB
% 用Kaiser窗设计这个低通滤波器

% 设置参数
wp1 = 0.35*pi;
ws1 = 0.2*pi;
wp2 = 0.65*pi;
ws2 = 0.8*pi;
Rp = 1; % 通带最大衰减（dB）
As = 60; % 阻带最小衰减（dB）

% 计算滤波器阶数和beta值
delta_w1 = wp1 - ws1;
delta_w2 = ws2 - wp2;
delta_w = min(delta_w1, delta_w2);
A = -20*log10(sqrt(Rp));
if A > 50
    beta = 0.1102*(A-8.7);
else
    beta = 0.5842*(A-21)^0.4 + 0.07886*(A-21);
end
M = ceil((As-8)/(2.285*delta_w)+1);

% 构建Kaiser窗
n = 0:M;
w = kaiser(M+1, beta);

% 计算理想的频率响应
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
title('Kaiser窗设计低通滤波器');
xlabel('归一化频率');
ylabel('幅度(dB)');
ylim([-80, 5]);
