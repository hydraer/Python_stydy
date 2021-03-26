# 1、进程是计算机操作系统进行资源分配的基本单位，一个程序至少有一个进程，进程是Python程序中实现多任务的一种方式
# 2、一个进程默认有一个线程，进程里面可以创建多个线程，线程是依附在进程里面的，没有进程就没有线程。
# 3、进程之间不共享全局变量(创建子进程会对主进程资源进行拷贝)
# 4、主进程会等待所有的子进程执行结束再结束
# 5、获取当前进程：multiprocessing.current_process()
import multiprocessing
import os
import time

g_list = [1,]

def dance(a):
    for i in range(a):
        g_list.append(i+10)
        # print('年年在第%u支跳舞...'%(i+1))
        # print(os.getpid())
        # print(os.getppid())
        time.sleep(0.2)
        print('当前线程名：', multiprocessing.current_process().name)

def singing(b):
    for i in range(b):
        g_list.append(i)
        print(g_list)
        # print('over')

        # print(f'年年在唱第{i+1}首歌...')
        # print(os.getpid())
        # print(os.getppid())

if __name__ == '__main__':
    dance_process = multiprocessing.Process(group=None, target=dance, name='dance', args=(5,), kwargs={})
    dance_process.start()

    sing_process = multiprocessing.Process(group=None, target=singing, name='sing', args=(7,), kwargs={})
    sing_process.start()
    print(g_list)
    time.sleep(0.2)
    print('over')
    exit()