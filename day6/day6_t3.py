class Person:
    def __init__(self, name, age, sex):
        """初始化"""
        self.name = name
        self.age = age
        self.sex = sex

    def personInfo(self):
        """打印个人信息"""
        print(f'姓名：{self.name}')
        print(f'年龄：{self.age}')
        print(f'性别：{self.sex}')


class Student(Person):
    def __init__(self, name, age, sex, college, stu_class):
        """初始化"""
        super(Student, self).__init__(name, age, sex)
        self.college = college
        self.stu_class = stu_class

    def personInfo(self):
        """打印更详细的个人信息"""
        super(Student, self).personInfo() #这样可以在重写之后依然调用父类中的方法
        print(f'学院：{self.college}')
        print(f'班级：{self.stu_class}')

    def __str__(self):
        """打印对象时返回个人信息"""
        return f'姓名：{self.name}, 年龄：{self.age}, 性别：{self.sex}, 学院：{self.college}, 班级：{self.stu_class}'


a = Person('a', '24', 'm')
a.personInfo()
print(a)
b = Student('b', '26', 'f', 'xfu', '9')
b.personInfo()
print(b)
