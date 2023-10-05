def add(matrix1, matrix2):
    """实现两个矩阵的加法"""
    res = []
    for rowid in range(len(matrix1)):
        line = []
        for colid in range(len(matrix1)):
            tmp = matrix1[rowid][colid] + matrix2[rowid][colid]
            line.append(tmp)
        res.append(line)
    return res

matrix1 = [[1,3, 4],
           [2, 4, 5],
           [4, 8, 9]
           ]
matrix2 = [[7,3, 3],
           [2, 6, 5],
           [-3, 8, 9]
           ]
print(add(matrix1, matrix2))