# -*- coding: utf-8 -*-
# __author__: MUSIBII
# __email__ : shaozuanzuan@gmail.com
# __file__  : send_task.py
# __time__  : 2019-05-26 15:07

from celery_task.task1 import test_celery
from celery_task.task2 import test_celery2

result = test_celery.delay('第一个')
print(result.id)

result = test_celery2.delay('第二个')
print(result.id)
