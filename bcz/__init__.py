# -*- coding: utf-8 -*-
# __file__  : __init__.py.py
# __time__  : 2020/7/28 4:30 PM

import time


def auth(engine='file'):
    def outter(func):
        print(id(func))
        def wrapper1(*args, **kwargs):
            if engine == 'file':
                input_name = input('name>>>')
                input_passwd = input('password>>>')
                if input_passwd == 'abc' and input_name == 'zz':
                    print('login successful')
                    res = func(*args, **kwargs)
                elif engine == 'mysql':
                    print('基于mysql的认证')
                else:
                    print('未识别的认证源')
            return res

        return wrapper1

    return outter


def timmer(func):
    def wrapper2(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print('process run time is %s' % (end - start))

    return wrapper2

print(1)
print(id(timmer))

@timmer
@auth(engine='file')
def index():
    print('this is from index')
    time.sleep(2)


index()
