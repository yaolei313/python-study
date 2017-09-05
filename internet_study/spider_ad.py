#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gzip
import pypinyin
import mysql.connector
from urllib import request
from scrapy.selector import Selector
from mysql.connector import errorcode

req_headers = {
    # 'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    # 'Cache-Control': 'no-cache',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip'
}

db_config = {
    'user': 'study',
    'password': 'study',
    'host': '127.0.0.1',
    'port': 3306,
    'database': 'XXX',
    'raise_on_warnings': True,
    'use_pure': True
}

insert_sql = """
INSERT INTO `standard_city` (`code`, `name`, `pinyin`, `pinyin_ab`) VALUES (%s, %s, %s, %s)
"""


# 若设置了gzip压缩会导致返回\x1f\x8B，参照如下文章
# https://stackoverflow.com/questions/5131985/why-urllib-returns-garbage-from-some-wikipedia-articles


def get_city_level(code):
    if str(code).endswith('0000'):
        return 1
    elif code.endswith('00'):
        return 2
    else:
        return 3


def get_city_list():
    req = request.Request(url="http://www.stats.gov.cn/tjsj/tjbz/xzqhdm/201608/t20160809_1386477.html",
                          headers=req_headers, method='GET')

    with request.urlopen(req) as rsp:
        if rsp.info().get('Content-Encoding') == 'gzip':
            body = gzip.decompress(rsp.read()).decode('UTF-8')
        else:
            body = rsp.read().decode('UTF-8')

    result_list = []

    sel = Selector(text=body)
    p_sels = sel.css('div.TRS_PreAppend p.MsoNormal')
    for p_sel in p_sels:
        city_code = p_sel.css('span[lang]::text').extract_first().strip()
        city_name = p_sel.css('span[style]::text').extract_first().strip()
        py1 = pypinyin.lazy_pinyin(city_name, style=pypinyin.NORMAL)
        py2 = pypinyin.lazy_pinyin(city_name, style=pypinyin.FIRST_LETTER)
        pinyin = "".join(py1)[:64], "".join(py2)[:16]
        result_list.append((city_code, city_name, pinyin[0], pinyin[1]))
    return result_list


def save_to_db(lst):
    try:
        cnx = mysql.connector.connect(**db_config)
        cur = cnx.cursor()
        count = 0
        for item in lst:
            count += 1
            if count % 200 == 0:
                print(count)
            cur.execute(insert_sql, item)
        cnx.commit()
        cur.close()
        cnx.close()
    except mysql.connector.Error as err:
        print(err)


if __name__ == '__main__':
    city_lst = get_city_list()
    print(len(city_lst))
    save_to_db(city_lst)
