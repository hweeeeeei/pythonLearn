# 练习
# 找一个网页，例如https://www.python.org/events/python-events/，
# 尝试解析一下HTML，输出Python官网发布的会议时间、名称和地点。

# html解析模块
from html.parser import HTMLParser

# 请求模块
from urllib import request

import re

import ssl

# mac系统需要设置ssl上下文, 不然会报错
ssl._create_default_https_context = ssl._create_unverified_context


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super(MyHTMLParser, self).__init__()
        self.__parsedata = ''  # 设置一个空的标志位

    # 标签开始
    def handle_starttag(self, tag, attrs):
        if ('class', 'event-title') in attrs:
            self.__parsedata = 'name'  # 通过属性判断如果该标签是我们要找的标签，设置标志位
        if tag == 'time':
            self.__parsedata = 'time'
        if ('class', 'say-no-more') in attrs:
            self.__parsedata = 'year'
        if ('class', 'event-location') in attrs:
            self.__parsedata = 'location'

    # 标签结束
    def handle_endtag(self, tag):
        self.__parsedata = ''  # 在HTML 标签结束时，把标志位清空

    # 标签中的数据
    def handle_data(self, data):
        if self.__parsedata == 'name':
            print('会议名称:%s' % data)  # 通过标志位判断，输出打印标签内容

        if self.__parsedata == 'time':
            print('会议时间:%s' % data)

        if self.__parsedata == 'year':
            if re.match(r'\s\d{4}', data):  # 因为后面还有两组 say-no-more 后面的data却不是年份信息,所以用正则检测一下
                print('会议年份:%s' % data.strip())

        if self.__parsedata == 'location':
            print('会议地点:%s' % data)
            print('----------------------------------')


URL = 'https://www.python.org/events/python-events/'

parse = MyHTMLParser()

# 打开网页并取到数据
with request.urlopen(URL, timeout=15) as f:
    data = f.read()
    parse.feed(data.decode('utf-8'))
