def insert(list, num):
    """把一个数插入到一个已经排好序的数组里面，要求是升序排列"""
    if num >= list[len(list) - 1]: #新插入的数是最大的
        list.append(num)
        return list
    #新插入的数在中间
    id = len(list) - 1
    tmp = list[id]
    while num < tmp: #先找出新的数应该插在哪里
        id -= 1
        tmp = list[id]
    i = len(list)
    list.append(0) #把数组拓展一个长度，以便把元素往后移
    while i > id + 1: #这个边界想清楚，可以结合实例
        list[i] = list[i - 1]
        i -= 1
    list[i] = num
    return list

list = [1, 2, 3, 4, 5]
list = insert(list, 3.5)
print(list)