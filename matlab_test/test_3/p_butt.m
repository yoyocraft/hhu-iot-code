function [b,a] = p_butt(Omegap,Omegas,Rp,As)
%   b = Ha(s)分子多项式系数
%   a = Ha(s)分母多项式系数
%   Omegap = 通带截止频率弧度/秒; Wp > 0
%   Omegas = 阻带截止频率弧度/秒; Ws > Wp > 0
%   Rp = 通带波纹 + dB; (Rp > 0)
%   As = 阻带衰减 + dB; (As > 0)
if Omegap <= 0
    error('通带截止频率必须大于0')
end
if Omegas <= Omegap
    error('阻带截止频率必须大于通带截止频率')
end
if (Rp <= 0) || (As < 0) 
    error('通带波纹和阻带衰减必须大于0')
end

N = ceil((log10((10^(Rp/10) - 1) / (10^(As/10) - 1))) / (2 * log10(Omegap / Omegas)));
fprintf('\n ==> 巴特沃兹滤波器阶次 = %2.0f\n', N);
OmegaC = Omegap / ((10^(Rp/10) - 1)^(1/(2 .* N)));
% OmegaC = Omegap / ((10^(As/10) - 1)^(1/(2 .* N)));
[b,a] = un_buttap(N, OmegaC);
end

