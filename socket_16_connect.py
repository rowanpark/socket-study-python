# connect
import socket

sock = socket.socket()
sock.connect(('127.0.0.1', 6030))

sock.close()
