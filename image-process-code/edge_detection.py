import cv2
import numpy as np
import matplotlib.pyplot as plt

# img_path = 'image/source/14_24_20.png'
# img_path = 'image/source/14_25_26.png'
img_path = 'image/source/14_27_40.png'
original_img = cv2.imread(img_path)
img = cv2.resize(original_img, None, fx=0.8, fy=0.8,
                 interpolation=cv2.INTER_CUBIC)

# 去噪
img = cv2.GaussianBlur(img, (3, 3), 0)
# 边缘提取
edges = cv2.Canny(img, 50, 150, apertureSize=3)

# # 检测直线
# lines = cv2.HoughLines(edges, 1, np.pi / 180, 150)
# # 对检测出的直线绘制成红线
# result = img.copy()
# for line in lines:
#     rho = line[0][0]
#     theta = line[0][1]
#     if (theta < (np.pi / 4)) or (theta > (np.pi * 3 / 4)):
#         # 直线起点坐标
#         pt1 = (int(rho / np.cos(theta)), 0)
#         # 直线终点坐标
#         pt2 = (int((rho - result.shape[0] * np.sin(theta)) / np.cos(theta)),
#                result.shape[0])
#         # 绘制绿线
#         cv2.line(result, pt1, pt2, (0, 255, 0))
#     else:
#         # 直线起点坐标
#         pt1 = (0, int(rho / np.sin(theta)))
#         # 直线终点坐标
#         pt2 = (result.shape[1],
#                int((rho - result.shape[1] * np.cos(theta)) / np.sin(theta)))
#         # 绘制绿线
#         cv2.line(result, pt1, pt2, (255, 0, 0))

# cv2.imshow('Origin', img)
# cv2.imshow('Canny', edges)
# cv2.imshow('Result', result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

plt.suptitle('Image Edge Detection')
# 显示变换前后的变化
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original')

plt.subplot(1, 2, 2)
plt.imshow(edges, cmap='gray')
plt.title('Edge')

plt.tight_layout()
plt.show()
