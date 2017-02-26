from multiprocessing import Process, Lock, Value, Queue, Pipe, Pool
import time

def f(num, lock):
    lock.acquire()
    print(num)
    lock.release()

def f2(q):
    while True:
        p = q.get()
        print(p)
        if p is None:
            break

def f3(conn):
    print(conn.recv())
    print(conn.recv())
    conn.send('send back')

def f4(arg):
    time.sleep(20)/usr/bin/python3
    return arg * arg


if __name__ == '__main__':
    lock = Lock()
    q = Queue()
    p = Process(target=f2 , args=(q, ) )
    # p.start()
    # q.put(1)
    # q.put(None)
    # p.join()

    # parent, child = Pipe()
    # p = Process(target=f3 , args=(child, ) )
    # p.start()
    # parent.send('Test')
    # parent.send('Test 2')
    # print(parent.recv())
    # p.join()

    with Pool(processes=10) as pool:
        print(pool.map(f4,  [2, 3, 4, 4, 5, 6]))

