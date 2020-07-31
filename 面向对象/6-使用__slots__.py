# 限制实例的属性
# 特殊的__slots__变量，来限制该class实例能添加的属性
class Student(object):
    __slots__ = ('age', 'name')


s = Student()
s.name = 'ggg'
# s.score=100


# __slots__定义的属性仅对当前类实例起作用，
# 对继承的子类是不起作用的
