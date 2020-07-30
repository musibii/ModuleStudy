# -*- coding: utf-8 -*-
# __file__  : login.py
# __time__  : 2020/7/28 4:30 PM

import requests
import time
import json

base_url = 'https://pk.baicizhan.com/api/rankpk/challenge/match?challenge_type=word&challenge_level=wood&time={}&activity_id=0&session_id=9'.format(
    time.time())
request_header = {'Content-Type': 'text/plain; charset=UTF-8',
                  'Origin': 'https://pk.baicizhan.com',
                  'Refer': 'https://pk.baicizhan.com/pages/challenge/index.html',
                  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
                  'cookie': 'access_token=g50BTz%2F9VaRj1tVRcY1eXDc9TJQiC4pypO37HbUuxEY%3D'
                  }

res = requests.get(base_url, headers=request_header)
print(res.text)
print(res.headers)
print(res.status_code)

if res.status_code == 200 and res.text['data']['again'] == '':
    import time
    time.clock()
