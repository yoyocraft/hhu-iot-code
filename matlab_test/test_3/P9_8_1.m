% 数字滤波器指标
wp = 0.1 * pi;  % 数字通带频率
ws = 0.25 * pi; % 数字阻带频率
Rp = 2;         % 以分贝为单位的通带波纹
As = 18;        % 以分贝为单位的阻带衰减

% 转换成模拟滤波器的指标：双线性变换的逆映射
T = 1;
OmegaP = (2 / T) * tan(wp / 2);     % 原型通带频率
OmegaS = (2 / T) * tan(ws / 2);     % 原型阻带频率
ep = sqrt(10^(Rp/10) - 1);          % 通带波纹参数
Ripple = sqrt(1 / (1 + ep .* ep));  % 通带波纹
Attn = 1 / (10^(As / 20));          % 阻带衰减

% 模拟巴特沃兹滤波器的计算
[cs, ds] = p_butt(OmegaP, OmegaS, Rp, As);
[b, a] = bilinear(cs, ds, T);   % 双线性变换
fprintf('\nb = ');
disp(b);
fprintf('\na = ');
disp(a);

% 计算数字滤波器的频率响应
[H, w] = freqz(b, a, 1000, 'whole');
    H = (H(1:1:501));
    w = (w(1:1:501));
    mag = abs(H);                               % 幅度响应
    db = 20 * log10((mag + eps) / max(mag));    % 以分贝为单位的幅度响应
    pha = angle(H);                             % 相位响应
grd = grpdelay(b, a, w);                        % 群延时

