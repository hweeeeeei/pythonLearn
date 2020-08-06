# dict
# Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

d1 = {'giao': 10, "olg": 12}
print(d1['giao'])

d1['giao'] = 123
print('修改后', d1['giao'])

d1['giao'] = 312
print('再次修改后', d1['giao'])

# in判断key是否存在
is_in = 'dfa' in d1
print('key是否存在', is_in)

# get()方法，如果key不存在，可以返回None，或者自己指定的value
print("d1.get('olg')", d1.get('olg'))
print("d1.get 为 None", d1.get('ajfjl'))

print(" d1.get('adaga','不存在')", d1.get('adaga', '不存在'))

# 删除key
d1.pop('giao')
print('删除giao ', d1.get('giao'))
#
#
# dict内部存放的顺序和key放入的顺序是没有关系的。
#
# 和list比较，dict有以下几个特点：
#
# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。
# 而list相反：
#
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。
# 所以，dict是用空间来换取时间的一种方法。
#
