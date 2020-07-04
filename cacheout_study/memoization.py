# -*- coding: utf-8 -*-
# __file__  : memoization.py
# __time__  : 2020/6/30 4:38 PM

from cacheout import memoization


def memoize(self, *, ttl=None, typed=False):
    """
    Decorator that wraps a function with a memoizing callable and works
    on both synchronous and asynchronous functions.

    Each return value from the function will be cached using the function arguments
    as the cache key. The cache object can be accessed at ``<function>.cache``. The
    uncached version (i.e. the original function) can be accessed at
    ``<function>.uncached``. Each return value from the function will be cached
    using the function arguments as the cache key.

    Keyword Args:
        ttl (int, optional): TTL value. Defaults to ``None`` which uses :attr:`ttl`.
        typed (bool, optional): Whether to cache arguments of a different type
            separately. For example, ``<function>(1)`` and ``<function>(1.0)`` would
            be treated differently. Defaults to ``False``.
    """
    marker = (object(),)

    def decorator(func):
        prefix = "{}.{}:".format(func.__module__, func.__name__)
        argspec = inspect.getfullargspec(func)

        if asyncio.iscoroutinefunction(func):

            @wraps(func)
            @asyncio.coroutine
            def decorated(*args, **kwargs):
                key = _make_memoize_key(
                    func, args, kwargs, marker, typed, argspec, prefix
                )
                value = self.get(key, default=marker)

                if value is marker:
                    value = yield from func(*args, **kwargs)
                    self.set(key, value, ttl=ttl)

                return value

        else:

            @wraps(func)
            def decorated(*args, **kwargs):
                key = _make_memoize_key(
                    func, args, kwargs, marker, typed, argspec, prefix
                )
                value = self.get(key, default=marker)

                if value is marker:
                    value = func(*args, **kwargs)
                    self.set(key, value, ttl=ttl)

                return value

        decorated.cache = self
        decorated.uncached = func

        return decorated

    return decorator