% 数字滤波器指标
wp = 0.1 * pi;  % 数字通带频率
ws = 0.25 * pi; % 数字阻带频率
Rp = 2;         % 以分贝为单位的通带波纹
As = 18;        % 以分贝为单位的阻带衰减

% 转换成模拟滤波器的指标：双线性变换的逆映射
T = 1;
OmegaP = wp / T;     % 原型通带频率
OmegaS = ws / T;     % 原型阻带频率
ep = sqrt(10^(Rp/10) - 1);          % 通带波纹参数
Ripple = sqrt(1 / (1 + ep .* ep));  % 通带波纹
Attn = 1 / (10^(As / 20));          % 阻带衰减

% 模拟巴特沃兹滤波器的计算
[cs, ds] = p_butt(OmegaP, OmegaS, Rp, As);
[b, a] = impinvr(cs, ds, T);   % 脉冲响应不变法
fprintf('\nb = \t');
disp(b);
fprintf('\na = \t');
disp(a);

% 计算数字滤波器的频率响应
[H, w] = freqz(b, a, 1000, 'whole');
H = (H(1:1:501));
w = (w(1:1:501));
mag = abs(H);                               % 幅度响应
db = 20 * log10((mag + eps) / max(mag));    % 以分贝为单位的幅度响应
pha = angle(H);                             % 相位响应
grd = grpdelay(b, a, w);                    % 群延时


subplot(2, 2, 1); plot(w/pi,mag);title('幅度响应');
xlabel('以pi为单位的频率');
ylabel('|H|'); axis([0,1,0,1.1]);
set(gca, 'XTickMode', 'manual', 'XTick', [0,0.2,0.4,1]);
set(gca, 'YTickmode', 'manual', 'YTick', [0,Attn, Ripple, 1]); grid;
subplot(2, 2, 2); plot(w/pi,pha/pi);title('相位响应');
xlabel('以 pi 为单位的频率'); ylabel('radians'); axis([0,0.5,-1,1])
set(gca, 'XTickMode', 'manual', 'XTick', [0,0.2,0.4,1]);
set(gca, 'YTickmode', 'manual', 'YTick',[-1,-0.5,0,0.5,1]); grid;
subplot(2, 2, 3); plot(w/pi,db);title('幅度 dB');
xlabel('以pi为单位的频率'); ylabel('分贝');
axis([0,1, -40,5]);
set(gca, 'XTickMode', 'manual', 'XTick', [0,0.2,0.4,1]);
set(gca, 'YTickmode', 'manual', 'yTick', [-30,-As,-Rp,0]); grid;
subplot(2, 2, 4); plot(w/pi, grd/max(grd)); title('群延时');
xlabel('以pi为单位的频率'); ylabel('归一化群延时'); axis([0,1,0,max(grd)/max(grd)])
set(gca, 'XTickMode', 'manual', 'XTick', [0,0.2,0.4,1]);
set(gca, 'YTickmode', 'manual', 'YTick', [0, round(max(grd)/2), max(grd)]); grid;
