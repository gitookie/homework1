import cv2 as cv
import numpy as np
import os

path = '/home/bluemouse/下载/~develop/python_work/cv_homework1/used_for_padding.jpg'
output = '/home/bluemouse/下载/~develop/python_work/cv_homework1/padding_img'

def padding(pic_path, method, delta, name, output_path = output):
    """对图像进行填充并输出图像"""
    image = cv.imread(pic_path)
    height, width, channels = image.shape

    if method == 'zero':
        #零填充
        for i in range(height): #填充左右两条边
            for j in range(delta):
                for k in range(channels):
                    image[i][j][k] = 0
                    image[i][width - 1 - j][k] = 0
        for j in range(delta, width - delta): #填充上下两条边
            for i in range(delta):
                for k in range(channels):
                    image[i][j][k] = 0
                    image[height - 1 - i][j][k] = 0
    
    elif method == 'reflect':
        #翻转填充
        for i in range(delta, height - delta): #填充左右两条边
            for j in range(delta):
                for k in range(channels):
                    image[i][j][k] = image[i][2 * delta - j][k]
                    image[i][width - 1 - j][k] = image[i][(width - 1 - (2 * delta)) + j][k]
        
        for j in range(delta, width - delta): #填充上下两条边
            for i in range(delta):
                for k in range(channels):
                    image[i][j][k] = image[2 * delta - i][j][k]
                    image[height - 1 - i][j][k] = image[(height - 1 - (2 * delta)) + i][j][k]

        for i in range(delta): #填充四个对角
            for j in range(delta):
                for k in range(channels):
                    image[i][j][k] = image[2 * delta - i][2 * delta - j][k]#左上角
                    image[i][width - 1 - j][k] = image[2 * delta - i][(width - 1 - (2 * delta)) + j][k]#右上角
                    image[height - 1 - i][j][k] = image[(height - 1 - (2 * delta)) + i][2 * delta - j][k]#左下角
                    image[height - 1 - i][width - 1 - j][k] = image[(height - 1 - (2 * delta)) + i]\
                         [(width - 1 - (2 * delta)) + j][k]

    else:
        print('换一种填充方式')
        return None
    cv.imwrite(os.path.join(output_path, name), image)

#padding(path, 'zero', 15, 'padding_res1.jpg')
padding(path, 'reflect', 15, 'padding_res2.jpg')