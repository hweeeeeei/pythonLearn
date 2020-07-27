names = ['giao', 'g2', 'g3', 'g4', 'g5']

for name in names:
    print(name)
    if name == 'g2':
        print('找到g2')

# range函数生成1-100的数字序列
list_a1 = list(range(101))
print("range list_a1", list_a1)

# 计算1加到100的和
sum_a = 0
for num in list_a1:
    sum_a = sum_a + num

print('sum_a', sum_a)

n = 1
while n <= 100:
    if n == 11:
        print("退出", n)
        break
    print('n', n)
    n = n + 1
