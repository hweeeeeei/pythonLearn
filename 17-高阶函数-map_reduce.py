# map()函数


def f(x):
    return x * x


# 我们先看map。map()函数接收两个参数，一个是函数，一个是Iterable，
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
m = map(f, [1, 2, 3, 4, 6, 7, 8, 9])

print(list(m))

# 把这个list所有数字转为字符串：
print('把这个list所有数字转为字符串：', list(map(str, [1, 2, 3, 4, 5, 6, 7, 8])))

# reduce
# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
# reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

from functools import reduce


# 求序列的累加和
def add2(x, y):
    return x + y


print('reduce(add2,', reduce(add2, [1, 2, 3]))


# *10
def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 2, 3, 4]))


# 把str转换为int的函数：
def toInt(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print('toInt', list(map(toInt, ['1', '2', '4', '6'])))

print('reduce', reduce(fn, map(toInt, ['1', '2', '4', '6'])))
