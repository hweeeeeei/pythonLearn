# 读文件

# Python内置的open()函数

f = open('/Users/giaogiao/.ssh/gpc-aillo', 'r')

# 读取文件
print(f.read())

# close()方法关闭文件。文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源
f.close()

# 文件读写时都有可能产生IOError，后面的f.close()就不会调用
# try:
#     f = open('错误路径', 'r')
#     print(f.read())
# finally:
#     f.close()

# 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：
with open('/Users/giaogiao/.ssh/gpc-aillo', 'r') as f:
    f.read()
# 这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。

# 文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法


# 如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：

f = open('/Users/giaogiao/.ssh/gpc-aillo', 'r')
for line in f.readlines():
    print(line.strip())  # 把末尾的'\n'删掉

print('---------------------------------------------')
