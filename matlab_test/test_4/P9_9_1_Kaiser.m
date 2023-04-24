% 设计参数
wp = 0.2*pi; % 通带截止频率
Rp = 0.25; % 通带最大衰减
ws = 0.3*pi; % 阻带截止频率
As = 50; % 阻带最小衰减

% 确定滤波器阶数
delta_w = ws - wp;
A = -20*log10(sqrt(Rp)); % 计算实际通带最大衰减量
if A > 50
    N = ceil((A-7.95)/(2.285*delta_w)); % 公式1
else
    N = ceil(5.79/delta_w); % 公式2
end

% 计算 Kaiser 窗函数参数 beta
if A <= 21
    beta = 0;
elseif A > 21 && A <= 50
    beta = 0.5842*(A-21)^0.4 + 0.07886*(A-21);
else
    beta = 0.1102*(A-8.7);
end

% 构建理想低通滤波器的频率响应
n = -(N-1)/2:(N-1)/2; % 滤波器长度为N
hd = sin(wp*n)./(pi*n); % 理想低通滤波器的频率响应
hd((N+1)/2) = wp/pi; % 当 n=0 时，直接计算

% 计算 Kaiser 窗函数
w = kaiser(N,beta);

% 计算实际低通滤波器的频率响应
h = hd .* w';

% 绘制幅度特性曲线
[H,f] = freqz(h,1,1024);
plot(f/pi,20*log10(abs(H)));
grid on;
xlabel('归一化频率');
ylabel('幅度(dB)');
title('Kaiser 窗设计数字FIR低通滤波器');

% 输出滤波器参数
disp(['滤波器阶数为：',num2str(N)]);
disp(['Kaiser窗参数beta为：',num2str(beta)]);
