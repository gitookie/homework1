import os

def judge_diff(file1, file2):
    """逐行判断两个文本文件是否相同，并输出不同的行的标号(从0开始)"""
    lines1 = open(file1, 'r').readlines()
    lines2 = open(file2, 'r').readlines()
    length = min(len(lines1), len(lines2))
    res = []
    for i in range(length):
        if lines1[i] != lines2[i]:
            res.append(i)
    if not res:
        print("在两个文件共同的行数内，它们每一行都相等")
    else:
        print('两个文本有不同的行，标号如下(从0开始)')
        for line in res:
            print(line)

judge_diff('test.txt', 'copy_test.txt')
    