# 使用模板，我们需要预先准备一个HTML文档，这个HTML文档不是普通的HTML，
# 嵌入变量和指令,根据传入的数据，替换后，得到最终的HTML，响应给用户：


from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    # 响应html
    return render_template('home.html')


@app.route('/signin', methods=['get'])
def signin_from():
    return render_template('form.html')


@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']

    if username == 'admin' and password == 'pwd':
        return render_template('signin-ok.html', username=username)

    return render_template('form.html', message='Bad user or pwd')


# 一定要把模板放到正确的templates目录下
if __name__ == '__main__':
    app.run()

# MVC，我们就分离了Python代码和HTML代码。HTML代码全部放到模板里，写起来更有效率。

# 除了Jinja2，常见的模板还有：
#
# Mako：用<% ... %>和${xxx}的一个模板；
#
# Cheetah：也是用<% ... %>和${xxx}的一个模板；
#
# Django：Django是一站式框架，内置一个用{% ... %}和{{ xxx }}的模板。
