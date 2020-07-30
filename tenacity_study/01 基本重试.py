# -*- coding: utf-8 -*-
# __file__  : tenacity_01.py
# __time__  : 2020/7/20 11:04 AM

from tenacity import retry

@retry
def tes_retry():
    print("等待重试，重试无间隔执行...")
    raise Exception

tes_retry()