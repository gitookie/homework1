import os
import random as rd

def create(i, j):
    """创建一个目录test,里面有i个以上的文件,每个文件有j行随机字符"""
    if not os.path.exists('test') or not os.path.isdir('test'):
        os.mkdir('test')

    num = rd.randint(i, i + 50)
    while num <= i: #获得一个大于i的整数
        num = rd.randint(i, i + 1000)

    for id in range(num):
        with open(os.path.join('test', f'{id}'), 'w') as file:
            for line in range(j):
                random_char = chr(rd.randint(32, 126))
                if line < j - 1:
                    file.write(random_char + '\n')
                else:
                    file.write(random_char)

def traverse(folder_name):
    """遍历一个文件夹中的所有文件，并对其中的文件内容和文件名做一定改动"""
    
    for root, dirs, files in os.walk(folder_name): #用walk来遍历文件夹中的文件，它会返回一个三元组，第一个是文件夹的路径，
        #第二个是子文件夹的名字，因此它是一个列表，并且如果这个文件夹里没有子文件夹的话，那么返回的dirs是一个空列表。
        # 第三个是一个列表，包含了所有文件的名字
        for name in files:
            #这里采取的方式是先读取出原先的内容，在此基础上进行改动，然后重新写回去。就地修改好像不是很方便，而且可能会出问题
            new_content = ''
            with open(os.path.join(root, name), 'r') as file:
                lines = file.readlines() #先把原内容读出来

            with open(os.path.join(root, name), 'w') as file: #写入模式的时候才会覆盖原先内容，如果是'r+'模式
                #则是接着写
                id = 0
                for line in lines:
                    line = line.strip() + '-python' #这里一定要注意，原先我的输入就是一行一行的，所以读出来的每一行，
                    #除了最后一行，都有换行符，要么把它去掉自己加，要么自己就不加了。调试了半天才看到
                    if id < len(lines) - 1:
                        new_content = new_content + line.strip() + '\n'
                    else:
                        new_content += line                        
                    id += 1
        
                file.write(new_content)

                old_path = os.path.join(root, name) #这里就获得了当前文件的绝对路径
                name += '-python'
                new_path = os.path.join(root, name)
                os.rename(old_path, new_path)



create(5, 6)
traverse('test')