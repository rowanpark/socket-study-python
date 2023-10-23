# gethostname
# 현재 동작중인 머신의 호스트 이름을 가져와 반환해주는 함수
import socket

print(socket.gethostname())  # 호스트네임만
print(socket.getfqdn())  # 호스트네임 + 그 컴퓨터에 설정된 도메인정보
# 맥에선 똑같았음

# 127.0.0.1

print(socket.gethostbyname(socket.gethostname()))
print(socket.gethostbyname(socket.getfqdn()))
