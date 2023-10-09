def calculate(*args): #这个*args其实就是指可以传入任意多个参数，它本质是个元组，一般如果有多个参数，它会放在最后；否则
    #在其它位置的话，剩余的元素需要提前指定好值
    """可以传入任意多个参数，返回一个元组，第一个元素是这些数的平均值，后面的是大于这个平均值的元素的索引"""
    sum = 0
    res = ()
    for arg in args:
        sum += arg
    mean = sum / len(args)
    tmp = (mean,)
    res += tmp
    for i in range(len(args)):
        if args[i] > mean:
            tmp = (i,)
            res += tmp
    return res

res = calculate(2, 3, 4, 5, 1, 6, 7)
print(res)