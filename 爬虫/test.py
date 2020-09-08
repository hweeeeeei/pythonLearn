from html.parser import HTMLParser
# 导入MySQL驱动:
import mysql.connector

from googletrans import Translator

# 创建连接
conn = mysql.connector.connect(user='root', password='123', database='vike', host='127.0.0.1')


class TypeParser(HTMLParser):
    def __init__(self):
        super(TypeParser, self).__init__()
        self.__parsedata = ''  # 设置一个空的标志位
        self.__pid2 = 0
        self.__pid3 = 0

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

        if self.__parsedata == '1':
            self.__pid2 = 0

    def handle_data(self, data):
        if data.strip() != '':
            if self.__parsedata == '1':
                print("1:", data)  # 通过标志位判断，输出打印标签内容

                conn = mysql.connector.connect(user='root', password='123', database='vike', host='127.0.0.1')
                # 打开游标Cursor，执行SQL语句
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO `vike`.`vk_task_type`(pid, `level`, `type_name_ch`) VALUES(0,1,'%s')" % data)
                pid = cursor.lastrowid
                self.__pid2 = pid
                conn.commit()
            if self.__parsedata == '2':
                print("2:", data)  # 通过标志位判断，输出打印标签内容

                conn = mysql.connector.connect(user='root', password='123', database='vike', host='127.0.0.1')
                # 打开游标Cursor，执行SQL语句
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO `vike`.`vk_task_type`(pid, `level`, `type_name_ch`) VALUES('%s',2,'%s')" % (
                        self.__pid2, data))
                pid = cursor.lastrowid
                self.__pid3 = pid
                conn.commit()

            if self.__parsedata == '33':
                print("3:", data)  # 通过标志位判断，输出打印标签内容
                conn = mysql.connector.connect(user='root', password='123', database='vike', host='127.0.0.1')
                # 打开游标Cursor，执行SQL语句
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO `vike`.`vk_task_type`(pid, `level`, `type_name_ch`) VALUES('%s',3,'%s')" % (
                        self.__pid3, data))
                pid = cursor.lastrowid
                #
                # runTrEn(pid,data)
                # runTrKm(pid,data)

                conn.commit()


if __name__ == '__main__':
    parse = TypeParser()
    try:
        f = open('/Users/giaogiao/Documents/hewei/code/pythonLearn/爬虫/type2.html', 'r')
        parse.feed(f.read())
    finally:
        if f:
            f.close()


def runTrEn(id, data):
    translator = Translator()
    translate = translator.translate(data, src='zh-cn', dest='en')
    en = translate.text

    conn = mysql.connector.connect(user='root', password='123', database='vike', host='127.0.0.1')
    # 打开游标Cursor，执行SQL语句
    cursor = conn.cursor()
    cursor.execute(" UPDATE    `vike`.`vk_task_type`  SET  `type_name_en` = '%s'  WHERE  `id` = '%s'" % (id, en))
    conn.commit()


def runTrKm(id, data):
    translator = Translator()
    translate = translator.translate(data, src='zh-cn', dest='km')
    km = translate.text

    conn = mysql.connector.connect(user='root', password='123', database='vike', host='127.0.0.1')
    # 打开游标Cursor，执行SQL语句
    cursor = conn.cursor()
    cursor.execute(" UPDATE    `vike`.`vk_task_type`  SET  `type_name_kh` = '%s'  WHERE  `id` = '%s'" % (id, km))
    conn.commit()
