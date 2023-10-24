from twisted.internet import protocol, reactor, endpoints


class Echo(protocol.Protocol):
    def dataReceived(self, data: bytes):
        self.transport.write(data)


class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()
    # protocol = Echo


endpoints.serverFromString(reactor, 'tcp:6543').listen(EchoFactory())
reactor.run()
