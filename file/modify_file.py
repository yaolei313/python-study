#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


SQL = """

"""

def merge_file():
    cities = []
    path = os.path.abspath("/Users/yaolei/11.txt")
    with open(path, mode='rb') as f:
        for line in f:
            array = line.decode('utf-8').split('\t')
            if len(array) == 5:
                order_uid = array[0]


if __name__ == '__main__':
    pass