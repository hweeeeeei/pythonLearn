# ORM框架
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()


# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:123@localhost:3306/im')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()
# 创建新User对象:
new_user = User(id='9', name='Bob')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
# session.commit()
# 关闭session:
session.close()

# 查询
# 创建Session:
session = DBSession()
user = session.query(User).filter(User.id == '5').one()

# 打印类型和对象的name属性:
print('type:', type(user))
print('name:', user.name)

# 关闭Session:
session.close()
