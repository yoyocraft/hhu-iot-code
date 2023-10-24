import cv2
import numpy as np
from numpy import fft
import matplotlib.pyplot as plt


def inverse(input, PSF, eps):
    """逆滤波"""
    input_fft = fft.fftshift(fft.fft2(input))
    PSF_fft = fft.fftshift(fft.fft2(PSF)) + eps
    result = fft.ifft2(fft.ifftshift(input_fft / PSF_fft))
    result = np.abs(result)
    return result


def wiener(input, PSF, eps, K=0.01):
    """维纳滤波, K = 0.01"""
    input_fft = fft.fftshift(fft.fft2(input))
    PSF_fft = fft.fftshift(fft.fft2(PSF)) + eps
    PSF_fft_after = np.conj(PSF_fft) / (np.abs(PSF_fft) ** 2 + K)
    result = fft.ifft2(fft.ifftshift(input_fft * PSF_fft_after))
    # result = fft.ifft2(input_fft * PSF_fft_after)
    result = np.abs(result)
    # result = np.abs(fft.ifftshift(result))
    return result


# img_path = 'image/blur/14_24_20_gaussian.png'
# img_path = 'image/blur/14_25_26_gaussian.png'
# img_path = 'image/blur/14_27_40_gaussian.png'
img_path = 'image/salt/14_27_40_salt.png'

img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
# 设置PSF的大小与图像大小完全匹配
psf_size = img.shape
PSF = np.ones(psf_size) / (psf_size[0] * psf_size[1])
eps = 1e-6

# 逆滤波
restored_inverse = inverse(img, PSF, eps)
# 维纳滤波
restored_wiener = wiener(img, PSF, eps, K=0.01)

plt.suptitle("Image Restoration")
# 显示变换前后的变化
plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray')
plt.title('Original')

plt.subplot(1, 3, 2)
plt.imshow(restored_inverse, cmap='gray')
plt.title('Inverse Filtering')

plt.subplot(1, 3, 3)
plt.imshow(restored_wiener, cmap='gray')
plt.title('Wiener Filtering')

plt.tight_layout()
plt.show()
