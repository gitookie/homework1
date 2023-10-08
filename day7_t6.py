import os

def replace_py(folder_name):
    """把文件夹中所有的文件名和文件内容中出现的python都替换成class"""
    #思路跟上一题很像，先改文件内容，再改文件名比较好
    for root, dirs, files in os.walk(folder_name):
        for name in files:
            with open(os.path.join(dirs, name), 'r') as file:
                content = file.read()
                content = content.replace('python', 'class')
            with open(os.path.join(root, name), 'w') as file:
                file.write(content)
            
            old_path = os.path.join(root, name)
            name = name.replace('python', 'class')
            new_path = os.path.join(root, name)
            os.rename(old_path, new_path)

replace_py('test')