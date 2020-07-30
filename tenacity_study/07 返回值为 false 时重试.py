# -*- coding: utf-8 -*-
# __file__  : tenacity_07.py
# __time__  : 2020/7/20 11:09 AM

from tenacity import retry, stop_after_attempt, retry_if_result

def is_false(value):
    return value is False

@retry(stop=stop_after_attempt(3),
       retry=retry_if_result(is_false))
def test_retry():
    return False

test_retry()