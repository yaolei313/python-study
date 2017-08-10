#!/usr/bin/env python3
# -*- encoding:utf-8 -*-
import threading
from time import ctime, sleep


class MyThread(threading.Thread):
    def __init__(self, func, args, name):
        super().__init__(target=func, args=args)
        self.name = name

    def run(self):
        print("ready run")
        super().run()


def loop(msg, nsec):
    cur_thread = threading.current_thread()
    print("ready run {}-{}.at {}".format(cur_thread.ident, cur_thread.name, ctime()))
    sleep(nsec)
    print("finished. message:{}, at {}".format(msg, ctime()))


msgs = ['hello world', 'no zuo no die']
threads = []
for i in range(len(msgs)):
    t = MyThread(loop, (msgs[i], i + 5), "thread" + str(i))
    threads.append(t)

for ti in threads:
    ti.start()

for ti in threads:
    ti.join()

print('all task finished.at {}'.format(ctime()))
