# htonl
# ntohl의 반대 기능 함수
# 호스트 바이트 순서의 숫자를 네트워크 바이트 순서로 바꿔주는 함수
import socket

# 56299008
print(socket.htonl(56299008))

print(socket.ntohl(940803))
