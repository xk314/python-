import threading, time

mutex = threading.Lock()#创建互斥锁
g_num = 0

class Thr1(threading.Thread):
    def run(self):
        global g_num
        for i in range(10000):
            mutex.acquire()
            g_num += 1
            mutex.release()
            # time.sleep(0.01)

class Thr2(threading.Thread):
    def run(self):
        global g_num
        for i in range(10000):
            mutex.acquire()
            g_num += 1
            mutex.release()
            # time.sleep(0.01)

t1 = Thr1()
t2 = Thr2()
t1.start()
t2.start()
t1.join()
t2.join()
print(g_num)
