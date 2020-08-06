# 函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！

print('abs -100', abs(-100))

a = abs(-200)
print('a', a)

# 变量可以指向函数
f = abs
# 直接调用abs()函数和调用变量f()完全相同。
print('f', f(-123))

# 函数名也是变量
# 如果把abs指向其他对象，会报错
# abs = 100
abs(-231)


# 把函数作为参数传入，这样的函数称为高阶函数
def add(a, b, f):
    return f(a) + f(b)


add_res = add(-100, -200, f)

print('add_res', add_res)
