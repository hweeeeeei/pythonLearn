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


main()
