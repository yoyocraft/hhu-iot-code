clf;
c = -(1 / 12) + (pi / 6) * 1i;
K = 2;
n = 0 : 40;
% x = K * exp(c * n);
% 产生实指数序列
% x = K * cos(imag(c) * n) .* exp(real(c) * n);
x = K * sin(imag(c) * n) .* exp(real(c) * n);
subplot(2, 1, 1);
stem(n, real(x));
xlabel('时间序号n');
ylabel('振幅');
title('实部');
subplot(2, 1, 2);
stem(n, imag(x));
xlabel('时间序号n');
ylabel('振幅');
title('虚部');