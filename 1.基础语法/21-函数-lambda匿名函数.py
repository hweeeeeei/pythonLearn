# 当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。

L1 = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print('L1', L1)


# 匿名函数lambda x: x * x实际上就是：
def f(x):
    return x * x

# 关键字lambda表示匿名函数，冒号前面的x表示函数参数。
