import threading
import time

def worker(timeout=5):
    time.sleep(timeout)
    print("worker {} sleep{}".format(threading.currentThread().getName(), timeout))

class MyThread(threading.Thread):
    def __init__(self, lst, lock, *args, **kwargs):
        super(MyThread, self).__init__(*args, **kwargs)
        self.lst = lst
        self.lock = lock

    def run(self):
        self.lock.acquire()
        for i in range(len(self.lst)):
           del self.lst[0]
           time.sleep(1)
        self.lock.release()


        
if __name__ == '__main__':
    l = [1,2,3,4]
    lock = threading.Lock()
    thread3 = MyThread(l, lock)
    thread4 = MyThread(l, lock)
    thread3.start()
    thread4.start()
    thread3.join()
    thread4.join()
    print(l)