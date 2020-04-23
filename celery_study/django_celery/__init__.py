# -*- coding: utf-8 -*-
# __author__: MUSIBII
# __email__ : shaozuanzuan@gmail.com
# __file__  : __init__.py.py
# __time__  : 2019-05-26 16:16

from django.core.signals import request_started
def call(*args, **kwargs):
    return kwargs

request_started.connect(call())

