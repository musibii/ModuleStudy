# -*- coding: utf-8 -*-
# __author__: MUSIBII
# __email__ : shaozuanzuan@gmail.com
# __file__  : celery.py
# __time__  : 2019-05-26 15:06
from threading import RLock, Timer

from celery import Celery
sorted()

cel = Celery('multest',
             broker='redis://192.168.2.238:6379/3',
             backend='redis://192.168.2.238:6379/4',
             include=['celery_task.task1',
                      'celery_task.task2'])

# 时区
cel.conf.timezone = 'Asia/Shanghai'

# 是否使用 UTC
cel.conf.enable_utc = False
cel.task()
RLock
import time
Timer
time.clock()
