# -*- coding: utf-8 -*-
# __file__  : mru_cache.py
# __time__  : 2020/6/30 3:41 下午

from cacheout import MRUCache

mru = MRUCache()


def __next__(self):
    return next(reversed(self._cache))