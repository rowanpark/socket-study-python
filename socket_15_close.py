# close
# 우리가 만든 소켓 서버나 클라이언트가 더이상 사용되지 않을 때
# 만들어진 소켓 객체의 자원을 운영체제에 반환해주기 위해 사용하는 함수
import socket

sock = socket.socket()
sock.bind(('127.0.0.1', 6030))
sock.listen()

sock.close()
