# echo client
import socket

client = socket.socket()

client.connect(('127.0.0.1', 6543))
# client.send(b'Hello Python Network Programming')  # 영어는 앞에 b만 붙여주면 됨
client.send('Hello Python Network Programming'.encode('utf-8'))  # 인코딩 해서 보내야 함

print(client.recv(1024))

# https://twistedmatrix.com
