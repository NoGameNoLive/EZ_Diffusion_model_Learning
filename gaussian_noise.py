'''
-*- coding: utf-8 -*-
time: 2024/7/23 10:06
file: gaussian_noise.py
author: Endy_Liu_Noonell
'''
import cv2
import numpy as np

# 读取图片
img = cv2.imread(r"C:\Users\pc\Desktop\diffusion\code\diffusion-model-master\pic\mechine.jpg")
# 设置高斯分布的均值和方差
mean = 0
# 设置高斯分布的标准差
sigma = 25
rou = 1000
# 根据均值和标准差生成符合高斯分布的噪声
gauss = np.random.normal(mean, sigma, (img.shape[0], img.shape[1], img.shape[2]))
# 给图片添加高斯噪声
noisy_img = img + gauss * rou
# 设置图片添加高斯噪声之后的像素值的范围
noisy_img = np.clip(noisy_img, a_min=0, a_max=255)
# 保存图片
cv2.imwrite(r"C:\Users\pc\Desktop\diffusion\code\diffusion-model-master\pic\noisy1000_img.png", noisy_img)
