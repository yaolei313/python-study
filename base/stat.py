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

list(range(3,10))