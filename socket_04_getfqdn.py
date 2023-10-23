# getfqdn
# 요청받은 이름을 가지고 정규화된 도메인 이름을 반환하는 함수
# host이름이나 ip를 주고 거기에 해당하는 정확한 도메인 정보를 가져올 수 있음
import socket

print(socket.getfqdn())
# 아무것도 전달되지 않으면 실행중인 로컬 호스트 네임을 가져옴

print(socket.getfqdn('kbs.co.kr'))
print(socket.getfqdn('imbc.com'))
print(socket.getfqdn('sbs.co.kr'))
print(socket.getfqdn('naver.com'))
print(socket.getfqdn('google.co.kr'))
