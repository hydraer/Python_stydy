# 集合
# 无序、唯一、无下标，创建空集合必须set（）
set1 = {1, 2, 1, 'hello', True, '111'}
print(set1)
# 增add增加数据、update增加序列
set1.add(11)
print(set1)
set1.update({111, 222})
print(set1)
# 删
set1.remove('111')
print(set1)
set1.discard('111')
print(set1)
print(set1.pop())
print(set1)
# 改
# /
# 查
print(1 in set1)