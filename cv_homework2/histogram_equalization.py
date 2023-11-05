import numpy as np
import os
import cv2 as cv

dir_path = '/home/bluemouse/下载/~develop/python_work/cv_homework2/histogram_equalization_result'
img_path = '/home/bluemouse/下载/~develop/python_work/cv_homework2/soyo.jpg'
def get_cdf(img):
    """得到一幅图像的累计分布函数"""
    row, col = img.shape
    num = row * col
    cdf = np.zeros(256)
    for i in range(row):
        for j in range(col):
            cdf[img[i, j]] += 1 / num
    for i in range(1, 256):
        cdf[i] = cdf[i] + cdf[i - 1]
    return cdf

def cdf_mapping(cdf):
    """把累计分布函数的结果进行映射"""
    mapping = np.zeros(256)
    for i in range(256):
        mapping[i] = np.round(cdf[i] * 256) - 1
    return mapping

def histogram_equalization(img_path, output_path, name, original_name = 'original.jpg'):
    """对图像进行直方图均衡化处理"""

    img = cv.imread(img_path, cv.IMREAD_GRAYSCALE)
    cv.imwrite(os.path.join(output_path, original_name), img)
    cdf = get_cdf(img)
    #print(cdf)
    mapping = cdf_mapping(cdf)
    #print(mapping)
    row, col = img.shape
    equalized = np.zeros_like(img)
    for i in range(row):
        for j in range(col):
            equalized[i, j] = mapping[img[i, j]]
    cv.imwrite(os.path.join(output_path, name), equalized)

#equalized和original是一对，剩下的是另一对。但是，感觉这两幅图都不太适合进行直方图均衡化。。出来以后感觉不如原来的。。
#不知道是不是代码问题。。。
histogram_equalization(img_path, dir_path, 'equalized.jpg')
histogram_equalization('/home/bluemouse/下载/~develop/python_work/cv_homework2/corner.jpg', \
                       dir_path, 'second_example.jpg', 'second_original.jpg')