# getservbyport
# getservbyname의 반대 기능을 하는 함수
# 포트번호를 주면 그 포트번호를 사용하는 프로토콜의 이름을 반환하는 함수
import socket

print(socket.getservbyport(80))   # http
print(socket.getservbyport(8080))   # http
print(socket.getservbyport(443))  # https
print(socket.getservbyport(21))   # ftp
print(socket.getservbyport(990))  # ftps
print(socket.getservbyport(22))   # ssh
print(socket.getservbyport(23))   # telnet
print(socket.getservbyport(25))   # smtp
print(socket.getservbyport(465))  # igmpv3lite
print(socket.getservbyport(110))  # pop3
print(socket.getservbyport(143))  # imap

print(socket.getservbyport(3306))  # imap
print(socket.getservbyport(5432))  # imap
