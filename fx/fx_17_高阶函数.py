# 1、abs：计算绝对值
import functools

print(abs(-10))

# 2、round()：四舍五入
print(round(2.1))
print(round(-3.2))

# 3、map():将传入的函数变量func作用到lst变量的每个元素中，并将结果组成新的列表（Python2）/迭代器（Python3）返回
list1 = [1, 2, 3, 4, 5]
def func(x):
    return x ** 2

list2 = [1, 1, 2, 3]
print(map(func, list1))
print(map(func, list2))
print(list(map(func, list1)))
print(list1)

# 4、reduce():累积计算
def func1(a, b):
    return a * b
print(functools.reduce(func1, list1))

# 5、filter()：过滤序列返回一个对象，可以用list转换为序列
list3 = [1, 2, 3, 4, 5, 6, 7, 8]
def func2(x):
    return x % 2 == 0
print(list(filter(func2, list3)))