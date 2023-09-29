nums = list(input("输入三个整数，用空格分开").split())
for i in range(len(nums)):
    nums[i] = int(nums[i])
print(nums)
for num in sorted(nums):
    print((num))