# getpeername
# 연결된 클라이언트 소켓 객체에 대해서
# 그 소켓 객체가 원격에서 어떤 호스트(ip)와 어떤 포트를 사용하는지 반환해주는 메서드
# getsockname
# 소켓 서버가 동작중인 ip와 listening 중인 포트를 반환
import socket

sock = socket.socket()
sock.bind(('127.0.0.1', 6030))
sock.listen()

while True:
    conn, address = sock.accept()
    print(conn)
    print(conn.getpeername())
    print(conn.getsockname())
