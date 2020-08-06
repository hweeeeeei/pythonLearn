import os  # 导入os模块，模块的概念后面讲到

list1 = list(range(100))

print(list1)

list2 = list(range(50, 100))

print('list2', list2)

# 但生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：

L2 = []

for i in list1:
    L2.append(i * i)

print(L2)

# 但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：
# 列表生成式
in_list_range_ = [i * i for i in list(range(10))]
print(in_list_range_)

# 仅选出偶数
range_if_i_ = [i * i for i in list(range(10)) if i % 2 == 0]
print(range_if_i_)

# 两层循环，可以生成全排列
print('--------')
print([g + h + h for g in 'ZXV' for h in 'ABC'])

# os.listdir可以列出文件和目录
print([d for d in os.listdir('/')])

print('--------')

# 多个变量
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, v)

# 列表生成式也可以使用两个变量来生成list：
d1 = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + ' = ' + v for k, v in d1.items()])

# list中所有的字符串变成小写：
L2 = ['Hello', 'World', 'IBM', 'Apple']
print("变成小写", [d1.lower() for d1 in L2])

# if ... else
print('if ... else', [x if x % 2 == 0 else -x for x in range(1, 11)])

# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [l.lower() for l in L1 if isinstance(l, str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
