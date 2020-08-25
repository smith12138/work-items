# _*_ coding: utf-8 _*_
"""
-------------------------------------------------
   File Name：     phantomjs
   Description :   
   Author :        MingHui/smith
   date:           2020/7/30 18:08
   Software:       PyCharm
-------------------------------------------------
"""
__author__ = 'will'

from selenium import webdriver


browser = webdriver.PhantomJS(executable_path='E:/Template/phantomjs.exe')

browser.get('https://item.taobao.com/item.htm?spm=a21bo.2017.201876.3.5af911d9LGuMN3&id=521171128389&scm=1007.12493.125018.0&pvid=70cde946-aaf9-48b1-a656-9c707dee2e70')
print(browser.page_source)
print(browser.find_element_by_css_selector('.tb-rmb-num'))

browser.quit()
