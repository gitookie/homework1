dict = {
    (1, 1):0,
    (2, 2):1,
    (3, 3):2
}
print(dict)
"""
dict = {
    [1, 1]:0,
    [2, 2]:1,
    [3, 3]:2
}
print(dict)
"""
"""dict = {
    {1, 1}:0,
    {2, 2}:1,
    {3, 3}:2
}
print(dict)"""



def test_func3(list2):
  list2 = list2 + [7]
  
list1 = [1, 3, 5]
list2 = list1
list1.append(6)
print(list2)
test_func3(list1)
print(list1)
