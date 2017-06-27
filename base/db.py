#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'study',
    'password': 'study',
    'host': '127.0.0.1',
    'database': 'test',
    'raise_on_warnings': True,
    'use_pure': True
}

root_config = {
    'user': 'root',
    'password': 'yaolei313',
    'host': '127.0.0.1',
    'database': 'test',
    'raise_on_warnings': True,
    'use_pure': True
}

TEST_DB_NAME = 'test2'

tables = {}
tables['administrative_divisions'] = """
CREATE TABLE `administrative_divisions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` int(11) NOT NULL COMMENT '国家定义行政区划编码',
  `name` varchar(32) NOT NULL COMMENT '国家定义行政区划名称',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB COMMENT='国家行政区划'
"""


def create_database(cursor, db_name):
    try:
        cursor.execute('create database {} '.format(db_name))
    except mysql.connector.Error as err:
        print("Fail create database: {}".format(err))
        exit(1)
    else:
        print("create database: {}", db_name)


try:
    # cnx = mysql.connector.connect(user='study', password='study', host='127.0.0.1', database='test')
    cnx = mysql.connector.connect(**root_config)
    print("current database %s" % cnx.database)
    cursor = cnx.cursor()

    try:
        cnx.database = TEST_DB_NAME
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor, TEST_DB_NAME)
            cnx.database = TEST_DB_NAME
        else:
            print(err)
            exit(1)

    print("current database %s" % cnx.database)

    for name, ddl in tables.items():
        try:
            print('create table {}: '.format(name), end='')
            cursor.execute(ddl)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print('table already exists.')
            else:
                print(err.msg)
        else:
            print("created")

    cursor.close()
    cnx.close()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('error username or password')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('error database name')
    else:
        print(err)
else:
    print('no exception')
    cnx.close()
finally:
    print('final')
