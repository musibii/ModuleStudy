# -*- coding: utf-8 -*-
# __author__: musibii
# __file__  : test01.py
# __time__  : 2019-06-23 19:11

from tornado.concurrent import Future
import tornado.gen


import motor
db = motor.MotorClient().test

@tornado.gen.coroutine
def loop_example(collection):
    cursor = db.collection.find()
    while (yield cursor.fetch_next):
        doc = cursor.next_object()
        print(doc)

if __name__ == '__main__':
    loop_example(db)