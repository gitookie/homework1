def mysum():
    num = int(input("输入一个数字："))
    cnt = int(input("输入一个求和的次数："))
    sum = 0
    for i in range(cnt):
        tmp = ((cnt - i) * num) * (10 ** i)
        sum += tmp
    print(str(sum))

mysum()