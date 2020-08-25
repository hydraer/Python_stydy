# 1、重复打印5次媳妇我错了
# i = 0
# while i < 5:
#     print('媳妇我错了')
#     i += 1

# 2、计算1-100的和
# i = 1
# count = 0
# while i <= 100:
#     if i%2 == 0:
#         count = count + i
#     i += 1
# print(count)

# # 3、吃苹果、第三个吃饱了
# i = 1
# while i<= 5:
#     print('正在吃第%d个苹果'%i)
#     if i == 3:
#         print('吃饱了')
#         break
#     i += 1
# print('一共吃了%d个苹果'%i)

# 4、吃苹果，第四个有大虫子
# i = 1
# while i<= 5:
#     if i == 4:
#         print('这个有大虫子，不吃这个了')
#         i += 1
#         continue
#     print('正在吃第%d个苹果' % i)
#     i += 1
# print('一共吃了%d个苹果'%i)

# i = 1
# while i <= 3:
#     j = 1
#     while j <= 3:
#         print('媳妇我错了')
#         j += 1
#     print(f'第{i}天刷碗筷')
#     i += 1

# 6、打正方形
# i = 1
# while i <= 5:
#     j = 1
#     while j <= 5:
#         print('*', end = '')
#         j += 1
#     print()
#     i += 1

# 7、打三角形
# i = 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         print('*', end = '')
#         j += 1
#     print()
#     i += 1
# 8、打等腰三角形
# i = 1
# while i <= 5:
#     j = 1
#     while
# 9、九九乘法表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f'{j}*{i}={i*j}', end='\t')
        j += 1
    i += 1
    print()