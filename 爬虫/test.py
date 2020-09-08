from html.parser import HTMLParser
# 导入MySQL驱动:
import mysql.connector

# 创建连接
conn = mysql.connector.connect(user='root', password='123', database='vike', host='127.0.0.1')


class TypeParser(HTMLParser):
    def __init__(self):
        super(TypeParser, self).__init__()
        self.__parsedata = ''  # 设置一个空的标志位

    def handle_starttag(self, tag, attrs):
        if ('class', 'title') in attrs:
            self.__parsedata = '1'  # 通过属性判断如果该标签是我们要找的标签，设置标志位    def handle_starttag(self, tag, attrs):
        if ('class', 'leftincaty') in attrs:
            self.__parsedata = '2'
        if ('class', 'letilistcaty') in attrs:
            self.__parsedata = '3'
        if (self.__parsedata == '3') & (tag == 'a'):
            self.__parsedata = '33'
        if ('class', 'catynavlist_right') in attrs:
            self.__parsedata = '44'

    def handle_endtag(self, tag):
        if self.__parsedata != '33':
            self.__parsedata = ''  # 在HTML 标签结束时，把标志位清空

    def handle_data(self, data):
        if data.strip() != '':
            if self.__parsedata == '1':
                print("1:", data)  # 通过标志位判断，输出打印标签内容
            if self.__parsedata == '2':
                print("2:", data)  # 通过标志位判断，输出打印标签内容
            if self.__parsedata == '33':
                print("3:", data)  # 通过标志位判断，输出打印标签内容


if __name__ == '__main__':
    parse = TypeParser()
    try:
        f = open('/Users/giaogiao/Documents/hewei/code/pythonLearn/爬虫/type2.html', 'r')
        parse.feed(f.read())
    finally:
        if f:
            f.close()
