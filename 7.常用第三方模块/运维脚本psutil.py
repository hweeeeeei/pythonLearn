# 实现系统监控，还可以跨平台使用，支持Linux／UNIX／OSX／Windows
import psutil

# 获取CPU信息

print(psutil.cpu_count())  # CPU逻辑数量

print(psutil.cpu_count(logical=False))  # CPU物理核心

# 统计CPU的用户／系统／空闲时间：
print(psutil.cpu_times())

# 每秒刷新一次，累计10次：
for i in range(1):
    # for i in range(10):
    print(psutil.cpu_percent(interval=1, percpu=True))

# 获取内存信息

# 物理内存
print('物理内存', psutil.virtual_memory())

# 交换内存
print('交换内存', psutil.swap_memory())

# 获取磁盘信息
print(psutil.disk_partitions())  # 磁盘分区信息

print(psutil.disk_usage('/'))  # 磁盘使用情况

print(psutil.disk_io_counters())  # 磁盘IO

# 获取网络信息

print('网络读写字节／包的个数', psutil.net_io_counters())  # 获取网络读写字节／包的个数)

# 获取进程信息

print(psutil.pids())  # 所有进程ID
