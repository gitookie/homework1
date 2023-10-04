import math
def judge(n:int):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n / i == int(n / i): #(n / i)前面不加int的话，会默认按浮点来处理，会有小数
            return False
    return True
if __name__ == '__main__':
    result = []
    for i in range(101, 201):
        if judge(i):
            result.append(i)

    for i in result:
        print(str(i))
