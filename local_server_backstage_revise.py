
import json
import os
import requests
import re
import random

with open('AI_status.json') as f:
    dict_data = json.load(f)


src = {0: 'feizhou_local',
       1: 'test_server',
       2: 'vi_formal',
       3: 'haoyou_local'}

model = src[int(input('input model params'))]
url, header, data = dict_data[model]

num_start = {0: 450, 1: 500, 2: 550, 3: 600, 4: 450, 5: -1, 6: 600, 7: 646}
num_end = {0: 501, 1: 551, 2: 601, 3: 651, 4: 651, 5: 2001, 6: 650, 7: 651}


def open_json(path):
    with open(path, 'rb') as f:
        data_json = json.load(f)
        try:
            return data_json
        except:
            print('打开错误')


def change_mode(start, end):
    while True:
        try:
            start += 1
            if start == end:
                break
            data['aiId'] = start
            data['mode'] = random.randint(1, 5)
            res = requests.post(url=url, headers=header, data=data).text
            if '非法访问' in res:
                header['Cookie'] = header['Cookie'].format(get_cookie(header['Host']))
                res = requests.post(url=url, headers=header, data=data).text
            if '修改成功' in res:
                print('玩家', start, '--', '模式', data['mode'], '成功')
            else:
                print('玩家', start, '--', '模式', data['mode'], '失败')
        except:
            pass


def change_name(start, end, conf=False):
    import random
    global header
    try:
        if conf:
            conf = open_json(conf)['RobotName']
        while True:
            start += 1
            if start == end:
                break
            else:
                pass
            if conf:
                name = conf[random.randint(0, len(conf))]
            else:
                name = 'Hello' + str(start * start)

            data['aiId'] = start
            data['name'] = name
            res = requests.post(url=url, headers=header, data=data).text
            if '非法访问' in res:
                header['Cookie'] = header['Cookie'].format(get_cookie(header['Host']))
                res = requests.post(url=url, headers=header, data=data).text
            if '修改成功' in res:
                print('玩家', start, '--', '昵称', name, '成功')
            else:
                print('玩家', start, '--', '昵称', name, '失败')
    except:
        pass


def change_status(start, end, status=1):
    try:
        while True:
            start += 1
            if start == end:
                break
            else:
                pass
            data['aiId'] = start
            data['status'] = status
            res = requests.post(url=url, headers=header, data=data).text
            if '非法访问' in res:
                header['Cookie'] = header['Cookie'].format(get_cookie(header['Host']))
                res = requests.post(url=url, headers=header, data=data).text
            info = '启用' if status else '禁用'
            # print(res)
            if '修改成功' in res:
                print('玩家', start, '--', info, '成功')
            else:
                print('玩家', start, '--', info, '失败')
    except:
        pass


def get_cookie(host):
    url = 'http://{}/admin/logincheck'
    res = requests.post(url=url.format(host), data={'account': 'admin', 'password': '123456'}).cookies
    res = re.findall(r' [\s\S]*? ', str(res))[0].replace(' ', '')
    return res

import threading

# change_name(5, 'E:\RobotName.conf')
# change_mode(450, 645)
change_status(500, 651, 0)



