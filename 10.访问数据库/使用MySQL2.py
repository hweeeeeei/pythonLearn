import mysql.connector

conn = mysql.connector.connect(user='root', password='123', database='vike', host='127.0.0.1')

# 打开游标Cursor，执行SQL语句
cursor = conn.cursor()

cursor.execute("INSERT INTO `vike`.`vk_task_type_copy1`(`type_name_ch`) VALUES ('gg')")
print(cursor.lastrowid)
commit = conn.commit()

# # 创建连接
# conn = mysql.connector.connect(user='root', password='123', database='vike', host='127.0.0.1')
# # 打开游标Cursor，执行SQL语句
# cursor = conn.cursor()
# cursor.execute("INSERT INTO `vike`.`vk_task_type_copy1`(`type_name_ch`) VALUES (", data, "))")
# conn.commit()
