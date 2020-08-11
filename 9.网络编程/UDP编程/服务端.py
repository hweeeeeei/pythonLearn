# UDP则是面向无连接的协议。
#
# 用UDP传输数据不可靠

# 优点是和TCP比，速度快

import socket

# SOCK_DGRAM指定了这个Socket的类型是UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口:
# 不需要调用listen()方法，而是直接接收来自任何客户端的数据：
s.bind(('127.0.0.1', 9999))

print('Bind UDP on 9999...')
while True:
    # 接收数据:

    # recvfrom()方法返回数据和客户端的地址与端口
    data, addr = s.recvfrom(1024)

    print('Received from %s:%s.' % addr)

    # 调用sendto() 把数据用UDP发给客户端
    s.sendto(b'Hello, %s!' % data, addr)
