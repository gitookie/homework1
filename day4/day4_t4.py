def move_backward(m:int, list):
    for i in range(m):
        tmp = list.pop() #默认弹出最后一个元素，也可以自己指定弹出元素的索引
        list.insert(0, tmp) #在指定索引处插入元素，这个指定索引指的是插入以后这个元素在新列表里的索引
    return list

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list = move_backward(3, list)
print(list)