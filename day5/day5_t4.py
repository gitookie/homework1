import os
from PIL import Image

def mkdir_png(path):
    """在指定路径上创建一个名为img的文件夹，并在其中创建100个.png文件"""
    folder_name = 'img'
    path = path + folder_name

    if not os.path.exists(path): #如果没有这个路径，就说明没有这个文件夹，那就创建一个
        os.makedirs(path)

    cnt = 0
    for i in range(100):
        file_name = str(i) + '.png'
        file_path = os.path.join(path, file_name) #创建文件和文件路径有很大关系，而文件路径和文件名也有很大关系

        image = Image.new("RGB", (100, 100)) #创建一个图像
        image.save(file_path) #把图像保存到指定路径
        if os.path.exists(file_path): #用来检测是否成功创建100个文件
            cnt += 1

    if cnt == 100:
        print('创建成功')
    else:
        print('出现错误')

mkdir_png('/home/bluemouse/下载/~develop/python_work/')