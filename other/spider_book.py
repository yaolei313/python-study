#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import string
import gzip
import json
from urllib import request
from scrapy.selector import Selector

page_count = 12

spider_url_template = "https://api-mit.xxx.com/library/books/?%23%2Febooks=&limit=9&page={0}&type=ebook"

req_headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip',
    'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8,ja;q=0.7,zh-TW;q=0.6,de;q=0.5',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjUyODgsInNzb19pZCI6MjUyODgsImxvZ2luIjoieWFvbGVpMDIiLCJuYW1lIjoi5aea56OKIiwiZXhwaXJlc19hdCI6MTUyNjYzNzUxMCwiaWF0IjoxNTI1NDI3OTEwfQ.TkX_KiA9Va2zLDPLcY4mtVu8aLNAE0XwIkbWG9BVabk',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'Host': 'api-mit.xxx.com',
    'Origin': 'https://book.xxx.com',
    'Pragma': 'no-cache',
    'Referer': 'https://book.xxx.com/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}


def spider_books():
    book_lst = []
    for index in range(1, 13):
        url = spider_url_template.format(index)
        print("url is %s" % url)
        req_category = request.Request(url=url, headers=req_headers, method='GET')
        with request.urlopen(req_category) as rsp_category:
            if rsp_category.info().get('Content-Encoding') == 'gzip':
                body = gzip.decompress(rsp_category.read()).decode('UTF-8')
            else:
                body = rsp_category.read().decode('UTF-8')
        book_page_lst = json.loads(body)
        for book in book_page_lst:
            book_meta = dict()
            book_meta['title'] = book['title']
            book_meta['url'] = book['ebook']['url']
            book_lst.append(book_meta)
    return book_lst


def is_pdf_file(file_name):
    if file_name.endswith('.pdf'):
        return True
    return False


def get_exists_books(file_dir='/Users/yaolei/OneDrive/StudyBook'):
    books = []
    for root, dirs, files in os.walk(file_dir):
        if dirs:
            for sub_dir_name in dirs:
                sub_dir = os.path.join(root, sub_dir_name)
                tmp_books = get_exists_books(sub_dir)
                books.extend(tmp_books)
        if files:
            books.extend(filter(is_pdf_file, files))
    return books


def is_already_exists(name, exists_list):
    for item in exists_list:
        if item.find(name) != -1:
            return True
    return False


if __name__ == "__main__":
    all_books = spider_books()
    print('all books:{}'.format(all_books))
    exists_books = get_exists_books()
    print('exists books:{}'.format(exists_books))

    target_directory = '/Users/yaolei/OneDrive/tmp/'
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
    downloads = []
    for ebook in all_books:
        if not is_already_exists(ebook['title'], exists_books):
            ebook_filename = target_directory + ebook['title'] + '.pdf'
            downloads.append(ebook['title'] + '.pdf')
            ebook_download_url = request.quote(ebook['url'], safe=string.printable)
            request.urlretrieve(ebook_download_url, ebook_filename)
    print('download book {}'.format(len(downloads)))
