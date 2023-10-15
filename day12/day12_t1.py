import csv
import random
import pandas
import os
import argparse

#下面这些内容就是t2增加的，增加后即可通过命令行指定参数
parser = argparse.ArgumentParser()
parser.add_argument('--path', type=str, help='文件路径')
parser.add_argument('--num', type=int, help='指定删除的列数(下标从0开始)')
args = parser.parse_args()
path = args.path
id = args.num


def create_csv():
    """随便创建一个csv文件，拿来测试"""
    data = []
    for i in range(5):
        row = [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]
        data.append(row)
    
    if not os.path.exists(os.path.join(os.getcwd(), path)):
        with open(os.path.join(os.getcwd(), path), 'w') as file:
            writer = csv.writer(file)
            writer.writerows(data)
    
def del_one_col(path, id = -1):
    """删除csv文件的某一列"""
    with open('day12/example.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader) #把reader读取到的内容以列表形式存储
        col_num = len(data[0]) #之所以提前在这里写，是因为后面会改动data，如果还用len(data[0])这种表达式的话，结果会变化
        row_num = len(data)

        if id == -1: #默认为-1,则随便删除一列；否则删除指定列
            id = random.randint(0, col_num - 1) #随机选一列来删除
        
        for i in range(row_num):
            tmp_row = data[i]
            row = []
            for j in range(col_num):
                if j != id:
                    row.append(tmp_row[j])
            data[i] = row
    with open('day12/example.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerows(data)
        #print(data)

def add_2_col(path):
    """随机挑两列相加，结果放到列数较小的那一列"""
    with open(path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    col_num = len(data[0])
    row_num = len(data)
    if col_num < 2:
        print('列数太少了')
        return None
    col_1 = random.randint(0, col_num - 1)

    col_2 = random.randint(0, col_num - 1)
    while (col_2 == col_1):
        col_2 = random.randint(0, col_num - 1)
    
    if col_1 < col_2:
        min = col_1
        max = col_2
    else:
        min = col_2
        max = col_1
    
    for i in range(row_num):
        row = data[i]
        for j in range(col_num):
            row[j] = int(row[j])

        row[min] += row[max]
        data[i] = row
    with open(path, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    #del_one_col(path, max) 删不删看需求吧，先不删了
    

    
#create_csv()
#add_2_col(path)
del_one_col('day12/example.csv')
