import cv2
import numpy as np
import matplotlib.pyplot as plt


# img_path = 'image/source/14_24_20.png'
# img_path = 'image/source/14_25_26.png'
img_path = 'image/source/14_27_40.png'

img = cv2.imread(img_path)

# 旋转变换
M1 = cv2.getRotationMatrix2D((img.shape[1] / 2, img.shape[0] / 2), 90, 1)
rotation_img = cv2.warpAffine(img, M1, (img.shape[1], img.shape[0]))

# 平移变换
M2 = np.float32([[1, 0, 200], [0, 1, 200]])
translation_img = cv2.warpAffine(img, M2, (img.shape[1], img.shape[0]))

# 缩放变换
zoom_img = cv2.resize(img, [480, 360], interpolation=cv2.INTER_CUBIC)

# 镜像变换
mirror_img = cv2.flip(img, 1)

plt.suptitle('Image Transformations')
# 显示变换前后的变化
plt.subplot(1, 5, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original')

plt.subplot(1, 5, 2)
plt.imshow(cv2.cvtColor(rotation_img, cv2.COLOR_BGR2RGB))
plt.title('Rotation')

plt.subplot(1, 5, 3)
plt.imshow(cv2.cvtColor(translation_img, cv2.COLOR_BGR2RGB))
plt.title('Translation')

plt.subplot(1, 5, 4)
plt.imshow(cv2.cvtColor(zoom_img, cv2.COLOR_BGR2RGB))
plt.title('Zoom')

plt.subplot(1, 5, 5)
plt.imshow(cv2.cvtColor(mirror_img, cv2.COLOR_BGR2RGB))
plt.title('Mirror')

plt.tight_layout()
plt.show()
