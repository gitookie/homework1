import numpy as np

class Point:
    def __init__(self, x, y, z = 0):
        """初始化点的坐标，并打印创建了Point(x, y, z)"""
        self.x = x
        self.y = y
        self.z = z
        print('创建了', end = '')
        print(self)

    def __add__(self, object):
        """重载加法, p加v得到v, p加p报错"""
        if isinstance(object, Point): #如果输入的参数是个点类
            print('Error!')
            print('点不能加点')
        elif isinstance(object, Vector):
            new_x = self.x + object.x
            new_y = self.y + object.y
            new_z = self.z + object.z
            return Vector(new_x, new_y, new_z)
        else:
            print('参数输入错误！')

    def __sub__(self, object):
        """重载减法, p减v得到v, p减p也得到v"""
        if isinstance(object, Point):
            new_x = self.x - object.x
            new_y = self.y - object.y
            new_z = self.z - object.z
            return Vector(new_x, new_y, new_z)
        elif isinstance(object, Vector):
            new_x = self.x - object.x
            new_y = self.y - object.y
            new_z = self.z - object.z
            return Vector(new_x, new_y, new_z)
        else:
            print('参数输入错误！')
    
    def __del__(self):
        """重载析构函数，销毁时输出内容"""
        print('销毁了', end = '')
        print(self)

    def __str__(self):
        """重载此函数，使得打印对象时返回对象的信息"""
        return 'Point(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')'

    def __eq__(self, object) -> bool:
        """重载判断相等的函数"""
        if isinstance(object, Point):
            if self.x == object.x and self.y == object.y and self.z == object.z:
                return True
            else:
                return False
        else:
            print('参数类型错误！')
            return False
        
    def __lt__(self, object) -> bool:
        """重载小于号，到原点的距离小才认为小于成立"""
        if isinstance(object, Point):
            if self.x ** 2 + self.y ** 2 + self.z ** 2 < object.x ** 2 + object.y ** 2 + object.z ** 2:
                return True
            else:
                return False
        else:
            print('参数类型错误！')
            return False 
        
    def __gt__(self, object) -> bool:
        """重载大于号"""
        if isinstance(object, Point) == False: #先排除类型不对的错误
            return False
        elif self == object:
            return False
        elif self < object:
            return False
        else:
            return True
    

        
class Vector:
    def __init__(self, x, y, z = 0):
        """初始化点的坐标"""
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        """重载此函数，使得打印对象时返回对象的信息"""
        return 'Vector(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')'
    
    def __add__(self, object):
        """重载加法, v加v得到v, v加p报错"""
        if isinstance(object, Point): #如果输入的参数是个点类
            print('Error!')
            print('向量不能加点')
        elif isinstance(object, Vector):
            new_x = self.x + object.x
            new_y = self.y + object.y
            new_z = self.z + object.z
            return Vector(new_x, new_y, new_z)
        else:
            print('参数输入错误！')
    
    def __sub__(self, object):
        """重载减法, v减v得到v, v减p报错"""
        if isinstance(object, Point):
            print('Error!')
            print('向量不能减点')
        elif isinstance(object, Vector):
            new_x = self.x - object.x
            new_y = self.y - object.y
            new_z = self.z - object.z
            return Vector(new_x, new_y, new_z)
        else:
            print('参数输入错误！')

    def __eq__(self, object) -> bool:
        """重载判断相等的函数"""
        if isinstance(object, Vector):
            if self.x == object.x and self.y == object.y and self.z == object.z:
                return True
            else:
                return False
        else:
            print('参数类型错误！')
            return False
        
    def __lt__(self, object) -> bool:
        """重载小于号，模长小才认为小于成立"""
        if isinstance(object, Vector):
            if self.x ** 2 + self.y ** 2 + self.z ** 2 < object.x ** 2 + object.y ** 2 + object.z ** 2:
                return True
            else:
                return False
        else:
            print('参数类型错误！')
            return False 
        
    def __gt__(self, object) -> bool:
        """重载大于号"""
        if isinstance(object, Vector) == False: #先排除类型不对的错误
            return False
        elif self == object:
            return False
        elif self < object:
            return False
        else:
            return True
        
    def __mul__(self, x: float): #x按题目意思是度数，所以需要单位转化
        """重载乘法,此时乘法代表旋转,且只转在xoy平面的投影"""
        projection = np.array([self.x, self.y])
        angel = x / 180 * np.pi #把度转化为弧度
        rotation = np.array([[np.cos(angel), -np.sin(angel)],
                             [np.sin(angel), np.cos(angel)]])
        cur = np.dot(rotation, projection)
        tmp = Vector(cur[0], cur[1], self.z)
        return tmp
        """length = (self.x ** 2 + self.y ** 2) ** 0.5 自己写的
        if length == 0: #此时在xoy的投影的模长为0,则只有z轴上的分量,直接返回就好
            return self
        else:
            cur_cos = self.x / length
            cur_sin = self.y / length"""
    
    def __truediv__(self, x: float):
        """重载除法，此时除法代表旋转，且只转在xoy平面的投影"""
        return self * -x #逆时针转-x也就是顺时针转x


A = Point(1, 2, 3)
B = Point(4, 5, 6)
print(A + B)
print(A == B)
C = Vector(1, 0, 3)
print(C * 45)
D = Vector(2, 4, 6)
print(C - D)
