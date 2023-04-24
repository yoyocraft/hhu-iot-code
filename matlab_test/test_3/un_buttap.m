function [b,a] = un_buttap(N,Omegac)
%   b = Ha(s)分子多项式系数
%   a = Ha(s)分母多项式系数
%   N = 巴特沃兹模拟原型滤波器的阶次
%   Omegac = 截止频率弧度/秒
    [z0, p0, k0] = buttap(N);
    p = p0 * Omegac;
    k = k0 * Omegac^N;
    B = real(poly(z0));
    b = k * B;
    a = real(poly(p));
end

