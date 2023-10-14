import threading
import os

def create(folder_name):
    """创建一个测试用的文件夹，里面放一些文件，之后拿来改名"""
    if not os.path.exists(os.path.join(os.getcwd(), folder_name)):
        #这里的工作路径还是只到PYTHON_WORK,没有到day11这个文件夹，要在这里面创建的话就要另写一些
        os.mkdir(os.path.join(os.getcwd(), folder_name))

    for i in range(50):
        file_path = os.path.join(os.path.join(os.getcwd(), folder_name), '%s.txt'%(i))
        with open(file_path, 'w'):
            pass #创建空的txt文件

def thread_rename(folder_name, file_name):
    """重命名的函数，这里就设置为在文件末尾加个python"""
    folder_path = os.path.join(os.getcwd(), folder_name)
    old_path = os.path.join(folder_path, file_name)
    new_path = os.path.join(folder_path, file_name + 'python')
    os.rename(old_path, new_path)


def get_name_list(folder_name):
    """获取文件夹内的文件的名字列表"""
    folder_path = os.path.join(os.getcwd(), folder_name)
    all_list = os.listdir(folder_path) #这个返回的列表里既有子文件夹的名字，也有文件的名字
    name_list = []
    for name in all_list:
        if os.path.isfile(os.path.join(folder_path, name)):
            name_list.append(name)
    return name_list

def multi_thread_rename(folder_name):
    """运用多线程给文件夹内的文件进行重命名"""
    name_list = get_name_list(folder_name)
    threads = []
    for i in range(1, len(name_list) + 1):
        thread = threading.Thread(target = thread_rename, args = (folder_name, name_list[i - 1])) #这里参数
        #一定要用元组形式
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

create('example_day11_t1')
multi_thread_rename('example_day11_t1')
print('重命名完成')

    