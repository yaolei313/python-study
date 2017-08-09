#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

from twisted.internet import protocol, reactor

HOST = '127.0.0.1'
PORT = 9100


class TSClientProtocol(protocol.Protocol):
    def send_data(self):
        imsg = input("please input message:\n")
        if imsg:
            print('sending {0}'.format(imsg))
            self.transport.write(imsg.encode('utf-8'))
        else:
            self.transport.loseConnection()

    def connectionMade(self):
        print('connection made')
        #self.send_data()

    def dataReceived(self, data):
        imsg = str(data, encoding='utf-8')
        print("receive message:", imsg)
        self.send_data()


class TSClientFactory(protocol.ClientFactory):
    protocol = TSClientProtocol
    clientConnectionFailed = clientConnectionLost = lambda self, connector, reason: reactor.stop()

    def __init__(self):
        pass

print('start client')
reactor.connectTCP(HOST, PORT, TSClientFactory())
reactor.run()
