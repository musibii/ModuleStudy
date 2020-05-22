# -*- coding: utf-8 -*-
# __author__: musibii
# __file__  : test_01.py
# __time__  : 2020/5/14 9:45 下午

from flask import Flask

app = Flask(__name__)

@app.route('/demo', methods=['GET'])
def demo():
    return 'gunicorn and flask demo'


# if __name__ == '__main__':
#     a = set((1,2))
#     b = set((2,3))
#
#     a = a | b
#
#     print(a)
import gunicorn

