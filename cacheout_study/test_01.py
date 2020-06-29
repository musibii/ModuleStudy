# -*- coding: utf-8 -*-
# __file__  : test_01.py
# __time__  : 2020/6/29 3:31 下午
import asyncio
import time

from cacheout import Cache, CacheManager

cache = Cache()

cache = Cache(maxsize=256, ttl=0, timer=time.time, default=None)  # defaults

cache.set(1, "foobar")

assert cache.get(1) == "foobar"

assert cache.get(2) is None
assert cache.get(2, default=False) is False
assert 2 not in cache

assert 2 not in cache
assert cache.get(2, default=lambda key: key) == 2
assert cache.get(2) == 2
assert 2 in cache

cache.set(3, {"data": {}}, ttl=1)
assert cache.get(3) == {"data": {}}
time.sleep(1)
assert cache.get(3) is None


# 异步生成器
@cache.memoize()
async def func(a, b):
    return a + b


@cache.memoize()
def func(a, b):
    pass


func.uncached(1, 2)

assert cache.copy() == {1: "foobar", 2: ("foo", "bar", "baz")}

cache.delete(1)
assert cache.get(1) is None

cache.clear()
assert len(cache) == 0


cache.set_many({"a": 1, "b": 2, "c": 3})
assert cache.get_many(["a", "b", "c"]) == {"a": 1, "b": 2, "c": 3}
cache.delete_many(["a", "b", "c"])
assert cache.count() == 0


import re

cache.set_many({"a_1": 1, "a_2": 2, "123": 3, "b": 4})

cache.get_many("a_*") == {"a_1": 1, "a_2": 2}
cache.get_many(re.compile(r"\d")) == {"123": 3}
cache.get_many(lambda key: "2" in key) == {"a_2": 2, "123": 3}

cache.delete_many("a_*")
assert dict(cache.items()) == {"123": 3, "b": 4}

cache.configure(maxsize=1000, ttl=5 * 60)


cache.set_many({"a": 1, "b": 2, "c": 3})
assert list(cache.keys()) == ["a", "b", "c"]
assert list(cache.values()) == [1, 2, 3]
assert list(cache.items()) == [("a", 1), ("b", 2), ("c", 3)]

for key in cache:
    print(key, cache.get(key))
    # 'a' 1
    # 'b' 2
    # 'c' 3

assert cache.has("a")
assert "a" in cache

cacheman = CacheManager(
    {"a": {"maxsize": 100}, "b": {"maxsize": 200, "ttl": 900}, "c": {}}
)

cacheman["a"].set("key1", "value1")
value = cacheman["a"].get("key")

cacheman["b"].set("key2", "value2")
assert cacheman["b"].maxsize == 200
assert cacheman["b"].ttl == 900

cacheman["c"].set("key3", "value3")

cacheman.clear_all()
for name, cache in cacheman:
    assert name in cacheman
    assert len(cache) == 0

if __name__ == "__main__":
    try:
        value = next(func(3, 5))
    except StopIteration as e:
        print("Generrator return value:", e.value)

    # loop = asyncio.get_event_loop()

    # loop.create_task(func(3, 5))

    # loop.run_forever()
    # loop.close()
    import poetry
