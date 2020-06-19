# -*- coding: utf-8 -*-
# __author__: MUSIBII
# __email__ : shaozuanzuan@gmail.com
# __file__  : __init__.py.py
# __time__  : 2019-05-26 10:10

# from celery.task.sets import TaskSet
from concurrent.futures.thread import ThreadPoolExecutor

from celery.backends.database import TaskSet

# TaskSet()

executor = ThreadPoolExecutor(max_workers=8)
import requests
import time
import aiohttp

# async def get_request():
#     r = await aiohttp.get(
#         "get",
#         "http://127.0.0.1:9001/api/v1/plugins/jala/qrcode/checkout/query?buyer_token=buyer_token_N8ohn6za2wpl14rxVWnmYFSbACHaBays&unique_code=oYSuZ5fNM-m5nY69KXFTPa5BuamI&shop_id=219&coupon_code_list=5039162079&activity_type=normal&track_code=",
#     )
#     print(r)
#
#
# for i in range(1000):
#     # a = executor.submit(
#     #     get_request,
#     #     "http://127.0.0.1:9001/api/v1/plugins/jala/qrcode/checkout/query?buyer_token=buyer_token_N8ohn6za2wpl14rxVWnmYFSbACHaBays&unique_code=oYSuZ5fNM-m5nY69KXFTPa5BuamI&shop_id=219&coupon_code_list=5039162079&activity_type=normal&track_code=",
#     # )
#     await get_request()
#     # print(r.status_code)


import aiohttp
import asyncio


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        for i in range(1000):
            html = await fetch(
                session,
                "http://127.0.0.1:9001/api/v1/plugins/jala/qrcode/checkout/query?buyer_token=buyer_token_N8ohn6za2wpl14rxVWnmYFSbACHaBays&unique_code=oYSuZ5fNM-m5nY69KXFTPa5BuamI&shop_id=219&coupon_code_list=5039162079&activity_type=normal&track_code=",
            )
            print(html)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
asyncio.sleep()

# {
#     "headers": {
#         "Accept": "*/*",
#         "Accept-Encoding": "gzip, deflate",
#         "Connection": "close",
#         "Host": "httpbin.org",
#         "User-Agent": "Python/3.6 aiohttp/3.2.1",
#     }
# }

# 我们的例子不涉及服务端
