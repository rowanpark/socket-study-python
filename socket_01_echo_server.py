# echo server, echo client
import socket

server = socket.socket()
server.bind(('0.0.0.0', 6543))  # 서버에, 네트워크 카드에 바인딩
# 루프백 주소: 127.0.0.1
# 실제 네트워크 카드 주소
# 0.0.0.0 -> 모든 네트워 카드로부터 들어오는 요청 처리
server.listen()  # 요청을 기다림

conn, addr = server.accept()
# conn: 접속한 클라이언트의 커넥션 객체
# addr: 클라이언트 객체의 주소

data = conn.recv(1024)   # 1024byte
# data.isupper()
conn.send(data)
