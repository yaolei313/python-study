#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import gzip
import os
import shutil
from html.parser import HTMLParser


class MyHtmlParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag != 'a':
            pass
        if len(attrs) == 0:
            pass
        else:
            for key, value in attrs:
                if key == 'href':
                    value = value.replace(r'\'', '')
                    if value.startswith('/'):
                        value = value[1:]
                    self.links.append(value)


qcs_headers = {
    # 'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    # 'Cache-Control': 'no-cache',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/59.0.3071.115 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip'
}

search_url = 'http://qcs.sankuai.com/api/uc/order/list.ajax?cityId&driverBiz=0&driverId=&driverMobile=&endTime=20180518%2023%3A59%3A59&orderId=099748213806666142252290000055&orderStatus&orderType=meituan&pageIndex=1&pageSize=10&payStatus&startTime=20180518%2000%3A00%3A00&userId=&userMobile='
end_url = 'http://qcs.sankuai.com/api/uc/order/forceEndTrip.ajax?operatorId=25288&operatorName=%E5%A7%9A%E7%A3%8A&orderId=099748213806666142252290000055'
reqObj = urllib.request.Request(url=search_url, headers=qcs_headers, method='GET')
with urllib.request.urlopen(reqObj, timeout=2000) as rsp:
    if rsp.getcode() != 200:
        exit(-1)

    text = rsp.read()
    if rsp.info().get('Content-Encoding') == 'gzip':
        print('is gzip')
        text = gzip.decompress(text).decode('UTF-8')
    print(text)

hp = MyHtmlParser()
hp.feed(text)
hp.close()
slinks = [i if i.startswith("http") else url1 + i for i in hp.links]
print(slinks)

if not os.path.isdir(r'd:\Work\temp'):
    os.makedirs(r'd:\Work\temp')
print(os.getcwd())
os.chdir(r'd:\Work\temp')

#shutil
