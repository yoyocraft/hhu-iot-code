wp = 0.2 * pi; ws = 0.3 * pi;
tr_width = ws - wp;

% Kaiser
M = ceil(4 / tr_width);
if rem(M, 2) == 0
    M = M + 1;
end
n = 0 : M-1;
alpha = (M-1)/2;
beta = 5.6535 * (ws-wp);
w_kai = kaiser(M,beta)';
wc = (ws + wp) / 2;
hd = ideal_lp(wc,M);
h = hd .* w_kai;
[H, w] = freqz(h, 1, 1000, 'whole');    % h为h(n)
H = (H(1:501))'; w = (w(1:501))';
mag = abs(H);   % 幅度响应
db = 20 * log10((mag + eps)/max(mag));  % 以分贝为单位的幅度响应
pha = angle(H); % 相位响应
grd = grpdelay(h, 1, w);    % 群延时
delta_w = 2 * pi / 1000;
Rp = -(min(db(1 : wp/delta_w + 1)));    % 通带波纹
As = -round(max(db(ws/delta_w + 1 : 501))); % 最小阻带衰减

% 画图
subplot(2, 2, 1); stem(n, hd); title('理想脉冲响应');
axis([0 M-1 -0.1 0.3]); xlabel('n'); ylabel('hd(n)');
subplot(2, 2, 2); stem(n, w_kai); title('Kaiser窗');
axis([0 M-1 0 1.1]); xlabel('n'); ylabel('w(n)');
subplot(2, 2, 3); stem(n, h); title('实际脉冲响应');
axis([0 M-1 -0.1 0.3]); xlabel('n'); ylabel('h(n)');
subplot(2, 2, 4); plot(w / pi, db); title('相对标尺的幅度响应'); grid;
axis([0 1 -100 10]); xlabel('frequency in pi units'); ylabel('Decibels');
set(gca, 'XTickMode', 'manual', 'XTick', [0,wp/pi,ws/pi,1]);
set(gca, 'YTickMode', 'manual', 'YTick', [-50,0]);
set(gca, 'YTickLabelMode', 'manual', 'YTickLabels', vertcat({'50'}, {'0'}));
