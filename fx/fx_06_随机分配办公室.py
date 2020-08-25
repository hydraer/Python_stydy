# 八位老师随机分配到三个办公室
import random

teachers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
offices = [[], [], []]
offices1 = [[], [], []]
for i in teachers:
    offices[random.randint(0, 2)].extend(i)
    # print(type())
print(offices)
i = 0
while i < len(teachers):
    offices1[random.randint(0, 2)].extend(teachers[i])
    i += 1
print(offices1)