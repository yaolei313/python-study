#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

from concurrent.futures import ThreadPoolExecutor
from urllib.request import urlopen
from re import compile
from time import ctime
from random import randint,randrange



REGEX = compile(b'#([\d,]+) in Books')
URL = 'http://www.amazon.com/dp/'
ISBNs = {
    '0132269937': 'Core Python Programming',
    '1621573486': 'Big-Lie-Exposing-Roots-American',
    '1449319793': 'Python-Data-Analysis-Wrangling-IPython'
}


def get_ranking(isbn):
    with urlopen("{0}{1}".format(URL, isbn)) as page:
        return str(REGEX.findall(page.read())[0], 'utf-8')



def _main():
    print("at {0} on Amazon...".format(ctime()))
    with ThreadPoolExecutor(3) as executor:
        zip1 = zip(ISBNs, executor.map(get_ranking, ISBNs))
        for isbn, ranking in zip1:
            print("- %r ranked %s" % (ISBNs[isbn], ranking))
    print('all Done at:', ctime())


if __name__ == "__main__":
    _main()
