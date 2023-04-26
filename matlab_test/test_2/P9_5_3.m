% 计算x和h的14点循环卷积
x = [1, 2, 3, 4];
h = [0, 1, -1, 1];
N = 14;
yc = circonv(x, h, N);
yl = conv(x, h);
fprintf('14点 ==>\n');
disp(yc);
disp(yl);
figure;
subplot(2,1,1);
stem(0:length(yc)-1, yc);
xlabel('n');
title('14点循环卷积 yc');

subplot(2,1,2);
stem(0:length(yl)-1, yl);
xlabel('n');
title('线性卷积 yl');

% 计算x和h的18点循环卷积
N = 18;
yc = circonv(x, h, N);
fprintf('18点 ==>\n');
disp(yc);
disp(yl);
figure;
subplot(2,1,1);
stem(0:length(yc)-1, yc);
xlabel('n');
title('18点循环卷积 yc');

subplot(2,1,2);
stem(0:length(yl)-1, yl);
xlabel('n');
title('线性卷积 yl');


% 计算x和h的22点循环卷积
N = 22;
yc = circonv(x, h, N);
fprintf('22点 ==>\n');
disp(yc);
disp(yl);

figure;
subplot(2,1,1);
stem(0:length(yc)-1, yc);
xlabel('n');
title('22点循环卷积 yc');

subplot(2,1,2);
stem(0:length(yl)-1, yl);
xlabel('n');
title('线性卷积 yl');
