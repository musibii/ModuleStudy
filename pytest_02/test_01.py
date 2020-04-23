# -*- coding: utf-8 -*-
# __author__: MUSIBII
# __email__ : shaozuanzuan@gmail.com
# __file__  : pytest_test01.py
# __time__  : 2019-05-15 21:28

import pytest

def func(x):
    return x + 1


def outter(func):
    def inner(*args, **kwargs):
        print(func.__dict__)
        res = func(*args, **kwargs)
        return res

    return inner

# @outter
@pytest.mark.test1(1, 2, name='musibii')
def test_answer():
    assert func(3) == 4

test_answer()



