# -*- coding: utf-8 -*-
# __file__  : elasticsearch_01.py
# __time__  : 2020/7/13 9:40 AM

from elasticsearch import Elasticsearch, client
from datetime import datetime

# 启动 elasticsearch 服务端
# 客户端连接
es = Elasticsearch(hosts='localhost:8080')
# es.indices.create(index='index', ignore=400)  # 会将该 index 接口的返回值设为索引，不支持 datetime 格式（为了速度）
# 创建索引
resp = es.indices.create(
    index="index",
    body={
        "settings": {
            "index": {"number_of_shards": 3, "number_of_replicas": 2}
        }
    },
)
print(resp)
# 索引分区并将 body 存入
es.index(index='index', id=42, body={"any": "data", "timestamp": datetime.now()})
# 获取索引中存储的数据
es.get(index="index", id=42)['_source']
