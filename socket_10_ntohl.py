# ntohl
# 32비트의 정수를 받으면 '네트워크 바이트 순서'에서 '호스트 바이트 순서'로 바꾸어 주는 함수
import socket

# 1bit * 8 = 1byte
# 2byte = 16bits

# 32bits = 8bits * 4 = 4bytes

# 940803
print(socket.ntohl(940803))

# 4바이트 단위의 스와프 연산
