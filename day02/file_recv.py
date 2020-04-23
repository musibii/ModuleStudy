# -*- coding: utf-8 -*-
# __author__: MUSIBII
# __email__ : shaozuanzuan@gmail.com
# __file__  : file_recv.py
# __time__  : 2019-06-02 10:46

import tornado.web
import tornado.ioloop
from tornado.httputil import HTTPFile


class FileUpload(tornado.web.RequestHandler):

    def post(self):
        files = self.request.files
        img_files = files.get('img')
        if img_files:
            img_file = img_files[0]['body']
            file = open('./file.png', 'wb')
            file.write(img_file)
            file.close()
        self.write('ok')


if __name__ == '__main__':
    app = tornado.web.Application([(r'/uploadfile', FileUpload)])
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()