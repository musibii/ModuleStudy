# -*- coding: utf-8 -*-
# __author__: MUSIBII
# __email__ : shaozuanzuan@gmail.com
# __file__  : result.py
# __time__  : 2019-05-26 11:27

from celery.result import AsyncResult
from celery_app_task import cel


asyncresult = AsyncResult(id='83fba363-e826-4ae7-99a8-b272c639f6bb', app=cel)

if asyncresult.successful():
    result = asyncresult.get()
    print(result)
elif asyncresult.failed():
    print('执行失败')

elif asyncresult.status == 'PENDING':
    print('任务等待被执行')

elif asyncresult.status == 'RETRY':
    print('任务异常后正在重试')
elif asyncresult.status == 'STARTED':
    print('任务已经开始被执行')