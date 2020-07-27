# 函数在内部调用自身本身，这个函数就是递归函数

#
# 计算阶乘 fact(n)=n!=1×2×3×⋅⋅⋅×(n−1)×n=(n−1)!×n=fact(n−1)×n
def fact(n):
    # 如果为1 则退出递归
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(5))


# ===> fact(5)
# ===> 5 * fact(4)
# ===> 5 * (4 * fact(3))
# ===> 5 * (4 * (3 * fact(2)))
# ===> 5 * (4 * (3 * (2 * fact(1))))
# ===> 5 * (4 * (3 * (2 * 1)))
# ===> 5 * (4 * (3 * 2))
# ===> 5 * (4 * 6)
# ===> 5 * 24
# ===> 120

# 下面这行会出现栈溢出
# print(fact(1000))


# 尾递归 解决栈溢出, 将每步计算结果传入下个调用
def fact2(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


print('尾递归', fact2(5))

# 可以看到，return fact_iter(num - 1, num * product)仅返回递归函数本身，num - 1和num * product在函数调用前就会被计算，不影响函数调用。
#
# fact2(5)对应的fact_iter(5, 1)的调用如下：
#
# ===> fact_iter(5, 1)
# ===> fact_iter(4, 5)
# ===> fact_iter(3, 20)
# ===> fact_iter(2, 60)
# ===> fact_iter(1, 120)
# ===> 120
