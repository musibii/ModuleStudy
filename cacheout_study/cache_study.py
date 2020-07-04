# -*- coding: utf-8 -*-
# __file__  : cache_study.py
# __time__  : 2020/6/29 5:55 下午

from cacheout import Cache

c = Cache()
# c.add()
c.full()


def MyRange(end):
    start = 0
    while start < end:
        x = yield start  # 这里增加了获取返回值
        print(x, "0")  # 打印出来
        start += 1


m = MyRange(5)
print(next(m))
print(next(m))


def MyRange(end):
    start = 0
    while start < end:
        x = yield start
        print(x)
        start += 1


m = MyRange(5)
print(next(m))
print(m.send(10))
