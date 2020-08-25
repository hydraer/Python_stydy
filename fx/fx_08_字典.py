# 字典
# 字典以键值对存储，与顺序无关，不支持下标，{}定义
circle = {'name': 'xiaoyuanquan', 'gender': 'boy', 'age': '0', 'mother': 'ning', 'father': 'kun'}
# 增
circle['grandmather'] = 'peng'
print(circle)
# 删
del circle['grandmather']
circle['father']
print(circle)
# 改
circle['father'] = 'me'
print(circle)
# 查
print(circle['name'])
print(circle.get('age', 1))
print(circle.keys())
print(circle.values())
print(circle.items())
# 字典遍历：key、value、item、键值对
# key
for key in circle.keys():
    print(key, end='\t')
print()
# value
for value in circle.values():
    print(value, end='\t')
print()
# item 遍历字典的元素
for item in circle.items():
    print(item, end= '\t')
print()
# 键值对
for a, n in circle.items():
    print(f'{a} = {n}')