# -*- coding: utf-8 -*-
# __file__  : tenacity_04.py
# __time__  : 2020/7/20 11:08 AM

from tenacity import retry, stop_after_delay

@retry(stop=stop_after_delay(10))
def test_retry():
    print("等待重试...")
    raise Exception

test_retry()