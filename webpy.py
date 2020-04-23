# -*- coding: utf-8 -*-
# __author__: MUSIBII
# __email__ : shaozuanzuan@gmail.com
# __file__  : webpy.py
# __time__  : 2019-05-25 16:22


import webtest

urls = (
    '/(.*)', 'hello',
)

app = webtest.application(urls, globals())


class hello:
    def GET(self, name):
        print(self.__dict__, 1)
        for k, v in self.__dict__.items():
            print('%15s: %s' % (k, v))
        if not name:
            name = 'World'

        return 'Hello, ' + name + '!'


if __name__ == '__main__':
    app.run()
