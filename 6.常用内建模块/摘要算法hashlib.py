# hashlib提供了常见的摘要算法，如MD5，SHA1等等。

# 什么是摘要算法呢？摘要算法又称哈希算法、散列算法。它通过一个函数，
# 把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。


import hashlib

# md5 128 bit字节，通常用一个32位的16进制字符串表示。
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print('md5', md5.hexdigest())

# 数据量很大，可以分块多次调用update()
md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print('md5分块', md5.hexdigest())

# SHA1的结果是160 bit字节 ,40位
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print('sha1', sha1.hexdigest())


# 比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长。


# 两个不同的数据通过某个摘要算法得到了相同的摘要 这种情况称为碰撞


# 摘要算法应用

# 练习
# 根据用户输入的口令，计算出存储在数据库中的MD5口令：
def calc_md5(password):
    pass


# 设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False：
def login(user, password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    pwd = md5.hexdigest()

    print(pwd, 'pwd')
    if pwd == db[user]:
        return True
    else:
        return False


# 存储MD5的好处是即使运维人员能访问数据库，也无法获知用户的明文口令。
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

print(' Salt ------------')


# 根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5：
def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')


# 然后，根据修改后的MD5算法实现用户登录的验证：
import hashlib, random


def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)


db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}


def login(username, password):
    user = db[username]

    return user.password == get_md5(password + user.salt)


# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')
