# -*- coding: utf-8 -*-
# __author__: MUSIBII
# __email__ : shaozuanzuan@gmail.com
# __file__  : check_result.py
# __time__  : 2019-05-26 15:06

from celery.result import AsyncResult
from celery_task.celery import cel


asyncresult = AsyncResult(id='97d0f7a1-d6f6-436c-8887-593a6cf68f48', app=cel)

if asyncresult.successful():
    result = asyncresult.wait()
    print(result)

elif asyncresult.failed():
    print('执行失败')
elif asyncresult.status == 'PENDING':
    print('任务等待中被执行')

elif asyncresult.status == 'RETRY':
    print('任务异常中正在重试')

elif asyncresult.status == 'STARTED':
    print('任务已经开始被执行')

