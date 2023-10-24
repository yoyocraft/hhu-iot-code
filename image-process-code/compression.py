import cv2
import os

# img_path = 'image/source/14_24_20.png'
# img_path = 'image/source/14_25_26.png'
img_path = 'image/source/14_27_40.png'
img = cv2.imread(img_path)

target_m = 0.5  # 压缩后的图像大小
compressed_folder = "image/compression"
os.makedirs(compressed_folder, exist_ok=True)

quality = 95
new_img_path = os.path.join(compressed_folder, os.path.splitext(
    os.path.basename(img_path))[0] + "_compression.jpg")

while quality > 10:
    cv2.imwrite(new_img_path, img, [cv2.IMWRITE_JPEG_QUALITY, quality])
    file_size = os.stat(new_img_path).st_size / 1000 / 1000
    print('Compressed image {} to {} MB'.format(img_path, str(file_size)))
    if file_size <= target_m:
        break
    quality -= 10 if file_size >= 6.5 else 5

file = open(new_img_path, 'rb')
