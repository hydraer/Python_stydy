# 文件操作
import os

f = open('a/a.txt', 'w')
f.write('helloworld')
f = open('a/a.txt', 'r')

print(f.read())

# 文件备份
old_name = input('请输入您要备份的文件')
if
old_index = old_name.rindex('.')
print(old_index)
print(old_name[:old_index])
print(old_name[old_index:])
new_name = old_name[:old_index] + '[备份]' + old_name[old_index:]
old_f = open(old_name, 'r')
new_f = open(new_name, 'w')
while True:
    con = old_f.read(1024)
    if len(con) == 0:
        break
    new_f.write(con)
old_f.close()
new_f.close()