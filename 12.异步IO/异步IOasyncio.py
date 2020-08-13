# 要执行的协程扔到EventLoop中执行，就实现了异步IO。
import asyncio


# 标记为coroutine类型,就可以在EventLoop中执行
@asyncio.coroutine
def hello():
    print("Hello world!")

    # 异步调用asyncio.sleep(1):
    # asyncio.sleep(1)看成是一个耗时1秒的IO操
    r = yield from asyncio.sleep(1)  # yield from语法可以让我们方便地调用另一个generator

    print("Hello again!")


# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()
