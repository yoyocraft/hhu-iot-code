function [b, a] = impinvr(c, d, T)
    % 从模拟滤波器到数字滤波器的脉冲响应不变法映射
    % b = 数字滤波器H(z)的分子系数
    % a = 数字滤波器H(z)的分母系数
    % c = 模拟滤波器的分子系数
    % d = 模拟滤波器的分子系数
    [R, p, k] = residue(c, d);  % 部分因式展开
    p = exp(p * T);
    [b, a] = residue(R, p, k);
    b = real(b); a = real(a);
end

