# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，
# 可以直接使用下面的代码创建一个新的函数int2：

import functools

# functools.partial的作用，把函数的某些参数固定住（也就是设置默认值）
int2 = functools.partial(int, base=2)
print(int2('1000000'))

# 也可以在函数调用时传入其他值：
print(int2('1000000', base=9))
