# -*- coding: utf-8 -*-
# __file__  : tenacity_06.py
# __time__  : 2020/7/20 11:08 AM

from requests import exceptions
from tenacity import retry, retry_if_exception_type

@retry(retry=retry_if_exception_type(exceptions.Timeout))
def test_retry():
    print("等待重试...")
    raise exceptions.Timeout

test_retry()