str = 'hello world'
# 1、切片
str1 = str[0: 8 : 1]
print(str1)
# 2、查找
print(str.find('lo', 0, 11))
print(str.index('l', 0, 11))
print(str.count('H', 0, 11))
# 3、修改
# 替换
print(str.replace(' ', '_', 2))
# 分割
print(str.split(' ', 2))
# 合并
list1 = ['hello', 'word', 'and', 'python']
print(' '.join(list1))
# 首字母变大写
print(str.capitalize())
# 每个单词首字母大写转换
print(str.title())
# 所有字母转小写
str2 = 'HELLO WORLD'
print(str2.lower())
# 所有字母转大写
print(str.upper())
# 删除左侧空白
str3 = ' HeLlo WorlD '
print(str3.lstrip())
# 删除右侧空白
print(str3.rstrip())
# 删除两侧空白
print(str3.strip())
# 右侧对齐，左侧填充字符至数字数，默认空格
print(str3.rjust(22))
# 左侧对齐，右侧填充字符，默认空格
print(str3.ljust(22, 'l'))
# 两侧填充字符
print(str3.center(22, 'l'))
# 4、判断
# 是否以子字符串开始、结束
print(str3.startswith(' ', 1, 22))
print(str3.endswith(' ', 1, 22))
# 字符串至少有一个字符且所有字符均为字母返回True，否则False
str4 = 'abc'
print(str4.isalpha())
# 字符串只包含数字
str5 = '12 3'
print(str5.isdigit())
# 字符串不为空，且所有字符均为字母或数字
str6 = '1ac2'
print(str6.isalnum())
# 非空字符串均为空格返回true
str7 = ''
print(str7.isspace())
