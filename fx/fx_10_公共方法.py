# 相对于字符串、序列、元祖、集合、列表、字典
# 运算符
# + *
# 元祖可行
s1 = (1, 2, 3)
s2 = (4, 5, 6)
s3 = s1 + s2
print(s3)
# 字符串可行
s1 = 'name'
# s2 = {'age': 19}
# s3 = s1 + s2
print(s3)
# 列表
s1 = [1, 2, 3]
s2 = [1, 2, 4]
s3 = s1 + s2
print(s3)
# 集合、字典、不可行，原因无序无下标
s3 = s1*1
print(s3)
# in 和 not in
s1 = [1, 2, 3]
print(1 in s1)

s1 = {'name': 'Tom', 'age': 19}
# print({'age': 'Tom'} in s1)

str1 = 'name'
list1 = [1, 2, 3]
tuple1 = (1, 2, 3)
set1 = {1, 2, 3}
dict1 = {'name': 'Jim', 'age': 10}

# 公共方法len()
print(len(str1))
print(len(list1))
print(len(tuple1))
print(len(set1))
print(len(dict1))
# 公共方法del()
print(str1[1])
del(str1[1])
print(str1)