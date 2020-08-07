# itertools操作迭代对象的函数。

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
