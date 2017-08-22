#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector
from urllib import request, parse
import hashlib

MAP_PLACE_BASE_URL = 'http://api.map.baidu.com'
AK = 'uaCUvGUxh26YGXsfOBOIrbdCOCA3Q8x0'
SK = 'dC8mz04FxwlSRjr4IRuMpMZbGxcfjE2F'


# query=%E6%B1%BD%E8%BD%A6%E7%AB%99&coord_type=1&city_limit=true&region=%E6%B7%84%E5%8D%9A%E5%B8%82&output=json&ak=uaCUvGUxh26YGXsfOBOIrbdCOCA3Q8x0
# %2Fplace%2Fv2%2Fsearch%3Fquery%3D%25E6%25B1%25BD%25E8%25BD%25A6%25E7%25AB%2599%26coord_type%3D1%26city_limit%3Dtrue%26region%3D%25E6%25B7%2584%25E5%258D%259A%25E5%25B8%2582%26output%3Djson%26ak%3DuaCUvGUxh26YGXsfOBOIrbdCOCA3Q8x0dC8mz04FxwlSRjr4IRuMpMZbGxcfjE2F
# 2909731f8fe7332d006c803389accfca
# http://api.map.baidu.com/place/v2/search?query=汽车站&coord_type=1&city_limit=true&region=淄博市&output=json&ak=uaCUvGUxh26YGXsfOBOIrbdCOCA3Q8x0&sn=2909731f8fe7332d006c803389accfca


def construct_param_dict(city):
    return {
        'query': '汽车站',
        'coord_type': '1',
        'city_limit': 'true',
        'region': city,
        'output': 'json'
    }


def compute_sn(context_path, param_dict):
    param_dict['ak'] = AK
    # 2次编码，第一次%E6,再次编码会变为%25%E6
    add_ak_text = parse.urlencode(param_dict)
    text = parse.quote(context_path + add_ak_text + SK, encoding='utf-8', safe='')
    md = hashlib.md5()
    md.update(text.encode(encoding='utf-8'))
    return md.hexdigest()


def spider_station(city):
    param_dict = construct_param_dict(city)
    encoded_param = parse.urlencode(param_dict)

    sn = compute_sn('/place/v2/search?', param_dict)

    url = MAP_PLACE_BASE_URL + '/place/v2/search?' + encoded_param + '&ak=' + AK + '&sn=' + sn

    req = request.Request(url)
    rsp = request.urlopen(req)
    print(rsp.geturl())
    print(rsp.info())
    print(rsp.getcode())
    print(rsp.read().decode('UTF-8'))


def spider_division(lat, lng):
    pass


if __name__ == "__main__":
    spider_station('淄博市')
    spider_division(lat=36.792133,lng=118.008456)
