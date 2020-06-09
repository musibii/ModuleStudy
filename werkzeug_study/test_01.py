# -*- coding: utf-8 -*-
# __author__: musibii
# __file__  : test_01.py
# __time__  : 2020/6/8 2:36 下午

from werkzeug.wrappers import Response


def application(environ, start_response):
    response = Response('hello world!', mimetype='text/plain')
    return response(environ, start_response)

