# -*- coding: utf-8 -*-
# __file__  : test_03.py
# __time__  : 2020/7/3 5:25 PM

import pytest


def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()