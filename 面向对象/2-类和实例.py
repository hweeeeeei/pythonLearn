class Student(object):
    # def __init__(self,name,score):
    #     self.name
    pass


c1 = Student()

c1.name = 'giaogiao'

print(c1.name)


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # 数据封装, 这种函数叫做'方法'
    def priSelf(self):
        print('priSelf', self.name, self.score)


c1 = Student('giaogiao2', 99)

print(c1.name)
print(c1.score)


# 函数
def pri(stu):
    print('pri', stu.name, stu.score)


pri(c1)

c1.priSelf()
