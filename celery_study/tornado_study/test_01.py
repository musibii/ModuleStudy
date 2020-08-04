# -*- coding: utf-8 -*-
# __file__  : test_01.py
# __time__  : 2020/8/3 6:28 PM
from celery.backends import asynchronous
from tornado import gen, web
import tcelery, tasks

tcelery.setup_nonblocking_producer()


class AsyncHandler(web.RequestHandler):
    @asynchronous
    def get(self):
        tasks.echo.apply_async(args=['Hello world!'], callback=self.on_result)

    def on_result(self, response):
        self.write(str(response.result))
        self.finish()
