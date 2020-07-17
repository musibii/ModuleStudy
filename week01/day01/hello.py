# -*- coding: utf-8 -*-
# __author__: musibii
# __file__  : hello.py
# __time__  : 2020/2/28 10:08 AM

from tornado import web
import tornado
from tornado.options import define, parse_command_line


class MainHandler(web.RequestHandler):
    def put(self):
        self.set_header("Content-Type", "application/json")
        self.write({'name': 'musibii'})


def make_app():
    return web.Application(
        [
            (r'/index', MainHandler),
        ]
    )


if __name__ == '__main__':

    app = make_app()
    app.listen(8080)
    from tornado import ioloop
    tornado.ioloop.IOLoop.current().start()
    from tornado.platform.asyncio import AsyncIOMainLoop
