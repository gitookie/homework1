# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('TKAgg')

img_path = '/home/bluemouse/下载/~develop/python_work/cv_homework3/soyo.jpg'
img2_path = '/home/bluemouse/下载/~develop/python_work/cv_homework3/corner.jpg'
def get_magnitude_spectrum(img_path):
    """对图像进行傅里叶变换，得到幅值图"""
    img = cv.imread(img_path, cv.IMREAD_GRAYSCALE)
    fourier = np.fft.fft2(img) #快速傅里叶变换算法得到频率分布
    fshift = np.fft.fftshift(fourier) #默认结果中心点位置是在左上角,调用fftshift()函数转移到中间位置
    magnitude_spectrum = np.log(np.abs(fshift)) #fft结果是复数, 其绝对值结果是振幅
    return magnitude_spectrum
   
def get_phase_spectrum(img_path):
    img = cv.imread(img_path, cv.IMREAD_GRAYSCALE)
    fourier = np.fft.fft2(img)
    fshift = np.fft.fftshift(fourier)    
    phase_spectrum = np.angle(fshift)
    return phase_spectrum


 
img = cv.imread(img_path, 0)
img2 = cv.imread(img2_path, 0)
magnitude = get_magnitude_spectrum(img_path)
phase = get_phase_spectrum(img_path)

#生成一个mask
mask = np.zeros(img.shape[:2], dtype = "uint8")
(cX, cY) = (img.shape[1] // 2, img.shape[0] // 2)
cv.rectangle(mask, (cX - 150, cY - 150), (cX + 150 , cY + 150), 255, -1)


#展示结果
#1.展示相位谱和幅度谱
plt.subplot(131), plt.imshow(img, 'gray'), plt.title('Original ')
plt.axis('off')
plt.subplot(132), plt.imshow(magnitude, 'gray'), plt.title('magnitude spectrum')
plt.axis('off')
plt.subplot(133), plt.imshow(phase, 'gray'), plt.title('phase spectrum')
plt.show()
masked = cv.bitwise_and(magnitude, magnitude, mask = mask)

inversed = cv.bitwise_or(masked, magnitude)

#2.mask一部分幅度谱
plt.subplot(121), plt.imshow(masked, 'gray'), plt.title('masked_magnitude')
plt.axis('off')
plt.subplot(122), plt.imshow(inversed, 'gray'), plt.title('inversed_magnitude')
plt.axis('off')
plt.show()

#3.混合两幅图的频域
#调整一下两幅图的尺寸，使它们匹配
img = cv.resize(img, (img2.shape[1], img2.shape[0]))

#得到两幅图的频域
f1_spectrum = np.fft.fft2(img) 
f2_spectrum = np.fft.fft2(img2)
f_blend = (f1_spectrum + f2_spectrum) / 2 #混合一下
#f_blend = f1_spectrum  * 49 / 50 + f2_spectrum / 50

f_blend = np.fft.ifft2(f_blend) #二维的傅里叶逆变换
f_blend = np.abs(f_blend) #保留振幅，去掉相位

plt.subplot(131), plt.imshow(img, 'gray'), plt.title('Original 1')
plt.axis('off')
plt.subplot(132), plt.imshow(img2, 'gray'), plt.title('Original 2')
plt.axis('off')
plt.subplot(133), plt.imshow(f_blend, 'gray'), plt.title('blended')
plt.show()
print(f_blend)