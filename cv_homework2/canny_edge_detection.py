import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TKAgg')
import cv2 as cv
import os

dir_path = '/home/bluemouse/下载/~develop/python_work/cv_homework2/canny_result'
img_path = '/home/bluemouse/下载/~develop/python_work/cv_homework2/soyo.jpg'

def Canny_edge_detection(img_path):
    """对图片进行边缘检测，用canny算法"""
    #0.先以灰度图形式读入图片
    image = cv.imread(img_path, cv.IMREAD_GRAYSCALE)
    
    #1.高斯模糊去噪
    blurred = cv.GaussianBlur(image, (5, 5), 1, 1) #第一个参数是指定要进行模糊的图片，然后是指定高斯核大小，接着是x,y
    #方向上的方差，最后还有一个参数，一般好像不用动

    #2.得到梯度图，包括x, y方向上的梯度，以及对应像素点的梯度幅值和梯度方向
    sobel_x = cv.Sobel(blurred, cv.CV_64F, 1, 0, ksize=3) #第一个参数指定了要求梯度的图像，第二个指定了输出图像的数据以
    #什么形式形式存储。这里是以64位浮点数存储。因为计算梯度时很可能会出现负值，如果用cv2.CV_8U，也就是0-255的整数来存储，那么
    #对于负数，就会被截断为0,造成信息损失。所以这里选择了浮点数存储。
    #第三四个参数则是分别指定x, y方向上求几阶导。第五个则是指定sobel核的大小

    sobel_y = cv.Sobel(blurred, cv.CV_64F, 0, 1, ksize=3)
    #sobel_y不是指y方向上的sobel算子，而是用y方向的sobel算子对图像求梯度后得到的梯度矩阵，sobel_x同理
    grad_magnitude = np.sqrt(sobel_x ** 2 + sobel_y ** 2)
    grad_angle = np.arctan2(sobel_y, sobel_x) #arctan2可以处理四个象限的情况，而arctan返回的角度只能是-90到90度
    print(grad_magnitude)
    print(grad_angle)
    cv.imwrite(os.path.join(dir_path, 'initial_grad.jpg'), grad_magnitude)
    cv.imwrite(os.path.join(dir_path, 'initial_sobel_x.jpg'), sobel_x)
    cv.imwrite(os.path.join(dir_path, 'initial_sobel_y.jpg'), sobel_y)

    #3.非极大抑制(好像一般只会处理梯度幅值的矩阵，而不会去处理x, y方向上的梯度矩阵)
    row = sobel_x.shape[0]
    col = sobel_x.shape[1]
    nms_x = sobel_x.copy()
    nms_y = sobel_y.copy()

    for i in range(row):
        for j in range(col):
            angle_to_degree = (grad_angle[i][j] + np.pi) / np.pi * 180 #把各个梯度的角度换算成0-360度
            if not (i == 0 or i == row - 1 or j == 0 or j == col - 1):
                if (angle_to_degree >= 22.5 and angle_to_degree < 67.5) or \
                (angle_to_degree >= 202.5 and angle_to_degree < 247.5):
                    if  grad_magnitude[i][j] < grad_magnitude[i - 1][j + 1] or \
                        grad_magnitude[i][j] < grad_magnitude[i + 1][j - 1]:
                        nms_x[i][j] = 0
                        nms_y[i][j] = 0
                        grad_magnitude[i][j] = 0
                elif   (angle_to_degree >= 67.5 and angle_to_degree < 112.5) or \
                    (angle_to_degree >= 247.5 and angle_to_degree < 292.5):
                    if  grad_magnitude[i][j] < grad_magnitude[i - 1][j] or \
                        grad_magnitude[i][j] < grad_magnitude[i + 1][j]: #越界了怎么办？
                        nms_x[i][j] = 0
                        nms_y[i][j] = 0
                        grad_magnitude[i][j] = 0
                elif   (angle_to_degree >= 112.5 and angle_to_degree < 157.5) or \
                    (angle_to_degree >= 292.5 and angle_to_degree < 337.5):
                    if  grad_magnitude[i][j] < grad_magnitude[i - 1][j - 1] or \
                        grad_magnitude[i][j] < grad_magnitude[i + 1][j + 1]: #越界了怎么办？
                        nms_x[i][j] = 0
                        nms_y[i][j] = 0
                        grad_magnitude[i][j] = 0
                else:
                    if  grad_magnitude[i][j] < grad_magnitude[i][j - 1] or \
                        grad_magnitude[i][j] < grad_magnitude[i][j + 1]: #越界了怎么办？
                        nms_x[i][j] = 0
                        nms_y[i][j] = 0
                        grad_magnitude[i][j] = 0
            

    sobel_x = nms_x.copy()
    sobel_y = nms_y.copy()
    #print(sobel_x)
    #print(sobel_y)
    cv.imwrite(os.path.join(dir_path, 'after_nms_grad.jpg'), grad_magnitude)
    #cv.imwrite(os.path.join(dir_path, 'after_sobel_x.jpg'), sobel_x)
    #cv.imwrite(os.path.join(dir_path, 'after_sobel_y.jpg'), sobel_y)

    #4.阈值边缘链接
    high_threshold = 120
    low_threshole = 30
    for i in range(row):
        for j in range(col):
            if not (i == 0 or i == row - 1 or j == 0 or j == col - 1):
                if grad_magnitude[i][j] <= low_threshole:
                    grad_magnitude[i][j] = 0
                elif grad_magnitude[i][j] > low_threshole and grad_magnitude[i][j] < high_threshold:
                    cnt = 0
                    for ii in range(i - 1, i + 2):
                        for jj in range(j - 1, j + 2):
                            if not (ii == i and jj == j):
                                if grad_magnitude[ii][jj] < high_threshold:
                                    cnt += 1
                    if cnt == 8:
                        grad_magnitude[i][j] = 0


    cv.imwrite(os.path.join(dir_path, 'final_grad.jpg'), grad_magnitude)


Canny_edge_detection(img_path)
