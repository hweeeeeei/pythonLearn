L = ['啊发发', 'adfr', '42414', 'eafdgzxv', '2222dddd']

# 切片取前三个元素
print(L[0:3])

# L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
#
# 如果第一个索引是0，还可以省略：
print(L[:3])

# 创建0-99数列
L2 = list(range(100))
print('list(range(100))', L2)

print('取前面10个数', L2[:10])

print('取后面10个数', L2[-10:])

print('前11到20个数', L2[11:20])

print('前10个数, 每两个取一个', L2[0:10:2])

print('所有数，每5个取一个：', L2[::5])

# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
str1 = 'ABCDEFG'
print(str1[0:1])
print(str1[0:2])
print(str1[::2])
print(str1[-1:])


# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(s):
    size = len(s)
    n = 1
    # 删除前面空字符
    while n <= size:
        if s[:n] == ' ':
            s = s[n + 1:size]
        else:
            break
        n = n + 1

    n = len(s)
    # 删除后面空字符
    while n >= 0:
        if s[n - 1:n] == ' ':
            s = s[0:n - 1]
        else:
            break
        n = n - 1

    return s


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
