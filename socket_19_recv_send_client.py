# euc-kr, utf-8
import socket

sock = socket.socket()
sock.connect(('127.0.0.1', 6030))
# sock.send('가'.encode('euc-kr'))  # 상대에게 보낼 데이터를 바이트 형태로 제공해줘야 함
sock.send('가'.encode('utf-8'))  # 상대에게 보낼 데이터를 바이트 형태로 제공해줘야 함
sock.send('나'.encode('utf-8'))  # 상대에게 보낼 데이터를 바이트 형태로 제공해줘야 함
sock.send('다'.encode('utf-8'))  # 상대에게 보낼 데이터를 바이트 형태로 제공해줘야 함
sock.send('라'.encode('utf-8'))  # 상대에게 보낼 데이터를 바이트 형태로 제공해줘야 함
sock.send('reneepark'.encode('utf-8'))  # 상대에게 보낼 데이터를 바이트 형태로 제공해줘야 함
sock.send('리니팍'.encode('utf-8'))  # 상대에게 보낼 데이터를 바이트 형태로 제공해줘야 함

# 영어와 키보드 상에 존재하는 글자는 모두 1바이트
# 한글은 euc-kr, utf-8 등으로 인코딩 가능
# euc-kr: 한 글자당 2바이트 차지  예) 대한민국 만세 -> 13bytes = 2bytes * 6 + 1byte
# utf-8: 한 글자당 3바이트 차지   예) 대한민국 만세 -> 19bytes = 3bytes * 6 + 1byte

resp = sock.recv(2)
print(resp.decode('utf-8'))

sock.close()
