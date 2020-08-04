# -*- coding: utf-8 -*-
# __file__  : test.py
# __time__  : 2020/7/31 10:27 AM
from typing import List


def fib(n):
    a, b, c = 1, 1, 1
    if n == 1 or n == 2:
        return 1
    if n > 3:
        for i in range(3, n+1):
            c = a + b
            a = b
            b = c

    return c

print(fib(6))


a = [1, 1, 2, 3, 4, 5, 5, 5]

def func(n: List) -> List:
    m = set(n)
    r_list = []
    for i in m:
        if n.count(i) == 1:
            r_list.append(i)


print(set(a))



