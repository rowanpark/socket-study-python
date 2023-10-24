# accept
import socket

sock = socket.socket()
sock.bind(('127.0.0.1', 6030))
sock.listen()

while True:
    # res = sock.accept()
    conn, address = sock.accept()
    # res = (conn, address)
    # conn: 클라이언트와의 연결을 위한 새로운 소켓 객체
    # address = (host, port)
    # host: ip 정보
    # port: 포트 정보

    print(conn)
    print(address)
