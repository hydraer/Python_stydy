import threading

a = 0

def count1():
    for i in range(10000000):
        global a
        a = a + 1
    print(a)
def count2(): 
    for i in range(10000000):
        global a
        a = a + 1
    print(a)

if __name__ == '__main__':
    count1_thread = threading.Thread(target=count1)
    count2_thread = threading.Thread(target=count2)
    count1_thread.start()
    count1_thread.join()
    count2_thread.start()
    print(a)