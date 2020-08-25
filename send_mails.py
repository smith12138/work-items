# _*_ coding: utf-8 _*_
# @Time : 2020/7/23 16:23 
# @File : mail_test.py 
# @Software: PyCharm
__author__ = 'will'

import requests
import json
import time

data = {"uid": "1",
        "type": "1",
        "status": "0",
        "title": "1",
        "content": "1"}

header = {
    'Cookie': 'PHPSESSID=4u6eanla7gjioqlud8hludacbl',
    'Host': '39.108.188.50:18001',
    'Origin': 'http://39.108.188.50:18001',
}


def send_mail(uid, count):
    data['uid'] = str(uid)
    while count:
        data['title'] = data['content'] = str(count)
        res = requests.post(url='http://39.108.188.50:18001/admin/player/message.html', data=data, headers=header).text
        if '操作成功！消息添加成功' in res or '发送消息成功' in res:
            print('邮件{}发送成功'.format(str(count)))
        else:
            print('send error', '\n', res)
        count -= 1
        # if num == 10:
        #     time.sleep(5)


send_mail(113504, 20)
