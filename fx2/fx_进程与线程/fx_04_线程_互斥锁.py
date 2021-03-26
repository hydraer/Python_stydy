import threading
import time

a = 0

lock = threading.Lock()

def count1():
    lock.acquire()
    global a
    for i in range(1000000):
        a = a + 1
    print('count1:', a)
    lock.release()
def count2():
    lock.acquire()
    global a
    for i in range(1000000):
        a = a + 1
    print('count2:', a)
    lock.release()

if __name__ == '__main__':
    count1_thread = threading.Thread(target=count1)
    count2_thread = threading.Thread(target=count2)
    count1_thread.start()
    count2_thread.start()
    time.sleep(1)
    print('count:', a)