# socket
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 주소 패밀리(소켓이 사용할 네트워크 주소의 형태), 소켓의 타입
# AF_INET: 기본값, 상수로 정의, ipv4기반
# SOCK_STREAM: 기본값, 상수로 정의, 소켓통신을 할 때 신뢰성 있게 (순차적으로 보내고 순차적으로 도착)
# SOCK_DGRAM: 상수로 정의, 소켓통신을 할 때 신뢰성 없게 (순차적으로 보내더라도 비순차적으로 도착)
print(sock)