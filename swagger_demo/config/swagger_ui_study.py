# -*- coding: utf-8 -*-
# __author__: musibii
# __file__  : swagger_ui_study.py
# __time__  : 2020/5/29 1:26 下午

import tornado.ioloop
import tornado.web
from swagger_ui import tornado_api_doc
from tornado_swagger.setup import setup_swagger
from tornado_swagger.model import register_swagger_model
from tornado_swagger.setup import export_swagger


# swagger_specification = export_swagger(routes)


@register_swagger_model
class PostModel:
    """
    ---
    type: object
    description: Post model representation
    properties:
        id:
            type: integer
            format: int64
        title:
            type: string
        text:
            type: string
        is_visible:
            type: boolean
            default: true
    """


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

class PostsDetailsHandler(tornado.web.RequestHandler):
    def get(self, posts_id):
        """
        ---
        # write swagger specification here
        """


class Application(tornado.web.Application):
    _routes = [
        tornado.web.url(r'/api/posts', MainHandler),
        tornado.web.url(r'/api/posts/(\w+)', PostsDetailsHandler),
    ]

    def __init__(self):
        setup_swagger(self._routes)
        super(Application, self).__init__(self._routes)




if __name__ == "__main__":
    app = Application()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
    # tornado_api_doc(app, config_path='config/test.yaml', url_prefix='/api/doc', title='API doc')
