#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections


str2 = 'hello \n world'
print(str2)
print("%r" % str2)
print(r'hello \n world')
print("{0}-{1}".format("北京", "上海"))
print("%s-%s" % ("北京", "上海"))
print(str2[0:1])


str3 = 4 * ' ' + 'hello libai'
print(str3)

str4 = str2 + str3
print("%r" % str4)

# number string list
a, b = 0, 1
while b < 10:
    print(b, sep='\t', end=' ')
    a, b = b, a + b
print("\n")
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

print('-------------')


def make_inc(n):
    """
    study summary.

    :param n: int
    :return: function
    """
    return lambda x: x + n


def make_inc2(n):
    """study summary.

    :param n: int
    :return: function
    """
    return lambda x: x + n


func1 = make_inc(10)
print(func1(1))
print(func1(2))

pairs = [(12, "hello"), (21, "world"), (5, "libai")]
pairs.sort(key=lambda pair: pair[0])
print(pairs)
dict2 = dict(pairs)
print(dict2)


def f(ham: str, eggs: str = 'eggs') -> str:
    print("annotations:", f.__annotations__)
    print("argument:", ham, eggs)
    return ham + ' and ' + eggs


f('spam')


lst1 = [22, 33, 12, 5, 7, 16, 21]
queue = collections.deque(lst1)
item = queue.popleft()
print(item)

lst2 = list(map(lambda x: x ** 2, range(10)))

lst3 = [(x, y) for x in [1, 2, 3] for y in [2, 3, 4] if x != y]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

[[row[i] for row in matrix] for i in range(3)]

dict1 = {'hello': 'world'}
dict1.keys()