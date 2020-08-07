# collections是Python内建的一个集合模块，提供了许多有用的集合类。

# namedtuple
# 我们知道tuple可以表示不变集合，例如，一个点的二维坐标就可以表示成：

p = (1, 2)

# 定义一个class又小题大做了，这时，namedtuple就派上了用场：


from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

p = Point(1, 2)

print(p.x)
print(p.y)

# 坐标和半径表示一个圆，也可以用namedtuple定义：
# namedtuple('名称', [属性list]):

Circle = namedtuple('Circle', ['x', 'y', 'r'])

c = Circle(22, 33, 55)

print(c)
print(c.r)

# deque 双向列表
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：

from collections import deque

q = deque(['a', 'b', 'c'])
q.append('d')
q.appendleft('z')

print('q', q)

# 实现list的append()和pop()外，还支持appendleft()和popleft()

q.popleft()

print('q.popleft()', q)

# defaultdict key不存在时，返回一个默认值
from collections import defaultdict

dd = defaultdict(lambda: 'N/A')

dd['a1'] = 'nihao'

# 存在
print(dd['a1'])

# 不存在
print(dd['a1241'])

# OrderedDict 保持Key的顺序
from collections import OrderedDict

d = dict([('a', 1), ('b', 2), ('c', 3)])

print('无序', d)

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

print('有序', od)


# OrderedDict可以实现一个FIFO（先进先出）
class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    # 当容量超出限制时，先删除最早添加的Key
    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


# ChainMap
# ChainMap可以把一组dict串起来并组成一个逻辑上的dict
from collections import ChainMap
import os, argparse

# 构造缺省参数:
defaults = {
    'color': 'red',
    'user': 'guest'
}

# 构造命令行参数:
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = {k: v for k, v in vars(namespace).items() if v}

# 组合成ChainMap:
combined = ChainMap(command_line_args, os.environ, defaults)

# 打印参数:
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])

# Counter
# Counter是一个简单的计数器，例如，统计字符出现的个数：
from collections import Counter

c = Counter()

for ch in 'programming':
    c[ch] = c[ch] + 1

print('c', c)

c.update('hello')  # 也可以一次性update

print('c', c)
