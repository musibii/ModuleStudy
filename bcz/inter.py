# -*- coding: utf-8 -*-
# __file__  : inter.py
# __time__  : 2020/7/29 8:13 PM

import time
import warnings


def timeit(max_time=1):
    def outter(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            func(*args, **kwargs)
            end = time.time()
            print('process run time is %s' % (end - start))
            if end - start > max_time:
                warnings.warn('function exceeds max_time')

        return wrapper

    return outter


@timeit(max_time=10)
def ti():
    time.sleep(11)


ti()
