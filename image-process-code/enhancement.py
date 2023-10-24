import cv2
import matplotlib.pyplot as plt

# img_path = 'image/source/14_24_20.png'
# img_path = 'image/source/14_25_26.png'
img_path = 'image/source/14_27_40.png'

img = cv2.imread(img_path)

# 转换为灰度图
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 直方图均衡化
img_after = cv2.equalizeHist(img)

plt.suptitle('Image Enhancement')
# 显示变换前后的变化
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original')

plt.subplot(1, 2, 2)
plt.imshow(img_after, cmap='gray')
plt.title('Enhancement')

plt.tight_layout()
plt.show()
