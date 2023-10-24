import cv2
import numpy as np
import matplotlib.pyplot as plt

# img_path = 'image/blur/14_24_20_gaussian.png'
# img_path = 'image/blur/14_25_26_gaussian.png'
img_path = 'image/blur/14_27_40_gaussian.png'

img = cv2.imread(img_path)

# 均值滤波
blur_img = cv2.blur(img, (5, 5))

# 方框滤波
box_img = cv2.boxFilter(img, -1, (5, 5))

# 高斯滤波
gaussian_img = cv2.GaussianBlur(img, (5, 5), 0)

# 中值滤波
median_img = cv2.medianBlur(img, 5)

# 双边滤波
bilateral_img = cv2.bilateralFilter(img, 9, 75, 75)

plt.suptitle('Image Denoising')
# 显示变换前后的变化
plt.subplot(2, 3, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original')

plt.subplot(2, 3, 2)
plt.imshow(cv2.cvtColor(blur_img, cv2.COLOR_BGR2RGB))
plt.title('Blur')

plt.subplot(2, 3, 3)
plt.imshow(cv2.cvtColor(box_img, cv2.COLOR_BGR2RGB))
plt.title('Box')

plt.subplot(2, 3, 4)
plt.imshow(cv2.cvtColor(gaussian_img, cv2.COLOR_BGR2RGB))
plt.title('Gaussian')

plt.subplot(2, 3, 5)
plt.imshow(cv2.cvtColor(median_img, cv2.COLOR_BGR2RGB))
plt.title('Median')

plt.subplot(2, 3, 6)
plt.imshow(cv2.cvtColor(bilateral_img, cv2.COLOR_BGR2RGB))
plt.title('Bilateral')

plt.tight_layout()
plt.show()
