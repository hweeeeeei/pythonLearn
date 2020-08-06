try:
    print('try...')
    r = 10 / 0

    print('r...', r)

except ZeroDivisionError as e:
    print('except..', e)


finally:
    print('finally...')

    # 认为某些代码可能会出错时，就可以用try来运行这段代码，
    # 如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，
    # 即except语句块，执行完except后，如果有finally语句块，
    # 则执行finally语句块，至此，执行完毕。

print('-------')

# 有多个except来捕获不同类型错误
try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)

#     没有错误发生时，会自动执行else
else:
    print('else..')
finally:
    print('finally...')
print('END')

print('跨越多层调用-------')


# 跨越多层调用

def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')


main()

print('调用栈-------')


# 调用栈

# err.py:
def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    bar('0')


# main()

print('记录错误logging-------')

# 记录错误
import logging


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)


# main()
print('END')

print('抛出错误-------')


# 抛出错误
# 定义错误class，选择继承关系，用raise语句抛出错误实例：

class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value' % s)

    return 10 / n


# foo('0')


# 练习
# 运行下面的代码，根据异常信息进行分析，定位出错误源头，并修复：
from functools import reduce


def str2num(s):
    # return int(s)
    # 如果使用int的话, 当传入带小数点的数时 会转换错误  所以改成float就不会报错了

    return float(s)


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)


main()
