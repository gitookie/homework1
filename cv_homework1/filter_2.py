import cv2 as cv
import numpy as np
from gaussian_kernel_1 import get_my_gaussian_kernel 
import os

path = '/home/bluemouse/下载/~develop/python_work/cv_homework1/soyo.jpg'
output_path = '/home/bluemouse/下载/~develop/python_work/cv_homework1'
def gaussian_blur(pic_path, output_path, name, kernel = get_my_gaussian_kernel(1), smaller = 1):
    """对图片进行高斯模糊"""
    kernel_size = kernel.shape
    image = cv.imread(pic_path)
    height, width, channels = image.shape #shape是类的一个属性，所以不用加括号  返回的是一个元组 而且注意一下，shape
    #返回维度是按照height, width, channels来的
    print(image)
    if smaller == 0: #要求图片尺寸不变小时
        blurred_image = np.zeros((height, width, channels))
    else:            #要求图片尺寸变小时
        blurred_image = np.zeros((height - kernel_size[0] + 1, width - kernel_size[0] + 1, channels))
    #而这个按给定形状生成零矩阵，三个参数按顺序分别是height, width, channels，跟上面不一样，要小心
    
    delta = int((kernel_size[0] - 1) / 2) #要变成整型，不然会按照浮点数进行计算，下面就用不了range了
    for i in range(channels):
        for j in range(delta, width - delta): #注意核的大小是不定的，所以要对齐像素
            for k in range(delta, height - delta):
                patch = np.zeros_like(kernel)
                for col in range(kernel_size[0]):
                    for row in range(kernel_size[0]):
                        patch[row][col] = image[k + row - delta, j + col - delta, i]
                blurred_image[k - delta, j - delta, i] = np.sum(np.dot(patch, kernel))

    cv.imwrite(os.path.join(output_path, name), blurred_image)

#gaussian_blur(path, output_path, 'blurred1.jpg')
#kernel = get_my_gaussian_kernel(3, size=5)
#gaussian_blur(path, output_path, 'blurred2.jpg', kernel)
#kernel = get_my_gaussian_kernel(5)
#gaussian_blur(path, output_path, 'blurred3.jpg')
"""kernel = get_my_gaussian_kernel(0.01)
gaussian_blur(path, output_path, 'blurred4.jpg')"""
"""kernel = get_my_gaussian_kernel(25)
gaussian_blur(path, output_path, 'blurred5.jpg')"""
"""kernel = get_my_gaussian_kernel(3, size=7)
gaussian_blur(path, output_path, 'blurred6.jpg', kernel)"""
"""kernel = get_my_gaussian_kernel(500)
gaussian_blur(path, output_path, 'blurred7.jpg')"""
#kernel = get_my_gaussian_kernel(0.00001)
#gaussian_blur(path, output_path, 'blurred8.jpg')

#前面的图片尺寸都变小了，最后一个则没有变小
kernel = get_my_gaussian_kernel(0.00001, size = 31)
gaussian_blur(path, output_path, 'used_for_padding.jpg', smaller = 0)


#对比一下1, 2, 6(尺寸变大，方差几乎没变),会发现卷积核的尺寸对模糊效果影响很大。尺寸越大，越模糊
#而对比7, 5, 3, 1, 4, 8(方差由大变小),发现方差的改变，影响好像不是很显著。应该是因为这几个都是三乘三的，太小了
#还有，最后一幅图对应的卷积核虽然尺寸很大，但模糊的效果也和前面差不多，应该是因为方差太小了。方差越小，越抑制模糊作用