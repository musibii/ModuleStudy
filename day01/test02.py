# -*- coding: utf-8 -*-
# __author__: MUSIBII
# __email__ : shaozuanzuan@gmail.com
# __file__  : test02.py
# __time__  : 2019-05-11 13:52

# a = set()
# b = dict()
#
# print(a, b)
#
# a = [11,22,33,33,44,22,55]
#
# a = set(a)
# print(a)
#
# c = {1, 2, 3, 4}
# print(type(c))
#
# v = '0b1111011'
# print(int(v, 2))
#
# v = 18
# print(bin(v))
#
# # v = '011'
# # print(oct())
#
# class D(type):
#     pass
#
# d = D('D', (object, ), {'name': 'musibii'})
# d()
#
# v = dict.fromkeys(['k1', 'k2'], ([1,2]))
# v['k1'].append(666)
# print(v)
# v['k1'] = 777
# print(v)
#
# print('\n'.join('\t'.join(['%s * %s = %s' % (x, y, x*y) for y in range(1, x + 1)]) for x in range(10)))
#
# print()

# a = []
# b = []
# a.append(b)
# b.append(a)
# # ccc = 'asdfasdaa1234214sdf'
# name = "musibii"
# age = "df"
# import sys
#
# print(sys.getrefcount(b))
# print(sys.getrefcount(a))
# print(sys.getrefcount(name))
# print(sys.getrefcount(age))
#
# import pdb
#
# a = 10
# print(id(a))
#
# c = [a]
# print(c, id(c))
#
#
# print(list(map(lambda x: x ** x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
# print(list((lambda x: x ** x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
#
#
# print(dir("a"))
# print(dir())
#
# # hasattr()
#
# # a.name = 'adf'
# # print(getattr(a, 'name', 'musibii'))
# # setattr()
# import socket

# print(hash("hello"))
# import hashlib

from test01 import func

a = func(3, 4)
if a == 12:
    print("test passes")
