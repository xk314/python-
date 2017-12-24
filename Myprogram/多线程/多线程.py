import threading
import time


def func(num):
    print('我是第%d个线程' % num)
    time.sleep(1)
    print('我是第%d个线程， 我睡醒了' % num)

# if __name__ == '__main__':
    # for i in range(5):
    #     t = threading.Thread(target=func, args=[i])  #给函数传递的参数必须是可迭代对象
    #     t.start()


class Thr(threading.Thread): #通过继承Thread来创建子进程对象，通过start方法开启子进程
    def run(self):
        print('我是子进程: %s' % self.name)
        time.sleep(1)
        print('子进程 %s 睡醒了' % self.name)
for i in range(5):
    t = Thr()
    t.start()

