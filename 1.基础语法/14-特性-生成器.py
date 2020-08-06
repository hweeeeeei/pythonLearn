L = [x * x for x in range(10)]

print('L', L)

# 列表生成式的[]改成()，就创建了一个generator：

L1 = (x * x for x in range(10))

print('L1', L1)

# 通过next()函数获得generator的下一个返回值：
print(next(L1))
print(next(L1))
print(next(L1))
print(next(L1))
print(next(L1))

print('-------')

# for循环获取generator的值, generator也是可以迭代的对象
L2 = (x * x for x in range(10))
for g in L2:
    print(g)

n, a, b = 0, 0, 1
print(n, a, b)

print('-------')


# 斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


fib(6)

print('-------')


# 定义一个generator，依次返回数字1，3，5：
def odd():
    print('1')
    yield 1

    print('2')
    yield 3

    print('3')
    yield 6


generator_odd = odd()
print(next(generator_odd))
print(next(generator_odd))
print(next(generator_odd))

print('-------for')

for o in odd():
    print(o)
