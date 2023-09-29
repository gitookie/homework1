string = input()

i = 0
space = 0
digit = 0
alpha = 0
other = 0
for cur in string:
    if cur == '\n':
        break
    if cur.isdigit():
        digit += 1
    elif cur.isalpha():
        alpha += 1
    elif cur == ' ':
        space += 1
    else:
        other += 1


print("digit:" + str(digit))
print("alpha:" + str(alpha))
print("space:" + str(space))
print("other:" + str(other))