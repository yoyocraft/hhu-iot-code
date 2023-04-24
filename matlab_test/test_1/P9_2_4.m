clf;
n = 0 : 40;
D = 10;
a = 3.0;
b = -2;
x = a * cos(2 * pi * 0.1 * n) + b * cos(2 * pi * 0.4 * n);
xd = [zeros(1, D) x];
num = [2.2403 2.4908 2.2403];
den = [1 -0.4 0.75];
ic = [0 0]; % 设置初始条件
% 计算输出y[n]
y = filter(num, den, x, ic);
% 计算输出yd[n]
yd = filter(num, den, xd, ic);
% 计算输出差值d[n]
d = y - yd(1 + D : 41 + D);
% Plot the outputs
subplot(3, 1, 1);
stem(n ,y);
ylabel('幅值');
title('输出y[n]');
grid;
subplot(3, 1, 2);
stem(n, yd(1:41));
ylabel('幅值');
title(['由延时输入x[n]得到的输出',num2str(D)]);
grid;
subplot(3, 1, 3);
stem(n, d);
xlabel('时间下标n');
ylabel('幅值');
title('信号差值');
grid;