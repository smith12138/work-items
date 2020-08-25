# _*_ coding: utf-8 _*_
"""
-------------------------------------------------
   File Name：     property_test
   Description :   
   Author :        MingHui/smith
   date:           2020/7/30 15:40
   Software:       PyCharm
-------------------------------------------------
"""
__author__ = 'will'


class Student(object):
    """学生分数录入"""
    def __init__(self):
        self.x = 100

    @property
    def score(self):
        """获取属性值的函数"""
        return self.x

    @score.setter
    def score(self, value):
        """设置属性值的函数"""
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if not 0 <= value <= 100:
            raise ValueError('score must between 0~100!')
        self.x = value
        print('self.x:{}'.format(self.x))

    @score.deleter
    def score(self):
        """删除属性值的函数"""
        del self.x

    @property
    def count(self):
        """返回剩余分数"""
        return 750 - self.score


t = Student()
t.score = 99
# t.score = 98
# del t.score
print(t.count)
# >>> 651