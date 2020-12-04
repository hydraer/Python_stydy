# 死锁
# 死锁原因：互斥锁使用不当

import threading
import time

lock = threading.Lock()

def get_value(index):
    lock.acquire()
    print(threading.current_thread())
    list = [2, 4, 6, 1]
    if index >= len(list):
        print('下标越界', index)
        lock.release()
        return
    value = list[index]

    print(value)
    time.sleep(0.2)
    lock.release()


if __name__ == '__main__':
    for i in range(30):
        get_value_thread = threading.Thread(target=get_value, args=(i,))
        get_value_thread.start()