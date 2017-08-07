#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from socket import *

HOST = '127.0.0.1'
PORT = 9100
BUF_SIZE = 1024

cli_socket = socket(AF_INET, SOCK_STREAM)
cli_socket.connect((HOST, PORT))

while True:
    send_data = input("please input message:\n")
    if not send_data:
        break
    cli_socket.send(send_data.encode('utf-8'))
    recv_data = cli_socket.recv(BUF_SIZE)
    if not recv_data:
        print('receive data.', recv_data)
    else:
        print('nothing receive')

cli_socket.close()
