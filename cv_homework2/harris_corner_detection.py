import os
import numpy as np
import cv2 as cv
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt


dir_path = '/home/bluemouse/下载/~develop/python_work/cv_homework2/harris_result'
img_path = '/home/bluemouse/下载/~develop/python_work/cv_homework2/many_corner.jpg'

def Harris_corner_detection(img_path, sigmax, sigmay, window_size = 3, name = 'final.jpg', alpha = 0.05):
    """对图像进行角点检测，用Harris算法"""
    
    #0.先以灰度图形式读入图片
    image = cv.imread(img_path, cv.IMREAD_GRAYSCALE)

    #1.用小方差高斯核对图像进行滤波
    blurred = cv.GaussianBlur(image, (5, 5), 0.5, 0.5)

    #2.用一阶差分计算图像的x, y方向上的梯度
    Ix = cv.Sobel(blurred, cv.CV_64F, 1, 0, ksize=3)
    Iy = cv.Sobel(blurred, cv.CV_64F, 0, 1, ksize=3)

    #3.求Ix, Iy各自平方后得到的图像，以及它们相乘后得到的图像
    I_xx = Ix ** 2
    I_yy = Iy ** 2
    I_xy = Ix * Iy
    cv.imwrite(os.path.join(dir_path, 'Ix_squared.jpg'), I_xx)
    cv.imwrite(os.path.join(dir_path, 'Iy_squared.jpg'), I_yy)
    cv.imwrite(os.path.join(dir_path, 'Ixy_squared.jpg'), I_xy)

    #4.用指定方差的高斯滤波核对I_xx, I_yy, I_xy 进行高斯滤波
    blurred_x = cv.GaussianBlur(I_xx, (5, 5), sigmax, sigmay)
    blurred_y = cv.GaussianBlur(I_yy, (5, 5), sigmax, sigmay)
    blurred_xy = cv.GaussianBlur(I_xy, (5, 5), sigmax, sigmay)
    #cv.imwrite(os.path.join(dir_path, 'Ix_squared_blurred.jpg'), blurred_x)

    #5.由4的结果构造M矩阵,然后记录各个像素点的响应函数R的值
    height, width = image.shape
    height = int(height)
    width = int(width)
    corner = np.array([])
    Response = np.zeros((height, width))
    delta = int((window_size - 1) / 2)
    for i in range(delta, height - delta):
        for j in range(delta, width - delta):
            M = np.array([[np.sum(blurred_x[i-delta:i+delta, j-delta:j+delta]), np.sum(blurred_xy\
                        [i-delta:i+delta, j-delta:j+delta])],
                        [np.sum(blurred_xy[i-delta:i+delta, j-delta:j+delta]), np.sum(blurred_y\
                        [i-delta:i+delta, j-delta:j+delta])]])
            det = np.linalg.det(M)
            trace = np.trace(M)
            Response[i][j] = det - alpha * np.power(trace, 2)

    #6.进行非极大抑制
    tmp = Response.copy()
    for i in range(delta, height - delta):
        for j in range(delta, width - delta):
            local_patch = tmp[i-delta:i+delta, j-delta:j+delta]
            local_max = np.max(local_patch)
            if tmp[i][j] < local_max:
                Response[i][j] = 0

    print(Response.shape)
    #7.由响应函数R的值，来筛选角点
    
    all_points = np.where(Response > 900000000000)
    
        #keypoints是单独的对象，如果要用drawKeypoints标注关键点，就要把点的坐标转化成这个对象类型
    keypoints = []
    size = 10.0
    angle = 30.0
    response = 0.0
    for i in range(len(all_points[0])):
        key_point_x = float(all_points[0][i])
        key_point_y = float(all_points[1][i])
        cur_point = cv.KeyPoint(key_point_y, key_point_x, size, angle, response)
        keypoints.append(cur_point)

    #print(len(keypoints))
    
    
    
    #8.展示结果(最后的结果是final.jpg)
    corner_result = cv.drawKeypoints(blurred, keypoints, None, color=(0, 0, 255)) #这里的color的排序好像是b,g,r
    cv.imwrite(os.path.join(dir_path, name), corner_result)
    
    

            
Harris_corner_detection(img_path, 0.5, 0.5)

#下面试了一下不同大小的窗口对图片角点检测的影响。从final到0一直到3,效果近乎一样。应该是因为纯网点图比较简单。
#而从4到7,大致是效果越来越差的。应该可以认为窗口越大，效果越粗糙
#应该是比较有道理的。因为原理推导部分用到了泰勒展开，然后取了一部分来近似。显然自变量的改变量越小，这个近似越精确。
#窗口太大的话，差别应该就会大起来了
#用corner.jpg这幅图来测试的话。它的结果不太尽如人意。阈值太小则角点太多;阈值太大则检测到的角点大部分都聚集在校卡
#的二维码上了，还有一部分聚集到了上面的字了。这点倒是一开始选图片的时候疏忽了。本来想的是校卡和鼠标垫都比较方正，
#应该有几个比较显眼的角点。忘了考虑二维码和字了
"""window_size = 5
for i in range(4):
    Harris_corner_detection(img_path, 0.5, 0.5, window_size, str(i)+'.jpg')
    window_size += 2"""

"""window_size = 5
for i in range(4, 8):
    Harris_corner_detection('/home/bluemouse/下载/~develop/python_work/cv_homework2/corner.jpg',\
                            0.5, 0.5, window_size, str(i) + '.jpg')
    window_size += 2"""