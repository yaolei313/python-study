#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request

#url = "https://www.chiphell.com/portal.php"
url = "http://www.baidu.com/"

request = urllib.request.Request(url)

response = urllib.request.urlopen(request)

data = response.read()

# 设置解码方式
data = data.decode('utf-8')

# 打印结果
print(data)

# 打印爬取网页的各类信息

print(type(response))
print(response.geturl())
print(response.info())
print(response.getcode())
