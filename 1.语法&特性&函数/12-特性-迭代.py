# 迭代 引用两个变量
for x in [(1, 2), (3, 3), (4, 5), (6, 7)]:
    print(x)

print(' -------')

# 迭代 引用两个变量
for x, y in [(1, 2), (3, 3), (4, 5), (6, 7)]:
    print(x, y)

print(' -------')


# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    min = 0
    max = 1

    # 判空
    if L == []:
        return None, None

    for num in L:

        print(num)

        # 判断最小数
        if num < min:
            min = num

        # 判断最大数
        if num > max:
            max = num

    return min, max


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
