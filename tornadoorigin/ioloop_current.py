# -*- coding: utf-8 -*-
# __file__  : ioloop_current.py
# __time__  : 2020/6/30 5:45 PM

import tornado
# tornado.ioloop.IOLoop.current().start()
from decimal import Decimal

a = Decimal('3.4')
print(a.to_integral_value())
print(a.to_integral())
print(type(a.to_eng_string()))
print(a.to_integral_exact())