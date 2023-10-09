height = 100
total = 0
for i in range(10):
    total += height
    height /= 2

print("第十次落地时经过的高度总和：" + str(total))
print("第十次反弹的高度：" + str(height))