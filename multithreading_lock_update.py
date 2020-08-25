# _*_ coding: utf-8 _*_
"""
-------------------------------------------------
   File Name：     multithreading_test
   Description :   
   Author :        MingHui/smith
   date:           2020/8/11 15:06
   Software:       PyCharm
-------------------------------------------------
"""
__author__ = 'will'

import time
import threading

exitFlag = 0


class TestThreading(threading.Thread):
    def __init__(self, delay, name, counter):
        super(TestThreading, self).__init__()
        self.delay = delay
        self.name = name
        self.counter = counter

    def run(self):
        lock = threading.Lock()
        lock.acquire()
        print('Starting'.format(self.name))
        print_time(self.name, self.delay, self.counter)
        # print('Exiting'.format(self.name))


def print_time(threadname, delay, counter):
    while counter:
        if exitFlag:
            threading.Thread.exit()
        time.sleep(delay)
        print('%s: %s' % (threadname, time.ctime(time.time())))
        counter -= 1


# thread1 = TestThreading(1, 'Thread-1', 1)
# thread2 = TestThreading(2, 'Thread-2', 1)
threads = [TestThreading(1, 'Thread-{}'.format(i), 1) for i in range(1, 11)]
[td.start() for td in threads]
for i in threads:
    i.join()
print('Exiting Threading')

# thread1.start()
# thread2.start()
