class Student(object):
    # 定义类属性
    name = 'Student'


s1 = Student()

print(s1.name)


# 练习
# 为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：

class Student(object):
    count = 0

    def __init__(self, name):
        # 计数器加1
        Student.count += 1
        self.name = name


# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')

# 小结
# 实例属性属于各个实例所有，互不干扰；
#
# 类属性属于类所有，所有实例共享一个属性；
