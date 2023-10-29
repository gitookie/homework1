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

def double_show(my_kernel, lib_kernel):
    """成对可视化滤波核"""
    
    plt.figure(figsize=(10, 5))


    plt.subplot(1, 2, 1)  # 创建第一个子图，位于第一列

    # 在第一个子图中绘制图像 pic1
    plt.imshow(my_kernel, cmap='hot', interpolation='nearest')
    plt.colorbar()
    plt.title('3x3 my_Gaussian Kernel')


    plt.subplot(1, 2, 2)  # 创建第二个子图，位于第二列
    
    # 在第二个子图中绘制图像 pic2
    plt.imshow(lib_kernel, cmap='hot', interpolation='nearest')
    plt.title('3x3 lib_Gaussian Kernel')
    plt.colorbar()

    plt.tight_layout()
    
    plt.show()
    

def double_show_in_3D(my_kernel, lib_kernel):
    """成对可视化高斯核，但是以三维图形的形式"""

    fig = plt.figure(figsize=(10, 5)) #生成一个figure对象，它表示整个图形窗口

    ax1 = fig.add_subplot(121, projection='3d') #创建一个三维子图对象，它可以画各种三维图形
    #121表示这是一乘二网格的子图里的第一个
    delta = (my_kernel.shape[0] - 1) / 2
    xx = np.arange(-delta, delta + 1)
    yy = xx.copy()
    xxx, yyy = np.meshgrid(xx, yy) #生成网格，其实就是把xx,yy的值拿来排列组合，所有的结果就是所有的点

    surf1 = ax1.plot_surface(xxx, yyy, my_kernel, cmap = 'viridis')#创建一个三维表面图
    #在xxx,yyy构成的平面上画图，第三维的数值就是my_kernel的数值
    
    ax2 = fig.add_subplot(122, projection='3d')
    surf2 = ax2.plot_surface(xxx, yyy, lib_kernel, cmap = 'viridis')

    cbar = fig.colorbar(surf2, ax=[ax1, ax2]) #重点在于第二个参数，它指定了这个颜色条会和两个子图关联，从而能同时显示
    #两个颜色映射
    
    plt.show()

if __name__ == '__main__':
    kernel_size = 3
    
    for i in range(1, 102, 20): #后面方差很大以后好像结果已经差不多了
        a = get_my_gaussian_kernel(i, size=kernel_size)
        print(a)
        b = get_my_gaussian_kernel(i, size=kernel_size)
        print(b)
        print('\n\n')
        #double_show(a, b)
        kernel_size += 2
        double_show_in_3D(a, b)
    
    

