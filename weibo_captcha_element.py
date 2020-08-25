# _*_ coding: utf-8 _*_
"""
-------------------------------------------------
   File Name：     weibo_captcha_element
   Description :   
   Author :        MingHui/smith
   date:           2020/7/28 17:25
   Software:       PyCharm
-------------------------------------------------
"""
__author__ = 'will'

import base64
import pyautogui
import pickle

button_login = pyautogui.locateOnScreen('check_image.png')
print(button_login)
# # button_point = pyautogui.center(button_login)
# # print(type(button_point))
# # print(len(button_login))
# # image_coord = (button_login[0], button_login[1], button_login[2])
# # print(button_point)
img = pyautogui.screenshot('123.png', region=(button_login[0] + 120, button_login[1] - 90, button_login[2] + 30, button_login[3]))
# print(img)

# print(pickle.load(open('check_image.png', 'rb')))
#
# with open('check_image.png', 'rb') as f:
#     data = f.read()
#
#     print(type(data))
#     encode_str = base64.b64encode(data)

    # print(type(str(encode_str, 'utf-8')))