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
RESET_URL = 'http://{}/admin/ai_player/edit.html'
LOGIN_URL = 'http://{}/admin/logincheck'
ID = 'admin'
PASSWORD = '123456'
HEADER = {
    "Host": "",
    "Cookie": "",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
}
STATUS = None
LIST_DATA = None


class GetCookie(object):
    """获取cookie"""
    def __init__(self, argv):
        global LOGIN_URL
        global RESET_URL
        global HEADER
        global STATUS
        self.host = None
        try:
            opts, args = getopt.getopt(argv, 'h:s:', ['host_name', 'use_status'])
        except getopt.GetoptError:
            print('robot_info_record.py -h <host name> -s <use status: 0-revise 1-save>')
            sys.exit(2)

        if len(opts) != 2:
            print('params input error!!!')
            print('you input {}'.format(str(opts)))
            print('robot_info_record.py -h <host name> -s <use status: 0-revise 1-save>')
            sys.exit()

        for opt, arg in opts:
            if opt in ('-h', '--host'):
                self.host = arg
            elif opt in ('-s', '--status'):
                STATUS = arg
            else:
                print('params input error!!!')
                print('you input {} <{}>'.format(opt, arg))
                print('robot_info_record.py -h <host name> and -s <use status: 0-revise 1-save>')
                sys.exit()
        LOGIN_URL = LOGIN_URL.format(self.host)
        RESET_URL = RESET_URL.format(self.host)
        HEADER['host'] = self.host

    def get_cookie(self):
        """获取cookie"""
        global HEADER
        print('get cookie ing .....')
        res = requests.post(url=LOGIN_URL, data={'account': ID, 'password': PASSWORD}).cookies
        HEADER['cookie'] = re.findall(r' [\s\S]*? ', str(res))[0].replace(' ', '')
        print('get cookie exit .....')


class ThreadRecord(threading.Thread):
    """多线程更改机器人信息"""
    def __init__(self, list_data):
        self.counter = len(list_data)
        self.list_data = list_data

    def send_record_info(self):
        """发送修改请求"""
        for dict_data in self.list_data:
            reset_data = {
                'aiId': dict_data['aiId'],  # ID
                'oldVirtualWin': dict_data['oldVirtualWin'],  # 该玩家虚拟输赢为, 当前的
                'oldSysVirtualWin': dict_data['oldSysVirtualWin'],  # 该玩家系统虚拟输赢为, 当前的
                'name': dict_data['name'],  # 昵称
                'avatar': dict_data['avatar'],  # 头像
                'status': dict_data['status'],  # 1是启用, 0/空是关闭
                'flower': dict_data['flower'],  # 1是有花, 0是无花
                'enter_low_coin': dict_data['enter_low_coin'],  # 最低金额
                'enter_high_coin': dict_data['enter_high_coin'],  # 最高金额
                'virtualWinType': 'add',  # add 修改
                'virtualWin': dict_data['virtualWin'],  # 虚拟输赢金额
                'systemVirtualWinType': 'add',  # add 修改
                'systemVirtualWin': dict_data['systemVirtualWin'],  # 系统输赢金额
                'mode': dict_data['mode']  # 模式
            }
            result = requests.post(url=RESET_URL, data=reset_data, headers=HEADER).text
            if '成功' in result:
                print('{}: Revise Success'.format(self.set_data['aiId']))
            else:
                print('{}: Revise Fail'.format(self.set_data['aiId']))

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
        user_key = self.conn.keys()
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
        td = ThreadRecord(list_data)
        print('get into revise stage...')
        td.start()
        print('robot info revise success')
    else:
        print('not file !!!')


def main(argv):
    """总入口"""
    gc = GetCookie(argv)
    gc.get_cookie()
    if STATUS == '0':
        run_revise()
    elif STATUS == '1':
        run_save()
    else:
        print('指令有误！！')
        sys.exit()


if __name__ == '__main__':
    main(sys.argv[1:])



    # gc = GetCookie(['robot_info_record.py', '-h', '192.168.2.103:18002', '-s', '1'][1:])
    # gc.get_cookie()
    # print(STATUS)
    # print(HEADER)
    # print(RESET_URL)
    # SaveRobotInfo()