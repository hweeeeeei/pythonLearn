# list
list2 = ['t1', 't2', 't3']
print(list2[2])

# 长度
print('size', len(list2))

# 追加
list2.append('t4')
print('追加后：', list2)

# 插入
list2.insert(2, 'insert to 2')
print('插入后：', list2)

# pop 删除末尾
list2.pop()
print('pop 删除末尾', list2)

# 删除指定下标
list2.pop(2)
print('删除指定下标=2', list2)

# 指定替换
list2[0] = 'replace'
print('指定替换下标=0', list2)

print('________')

# 数组包含数组
list3 = ['a0', [1, 'sfa']]
print("list3", list3)

# 包含不同类型
list4_a = ['g1', 'g2', 33.11]
list4 = ['a1', list4_a, True, 2.212]

print("list4", list4)

# 拿到'g2'
print('拿到"g2"', list4[1][1])
