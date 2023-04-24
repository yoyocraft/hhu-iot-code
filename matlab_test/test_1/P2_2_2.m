% 产生一个正弦序列
n = 0 : 40;
f = 0.1;
phase = 0;
A = 1.5;
arg = 2 * pi * f * n - phase;
x = A * cos(arg);
clf;
stem(n, x);
axis([0 40 -2 2]);
grid;
title('正弦序列');
xlabel('时间序号n');
ylabel('振幅');
axis;