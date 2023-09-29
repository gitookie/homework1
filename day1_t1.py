cnt = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i == j or i == k or j == k:
                continue
            cnt += 1
            print(str(i) + str(j) + str(k))

print("能组成" + str(cnt) + "个符合要求的三位数")