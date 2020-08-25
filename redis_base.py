# _*_ coding: utf-8 _*_
"""
-------------------------------------------------
   File Name：     redis_read_test
   Description :   
   Author :        MingHui/smith
   date:           2020/8/24 17:26
   Software:       PyCharm
-------------------------------------------------
   Change Activity:
                   2020/8/24:
-------------------------------------------------                
"""
__author__ = 'will'

import redis
import json

REDIS_HOST = '127.0.0.1'
REDIS_PWD = 'huobao@zjh8888'


conn = redis.Redis(host=REDIS_HOST, decode_responses=True)
conn.mset({'user_info': json.dumps({'1': '2'})})
test_list = [{'id1': '222'}, {'id2': '333'}, {'id3': '444'}]
for dict_data in test_list:
    if conn.exists('id1'):
        for key, value in dict_data.items():
            conn.hset(key, key, value)
print(conn.keys())
print(type(conn.hgetall('use_proxy')))
print(conn.hgetall('id1'))
