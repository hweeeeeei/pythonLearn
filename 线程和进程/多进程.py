from multiprocessing import Process

# os模块封装了常见的系统调用
import os


# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())

    # 指定调用的函数, 并传入参数
    p = Process(target=run_proc, args=('test',))

    print('Child process will start.')

    # 启动
    p.start()

    # join()等待子进程结束后再往下运行，用于进程间的同步

    p.join()

    print('Child process end.')

# Pool
# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：

from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())

    # 设置最多同时执行4个进程
    p = Pool(4)

    # 启动5个进程,  第5个进程会等待前面4个进程执行完毕再执行
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))

    print('Waiting for all subprocesses done...')

    # 必须先调用close() , 调用close()之后就不能继续添加新的Process
    p.close()

    # 等待所有子进程执行完毕
    # p.join()
    print('All subprocesses done.')

# 子进程
# 很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。

# subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])

r = subprocess.call(['ping', 'www.python.org'])

print('Exit code:', r)

# ----
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)
