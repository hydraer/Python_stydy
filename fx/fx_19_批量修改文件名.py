# 批量修改文件名
import os
flag = 2
dir_name = './'
dir_list = os.listdir()
print(dir_list)
for name in dir_list:
    if flag == 1:
        new_name = 'python_' + name
    elif flag == 2:
        num = len('python_')
        new_name = name[num:]
    os.rename(name, new_name)