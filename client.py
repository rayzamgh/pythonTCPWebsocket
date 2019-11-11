import socket

HOST = "127.0.0.1"
PORT = 65432

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST,PORT))
test = "GET /chat HTTP/1.1\r\n"+"Host: example.com:8000\r\n"+ "Upgrade: websocket\r\n" +"Connection: Upgrade\r\nSec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==\r\n"+"Sec-WebSocket-Version: 13\r\n"
sock.sendall(bytes(test, 'utf-8'))
data = sock.recv(1024)
sock.close()
str = data.decode('utf-8')

print('Received\n\r', data.decode('utf-8'))