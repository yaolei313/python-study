#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

str1 = """I'm from \
beijing
My name is yaolei
"""

print(str1)

str2 = 'hello \n world'
print(str2)
print("%r" % str2)
print('%r' % str2)
print("{0}-{1}".format("北京", "上海"))
print(r'hello \n world')

str3 = 4 * ' ' + 'hello libai'
print(str3)

str4 = str2 + str3
print(str4)

# number string list
a, b = 0, 1
while b < 10:
    print(b, sep='\t', end=' ')
    a, b = b, a + b
print('====================')

# x = int(input('please input an integer'))
# if x < 0:
#     x = 0
#     print('negative change to zero')
# elif x == 0:
#     print('zero')
# elif x == 1:
#     print('single')
# else:
#     print('more')

# word = ['hello 123', 'word 123', 'test', 'libai']
# for w in word:
#     print(w, len(w))
# words = word[:]
# for w in words:
#     if len(w) > 6:
#         words.insert(0, w)

for i in range(10):
    print(i, end=' ')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(__file__)
print(BASE_DIR)