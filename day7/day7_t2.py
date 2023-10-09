import os
import random
import shutil

def create(line_i):
    """创建一个含有i行随机内容的test.txt文件"""
    if not os.path.exists('test.txt') or os.path.getsize('test.txt') == 0: #此时会默认在当前的工作目录中
        #找有没有这个文件,如果没有或者虽然存在但是为空，那就写入
        with open('test.txt', 'w') as file:
            for i in range(line_i):
                random_char = chr(random.randint(32, 126))
                if i < line_i - 1:
                    file.write(random_char + '\n')
                else:
                    file.write(random_char)

def copy_text(src_file, file_name):
    """拷贝一份文件，命名为指定名字"""
    if not os.path.exists(file_name):
        with open(file_name, 'w') as file:
            pass #可以拿来占位，也可以先暂时放这里保留代码结构，之后再回来补充
    shutil.copy(src_file, file_name)

create(7)
copy_text('test.txt', 'copy_test.txt')