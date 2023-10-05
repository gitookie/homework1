def find(n:int):
    """判断正整数的位数"""
    digits = 0
    while n >= 1:
        digits += 1
        n /= 10
    return digits
def reverse_str(text:str):
    """另一种反转字符串的方法"""
    result= ''
    for char in text:
        result = char + result #之所以能反转字符串，重点在于这里是把text中的字符加在了result的前面，所以等效于反转
    return result
def recur_reverse(text:str):
    """用递归来实现字符串反转，但是对字符串有长度限制"""
    if len(text) == 1: #当字符串长度为1时，此时是一个单字符，直接返回
        return text
    return recur_reverse(text[1:]) + text[:1] #核心，逻辑上就是，当字符串长度大于1时，整个字符串反转的结果，也就是把
    #当前第一个字符放到最后，把从第二个字符到最后一个字符组成的字符串反转以后，拼到第一个字符的前面。这里用到了切片
num = int(input("输入一个正整数:"))
print("这是一个" + str(find(num)) + "位数")
str = str(num)
print(str[::-1]) #直接用切片
print(reverse_str(str)) #反向拼接字符
print(''.join(reversed(str))) #
print(recur_reverse(str)) #递归方法