import socket
import time
import threading

# 基于UDP的Socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 不需要调用connect()，直接通过sendto()给服务器发数据：
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.sendto(data, ('127.0.0.1', 9999))
    # 接收数据:
    print(s.recv(1024).decode('utf-8'))

s.close()
