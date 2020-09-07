# -*- coding: utf-8 -*-

from fabric import SerialGroup as Group
from fabric import Connection

# 使用密码登录远程服务器

conn = Connection('172.16.253.125', user='root', port=22,
                  connect_kwargs={"password": 'musibii', 'key_filename': ['/Users/musibiis/.ssh/vm_test']})
conn.run('uname -s')