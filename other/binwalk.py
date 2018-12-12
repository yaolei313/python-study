#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
import binwalk

if __name__ == "main":
    lst = sys.argv
    if len(lst) < 2:
        print("no file choose")
        exit(-1)
    try:
        if lst[1][0] == "-":
            binwalk.scan(*lst[2:], signature=lst[1])
        else:
            binwalk.scan(*lst[1:], signature=True)
    except Exception as error:
        print(error)
