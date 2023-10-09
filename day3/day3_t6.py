def judge(year:int):
    """判断一个年份是不是闰年"""
    if year % 100 == 0: #判断世纪闰年
        if year % 400 == 0:
            return True
        else:
            return False
    else: #判断普通闰年
        if year % 4 == 0:
            return True
        else:
            return False

def output(year:int, month:int, day:int):
    """输出某一天是这一年的第几天"""
    res = 0
    if judge(year): #闰年的情况
        if month == 1:
            res = day
        elif month == 2:
            res = day + 31
        elif month <= 7:
            i = 1
            while i < month:
                i += 2
                res += 31
            i = 4
            res += 29
            while i < month:
                i += 2
                res += 30
            res += day
        else:
            res += output(year, 7, 31)
            i = 8
            while i < month:
                i += 2
                res += 31
            i = 9
            while i < month:
                i += 2
                res += 30
    else: #普通年份的情况
        if month <= 2: #一月二月的情况和闰年计算方法完全一样
            res = output(2000, month, day)
        else: #三到十二月也几乎一样，只是二月会少一天而已
            res = output(2000, month, day) - 1
    return res
date = input('输入一个日期，以yyyymmdd的形式，中间不要分隔或加符号')
year = int(date[:4:])
month = int(date[4:6:])
day = int(date[6::])
print('这是第' + str(output(year, month, day)) + '天')
