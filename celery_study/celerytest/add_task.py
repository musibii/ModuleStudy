# -*- coding: utf-8 -*-
# __author__: MUSIBII
# __email__ : shaozuanzuan@gmail.com
# __file__  : add_task.py
# __time__  : 2019-05-26 11:11
from amqp.spec import method
from celery.local import PromiseProxy
from celery_app_task import add
result = add.delay(3, 4)
print(result.id, type(add))

from celery.result import AsyncResult

