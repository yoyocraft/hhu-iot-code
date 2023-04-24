n = 0 : 1 : 11;
m = 0 : 1 : 5;
N1 = length(n);
N2 = length(m);
xn = 0.8 .^ n;  % 生成x(n)
hn = ones(1, N2);   % 生成h(n)
N = N1 + N2 - 1;
XK = fft(xn, N);    % 对x(n)进行FFT得到X(K)
HK = fft(hn, N);    % 对h(n)进行FFT得到H(K)
YK = XK .* HK;   
yn = ifft(YK, N);
stem(abs(yn));

% 使用MATLAB的函数conv来验证上述程序的正确性
% step1: 利用conv函数计算xn与hn的卷积，得到yn1
yn1 = conv(xn, hn);
% step2: 对yn1进行FFT得到Y1(K)
Y1K = fft(yn1, N);
% step3: 比较YK和Y1K两个结果的最大差异
if max(abs(YK - Y1K)) < 1e-10
    fprintf('The two methods produce almost identical results.\n');
else
    fprintf('The two methods produce different results.\n');
end