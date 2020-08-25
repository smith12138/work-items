# _*_ coding: utf-8 _*_
"""
-------------------------------------------------
   File Name：     mulitthreading_test1
   Description :   
   Author :        MingHui/smith
   date:           2020/8/11 16:01
   Software:       PyCharm
-------------------------------------------------
"""
__author__ = 'will'


from multithreading import *


COUNTER = 0
URL, DATA, HEADERS = URL, DATA, HEADERS


class TestThreadings(threading.Thread):
    def __init__(self, name: str, counter: int, delay: int = 0):
        super(TestThreadings, self).__init__()
        self.delay = delay
        self.name = name
        self.counter = counter

    def run(self):
        print('Starting'.format(self.name))
        lock = threading.Lock()
        lock.acquire()
        # self.request_send(self.name, self.delay, self.counter)
        self.print_time(self.name, self.delay, self.counter)

    def request_send(self, thread_name, delay, counter):
        thread_run = ThreadingTest(URL, DATA, HEADERS)
        while counter:
            time.sleep(delay)
            thread_run.post_send()
            counter -= 1

    def print_time(self, thread_name, delay, counter):
        while counter:
            global COUNTER
            COUNTER += 1
            time.sleep(delay)
            print('%s: %s' % (thread_name, time.ctime(time.time())), 'COUNTS:{}'.format(COUNTER))
            counter -= 1


threads_list = list()
threads = [TestThreadings('thread-1', 1) for i in range(100)]
for thread in threads:
    threads_list.append(thread)
[thread.start() for thread in threads]
for t in threads_list:
    t.join()
print('Exiting Main Thread')
