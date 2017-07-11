#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector
import gzip
from urllib import request
from urllib import response
from mysql.connector import errorcode

req_headers = {
    # 'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    # 'Cache-Control': 'no-cache',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip'
}

# 若设置了gzip压缩会导致返回\x1f\x8B，参照如下文章
# https://stackoverflow.com/questions/5131985/why-urllib-returns-garbage-from-some-wikipedia-articles

req = request.Request(url="http://www.stats.gov.cn/tjsj/tjbz/xzqhdm/201608/t20160809_1386477.html",
                      headers=req_headers, method='GET')
# with request.urlopen(req) as rsp:
#     text = rsp.read().decode('UTF-8')
#     print('text:{}'.format(text))


with request.urlopen(req) as rsp:
    print(rsp.info())
    print(rsp.geturl())
    print(rsp.getcode())
    if rsp.info().get('Content-Encoding') == 'gzip':
        text = gzip.decompress(rsp.read())
    else:
        text = rsp.read().decode('UTF-8')
    print('text:{}'.format(text))

config = {
    'user': 'study',
    'password': 'study',
    'host': '127.0.0.1',
    'database': 'test2',
    'raise_on_warnings': True,
    'use_pure': True
}

try:
    cnx = mysql.connector.connect(**config)
    print("current database:{}", cnx.database)

    cursor = cnx.cursor()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        print('db not exists')
    else:
        print(err)
else:
    print('success')
