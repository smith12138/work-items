# _*_ coding: utf-8 _*_
"""
-------------------------------------------------
   File Name：     robot_info_record_one
   Description :   
   Author :        MingHui/smith
   date:           2020/8/24 10:59
   Software:       PyCharm
-------------------------------------------------
"""
__author__ = 'will'


import sys
import requests
import getopt
import json
import re
import time
import threading
import redis


REDIS_HOST = '127.0.0.1'
REDIS_PWD = 'huobao@zjh8888'
STATUS = None
LIST_DATA = None


class GetCmd(object):
    """获取cookie"""
    def __init__(self, argv):
        global STATUS
        self.host = None
        try:
            opts, args = getopt.getopt(argv, 's:', ['use_status'])
        except getopt.GetoptError:
            print('robot_info_record.py -s <use status: 0-revise 1-save>')
            sys.exit(2)

        if len(opts) != 1:
            print('params input error!!!')
            print('you input {}'.format(str(opts)))
            print('robot_info_record.py -s <use status: 0-revise 1-save>')
            sys.exit()

        for opt, arg in opts:
            if opt in ('-s', '--status'):
                STATUS = arg
            else:
                print('params input error!!!')
                print('you input {} <{}>'.format(opt, arg))
                print('robot_info_record.py -s <use status: 0-revise 1-save>')
                sys.exit()


class ThreadRecord(threading.Thread):
    """多线程更改机器人信息"""
    def __init__(self, list_data, port_id):
        self.list_data = list_data
        port_id += 20000
        self.conn = redis.Redis(host=REDIS_PWD, password=REDIS_PWD, port=port_id, decode_responses=True)

    def send_record_info(self):
        """发送修改请求"""
        for dict_data in self.list_data:
            robot_id = 'hu:' + dict_data['aiId']
            try:
                if self.conn.exists(robot_id):
                    for key, value in dict_data.items():
                        self.conn.hset(robot_id, key, value)
                        print('robot:{} revise success')
            except KeyError as e:
                print('robot:{} revise error'.format(robot_id), '\n', e)
        self.conn.close()

    def run(self):
        """启动线程"""
        lock = threading.Lock()
        lock.acquire()
        self.send_record_info()


class SaveRobotInfo(threading.Thread):
    """保存机器人信息"""
    def __init__(self, port_id):
        super(SaveRobotInfo, self).__init__()
        port_id += 20000
        self.pool = redis.ConnectionPool(host=REDIS_HOST, decode_responses=True, port=port_id, password=REDIS_PWD)
        self.conn = redis.Redis(connection_pool=self.pool)

    def get_all_data(self):
        """获取所有玩家数据"""
        user_key = self.conn.keys('hu:*')
        convert_data = [u.encode('utf-8') for u in user_key]
        user_id = [''.join(re.findall(r'\d', us)) for us in convert_data]
        robot_list = [self.conn.hgetall('hu:{}'.format(uid)) for uid in user_id if uid and 0 < int(uid) <= 10000]
        global LIST_DATA
        LIST_DATA = robot_list

    def run(self):
        """启动方法"""
        lock = threading.Lock()
        lock.acquire()
        self.get_all_data()


def save_json():
    """保存数据为JSON"""
    with open('robot_info.json', 'w') as f:
        f.write(json.dumps(LIST_DATA))


def run_save():
    """保存机器人数据"""
    print('get into robot save ing...')
    sr = [SaveRobotInfo(i) for i in range(1, 11)]
    [td.start() for td in sr]
    for i in sr:
        i.join()
    save_json()
    print('Info Save Success Exiting Threading')


def run_revise():
    """更改机器人信息"""
    import os
    if os.path.exists('robot_info.json'):
        with open('robot_info.json', 'rb') as f:
            list_data = json.loads(f.read())
        threads = [ThreadRecord(list_data, td) for td in range(1, 11)]
        print('get into revise stage...')
        [td.start() for td in threads]
        [i.join() for i in threads]
        print('all robot info revise success')
    else:
        print('not file !!!')


def main(argv):
    """总入口"""
    GetCmd(argv)
    if STATUS == '0':
        run_revise()
    elif STATUS == '1':
        run_save()
    else:
        print('指令有误！！')
        sys.exit()


if __name__ == '__main__':
    main(sys.argv[1:])
