# Python的标准库提供了两个模块：_thread和threading
# _thread是低级模块，threading是高级模块，对_thread进行了封装。
# 绝大多数情况下，我们使用threading高级模块。


# 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：

import time, threading


def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


# current_thread()函数，它永远返回当前线程的实例
print('thread %s is running...' % threading.current_thread().name)

# name='' 可以命名子线程
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

# Lock
# 多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，
# 而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，
# 因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。
#
# 来看看多个线程同时操作一个变量怎么把内容给改乱了：
import time, threading

# 假定这是你的银行存款:
balance = 0


def change_it(n):
    # 先存后取，结果应该为0:
    global balance

    # 计算balance + n，存入临时变量中；
    # 将临时变量的值赋给balance。
    balance = balance + n

    balance = balance - n


# 运行很多次
def run_thread(n):
    for i in range(2000000):
        change_it(n)


# 开启两个线程进型存取款操作
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))

t1.start()
t2.start()

t1.join()
t2.join()

print('balance :', balance)

# 我们定义了一个共享变量balance，初始值为0，并且启动两个线程，先存后取，理论上结果应该为0，
# 但是，由于线程的调度是由操作系统决定的，当t1、t2交替执行时，只要循环次数足够多，balance的结果就不一定是0了。


# 要确保balance计算正确，就要给change_it()上一把锁


balance = 0
lock = threading.Lock()


def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()


# 当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止。

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))

t1.start()
t2.start()

t1.join()
t2.join()

print('balance lock :', balance)
