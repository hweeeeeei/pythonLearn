# 导入MySQL驱动:
import mysql.connector

# 创建连接
conn = mysql.connector.connect(user='root', password='123', database='im', host='127.0.0.1')

# 打开游标Cursor，执行SQL语句
cursor = conn.cursor()

# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

# 插入一行记录，注意MySQL的占位符是%s:
# for i in range(10,40):
cursor.execute('insert into user (id, name) values (%s, %s)', ['93', 'Michael'])
print(cursor.rowcount)
# 最后插入行的主键ID
print('ID of last record is ', int(cursor.lastrowid))

# 提交事务:
commit = conn.commit()
conn.close()
#
# # 运行查询:
# cursor = conn.cursor()
# # 创建连接
# conn = mysql.connector.connect(user='root', password='123', database='im', host='127.0.0.1')
# cursor.execute('select * from user where id = %s', ('890',))
# values = cursor.fetchall()
#
# print('values', values)
#
# # 关闭Cursor和Connection:
# cursor.close()
# conn.close()
