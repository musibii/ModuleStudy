# -*- coding: utf-8 -*-
# __author__: musibii
# __file__  : __init__.py.py
# __time__  : 2020/6/17 2:37 下午


with open('text.json', 'r') as f:
    import json
    a = json.loads(f.read())
    print(a)
    b = json.dumps(a)
    # f.write(b)

    with open('text1.json', 'w') as fi:
        fi.write(json.dumps(b))
    #
    # with open('text2.json', 'w') as f2:
    #     f2.write(a)
