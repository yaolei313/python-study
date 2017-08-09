#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from twisted.internet import protocol, reactor
from time import ctime

PORT = 9100


class TsProtocol(protocol.Protocol):
    def __init__(self):
        pass

    def connectionMade(self):
        msg = 'welcome to app.yao.com'
        self.transport.write(msg.encode('utf-8'))
        address = self.transport.getPeer()
        print(str(address), type(address))
        host = self.transport.getHost()
        print(str(host), type(host))
        print('connection from:', address)

    def dataReceived(self, data):
        imsg = str(data, encoding='utf-8')
        omsg = '[%s] %s' % (ctime(), imsg)
        print('ready send message:', omsg)
        self.transport.write(omsg.encode('utf-8'))


factory = protocol.Factory()
factory.protocol = TsProtocol
print('waiting for connection...')
reactor.listenTCP(PORT, factory)
reactor.run()
