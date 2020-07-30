# -*- coding: utf-8 -*-
# __file__  : tenacity_02.py
# __time__  : 2020/7/20 11:07 AM

from tenacity import retry, wait_fixed

@retry(wait=wait_fixed(2))
def test_retry():
    print("等待重试...")
    raise Exception

if __name__ == '__main__':
    test_retry()