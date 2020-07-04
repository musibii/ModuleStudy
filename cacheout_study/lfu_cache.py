# -*- coding: utf-8 -*-
# __file__  : lfu_cache.py
# __time__  : 2020/6/30 3:49 下午
from collections import Counter

from cacheout import LFUCache

lfu = LFUCache()


def setup(self):
    super().setup()
    self._access_counts = Counter()


def __next__(self):
    with self._lock:
        try:
            return self._access_counts.most_common(1)[0][0]
        except ValueError:  # pragma: no cover
            # Empty cache.
            raise StopIteration


def _touch(self, key):
    # Decrement access counts so we can use Counter.most_common() to return
    # the least accessed keys first (i.e. keys with a higher count).
    self._access_counts[key] -= 1


def _get(self, key, default=None):
    value = super()._get(key, default=default)
    if key in self:
        self._touch(key)
    return value


def _set(self, key, value, ttl=None):
    super()._set(key, value, ttl=ttl)
    self._touch(key)


def _delete(self, key):
    count = super()._delete(key)

    try:
        del self._access_counts[key]
    except KeyError:  # pragma: no cover
        pass

    return count


def _clear(self):
    super()._clear()
    self._access_counts.clear()
