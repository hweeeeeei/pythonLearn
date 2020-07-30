class 人物(object):

    def __init__(self, name, sex, slogan, *status):  # 创建属性

        self.name = name

        self.sex = sex

        self.status = status

        self.slogan = slogan

    def 简介(self):  # 创建实例属性的具体介绍

        print(self.name)

        print('%s的性别是:%s' % (self.name, self.sex))

        print('{0}的身份是:{1}'.format(self.name, self.status))

        print('%s的标语是:%s' % (self.name, self.slogan))


鲁迅 = 人物('周树人', '男', '你抓鲁迅关我周树人什么关系', '文学家', '思想家', '教育家等')

陈独秀 = 人物('陈乾生', '男', '陈独秀同志请你坐下', '新文化运动的发起者和倡导者', '中国共产党的创始人之一等')

鲁迅.简介()

print('.......................' * 6)

陈独秀.简介()

print('.......................' * 6)
