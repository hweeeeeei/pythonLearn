# 函数作为返回值
# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。


# 通常情况下，求和的函数
def sum(*args):
    ax = 0
    for n in args:
        ax = ax + n

    return ax


print('通常情况下，求和的函数', sum(1, 2, 3, 4, 5))


# 返回求和的函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n

        return ax

    return sum


f = lazy_sum(1, 2, 3, 4, 56, 7)
# 调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
print('f', f)

# 调用函数f时，才真正计算求和的结果：
print('f()', f())
