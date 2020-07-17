# -*- coding: utf-8 -*-
# __file__  : pymysql_o1.py
# __time__  : 2020/7/14 5:51 PM

import pymysql

conn = pymysql.connect(
    host='',
    user='',
    password='',
    database='',
    charset='')

conn.cursor()