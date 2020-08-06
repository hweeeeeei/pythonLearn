# 文档 https://docs.python.org/zh-cn/3/library/functions.html#abs

# 绝对值
print(abs(-20))


# 定义一个函数
def my_ads(x):
    # 验证参数类型
    if not isinstance(x, int):
        raise TypeError(' x type error')

    if x >= 0:
        return x
    else:
        return -x


print('my_ads(20)', my_ads(20))

print('my_ads(-30)', my_ads(-30))


# print('my_ads(-30)', my_ads('2'))


# 计算次方
def cifang(num, count=2):
    return num ** count


print('cf', cifang(2))

print('cf count=3', cifang(2, 3))


# 可变参数 累加
def kebian(*num):
    sum = 0

    for n in num:
        sum = sum + n

    return sum


print("1+2+3+4", kebian(1, 2, 3, 4))

# 数组下标传参
nums = [1, 2, 3, 4, 5]
print("nums", kebian(nums[2], nums[3]))

# 传递数组
print("*nums", kebian(*nums))


# 可变默认参数
def kebian2(name, age=18):
    print('kebian2', name, age)


kebian2('hhhh')
kebian2('hhhh', 12)


# 关键字参数
def person(name, age, **kw2):
    if 'sk' in kw2:
        print('有sk', kw2.get('sk'))
    print(name, age, kw2)


person('giao', 12)
person('giao', 123, sjsj='sshhs')
person('giao', 123, sjsj='sshhs', shdh='dfgs')
person('giao2', 123, sjsj='ad', sk='市分公司答复')


# 命名关键字参数
def person2(name, age, *, city, sex):
    print(name, age, city, sex)


person2('的', 123, city='ad', sex='阿道夫')


# 可变参数 + 命名关键字参数 + 默认参数
def person4(name, age, *args, sex='f', city):
    print(name, age, args, sex, city)


person4('giao', 18, 'g', city='cs')
