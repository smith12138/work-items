import json
import time
import threading
import uuid
import requests
# data = json.load(open('luckySon_interface.json', 'rb'))['login_money']
data = json.load(open('luckySon_interface.json', 'rb'))['proxy_money']
URL, DATA, HEADERS = [value for key, value in data.items()]
DATA['param'] = json.dumps(DATA['param'])


class ThreadingTest(object):
    def __init__(self, url, data, headers):
        self.url = url
        self.data = data
        self.headers = headers

    def post_send(self):
        try:
            res = requests.get(url=self.url, params=self.data, headers=self.headers).text
            print(res)
        except Exception as e:
            print('1', e)


def kquan_bf():
    login = ThreadingTest(URL, DATA, HEADERS)
    return login.post_send()


# if __name__ == '__main__':
#     try:
#         i = 0
#         tasks_number = 100
#         print('test start ... ')
#         time1 = time.perf_counter()
#         while i < tasks_number:
#             t = threading.Thread(target=kquan_bf)
#             t.start()
#             i += 1
#         time2 = time.perf_counter()
#         times = time2 - time1
#         print(times / tasks_number)
#     except Exception as e:
#         print('2', e)


import threading
import time


def irr():
    print('irr')


def aps():
    print('aps')
    while True:
        time.sleep(6)
        irr()


def view():
    t2 = threading.Thread(target=aps)
    t2.daemon = True
    t2.start()
    print('test1')


t = threading.Thread(target=view)
t.daemon = True
t.start()
while True:
    time.sleep(1)