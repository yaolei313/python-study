#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import *
from time import ctime

HOST = ''
PORT = 9100
BUF_SIZE = 1024

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(511)

while True:
    print('waiting connect...')
    cli_socket, address = server_socket.accept()
    print('connect from {}'.format(address))
    while True:
        data = cli_socket.recv(BUF_SIZE)
        if not data:
            break
        rsp_data = '[%s] %s' % (ctime(), str(data, encoding='utf-8'))
        cli_socket.send(rsp_data.encode(encoding='utf-8'))
    cli_socket.close()
server_socket.close()
