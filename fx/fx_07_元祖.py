# 元祖：可以存储多个数据，不可修改
# 定义：小括号，数据后加逗号
# 若只有一个数据时，数据后应加逗号，否则电脑会认为这不是元祖
tuple1 = (1, 'a', False, ['hello', 1, True, 1])
# index:查找某个数据，若存在则返回下标，不存在则报错
print(tuple1.index(1,0,2))
# count：查找数据出现次数
print(tuple1.count(0))
# len()统计元祖中数据个数
print(len(tuple1))

# 元祖内数列可以修改数据
print(tuple1)
tuple1[3][1] = '呵呵'
print(tuple1)