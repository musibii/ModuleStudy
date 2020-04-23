# -*- coding: utf-8 -*-
# __author__: MUSIBII
# __email__ : shaozuanzuan@gmail.com
# __file__  : celery.py
# __time__  : 2019-05-26 15:06

from celery import Celery
from datetime import timedelta
from celery.schedules import crontab

cel = Celery('multest',
             broker='redis://192.168.2.238:6379/5',
             backend='redis://192.168.2.238:6379/6',
             include=['celery_task.task1',
                      'celery_task.task2'])

# 时区
cel.conf.timezone = 'Asia/Shanghai'

# 是否使用 UTC
cel.conf.enable_utc = False


cel.conf.beat_schedule = {
    # 名字随意命名
    'add-every-10-seconds': {
        # 执行tasks1下的test_celery函数
        'task': 'celery_task.task1.test_celery',
        # 每隔2秒执行一次
        # 'schedule': 1.0,
        # 'schedule': crontab(minute="*/1"),
        'schedule': timedelta(seconds=2),
        # 传递参数
        'args': ('test',)
    },
    'add-every-12-seconds': {
        'task': 'celery_task.task2.test_celery',
        # 每年4月11号，8点42分执行
        'schedule': crontab(minute=6, hour=16, day_of_month=26, month_of_year=5),
        # 'schedule': crontab(minute=42, hour=8, day_of_month=11, month_of_year=4),
        'args': ('sssss')
    # },
}}