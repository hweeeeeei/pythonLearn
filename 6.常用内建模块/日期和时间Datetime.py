# datetime是Python处理日期和时间的标准库。

# 获取当前日期和时间

from datetime import datetime

# 获取当前datetime
now = datetime.now()
print(now)

# 获取指定日期和时间

dt = datetime(2015, 4, 19, 12, 20)  # 用指定日期时间创建datetime
print(dt)

# datetime转换为timestamp
# 在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，
# 记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp。
# timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00

# 对应的北京时间是：
# timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00

# 可见timestamp的值与时区毫无关系，因为timestamp一旦确定，其UTC时间就确定了，转换到任意时区的时间也是完全确定的，
# 这就是为什么计算机存储的当前时间是以timestamp表示的，因为全球各地的计算机在任意时刻的timestamp都是完全相同的（假定时间已校准）。


# datetime类型转换为timestamp只需要简单调用timestamp()
dt = datetime(2015, 4, 19, 12, 20)  # 用指定日期时间创建datetime
print('dt.timestamp()', dt.timestamp())

# timestamp转换为datetime

ts = 1429420800.0

print(datetime.fromtimestamp(ts))

# timestamp也可以直接被转换到UTC标准时区的时间：
t = 1429417200.0
print(datetime.fromtimestamp(t))  # 本地时间

# 转UTC时间
print('utc:', datetime.utcfromtimestamp(t))

# str转换为datetime
# datetime.strptime()
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print('cday', cday)

# datetime转换为str
now = datetime.now()
print('datetime转换为str', now.strftime('%a, %b %d %H:%M'))
print('datetime转换为str', now.strftime('%Y-%m-%d %H:%M:%S'))

# datetime加减
# datetime往后或往前计算，得到新的datetime。加减可以直接用+ - ,导入timedelta
from datetime import timedelta

now = datetime.now()

print('now', now)

nowto10h = now + timedelta(hours=10)
print('now + 10h', nowto10h)

nowsub10h = now + timedelta(hours=-10)
print('now - 10h', nowsub10h)

print(now + timedelta(days=2, hours=25))

# 本地时间转换为UTC时间
# 本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间。

# 一个datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区，
# 除非强行给datetime设置一个时区：
from datetime import datetime, timedelta, timezone

# 创建时区UTC+8:00
tz_utc_8 = timezone(timedelta(hours=8))

now = datetime.now()
print('now', now)

# 强制设置为UTC+8:00
dt = now.replace(tzinfo=tz_utc_8)

print('强制设置为UTC+8:00', dt)

# 时区转换
# 我们可以先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间：
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print('utc_dt', utc_dt)

# astimezone()将转换时区为北京时间:
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('bj_dt', bj_dt)

# astimezone()将bj_dt转换时区为东京时间:
totyo_dt = bj_dt.astimezone(timezone(timedelta(hours=9)))
print('totyo_dt', totyo_dt)

# 注：不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换，例如上述bj_dt到tokyo_dt的转换。


# 练习
# 假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，
# 均是str，请编写一个函数将其转换为timestamp：
import re
from datetime import timezone, timedelta, datetime


def to_timestamp(dt_str, tz_str):
    # 格式化日期时间
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')

    # 格式化传入时区
    dz = int(tz_str[3:-3])

    # 创建时区
    dz_tf = timezone(timedelta(hours=dz))

    # 修改时间的时区
    my_dt = dt.replace(tzinfo=dz_tf)

    # 转换为timestamp
    timestamp = my_dt.timestamp()
    print('my_dt.timestamp()', timestamp)

    return timestamp


# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')
