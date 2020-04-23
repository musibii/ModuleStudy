# -*- coding: utf-8 -*-
# __author__: MUSIBII
# __email__ : shaozuanzuan@gmail.com
# __file__  : celery_01.py
# __time__  : 2019-05-26 10:10

from celery import Celery
import time

backend = 'redis://192.168.2.238:6379/1'
broker = 'redis://192.168.2.238:6379/2'

cel = Celery('test',  backend=backend, broker=broker)

@cel.task
def add(x, y):
    return x + y