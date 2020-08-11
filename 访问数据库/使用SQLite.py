# SQLite是一种嵌入式数据库 它的数据库就是一个文件

# Python就内置了SQLite3


# 导入SQLite驱动:
import sqlite3

# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
conn = sqlite3.connect('test.db')

# 打开游标，称之为Cursor，通过Cursor执行SQL语句

cursor = conn.cursor()

# 执行一条SQL语句，创建user表:
cursor.execute('drop table user ')  # 防止重复 先删除
cursor.execute('create table user (id varchar(20) primary key ,name varchar (20))')

# 继续执行一条SQL语句，插入一条记录:
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')

# 通过rowcount获得插入的行数:
print('cursor.rowcount', cursor.rowcount)

# 关闭Cursor:
cursor.close()

# 提交事务:
conn.commit()

# 关闭Connection:
conn.close()

# ------查询记录
conn = sqlite3.connect('test.db')

cursor = conn.cursor()
# 执行查询语句:
cursor.execute('select * from user where id=?', ('1',))

# fetchall获得查询结果集:
values = cursor.fetchall()

print(values)
