import random


class Universe():
    def __init__(self, length = 80, width = 15):
        """初始化地图和所有细胞"""
        self.length = length
        self.width = width
        self.grid = []
        for row in range(width):
            tmp_row = []
            for col in range(length):
                tmp_row.append(' ')
            self.grid.append(tmp_row)

    def Show(self):
        """打印当前情况"""
        for row in self.grid:
            print(''.join(row)) #不用空字符拼起来的话，打印出来的东西很抽象，因为会以列表形式直接打印

    def Seed(self):
        """激活当前世界，使一定数量的细胞活过来"""
        cnt = 0
        while cnt < int(self.width * self.length / 4):
            row = random.randint(0, self.width - 1)
            col = random.randint(0, self.length - 1)
            if self.grid[row][col] == ' ':
                self.grid[row][col] = '*'
                cnt += 1
    def Alive(self, row, col):
        """判断一个细胞是延续还是死亡还是复活"""
        cnt = 0
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if i >= 0 and i <= self.width - 1 and j >= 0 and j <= self.length - 1: #还是去遍历“周围八个点”
                    #但是先检查一下下标是否合法
                    if self.grid[i][j] == '*' or self.grid[i][j] == 2 or self.grid[i][j] == 3:
                        cnt += 1

        if cnt < 2 or cnt > 3: #死亡
            return False
        elif cnt == 3: #复活
            return True
        else: #剩下的情况为延续，则原先存活，之后还是存活;原先死亡，现在还是死亡
            if self.grid[row][col] == '*':
                return True
            else:
                return False
    
    def Next(self): #用符合状态来兼顾表示之前和之后的状态。一个细胞前后两个世代只有四种状态组合，死死，死活，活死，活活
        #分别对应0, 1, 2, 3 
        #不过用这个方法的话，前面的Alive函数也需要相应的进行一些修改
        """更新世界"""
        for i in range(self.width):
            for j in range(self.length):
                if self.grid[i][j] == ' ':
                    if self.Alive(i, j) == False:
                        self.grid[i][j] = 0
                    else:
                        self.grid[i][j] = 1
                else:
                    if self.Alive(i, j) == False:
                        self.grid[i][j] = 2
                    else:
                        self.grid[i][j] = 3
        for i in range(self.width):
            for j in range(self.length):
                if self.grid[i][j] == 0 or self.grid[i][j] == 2:
                    self.grid[i][j] = ' '
                else:
                    self.grid[i][j] = '*'
universe = Universe()
#universe.Show()
universe.Seed()
universe.Show()
print('\n\n')
universe.Next()
universe.Show()


for i in range(500):
    universe.Next()

print('\n\n\n')
universe.Show()