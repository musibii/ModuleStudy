# -*- coding: utf-8 -*-
# __author__: musibii
# __file__  : test_o1.py
# __time__  : 2020/5/21 6:46 下午
from typing import Any

from pkg_resources import resource_filename
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
import pipreqs

class TestDesc(object):
    x = Desc()


class Man:
    gender = '男'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getattribute__(self, item):
        print('拦截')
        if item != 'n':
            raise AttributeError()

    def __getattr__(self, item: Any) -> Any:
        print('get')
        return self.item




# 以下为测试代码
if __name__ == '__main__':
    t = TestDesc()
    t.x
    a = Man('musibii', '18')
    a.name