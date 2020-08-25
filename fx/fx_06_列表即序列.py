# 列表可一次性存储多个有序数据，且可为不同数据类型

list1 = ['hello', '1', 2, True, 2]

# 一、查找
# 返回指定数据的下标
print(list1.index(True))
# 统计指定数据在序列中出现的次数
print(list1.count(2))
# 统计列表长度，即列表中数据个数
print(len(list1))
# 判断数据是否在列表里
print('hello' not in list1)
# 二、增加
# 1、append、列表后面添加数据，若添加的数据为列表时，则列表作为元素添加进列表
list1.append('123')
print(list1)
list2 = ['hello', '1', 2, True, 2]
list1.append(list2)
# 当输出列表中元素为列表显示为省略号时，表示有循环或者引用了自己
print(list1)
# 2、extend、往列表结尾追加数据，若追加的数据为列表时，则将列表内元素依次添加进列表
list1.extend(list2)
print(list1)
# 3、insert，在指定下标处添加数据，若添加的为列表，则列表作为元素添加
list2.insert(1,[1, 2])
print(list2)

# 三、修改
# 1、修改指定下标的数据
list1[5] = 5
print(list1[5])
# 2、逆置
list1.reverse()
print(list1)
# 3、排序
list3 = [1, 2, 4, 3]
list3.sort()
print(list3)


# 五、复制
list4 = list3.copy()
list5 = list3
print(list5)
print(list4)
list3.clear()
print(id(list5))
print(id(list4))
print(list3 == list4)


# 四、删除
# 1、del：删除数列、删除数列内元素
del list1
print(list2)
del list2[1]
print(list2)
# 2、pop删除下标数据，并返回该数据，默认末尾
print(list2.pop())
print(list2)
list2.append(2)
list2.extend('True')
print(list2)
# 3、remove删除第一个匹配的数据
list2.remove(2)
print(list2)