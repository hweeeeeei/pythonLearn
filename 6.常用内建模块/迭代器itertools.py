# itertools操作迭代对象的函数。

# itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算。


import itertools

# ”无限”迭代器

# 创建一个无限的迭代器
natuals = itertools.count(1)
# for n in natuals:
#     print(n)

# cycle()会把传入的一个序列无限重复下去：
cs = itertools.cycle('ABC')  # 注意字符串也是序列的一种
# for c in cs:
#     print(c)

# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
ns = itertools.repeat('A', 3)  # 迭代3次
for n in ns:
    print(n)

# takewhile()等函数根据条件判断来截取出一个有限的序列：
natuals = itertools.count(1)
# 迭代10次
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print('ns', list(ns))

# chain()
# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：

for c in itertools.chain('ABC', 'XYZ'):
    print(c)

# groupby()
print('# groupby()把迭代器中相邻的重复元素挑出来放在一起：')
for key, group in itertools.groupby('AAABBBCCDDAAADdd'):
    print(key, list(group))

# 忽略大小写
print('# groupby()忽略大小写：')
for key, group in itertools.groupby('AAABBBCCDDAAADdd', lambda c: c.upper()):
    print(key, list(group))

print('练习 计算圆周率可以根据公式：')


def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    odd = itertools.count(1, 2)

    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    odd_n = itertools.takewhile(lambda x: x <= 2 * N - 1, odd)

    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    tmp = map(lambda x: 4 / x if x % 4 == 1 else -4 / x, odd_n)

    # step 4: 求和:
    return sum(tmp)


print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')
