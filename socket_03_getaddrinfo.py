# getaddrinfo
# 소켓을 만들 때 필요한 모든 인자를 제공해주는 함수
import socket

# res = socket.getaddrinfo('kbs.co.kr', 80)
res = socket.getaddrinfo('kbs.co.kr', 80, socket.AF_INET, socket.SOCK_STREAM, flags=socket.AI_CANONNAME)
print(res)

# (family, type, proto, canonname, sockaddr)
# canonname: 우리가 알기 쉽게 명명해 놓은 이름
# sockaddr: ip주소와 포트번호로 이루어진 튜플

sock = socket.socket(*res[0][:3])
print(sock)
