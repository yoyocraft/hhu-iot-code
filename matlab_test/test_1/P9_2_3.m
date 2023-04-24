clf;
n = 0 : 40;
a = 2;
b = -3;
x1 = cos(2 * pi * 0.1 * n);
x2 = cos(2 * pi * 0.4 * n);
x = a * x1 + b * x2;
num = [2.2403 2.4908 2.2403];
den = [1 -0.4 0.75];
ic = [0 0]; % 设置零初始条件
y1 = filter(num, den, x1, ic);  % 计算输出y1[n]
y2 = filter(num, den, x2, ic);  % 计算输出y2[n]
y = filter(num, den, x, ic);    % 计算输出y[n]
yt = a * y1 + b * y2;
d = y - yt; % 计算输出差值d[n]
subplot(3, 1, 1);
stem(n, y);
ylabel('幅度');
title('针对不同的权重输入的输出: a \cdot x_{1}[n] + b \cdot x_{2}[n]');
subplot(3, 1, 2);
stem(n, yt);
ylabel('幅度');
title('权重及输出: a \cdot y_{1}[n] + b \cdot y_{2}[n]');
subplot(3, 1, 3);
stem(n, d);
xlabel('时间下标n');
ylabel('幅值');
title('信号差值');
