class Animal(object):
    def run(self):
        print('animal run..')


class Cat(Animal):
    def run1(self):
        pass


class Dog(Animal):
    def run(self):
        print('dog run..')


Animal().run()
Dog().run()
Cat().run()


def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Dog())
run_twice(Cat())
run_twice(Animal())


# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。
# 我们只需要保证传入的对象有一个run()方法就可以了：
class Timer(object):
    def run(self):
        print("Timer run..")


run_twice(Timer())

# 继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。
#
# 动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。
