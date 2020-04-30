# -*- coding: utf-8 -*-
# __author__: musibii
# __file__  : test4.py
# __time__  : 2020/4/26 12:10 AM

import socket


def func(x: int, y: int):
    print(x, y)
    return x + y


if __name__ == '__main__':
    func(1, '23')
