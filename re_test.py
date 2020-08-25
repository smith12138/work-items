
# -*- coding: utf-8 -*-
import re
from urllib.parse import unquote
import base64
import hashlib


str1 = 'a, b, c,,,,d, f'
url = 'https://www.lagou.com/utrack/trackMid.html?f=https%3A%2F%2Fwww.lagou.com%2Fjobs%2F7322575.html&t=1593592006&_ti=1'
url = unquote(url)
print(url)
reObj = re.compile(r'https://www.lagou.com/jobs/(\d+).html')
res = reObj.search(url)
print(res)


num = '2020-05-28\xa0 发布于拉勾网'
print(num.replace('\xa0', ''))

# db_data = 'eab4f02b1f809f25f929f5c4360a3573'
# password = input('input password')
#
# m = hashlib.md5()
# m.update(password.encode('utf-8'))
# md5_data = m.hexdigest()
# if db_data == md5_data:
#     print('success')


cookies = [{23: 2}]
a = cookies or {}
print(a)
import random

USER_AGENT_LIST = [1, 2, 3, 23, 434, 32]
print('random value: %s' % USER_AGENT_LIST[random.randint(0, len(USER_AGENT_LIST) - 1)])

user_agent = USER_AGENT_LIST[random.randint(0, len(USER_AGENT_LIST) - 1)]


number_str = 'efs'

print(re.findall(r'\d', number_str))