# -*- coding: utf-8 -*-
# __author__: MUSIBII
# __email__ : shaozuanzuan@gmail.com
# __file__  : run.py
# __time__  : 2019-05-26 11:14

from celery_app_task import cel

if __name__ == '__main__':
    cel.worker_main(argv=['-l=info'])