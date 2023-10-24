# version:1.0.1905.9051
from PIL import Image
import time
import os
import cv2
import numpy 

def main():
    print("")
    print("Initializing......")
    print("")

     # 请填写学号
    Student_id = '2162410112'

    Date = time.strftime("%Y_%m_%d",time.localtime(time.time())) 
    file_dir = './' + Student_id + '/'+  Date    # 原始图像保存路径
    if os.path.exists(file_dir) == False:
        os.makedirs(file_dir)

    
    file_dir_blur = './' + Student_id + '/'+ Date + '_blur'  # 高斯图像保存路径
    if os.path.exists(file_dir_blur) == False:
        os.makedirs(file_dir_blur)

       
    file_dir_salt = './' + Student_id + '/' + Date + '_salt'   # 椒盐图像保存路径
    if os.path.exists(file_dir_salt) == False:
        os.makedirs(file_dir_salt)
    
    cam = cv2.VideoCapture(0)
    
    while True:
        
        ret, img = cam.read()
        TimeStr = time.strftime("%H_%M_%S", time.localtime(time.time()))
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        img_cv = cv2.cvtColor(numpy.asarray(img),cv2.COLOR_RGB2BGR)   # Image 转为 cv2 的RGB
        img_cv = cv2.resize(img_cv,(1920,1440))   #  修改保存图像尺寸
        show_image = cv2.resize(img_cv,(1000,750))   # 修改显示图像尺寸

        # 显示图像
        cv2.imshow('Image', show_image)

        # 图像加高斯噪声并保存
        mean = 0 
        sigma = 25 # 设置高斯分布的均值和方差
        gauss = numpy.random.normal(mean,sigma,(img_cv.shape[0],img_cv.shape[1],3))  # 生成高斯噪声        
        img_gaussian = img_cv + gauss   # 添加高斯噪声       
        img_gaussian = numpy.clip(img_gaussian,a_min=0,a_max=255) # 设置图像像素值取值范围

        # 添加椒盐噪声并保存
        s_vs_p = 0.5  # 设置添加椒盐噪声的数目比例
        amount = 0.04  # 设置添加噪声图像像素的数目
        img_salt = numpy.copy(img)

        num_salt = numpy.ceil(amount * img.size * s_vs_p) # 添加salt噪声
        coords = [numpy.random.randint(0,i-1, int(num_salt)) for i in img.shape]   # 设置添加噪声的坐标位置
        img_salt[coords[0],coords[1],coords[2]] = 255
       
        #添加pepper噪声
        num_pepper = numpy.ceil(amount * img.size * (1. - s_vs_p))
        coords = [numpy.random.randint(0,i - 1, int(num_pepper)) for i in img.shape] #设置添加噪声的坐标位置
        img_salt[coords[0],coords[1],coords[2]] = 0

        #请补充保存以上原始图像（img_cv）、高斯噪声图像（img_gaussian）、椒盐噪声图像代码（img_salt）
        #存储要求为：
        #根目录（file_dir、file_dir_blur、file_dir_salt）/ 当前时间（now_time）+ 图像后缀名（'.png'、'_gaussian.png'、'_salt.png'）

        picname = file_dir + "/" + TimeStr + ".png"
        img_gaussian_name = file_dir_blur  + "/" + TimeStr + "_gaussian.png"
        img_salt_name = file_dir_salt + "/" + TimeStr + "_salt.png"

        cv2.imwrite(picname, img_cv)
        cv2.imwrite(img_gaussian_name, img_gaussian)
        cv2.imwrite(img_salt_name, img_salt)



        # 按‘Esc’键退出
        if (cv2.waitKey(1) & 0xFF) == 27:
            break

if __name__ == "__main__":
    main()
