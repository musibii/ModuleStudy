# -*- coding: utf-8 -*-
# __author__: musibii
# __file__  : __init__.py.py
# __time__  : 2020/6/16 5:14 下午
import json

import requests

url = 'https://api.weixin.qq.com/wxa/getwxacode?access_token=35_kjbWulh46JL6T8J6W8KremIv5Jm1OM4O0qSILh6snlybZ6osKF08Mrwng0Uom0jeSJ5ZScls05YhjPSt2TrqQYWnCnCh3_OV9Yj4U9xboGwqd5_VavTb5z95qP_W_jV8raRBf6czB87aPnefTXThADDFJF'
li = [
    # 8553541,
    # 8583120,
    # 8503969,
    # 8607538,
    # 8544256,
    # 8491266,
    # 8615625,
    # 8556675,
    # 8382225,
    # 8547681,
    # 8574896,
    # 967348,
    # 8607147,
    # 8555819,
8574900,
8590450,
8600010,
8491269,
]
headers = {'content-type': 'application/json'}
for i in li:
    post_param = {}
    post_param['path'] = 'pages/dcl_before_order/goods/goods?id=312046&model_code={}'.format(i)
    # post_param['path'] = 'pages/dcl_before_order/cart/cart'
    post_param['line_color'] = {"r": 0, "g": 130, "b": 195}
    post_param['width'] = 1280
    post_param['is_hyaline'] = True
    data = json.dumps(post_param)
    response = requests.post(url, data=json.dumps(post_param), headers=headers)
    with open('{}'.format(i) + '.png', 'wb') as f:
        f.write(response.content)
    print(response)
