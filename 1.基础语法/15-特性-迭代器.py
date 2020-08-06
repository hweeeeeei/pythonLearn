# isinstance()判断一个对象是否是Iterable 可迭代对象

from collections.abc import Iterable

print('[] :', isinstance([], Iterable))

print(100, isinstance(100, Iterable))

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。

from collections.abc import Iterator

print('Iterator []', isinstance([], Iterator))
print('Iterator 100', isinstance(100, Iterator))

# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：
isinstance(iter([]), Iterator)

isinstance(iter('abc'), Iterator)
