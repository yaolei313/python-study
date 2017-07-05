#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector
import os
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
    # 'database': 'study',
    'raise_on_warnings': True,
    'use_pure': True
}

TEST_DB_NAME = 'study'

tables = {}
tables['administrative_divisions'] = """
CREATE TABLE `administrative_divisions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` int(11) NOT NULL COMMENT '国家定义行政区划编码',
  `name` varchar(32) NOT NULL COMMENT '国家定义行政区划名称',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB COMMENT='国家行政区划'
"""
insert_sql = """
insert into administrative_divisions(code,name) VALUES (%s,%s)
"""


def create_database(cur, dbname):
    try:
        cur.execute('create database {} '.format(dbname))
    except mysql.connector.Error as err:
        print("Fail create database: {}".format(err))
        exit(1)
    else:
        print("create database: ", dbname)


def create_tables(cur, tbs):
    for name, ddl in tbs.items():
        try:
            print('create table {}: '.format(name), end='')
            cur.execute(ddl)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print('table already exists.')
            else:
                print(err.msg)
        else:
            print("created")


def read_file():
    cities = []
    # D:\Work\python-study\resources
    path = os.path.abspath("../resources/city.txt")
    with open(path, mode='rb') as f:
        for line in f:
            array = line.decode('utf-8').split()
            if len(array) == 2:
                cities.append(tuple(array))
    return cities


def insert(conn, cur, rows):
    try:
        for row in rows:
            cur.execute(insert_sql, row)
        conn.commit()
    except mysql.connector.Error as err:
        print(err)


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
            cursor.close()
            cnx.close()
            print(err)
            exit(1)

    print("current database ", cnx.database)

    create_tables(cursor, tables)

    insert_cities = read_file()

    print("insert cities ", insert_cities)

    insert(cnx, cursor, insert_cities)

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('error username or password')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('error database name')
    else:
        print(err)
else:
    print('no exception')
finally:
    cursor.close()
    cnx.close()
    print('final')
