# bind
# 묶다
# 소켓을 주소 패밀리에 묶어주는 역할을 하는 함수
import socket

sock = socket.socket()
sock.bind(('127.0.0.1', 6030))
# 1~1024번 까지는 시스템에서 예약이 되어 있는 포트 번호
