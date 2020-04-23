# -*- coding: utf-8 -*-
# __author__: MUSIBII
# __email__ : shaozuanzuan@gmail.com
# __file__  : task1.py
# __time__  : 2019-05-26 15:06

import time
from celery_task.celery import cel


@cel.task
def test_celery(res):
    # time.sleep(5)

    return 'test_celery 任务结果：%s' % res