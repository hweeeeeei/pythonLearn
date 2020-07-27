# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

# set和dict的唯一区别仅在于没有存储对应的value

set_a = set([1, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(set_a)

set_a.add(10)
print("set_a.add(10)", set_a)

set_a.remove(1)
print("set_a.remove(1)", set_a)

set1 = set([1, 2, 4])
set2 = set([1, 3, 4])

# 交集
print('交集', set1 & set2)

# 并集
print('并集', set1 | set2)
