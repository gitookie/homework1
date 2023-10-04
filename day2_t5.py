import math
def judge(n:int):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n / i == int(n / i): #(n / i)前面不加int的话，会默认除出小数来
            return False
    return True

result = []
for i in range(101, 201):
    if judge(i):
        result.append(i)

for i in result:
    print(str(i))