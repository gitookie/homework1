def judge(i:int):
    first = i % 10
    second = int(i / 10) % 10
    third = int(i / 100) % 10
    if first ** 3 + second ** 3 + third ** 3 == i:
        return True
    return False

result = []
for i in range(100, 1000):
    if judge(i):
        result.append(i)
for i in result:
    print(str(i))

