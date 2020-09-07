# -*- coding: utf-8 -*-
from fabric import Connection

# result = Connection('www.baidu.com').run('uname -s', hide=True)
# msg = "Ran {0.command!r} on {0.connection.host}, got stdout:\n{0.stdout}"
# print(msg.format(result))


c = Connection('172.16.253.125', user='root', port=22,
               connect_kwargs={"key_filename": ['/Users/musibiis/.ssh/vm_centos']})
c.run('uname -s')
# c.sudo
# 上传本地文件到远程服务器
c.put('__init__.py', '/opt')
# print(c)

