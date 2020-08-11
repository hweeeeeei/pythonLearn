# chardet检测编码 第三方库,

import chardet

# 检测编码
print(chardet.detect(b'Hello, world!'))
# {'encoding': 'ascii', 'confidence': 1.0, 'language': ''}
# confidence字段，表示检测的概率是1.0（即100%）。

# 检测GBK编码的中文：
data = '离离原上草，一岁一枯荣'.encode('gbk')
print(chardet.detect(data))

# UTF-8编码
data = '离离原上草，一岁一枯荣'.encode('utf-8')
print('UTF-8编码', chardet.detect(data))

# 日文检测
data = '最新の主要ニュース'.encode('euc-jp')
print('日文进行检测', chardet.detect(data))
