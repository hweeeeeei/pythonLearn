#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('hello world!')
print('一给哦里giao giao ')
print('加油 坚持就是胜利  奥利给')

# 我是一行可爱的小注释

a = 10
b = 20
if a < b:
    print('a小于b')
else:
    print('大于b')

# 浮点
c = 12.11
d = 0.11
print('c - d :', c - d)

# 字符占位符 格式化
str_a = '你好，%s， 欢迎来到 %s！' % ('啊giao', '我的python代码世界')
print(str_a)

str_b = '你好，%s， 欢迎来到 %s！'
str_c = str_b % ('啊giao22', '我的python代码世界2')
print(str_c)

# 浮点占位
str_1 = '余额为，%.2f'
print(str_1 % 2.123123)

# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
promote = (85 - 72) / 72 * 100
print('提升: %0.1f%%' % promote)
print('提升: %s%%' % promote)
