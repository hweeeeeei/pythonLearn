from flask import Flask
from flask import request

# 处理3个URL，分别是：
#
# GET /：首页，返回Home；
#
# GET /signin：登录页，显示登录表单；
#
# POST /signin：处理登录表单，显示登录结果。

app = Flask(__name__)


@app.route('/', methods=['get', 'POST'])
def home():
    return '<h1>Home<h1>'


@app.route('/signin', methods=['GET'])
def signin_from():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''


@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'


# Flask自带Server在端口5000上监听
if __name__ == '__main__':
    app.run()

# 除了Flask，常见的Python Web框架还有：
#
# Django：全能型Web框架；
#
# web.py：一个小巧的Web框架；
#
# Bottle：和Flask类似的Web框架；
#
# Tornado：Facebook的开源异步Web框架。
