# 推导式
# 作用：用一个表达式创建一个有规律的列表或控制一个有规律的列表，列表推导式又叫列表生成式
# 列表推导式
list1 = []
for i in range(10):
    list1.append(i)
print(list1)
i = 0
while i < 10:
    list1.append(i)
    i += 1
print(list1)
list2 = [i for i in range(0, 10, 2)]
print(list2)

list3 = [(i, j) for i in range(3) for j in range(11, 13)]
print(list3)

# 字典推导式
list4 = ['name', 'age', 'teacher']
list5 = ['Jim', 22, 'yezi']
dict1 = {list4[i]: list5[i] for i in range(len(list4))}
print(dict1)

# 集合推导式
set2 = {i for i in range(1, 10)}
print(set2)

set3 = {(i, j) for i in list5 for j in list4}
print(set3)