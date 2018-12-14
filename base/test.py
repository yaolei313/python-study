#!/usr/bin/env python3
# -*- coding: utf-8 -*-

sql_template0 = """alter table _shadow_orders_{0}_ modify fingerprint text DEFAULT '' COMMENT '下单fingerprint';"""


if __name__ == '__main__':
    for index in range(0, 50):
        print(sql_template0.format(index))

    print("------")
    for index in range(50, 100):
        print(sql_template0.format(index))