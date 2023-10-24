# listen
# 소켓이 다른 호스트로부터의 접속을 기다리도록 하는 함수
import socket

sock = socket.socket()
sock.bind(('127.0.0.1', 6030))
sock.listen()  # 한개의 인자 -> backlog(백로그): 시스템이 커버할 수 있는 연결의 갯수
# sock.listen(5): 5개까지는 추가적인 연결을 받아들이되 그 이상의 연결은 거부하라
