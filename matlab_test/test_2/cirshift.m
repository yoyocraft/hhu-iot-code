function y = cirshift(x,m, N)
    if length(x)>N
        error('N必须大于等于x的长度')
    end
    x = [x zeros(1,N-length(x))];
    n = 0:1:N-1;
    n = mod(n - m, N);
    y = x(n + 1);
