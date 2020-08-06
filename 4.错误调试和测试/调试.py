# 断言
# 凡是用print()来辅助查看的地方，都可以用断言（assert）来替代：
def foo(s):
    n = int(s)

    # assert的意思是，表达式n != 0
    # 应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
    assert n != 0, 'n is zero!'

    return 10 / n


def main():
    foo('0')


# main()

# logging
# 把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件：
import logging

logging.basicConfig(level=logging.DEBUG)

s = '0'
n = int(s)
logging.debug('n = %d' % n)
print(10 / n)
