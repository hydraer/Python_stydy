# 1、带判断的lambda表达式
fn1 = lambda a, b : a if a > b else b
print(fn1(1, 100))

# 2、列表参数按字典key的值排序
students = [{'name': 'Lilei', 'age': 22},
            {'name': 'Jim', 'age': 23}]

# def sort_dic(x):
#     return x['age']

a = lambda students: students['name']

print(a)