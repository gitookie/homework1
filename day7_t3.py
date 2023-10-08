import os

def add2file(filename, str_append):
    """追加指定字符到文件的开头和结尾"""
    with open(filename, 'r+') as file: #这个方法是先读取原先内容，再在此基础上加上追加内容，最后写回去
        origin = file.read() #没有参数时会默认读取全部内容
        file.seek(0,0) #移动读写指针
        new = str_append + '\n' + origin + '\n' + str_append
        file.write(new)

add2file('test.txt', 'python')