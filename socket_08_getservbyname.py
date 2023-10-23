# getservbyname
# 응용 계층에 있는 프로토콜의 이름을 주면 그 프로토콜이 사용하는 포트를 알려주는 함수
import socket

print(socket.getservbyname('http'))     # 80
print(socket.getservbyname('https'))    # 443
print(socket.getservbyname('ftp'))      # 21
print(socket.getservbyname('ftps'))     # 990
print(socket.getservbyname('ssh'))      # 22
print(socket.getservbyname('telnet'))   # 23
print(socket.getservbyname('smtp'))     # 25
# print(socket.getservbyname('smtps'))  # 465 (강의에선 떴는데 내가 실행하니 에러)
print(socket.getservbyname('pop3'))     # 110
print(socket.getservbyname('imap'))     # 143

print(socket.getservbyname('http', 'tcp'))  # 80
print(socket.getservbyname('http', 'udp'))  # 80
