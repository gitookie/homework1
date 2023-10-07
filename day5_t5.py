import os
import random as rd

def get_50nums():
    """获得50个各不相同的随机数"""
    res = []
    while len(res) < 50:
        tmp = rd.randint(0, 99)
        if tmp not in res:
            res.append(tmp)
    return res

def change_extension(folder_path, new_exten):
    """随机改变文件夹中50个文件的后缀为指定后缀"""

    files = os.listdir(folder_path)#获取所有文件的名字
    
    nums = get_50nums() #获取要更改的文件在files中的下标

    for id in nums: #开始更改后缀
        root, old_exten = os.path.splitext(files[id])
        new_filename = root + new_exten
        old_filepath = os.path.join(folder_path, root + old_exten)
        new_filepath = os.path.join(folder_path, new_filename)

        try:
            os.rename(old_filepath, new_filepath) #这个rename最好提供文件的完整路径，否则它默认会在当前的工作目录里
            #找文件，显然那些图片都不在当前的目录里
            #print('修改成功')  修改成功可以没反应，失败了再提醒
        except OSError:
            print('修改时出错')

change_extension('/home/bluemouse/下载/~develop/python_work/img/', '.jpg')