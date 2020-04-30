# -*- coding: utf-8 -*-
# __author__: musibii
# __file__  : test1.py
# __time__  : 2020/4/29 11:05 上午

import rbac.acl
acl = rbac.acl.Registry()

acl.add_role()
acl.add_resource(acl)

acl.allow()
acl.deny()

acl.is_allowed()
