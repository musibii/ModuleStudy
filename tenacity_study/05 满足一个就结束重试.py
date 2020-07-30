# -*- coding: utf-8 -*-
# __file__  : tenacity_05.py
# __time__  : 2020/7/20 11:08 AM

from tenacity import retry, stop_after_delay, stop_after_attempt

@retry(stop=(stop_after_delay(10) | stop_after_attempt(7)))
def test_retry():
    print("等待重试...")
    raise Exception

test_retry()