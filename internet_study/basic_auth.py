#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request, parse
import base64

URL = "http://app.yao.com"
USERNAME = "libai"
PASSWORD = "libai"


def handler_version(url):
    password_mgr = request.HTTPPasswordMgrWithDefaultRealm()
    handler = request.HTTPBasicAuthHandler(password_mgr)
    netloc = parse.urlparse(url)[1]
    handler.add_password(realm=None,
                         uri=netloc,
                         user=USERNAME,
                         passwd=PASSWORD)

    basic_opener = request.build_opener(handler)
    request.install_opener(basic_opener)
    return url


def header_version(url):
    req = request.Request(url)
    raw = '%s:%s' % (USERNAME, PASSWORD)
    # base64_str = encodebytes(raw.encode('utf-8')).decode('ascii')
    base64_str = base64.b64encode(raw.encode()).decode()
    req.add_header('Authorization', 'Basic %s' % base64_str)
    return req


# for func_type in ['header']:
for func_type in ['handler', 'header']:
    print("eval %s_version" % func_type)
    url = eval('%s_version' % func_type)(URL)
    rsp = request.urlopen(url)
    print(rsp.read().decode('utf-8'))
    rsp.close()
    request.urlcleanup()

    # 'Basic bGliYWk6bGliYWk='
    # raw = "%s:%s" % (user, pw)
    # auth = "Basic " + base64.b64encode(raw.encode()).decode("ascii")
