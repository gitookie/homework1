num = input('输入一个正整数：')
if num == num[::-1]:
    print(num + '是一个回文数')
else:
    print(num + '不是一个回文数')