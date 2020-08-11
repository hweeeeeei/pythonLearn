# HTML本质上是XML的子集，但是HTML的语法没有XML那么严格，所以不能用标准的DOM或SAX来解析HTML。

from html.parser import HTMLParser
from html.entities import name2codepoint


# 继承HTMLParser
class MyHTMLParser(HTMLParser):

    # 标记开始
    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    # 标记结束
    def handle_endtag(self, tag):
        print('</%s>' % tag)

    # 开始 + 结束标签完成处理:
    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    # 换行
    def handle_data(self, data):
        print(data)

    # 处理注释
    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)


parser = MyHTMLParser()

parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')

# 练习
# 找一个网页，例如https://www.python.org/events/python-events/，用浏览器查看源码并复制，然后尝试解析一下HTML，输出Python官网发布的会议时间、名称和地点。

uri = 'https://www.python.org/events/python-events/'
