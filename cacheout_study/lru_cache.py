# -*- coding: utf-8 -*-
# __file__  : lru_cache.py
# __time__  : 2020/6/30 2:00 下午

from cacheout import LRUCache

lru = LRUCache()

'''
class LRUCache(Cache):
    """
    Like :class:`.Cache` but uses a least-recently-used eviction policy.

    The primary difference with :class:`.Cache` is that cache entries are moved to the
    end of the eviction queue when both :meth:`get` and :meth:`set` are called (as
    opposed to :class:`.Cache` that only moves entries on ``set()``.
    """

    def _get(self, key, default=None):
        value = super()._get(key, default=default)

        if key in self._cache:
            self._cache.move_to_end(key)

        return value
        
    def move_to_end(self, key, last=True):
        """Move an existing element to the end (or beginning if last is false).

        Raise KeyError if the element does not exist.
        """
        link = self.__map[key]
        link_prev = link.prev
        link_next = link.next
        soft_link = link_next.prev
        link_prev.next = link_next
        link_next.prev = link_prev
        root = self.__root
        if last:
            last = root.prev
            link.prev = last
            link.next = root
            root.prev = soft_link
            last.next = link
        else:
            first = root.next
            link.prev = root
            link.next = first
            first.prev = soft_link
            root.next = link
        
'''
