import threading, time

mutex = threading.Lock()#创建互斥锁
g_num = 0

class Thr1(threading.Thread):
    def __init__(self, lock):
        self.lock = lock
        super().__init__()   #必须调用父类的init方法来初始化线程实例

    def run(self):
        global g_num
        for i in range(10000):
            self.lock.acquire()
            g_num += 1
            self.lock.release()
            # time.sleep(0.01)


class Thr2(threading.Thread):
    def __init__(self, lock):
        self.lock = lock
        super().__init__()

    def run(self):
        global g_num
        for i in range(10000):
            self.lock.acquire()
            g_num += 1
            self.lock.release()
            # time.sleep(0.01)
t1 = Thr1(mutex)
t2 = Thr2(mutex)
t1.start()
t2.start()
t1.join()
t2.join()
print(g_num)
