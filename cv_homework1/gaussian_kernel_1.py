import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TKAgg')

def gaussian_2d(x, y, sigma, mu_x = 0, mu_y = 0):
    a = 1 / (np.sqrt(2 * np.pi) * np.power(sigma, 2.)) #这里2后面加个点是明确指定这是一个浮点数
    #避免出现截断为整数的错误
    return np.power(a, 2.) * np.exp(-(np.power(x - mu_x, 2.) + np.power(y - mu_y, 2.)) / (2 * np.power(sigma, 2.)))

def get_my_gaussian_kernel(sigma, mu_x = 0, mu_y = 0, size = 3):
    """获得一个高斯滤波核"""
    kernel = np.empty((size, size))
    delta = (size - 1) / 2 #这是针对size为奇数的情况。一般滤波核好像都是奇数尺寸的。这样好对齐像素吧
    for i in range(size):
        for j in range(size):
            kernel[i][j] = gaussian_2d(i - delta, j - delta, sigma)

    sum = np.sum(kernel)
    kernel = kernel / sum #运用了广播机制，除了以后会返回一个新的矩阵
    return kernel

def get_lib_gaussian_kernel(sigma, size = 3):
    """获得一个opencv库中的高斯滤波核"""
    gaussian_one_d = cv.getGaussianKernel(size, sigma)
    return np.outer(gaussian_one_d.T, gaussian_one_d) #二维的高斯核其实可以看成是两个一维高斯核得到的。从数学的式子上
    #可以看出来

def show(subplot, kernel, whose, sigma):
    """单独可视化一个子图,需指定是哪里来的"""
    subplot.imshow(kernel, cmap = 'grey', interpolation = None) #imshow用来显示一个矩阵或图像通常是numpy矩阵
    #第一个参数就是要显示的对象，第二个则是指定了颜色映射colormap方式，这里是灰度颜色映射，最后会生成黑白图片
    #第三个参数是指定插值方式，这里没缺失值，不用插值
    subplot.set_title(whose + f'_kernel, sigma = {sigma}')
    subplot.colorbar() #生成一个颜色条，显示不同灰度对应的数值

def double_show(my_kernel, lib_kernel):
    """成对可视化滤波核"""
    #pic, (pic1, pic2) = plt.subplot(figsize=(10, 5)) #生成一个图形，它有两个子图，一左一右
    plt.figure(figsize=(10, 5))
    #1, 2指定了pic是一行两列的，(10, 5)则指定了子图的尺寸
    #show(pic1, my_kernel, 'my', 1)
    #show(pic2, lib_kernel, 'lib', 1)
    plt.subplot(1, 2, 1)  # 创建第一个子图，位于第一列
# 在第一个子图中绘制图像 pic1
    plt.imshow(my_kernel, cmap='hot', interpolation='nearest')
    plt.title('3x3 my_Gaussian Kernel')
    plt.subplot(1, 2, 2)  # 创建第二个子图，位于第二列
# 在第二个子图中绘制图像 pic2
    plt.imshow(lib_kernel, cmap='hot', interpolation='nearest')

    plt.title('3x3 lib_Gaussian Kernel')
    plt.colorbar()
    plt.tight_layout()
    plt.show()
    
if __name__ == '__main__':
    for i in range(1, 102, 20): #后面方差很大以后好像结果已经差不多了
        a = get_my_gaussian_kernel(i)
        print(a)
        b = get_my_gaussian_kernel(i)
        print(b)
        print('\n\n')
        double_show(a, b)

    
"""a = get_my_gaussian_kernel(1)
print(a)
b = get_lib_gaussian_kernel(1)
print(b)
double_show(a, b)"""
#plt.imshow(a, cmap = 'grey', interpolation=None)
