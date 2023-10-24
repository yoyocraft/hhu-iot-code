import numpy as np
import cv2
import matplotlib.pyplot as plt

# 读取图像
# img_path = 'image/source/14_24_20.png'
# img_path = 'image/source/14_25_26.png'
img_path = 'image/source/14_27_40.png'
img = cv2.imread(img_path, 0)
# dft函数傅里叶变换
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
# 移动左上角低频到图像中心
dftShift = np.fft.fftshift(dft)
# 傅里叶变换结果是双通道，需要把双通道转换为三通道灰度图像，20 * (转换到0-255的图像)
result = 20 * np.log(cv2.magnitude(dftShift[:, :, 0], dftShift[:, :, 1]))

plt.suptitle("DFT")
plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray")
plt.title("original")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(result, cmap="gray")
plt.title("dft")
plt.axis("off")
plt.show()
