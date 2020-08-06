# Python内置的sorted()函数就可以对list进行排序：

list1 = [-22, -33, 3, 4, 2, 1]

print('sorted排序', sorted(list1))
print('sorted排序 + 反向', sorted(list1, reverse=True))

# 字符串排序
strList = ['afbkasd', 'a', 'b', 'd', 'c', 'bd']
print('sorted strList排序', sorted(strList))

# 此外，sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
print('sorted abs', sorted(list1, key=abs))

# 字符串 排序忽略大小写
strList2 = ['Afbkasd', 'a', 'B', 'D', 'c', 'bd']
print('sorted 字符串 排序忽略大小写', sorted(strList2, key=str.lower))

print('sorted 字符串 排序忽略大小写 + 反向排序', sorted(strList2, key=str.lower, reverse=True))

# 练习
# 假设我们用一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


# 请用sorted()对上述列表分别按名字排序：
def by_name(t):
    # 下标为0的是名字
    return t[0]


L2 = sorted(L, key=by_name)
print('by_name', L2)

# 成绩从高到低排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_score(t):
    # 数组中下标为1的是分数
    # 带负号 可以反转
    return -t[1]


L2 = sorted(L, key=by_score)
print('by_score', L2)
