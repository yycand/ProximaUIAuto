#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json

from elasticsearch import Elasticsearch

es = Elasticsearch(
    ["192.168.21.82"],
    sniff_on_start=True,  # 连接前测试
    sniff_on_connection_fail=True,  # 节点无响应时刷新节点
    sniff_timeout=60  # 设置超时时间
)


# 获取一条记录
def get_one_data(indexes, ides, typees):
    res = es.get(indexes, ides, typees)
    return res
