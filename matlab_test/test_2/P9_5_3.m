% 计算x和h的14点循环卷积
x = [1,2,3,4,4,3,2,1];
h = rand(1, 8); % 生成长度为8的随机向量
N = 14;
yc = cconv(x, h, N);
yl = conv(x, h);
fprintf('14点 ==>\n');
disp(yc);
disp(yl);

% 计算x和h的18点循环卷积
N = 18;
yc = cconv(x, h, N);
fprintf('18点 ==>\n');
disp(yc);
disp(yl);

% 计算x和h的22点循环卷积
N = 22;
yc = cconv(x, h, N);
fprintf('22点 ==>\n');
disp(yc);
disp(yl);
