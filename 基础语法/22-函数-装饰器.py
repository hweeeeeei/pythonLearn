# 代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

# 定义能打印日志的decorator
# 接受一个函数作为参数，并返回一个函数
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


# 观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处：

# 把@log放到now()函数的定义处，相当于执行了语句：
# now = log(now)
@log
def test1():
    print('hhh')


test1()

print('---')


# decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数

# 接受一个函数作为参数，并返回一个函数
def log2(text):
    def log(func):
        def wrapper(*args, **kw):
            print('%s %s():', text, func.__name__)
            return func(*args, **kw)

        return wrapper

    return log


@log2('pppppp2')
def pri2():
    print('pri2')


pri2()

#
# 和两层嵌套的decorator相比，3层嵌套的效果是这样的：
#
# >>> now = log('execute')(now)
