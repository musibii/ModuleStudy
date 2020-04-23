# -*- coding: utf-8 -*-
# __author__: MUSIBII
# __email__ : shaozuanzuan@gmail.com
# __file__  : test.py
# __time__  : 2019-05-14 17:06

a = [2, 5]
b = [a] * 4

print(id(b[0]), id(a))
print(b)
b = tuple(b)
print(b)

b[0][0] = 3
print(b)

import pytest

def jumping_range(N):
    index = 0
    while index < N:
        # 通过send()发送的信息将赋值给jump
        jump = yield index
        if jump is None:
            jump = 1
        index += jump

if __name__ == '__main__':
    itr = jumping_range(5)
    print(next(itr))
    print(itr.send(2))
    print(next(itr))
    print(itr.send(-1))

