# 通过多重继承，一个子类就可以同时获得多个父类的所有功能。


# 动物
class Animal(object):
    pass


# 大类:
# 哺乳
class Mammal(Animal):
    pass


# 鸟类
class Bird(Animal):
    pass


# 各种动物:
class Dog(Mammal):
    pass


class Bat(Mammal):
    pass


# 鹦鹉
class Parrot(Bird):
    pass


# 鸵鸟
class Ostrich(Bird):
    pass


# 跑的功能
class Runnable(object):
    def run(self):
        print('Running...')


# 飞的功能
class Flyable(object):
    def fly(self):
        print('Flying...')


# 对于需要Runnable功能的动物，就多继承一个Runnable，例如Dog：
class Dog(Mammal, Runnable):
    pass


# 对于需要Flyable功能的动物，就多继承一个Flyable，例如Bat：
class Bat(Mammal, Flyable):
    pass

# 由于Python允许使用多重继承，因此，MixIn就是一种常见的设计。
#
# 只允许单一继承的语言（如Java）不能使用MixIn的设计。
