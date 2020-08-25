# _*_ coding: utf-8 _*_
"""
-------------------------------------------------
   File Name：     super_test
   Description :   
   Author :        MingHui/smith
   date:           2020/7/31 14:27
   Software:       PyCharm
-------------------------------------------------
"""
__author__ = 'will'


class Source(object):
    def __init__(self):
        print('over')


class Base(Source):
    def __init__(self):
        print('Base create')
        # Source.__init__(self)
        super(Base, self).__init__()


class ChildA(Base):
    def __init__(self):
        print('enter A ')
        # Base.__init__(self)
        super(ChildA, self).__init__()
        print('leave A')


class ChildB(Base):
    def __init__(self):
        print('enter B ')
        # Base.__init__(self)
        super(ChildB, self).__init__()
        print('leave B')


class ChildC(ChildA, ChildB):
    def __init__(self):
        super(ChildC, self).__init__()


class TestA(object):
    def __init__(self):
        print('enter TestA')
        super(TestA, self).__init__()


class TestB(TestA):
    def __init__(self):
        print('enter B')
        super(TestB, self).__init__()


class TestC(TestB, TestA):
    def __init__(self):
        super(TestC, self).__init__()
        print('over c')


# c = ChildC()
# print(c.__class__.__mro__)
a = TestC()
print(a.__class__.__mro__)

if 'a' is 'a':
    print('y')
if 'b' is 'bb':
    print('y.')