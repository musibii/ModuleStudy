# -*- coding: utf-8 -*-
# __file__  : rr_cache.py
# __time__  : 2020/6/30 4:35 PM
from random import random

from cacheout import RRCache

rr = RRCache()


def __next__(self):
    with self._lock:
        try:
            return random.choice(list(self._cache.keys()))
        except IndexError:  # pragma: no cover
            raise StopIteration