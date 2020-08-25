# num = input('请输入：')
# print(type(num))
# num1 = int(num)
# print(type(num1))
# num2 = float(num)
# print(type(num2))
# list1 = [1, 2, 3, 400]
# print(list1)
# tuple1 = tuple(list1)
# print(tuple1)
# print(type(tuple1))

# t1 = (1, 2, 300)
# print(t1)
# print(type(t1))
# t2 = list(t1)
# print(t2)
# print(type(t2))

t1 = '10'
# 元祖
t2 = '(1,2,3)'
# 列表,可重复，有序
t3 = '[1,2,3]'
# 集合，不可重复，无序
t5 = '{1, 2, 3}'
# 字典
t6 = '{"a": 1, "b": 2}'

# print(type(eval(t1)))
# print(type(eval(t2)))
# print(type(eval(t3)))

t4 = int(t1, 16)
print(t4)
print(type(t4))

print(type(eval(t1)))
print(type(eval(t2)))
print(type(eval(t3)))
print(type(t4))
print(type(eval(t5)))
print(type(eval(t6)))