# _*_ coding: utf-8 _*_
"""
-------------------------------------------------
   File Name：     tcp_data_parse
   Description :   
   Author :        MingHui/smith
   date:           2020/8/14 16:15
   Software:       PyCharm
-------------------------------------------------
"""
__author__ = 'will'


import json
import pickle

sourse = '825b57000000762f4e62612f3738212f486168606863792f37565635213b213b213521355021563b213f2135213c3d21355021563b213a21392139213b5050212f5f68792f373d212f5f627a2f373e212f6e60692f373f3d3f3d3e7007825753000000762f4f6263787e2f373c212f446e682f373d212f446e685f6c6964622f373c3d3d212f446e685f627863692f373d212f416463682f372f2f212f5a646340786179642f373d212f6e60692f373f3d3f3f397007827e00b8b4000000762f4f6c7e68427a634e6264632f373c3c3d3c3b3b3e3c212f4f6c7e685a64634e6264632f373d212f4a6c60685e796c79682f373e212f427a634e6264632f373c3c3d3c3b3b3e3c212f5962796c615d6263692f373e38353b212f59787f63596460687e2f373c353f393f3e3b35212f587e687f44492f373c3c3e393434212f5a64634e6264632f373d212f5a6463416463682f373d212f5a64635d6263694e6264632f373d212f6e60692f373f3d3f3d3f7007'
result1 = []
result2 = []

for i in range(len(sourse)):
    if i % 2 == 0:
        result1.append(int(sourse[i], 16) * 16)
    else:
        result2.append(int(sourse[i], 16))

result_data = [z + j for z, j in zip(result1, result2)]
result_data = [chr(result_data[i] ^ 13) for i in range(len(result_data))]
# print([i for i in result_data if i >255])
# print(result_data)
print(''.join(result_data))

