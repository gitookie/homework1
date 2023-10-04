import math
def judge(n:int):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n / i == int(n / i):
            return False
    return True
a = int(input("输入一个正整数："))
tmp = a
result = []
i = 2
while i < a + 1:
    if judge(i):
        if tmp % i == 0:
            result.append(i)
            tmp /= i
        else: #这里的else不能漏了
            i += 1
    else: #想清楚两个else
        i += 1

print(str(a) + '=', end = '')  #要让输出在同一行，就改一下end，它默认是'\n'
i = 0
for num in result:
    if i == 0:
        print(str(num), end = '')
    else:
        print('*' + str(num), end = '')
    i += 1

