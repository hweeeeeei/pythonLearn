# Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较。


from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# 枚举它的所有成员

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

    # Jan = > Month.Jan, 1
    # Feb = > Month.Feb, 2
    # Mar = > Month.Mar, 3
    # Apr = > Month.Apr, 4
    # May = > Month.May, 5
    # Jun = > Month.Jun, 6
# value属性则是自动赋给成员的int常量，默认从1开始计数。
#
# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
from enum import Enum, unique


# @unique装饰器可以帮助我们检查保证没有重复值。
@unique
class Weekday(Enum):
    Sum = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


day1 = Weekday.Sum
print('day1', day1.name)

print(Weekday(2))
print('-------')
# 获取枚举的所有类型
for name, menber in Weekday.__members__.items():
    print(name, '=>', menber, menber.value)


# 练习
# 把Student的gender属性改造为枚举类型，可以避免使用字符串：
@unique
class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
