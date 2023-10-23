# getprotobyname
# 인터넷 프로토콜의 이름을 받아서 그 프로토콜에 해당하는 번호를 반환해주는 함수
# 프로토콜에 해당하는 번호:
# - 프로토콜의 통신 포트 번호가 아님
# - 시스템 내부적으로 그 프로토콜이 어떤 번호를 사용하고 있는지 반환
import socket

# sock = socket.socket()

# 전송 계층 (Transport Layer)
print(socket.getprotobyname('tcp'))   # 6
print(socket.getprotobyname('udp'))   # 16
# 인터넷 계층 (Ineternet Layer) or 네트워크 계층 (Network Layer)
print(socket.getprotobyname('ip'))    # 0
print(socket.getprotobyname('icmp'))  # 1

# TCP/IP
# TCP: 전송계층에 있는 프로토콜의 이름
# IP: 인터넷계층에 있는 프로토콜의 이름

# UDP/IP

# sock = socket.socket(proto=6)
# sock = socket.socket(proto=17)
# sock = socket.socket(proto=socket.getprotobyname('tcp'))
# 기본적으로는 proto 값에 0이 할당됨

