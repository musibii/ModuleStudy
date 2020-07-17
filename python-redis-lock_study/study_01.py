# -*- coding: utf-8 -*-
# __file__  : study_01.py
# __time__  : 2020/7/8 5:17 PM
import redis_lock

lock = redis_lock.Lock(conn, "name-of-the-lock")
if lock.acquire(blocking=False):
    print("Got the lock.")
    lock.release()
else:
    print("Someone else has the lock.")
