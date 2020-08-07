# Hmac算法 计算哈希的过程中，把key混入计算过程中。
# Hmac算法针对所有哈希算法都通用
# MD5还是SHA-1。采用Hmac替代我们自己的salt算法，可以使程序算法更标准化，也更安全。

# 准备待计算的原始消息message，随机key，哈希算法，这里采用MD5

import hmac

# 需要传入bytes类型
message = b'Hello, World..!'
key = b'secret'

h = hmac.new(key, message, digestmod='MD5')
# 如果消息很长，可以多次调用h.update(msg)
print('h.hexdigest()', h.hexdigest())

# 练习------------------
# 将上一节的salt改为标准的hmac算法，验证用户口令：

import hmac, random


def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()


class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac_md5(self.key, password)


db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}


def login(username, password):
    user = db[username]
    return user.password == hmac_md5(user.key, password)


# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')
