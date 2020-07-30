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


# 闭包
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()

print('f1', f1())
print('f2', f2())
print('f3', f3())

print(' ---')

print('f1', f1())
print('f2', f2())
print('f3', f3())


# 如果一定要引用循环变量怎么办？方法是再创建一个函数，
# 用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


f1, f2, f3 = count()

print(' ---')

print('f1', f1())
print('f2', f2())
print('f3', f3())


# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
    cnt = [0]

    def counter():
        cnt[0] = cnt[0] + 1

        return cnt[0]

    return counter


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
