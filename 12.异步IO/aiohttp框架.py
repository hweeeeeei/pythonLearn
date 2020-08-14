# aiohttp则是基于asyncio实现的HTTP框架

# from urllib import request
import asyncio
from aiohttp import web


# 编写一个HTTP服务器，分别处理以下URL：
#
# / - 首页返回b'<h1>Index</h1>'；
#
# /hello/{name} - 根据URL参数返回文本hello, %s!。

async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>')


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('get', '/', index)

    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    print('Server started at http://127.0.0.1:8000...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
