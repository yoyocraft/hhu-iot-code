function hd = ideal_lp(wc, N)
    % hd = 点0到N-1之间的理想单位取样相应
    % wc = 截止频谱（弧度）
    % N = 理想滤波器的长度
    a = (N - 1) / 2;
    n = 0 : 1 : N - 1;
    m = n - a + eps;
    hd = sin(wc * m) ./ (pi * m);
end

