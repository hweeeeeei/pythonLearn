# 用asyncio提供的@asyncio.coroutine可以把一个generator标记为coroutine类型，然后在coroutine内部用yield from调用另一个coroutine实现异步操作。

import asyncio


# 替换：
#
# 把@asyncio.coroutine替换为async；
# 把yield from替换为await。


async def hello():
    print('Hello world')
    r = await asyncio.sleep(1)
    print("Hello again!")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(hello())
    loop.close()
