# -*- coding: utf-8 -*-
# __file__  : study_o1.py
# __time__  : 2020/8/10 10:01 AM

import simdjson
doc = simdjson.loads('{"hello": "world"}')

print(type(doc))