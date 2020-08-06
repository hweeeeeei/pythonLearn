# 内部属性不被外部访问，可以把属性的名称前加上两个下划线__
# 私有变量以__开头

class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def priSelf(self):
        print('priSelf', self.__name, self.__score)

    # 外部代码要获取name和score怎么办增加get_name和get_score方法：
    def get_name(self):
        return self.__name

    # 允许外部代码修改score 可以\增加set_score方法
    def set_name(self, name):
        self.__name = name


st1 = Student("hhhh", 98)

# 外部访问实例变量.__name和实例变量.__score了：
# st1.__name 报错

#  可以通过方法访问
st1.priSelf()

# 通过get方法 获取私有变量
st1_name = st1.get_name()
print('st1_name = st1.get_name()', st1_name)

# 修改内部name属性
st1.set_name("修改名称  奥利给")

st1_name = st1.get_name()
print('修改后st1_name:', st1_name)

print('-------')


# 请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：
class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender


# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
