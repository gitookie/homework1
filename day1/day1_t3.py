def Fibonacci(num):
    last = 0
    cur = 1
    if num > 1:
        print(str(last))
    if num > 2:
        print(str(cur))
    for i in range(num - 2):
        next = last + cur
        last = cur
        cur = next
        print(str(cur))

Fibonacci(20)
