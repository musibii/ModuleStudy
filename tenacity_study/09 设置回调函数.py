# -*- coding: utf-8 -*-
# __file__  : 08 设置回调函数.py
# __time__  : 2020/7/20 11:09 AM

from tenacity import *

def return_last_value(retry_state):
    print("执行回调函数")
    return retry_state.outcome.result()  # 表示返回原函数的返回值

def is_false(value):
    return value is False

@retry(stop=stop_after_attempt(3),
       retry_error_callback=return_last_value,
       retry=retry_if_result(is_false))
def test_retry():
    print("等待重试中...")
    return False

print(test_retry())