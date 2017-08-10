#!/usr/bin/env python3
# -*- encoding:utf-8 -*-
import threading
from time import ctime, sleep


def loop(msg, nsec):
    print("ready run.at {}".format(ctime()))
    sleep(nsec)
    print("finished. message:{}, at {}".format(msg, ctime()))


msgs = ['hello world', 'no zuo no die']
threads = []
for i in range(len(msgs)):
    t = threading.Thread(target=loop, args=(msgs[i], i + 5))
    threads.append(t)

for ti in threads:
    ti.start()

for ti in threads:
    ti.join()

print('all task finished.at {}'.format(ctime()))
