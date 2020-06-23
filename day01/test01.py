# -*- coding: utf-8 -*-
# __author__: MUSIBII
# __email__ : shaozuanzuan@gmail.com
# __file__  : test01.py
# __time__  : 2019-05-09 12

import tornado.ioloop
import tornado.web

__all__ = ["func"]


def func(args1, args2):
    return args1 * args2


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def make_app():
    return tornado.web.Application([(r"/", MainHandler),])


# if __name__ == "__main__":
#     app = make_app()
#     app.listen(8888)
#     tornado.ioloop.IOLoop.current().start()
