# -*- coding: utf-8 -*-
# __author__: musibii
# __file__  : test_o1.py
# __time__  : 2020/5/21 6:46 下午

class Desc(object):

    def __get__(self, instance, owner):
        print("__get__...")
        print("self : \t\t", self)
        print("instance : \t", instance)
        print("owner : \t", owner)
        print('=' * 40, "\n")

    def __set__(self, instance, value):
        print('__set__...')
        print("self : \t\t", self)
        print("instance : \t", instance)
        print("value : \t", value)
        print('=' * 40, "\n")


class TestDesc(object):
    x = Desc()


# 以下为测试代码
if __name__ == '__main__':
    t = TestDesc()
    t.x
