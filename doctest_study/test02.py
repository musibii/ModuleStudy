# -*- coding: utf-8 -*-
# __file__  : test02.py
# __time__  : 2020/6/23 9:09 下午
import doctest
import test01

if __name__ == "__main__":
    doctest.testmod(test01)
    import socket

    s = socket.socket()
    s.listen()
import cgi
