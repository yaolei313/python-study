import logging
import traceback
import math


def normalize(s):
    """
    Convert s to a normalized string
    :param s: 
    :return: 
    """
    keep = {'a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z',
            ' ', '-', "'"
            }
    result = ''
    for c in s:
        if c in keep:
            result += c
        else:
            result += ' '
    return result


def make_freq_stat(s):
    s = normalize(s)
    words = s.split()
    result = {}
    for w in words:
        if w in result:
            result[w] += 1
        else:
            result[w] = 1
    return result


def stat_file():
    fd = open('E:\download\The Life Story of an Otter.txt', 'r', encoding='utf-8')
    body = fd.read()
    num_chars = len(body)
    d = make_freq_stat(body)
    s1 = sum(d[k] for k in d)
    s2 = len(d.keys())
    print('%s %s %s' % (num_chars, s1, s2))

    lst = [(d[w], w) for w in d]
    lst.sort()
    lst.reverse()
    i = 1
    for (count, word) in lst[:10]:
        print('%2s %4s %s' % (i, count, word))
        i += 1


def stat_file_line():
    num_chars = 0
    d = {}
    with open('E:\download\The Life Story of an Otter.txt', 'r', encoding='utf-8') as fd:
        for line in fd:
            num_chars += len(line)
            t_d = make_freq_stat(line)
            for item in t_d:
                if item in d:
                    d[item] += t_d[item]
                else:
                    d[item] = t_d[item]
    s1 = sum(d[k] for k in d)
    s2 = len(d.keys())
    print('{} {} {}', (num_chars, s1, s2))
    lst = [(d[w], w) for w in d]
    lst.sort()
    lst.reverse()
    i = 1
    for (count, word) in lst[:10]:
        print('%2s %4s %s' % (i, count, word))
        i += 1


def ask_retry(prompt, retries=2, reminder="please try again"):
    while True:
        ok = input(prompt).lower()
        if ok in ('y', 'yes'):
            return True
        elif ok in ('n', 'no'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


print(f(0))
print(f(1))
print(f(2))
print('-------------')
str1 = "hello world,li bai!"
print(normalize(str1))

stat_file()
print('-------------')
# stat_file_line()
# print('-------------')
# try:
#     ask_retry("input y to end")
# except ValueError as e:
#     # logging.error(e)
#     logging.exception("error message")

list(range(3, 10))


def fib(n):
    a, b = 0, 1
    while b < n:
        print(a, end=' ')
        a, b = b, a + b


def fib2(n):
    a, b = 0, 1
    result = []
    while b < n:
        result.append(a)
        a, b = b, a + b
    return result


fib(10)
print(*fib2(10))


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


def f(ham: str, eggs: str = 'eggs') -> str:
    print("annotations:", f.__annotations__)
    print("argument:", ham, eggs)
    return ham + ' and ' + eggs


f('spam')

import collections

lst1 = [22, 33, 12, 5, 7, 16, 21]
queue = collections.deque(lst1)
item = queue.popleft()
print(item)

lst2 = list(map(lambda x: x ** 2, range(10)))

lst3 = [(x, y) for x in [1, 2, 3] for y in [2, 3, 4] if x != y]

matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

[[row[i] for row in matrix] for i in range(4)]


