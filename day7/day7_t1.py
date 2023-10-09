import random
import os

def create(filename: str) -> None:
    """创建一个10行3列的文件"""
    if not os.path.exists(os.getcwd() + '/' + filename): #不想重复创建，可以这样写，而且这里的/好像不能少，少了的话每次
        #还是会重新创建，或者用path.join的话应该就不用这么麻烦了
        with open(filename, 'w') as file:
            for row in range(10):
                for column in range(3):
                    if column < 2:
                        file.write(str(random.random()) + ',')
                    elif row < 9:
                        file.write(str(random.random()) + '\n')
                    else:
                        file.write(str(random.random()))
    

def analyze(filename: str) -> None:
    """对10行3列,都是数,且用逗号分隔的文件(也就是上面创建的那种文件)的第二列进行分析，
    找出最大值，最小值，平均值，中位数"""
    with open(filename, 'r') as file:
        lines: list = file.readlines()
    
    #获取第二列的全部数据
    second_column = []
    for line in lines:
        second_column.append(float(line.strip().split(',')[1]))#先把每一行的空白符去掉，然后按逗号进行分割，此时会
        #返回一个列表，存放分割后得到的结果；再把结果变成浮点数，最后取第二列的，加入到存储列表中
    maxi: float = max(second_column) #注意一下，这里变量名似乎不能起max，跟自带的函数max重名了，好像有点问题，下面一样
    mini: float = min(second_column)
    mean: float = sum(second_column) / len(second_column)
    tmp: list = sorted(second_column)
    mid: float = (tmp[4] + tmp[5]) / 2
    print(f'最大值是{maxi}, 最小值是{mini}, 平均值是{mean}, 中位数是{mid}')

create('example_day7_t1.txt')
analyze('example_day7_t1.txt')
    

    