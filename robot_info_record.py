# _*_ coding: utf-8 _*_
"""
-------------------------------------------------
   File Name：     robot_info_record
   Description :   
   Author :        MingHui
   date:           2020/8/21 19:04
   Software:       PyCharm
-------------------------------------------------
"""
__author__ = 'will'


import requests
import threading
import json
import redis
import re
import sys
import getopt


print('参数个数为:', len(sys.argv), '个参数')
print('参数个数为:{}'.format(str(sys.argv)))
print('参数个数为:{}'.format(str(sys.argv[1:])))


def main(argv):
    inputfile = None
    outputfile = None
    try:
        opts, args = getopt.getopt(argv, 'i:o:', ['ifile=', 'ofile='])
    except getopt.GetoptError:
        print('robot_info_record.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('robot_info_record.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ('-i', '--ifile'):
            inputfile = arg
        elif opt in ('-o', '--ofile'):
            outputfile = arg
    print('输入文件为:{}'.format(inputfile))
    print('输出文件为:{}'.format(outputfile))


class SaveRobotInfo(threading.Thread):
    """保存机器人信息"""
    def __init__(self):
        self.pool = redis.ConnectionPool(host='127.0.0.1', decode_responses=True)
        self.conn = redis.Redis(connection_pool=self.pool)
        self.conn.mset({'aiId': '1', 'oldVirtualWin': '11', 'oldSysVirtualWin': '11', 'name': '11',
                               'avatar': '11', 'status': '11', 'flower': '11', 'enter_low_coin': '11',
                               'enter_high_coin': '11', 'virtualWinType': '11',
                               'virtualWin': '11', 'systemVirtualWinType': '11', 'systemVirtualWin': '11', 'mode': '11'})
        self.conn.delete('aiId', 'oldVirtualWin', 'oldSysVirtualWin', 'name', 'avatar', 'status', 'flower', 'enter_low_coin', 'enter_high_coin', 'virtualWinType', 'virtualWin',
                         'systemVirtualWinType', 'systemVirtualWin')
        print(self.conn.keys())
        print(self.conn.hset('id1', 'virtualWinType', '11'))
        print(self.conn.hgetall('myhash'))
        self.conn.close()


if __name__ == '__main__':
    import sys
    # main(['robot_info_record.py', '--ifile', 'e:/wellhome', '-o', 'c:/wellhome'][1:])
    sr = SaveRobotInfo()
