def judge(year:int):
    """判断一个年份是不是闰年"""
    if year % 100 == 0: #判断世纪闰年
        if year % 400 == 0:
            print('这是一个闰年')
        else:
            print('这不是一个闰年')
    else: #判断普通闰年
        if year % 4 == 0:
            print('这是一个闰年')
        else:
            print('这不是一个闰年')

year = int(input('输入一个年份：'))
judge(year)