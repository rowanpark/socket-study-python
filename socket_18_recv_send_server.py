# recv, send
import socket

sock = socket.socket()
sock.bind(('127.0.0.1', 6030))
sock.listen()

while True:
    conn, address = sock.accept()

    while True:
        try:
            data = conn.recv(3)  # 1바이트만 읽겠다

            if not data:
                break

            print(data)
            # print(data.decode('euc-kr'))  # 레거시
            decode_data = data.decode('utf-8')
            print(decode_data)

            conn.send('OK'.encode('utf-8'))
        except ConnectionResetError as e:
            print('ConnectionResetError: ', e)
        except BrokenPipeError as e:
            print('BrokenPipeError: ', e)
        except Exception as e:
            print('Exception: ', e)

    conn.close()
