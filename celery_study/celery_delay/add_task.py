# -*- coding: utf-8 -*-
# __author__: MUSIBII
# __email__ : shaozuanzuan@gmail.com
# __file__  : add_task.py
# __time__  : 2019-05-26 11:11
from datetime import datetime

from amqp.spec import method
from celery.local import PromiseProxy
from celery_app_task import add
# result = add.delay(3, 4)
# print(result.id, type(add))

# from celery.result import AsyncResult

# eta 事件对象，datetime 类型


# 获取一个 当地 时间
# v1 = datetime(2019, 5, 26, 15, 38, 56)
# print(v1)

# 把当地时间转成 utc 时间，如果配置了时区为当地的，就不用转直接用当地时间
# v2 = datetime.utcfromtimestamp(v1.timestamp())
# print(v2)
# result = add.apply_async(args=[1, 3], eta=v2)
# print(result.id)


# 时间转换方式二
ctime = datetime.now()
# 默认用utc时间
utc_ctime = datetime.utcfromtimestamp(ctime.timestamp())
from datetime import timedelta

# 取一个 10 秒之后的时间
time_delay = timedelta(seconds=10)
# 这个时间比当前时间晚 10 秒
task_time = utc_ctime + time_delay
result = add.apply_async(args=[5, 3], eta=task_time)




