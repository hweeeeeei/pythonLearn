# 内置的urllib模块缺少很多实用的高级功能

# requests第三方库，处理URL资源特别方便。

# GET页面
import requests

import ssl

# mac系统需要设置ssl上下文, 不然会报错
ssl._create_default_https_context = ssl._create_unverified_context

# 豆瓣首页
r = requests.get('https://www.baidu.com/')

print(r.status_code)
print(r.text)
print(r.encoding)

# content属性获得bytes对象
print('r.content', r.content)

# 带参数的URL,dict作为params参数
r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
print(r.url)

print(r.encoding)

# 响应JSON，可以直接获取：
r = requests.get('https://api.apiopen.top/getJoke?page=1&count=2&type=video')
print('r.json()', r.json())

# 传入HTTP Header时,dict作为参数
r = requests.get('https://www.douban.com/',
                 headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
print('r.text', r.text)

# POST请求,data参数作为请求数据
r = requests.post('https://accounts.douban.com/login', data={'email': '12456@qq.com'})
print('POST请求', r)

# 传递JSON数据
params = {'key': 'value'}
r = requests.post('https://accounts.douban.com/login', json=params)  # 内部自动序列化为JSON
print(r.request)

url = 'https://accounts.douban.com/login'
# 上传文件
# upload_files = {'file': open('report.xls', 'rb')}  # 'rb'即二进制模式读取
# r = requests.post(url, files=upload_files)

# 获取指定的Cookie
# print('cookies',r.cookies['ts'])

# 传入Cookie
cs = {'token': '12345', 'status': 'working'}
r = requests.get(url, cookies=cs)

# 指定超时
url = 'https://www.baidu.com/login'

r = requests.get(url, timeout=2.5)  # 2.5秒后超时
print("time out", r.headers)
