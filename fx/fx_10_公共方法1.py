# 公共方法、顾名思义、容器共有的方法
str1 = 'namez'
list1 = [1, 2, 3]
tuple1 = (4, 5, 6)
set1 = {7, 8, 9}
dict1 = {'name': 'circle', 'age': 19}
# 1、运算符 +   *   in      not in
str2 = ' circle'
str3 = str1 + str2
print(str3)


# 2、公共方法len()、del或del()、max()、min()、range(start,end,step)、enumerate()
# len()
print(len(str1))
print(len(list1))
print(len(set1))
print(len(tuple1))
print(len(dict1))
# del()或del()
# del str1[1]
# del list1[1]
# del tuple1[1]
# del set1[1]
# del dict1[1]

# max()
print(max(str1), end= '\t')
print(max(list1), end= '\t')
print(max(tuple1), end= '\t')
print(max(set1), end= '\t')
print(max(dict1))

# min()
print(min(str1), end= '\t')
print(min(list1), end= '\t')
print(min(tuple1), end= '\t')
print(min(set1), end= '\t')
print(min(dict1))

# range(start,end,step)
for i in range(2,0):
    print(i)

# enumerate()
for i, j in enumerate(str1):
    print(f'下标为{i}的数据为{j}')

# 3、容器类型转换list、set、tuple
list2 = list(str1)
print(list2)
set2 = set(str1)
print(set2)
tuple2 = tuple(str1)
print(tuple2)