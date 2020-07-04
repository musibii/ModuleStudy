# -*- coding: utf-8 -*-
# __file__  : http_status_s.py
# __time__  : 2020/7/1 11:07 AM
from http import HTTPStatus

class MyHTTPStatus(HTTPStatus):
    CONTINUE = 100, 'Continue', 'Request received, please continue'


if __name__ == '__main__':
    my = MyHTTPStatus('23')