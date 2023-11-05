import numpy as np
import cv2 as cv
import os
import math



img_path = '/home/bluemouse/下载/~develop/python_work/cv_homework2/soyo.jpg'
dir_path = '/home/bluemouse/下载/~develop/python_work/cv_homework2/sobel_filter_result'
def get_sobel_smoothing(size):
    """得到指定尺寸的sobel平滑算子"""
    smooth = np.zeros(size)
    for i in range(size):
        smooth[i] = math.comb(size - 1, i)
    return smooth

def get_sobel_difference(size):
    """得到指定尺寸的sobel差分算子"""
    diff = np.zeros(size)
    for i in range(size):
        if i == 0:
            cur = math.comb(size - 2, i)
        elif i == size - 1:
            cur = -math.comb(size - 2, i - 1) 
        else:
            cur = math.comb(size - 2, i) - math.comb(size - 2, i - 1)
        diff[i] = cur
    return diff

def get_sobel_x(size):
    """得到指定尺寸的sobel水平方向的算子"""
    return np.outer(get_sobel_smoothing(size), get_sobel_difference(size))

def get_sobel_y(size):
    """得到指定尺寸的sobel竖直方向的算子"""
    return np.outer(get_sobel_difference(size), get_sobel_smoothing(size))

def sobel_filter(img_path, output_path, name, direction, kernel_size = 3):
    """用sobel算子进行滤波"""
    img = cv.imread(img_path, cv.IMREAD_GRAYSCALE)
    #img = cv.GaussianBlur(img, (5, 5), 0.5, 0.5)
    result = np.zeros_like(img)
    if direction == 0: #进行水平方向的滤波
        sobel = get_sobel_x(kernel_size)
    else:
        sobel = get_sobel_y(kernel_size)
    row = int(img.shape[0])
    col = int(img.shape[1])
    delta = int((kernel_size - 1) / 2)
    for i in range(delta, row - delta):
        for j in range(delta, col - delta):
            local_patch = img[i-delta:i+delta+1, j-delta:j+delta+1] #这里的冒号也是，右边界是取不到的，要注意
            tmp = local_patch * sobel
            result[i, j] = np.sum(tmp)
    cv.imwrite(os.path.join(output_path, name), result)


sobel_filter(img_path, dir_path, 'after_filter3.jpg', 1)
#一共有三幅图，没有数字的是没有高斯滤波过的，水平方向的sobel滤波结果
#带2的是高斯滤波过之后，再进行水平方向的sobel滤波的结果
#带3的是高斯滤波过后，进行竖直方向的sobel滤波的结果
#感觉跟opencv库里自带的效果差了很多。。。



