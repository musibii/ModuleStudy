# -*- coding: utf-8 -*-
# __file__  : lifo_cache.py
# __time__  : 2020/6/30 10:10 上午

from cacheout import LIFOCache

lifo = LIFOCache()
# lifo.get()
# lifo.popitem()

def __next__(self):
    return next(reversed(self._cache))

lifo.add_many({"name": "musibii", "age": 18, "address": "ShangHai"})

for i in lifo:
    print(i, lifo.get(i))


lifo.popitem()
