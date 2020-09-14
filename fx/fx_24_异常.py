# # 异常
# try:
#     print(num)
# except(NameError, ZeroDivisionError):
#     print('有指定性错误')
# except(NameError, ZeroDivisionError) as result:
#     print(result)
# except Exception as result:
#     print('不知道什么错误反正有错误')
#     print(f'错误内容{result}')
# except:
#     print('不知道什么错误反正有错误')
# else:
#     print('没有错误')
# finally:
#     print('不管有没有错误，我都得执行啊')

# 读取文件捕获异常
import time
try:
    f = open('a/a.txt')
    while True:
        content = f.readline()
        if len(content) == 0:
            break
        time.sleep(2)
        print(content)
except:
    print('意外退出')
finally:
    print('关闭文件')
    f.close()


# 自定义异常
class ShotInputError(Exception):
    def __init__(self, lenth, short_lenth):
        self.lenth = lenth
        self.short_lenth = short_lenth
    def __str__(self):
        return f'最小密码长度为{self.short_lenth},您输入密码长度为{self.lenth}'

def main():
    try:
        con = input('请输入密码')
        if len(con) < 3:
            raise ShotInputError(len(con), 3)
    except Exception as result:
        print(result)
    else:
        print('密码输入符合要求')

main()