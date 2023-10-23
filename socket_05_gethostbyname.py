# gethostbyname
# 도메인을 주면 그 도메인에 해당하는 ip를 돌려주는 함수
import socket

print(socket.gethostbyname('naver.com'))
print(socket.gethostbyname('google.co.kr'))
print(socket.gethostbyname('8.8.8.8'))
print(socket.gethostbyname('netshot.co.kr'))  # 현재 유지보수중인 웹사이트... :) (231019 기준)

print(socket.gethostbyname(socket.getfqdn()))  # 현재 유지보수중인 웹사이트... :) (231019 기준)
