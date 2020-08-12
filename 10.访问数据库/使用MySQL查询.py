# 导入MySQL驱动:
import mysql.connector

# 创建连接
conn = mysql.connector.connect(user='root', password='123', database='im', host='127.0.0.1')

# 打开游标Cursor，执行SQL语句
cursor = conn.cursor()

cursor.execute('select * from user where id = %s', ('2',))
values = cursor.fetchall()

print('values', values)

# 关闭Cursor和Connection:
cursor.close()
conn.close()
