import threading
import time

lock = threading.Lock()

def get_value(index):
    lock.acquire()
    print(threading.current_thread())
    g_list = [2, 1, 4, 8]
    if index >= len(g_list):
        print('下表越界：', index)
        lock.release()
        return
    value = g_list[index]
    print(value)
    time.sleep(0.5)
    lock.release()

if __name__ == '__main__':
    for i in range(30):
        thread1 = threading.Thread(target= get_value, args=(i, ))
        thread1.start()