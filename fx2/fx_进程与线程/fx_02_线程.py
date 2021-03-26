# 1、线程是实现多任务的另一种方式
# 2、线程是CPU调度的基本单位，每个进程至少有一个主线程
# 3、getpid是获取进程号，而非线程号
# 4、线程间可以共享全局变量,但会出现错误
# 5、设置线程守护：线程.setDaemon(True)
# 6、互斥锁所有需要的线程都需要添加，但是同一时刻锁之间的代码执行完，才可执行另一个锁内
# 7、互斥锁能保证同一时间只有一个线程去应用共享数据，避免数据错误
# 8、互斥锁降低效率，多任务变为单任务
# 9、互斥锁应用不当形成死锁（应在合适位置释放锁,如循环内，函数内等）

import threading
import time
import os

g_list = [100]

def sing(count):
    print('开始写入数据')
    for i in range(count):
        # time.sleep(1)
        g_list.append(i)
        print(i)

        # print('年年在唱歌')
        # print('唱歌：', os.getpid())
        # print('唱歌父线程：', os.getppid())

def dance(count):
    print('开始读取数据')
    for i in range(count):
        print(g_list[i])
        # g_list.append(2)
        # print('年年在跳舞')
        # print('跳舞:', os.getpid())
        # print('跳舞父线程', os.getppid())

def task():
    time.sleep(1)

    print('当前线程：', threading.current_thread().name)

if __name__ == '__main__':
    sing_thread = threading.Thread(group=None, target=sing, name='sing', args=(), kwargs={'count':3})
    sing_thread.setDaemon(True)
    dance_thread = threading.Thread(group=None, target=dance, args=(), kwargs={'count':3})

    sing_thread.start()

    dance_thread.start()

    print(g_list)
    time.sleep(2)
    print('over')
    print(g_list)
    exit()

    # for i in range(17):
    #     threading.Thread(target=task).start()
    # time.sleep(5)
    # print('over')
    # exit()
