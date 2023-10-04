str = '*'
for i in range(3):
    print(str.center(7, ' ')) #center方法会以当前字符串为中心，放到指定长度的中间，然后用指定的字符来填充其它地方
    str += '**' #字符串在末尾加上字符可以直接加

print(str)
str = str.replace('**', '', 1) #但是要删除就不能直接用-，而是用replace 或 translate
for i in range(3):
    print(str.center(7, ' '))
    str = str.replace('**', '', 1)