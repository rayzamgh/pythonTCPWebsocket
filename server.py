import socket
import base64
import hashlib

HOST = '127.0.0.1'
PORT = 65432

class WebSocketRoutes():
	
	# conn, addr = self.sock.accept()
	def __init__(self):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind((HOST,PORT))
		self.sock.listen()
	# 	self.endpoints = dict()
	
	# def addElem(self, key, endpoint):
	# 	self.endpoints.update({key : endpoint})
	
	# def getEndpoint(self, key):
	# 	return self.endpoints.get(key, False)

	# def failEndpoint(self, key):
	# 	self.getEndpoint(key).close()

class endpoint():

	def __init__(self, key):


	def close():



class frame():

	def __init__(self, isfin, ):

		
	

ws = WebSocketRoutes()

while (True):

	conn, addr = self.sock.accept()

	ws.addElem()


	data = conn.recv(1024)
	str = data.decode('utf-8')
	if (str.lower().find("upgrade: websocket") != -1 and str.lower().find("connection: upgrade") != -1 and str.lower().find("http/1.1") != -1 and str.lower().find("get /") != -1):
		proc = str.split("\r\n")
		conn.
		res = ""
		for i in proc:
			if (i.lower().find("sec-websocket-key") != -1):
				res = i
				break
		res = res.split(":")
		print("res")
		print(res)
		hashobj = hashlib.sha1((res[1]+"258EAFA5-E914-47DA-95CA-C5AB0DC85B11").encode())
		
		key = base64.b64encode(hashobj.hexdigest().encode()).decode()
		output = "HTTP/1.1 101 Switching Protocols\r\n"+"Upgrade: websocket\r\n"+"Connection: Upgrade\r\n"+"Sec-WebSocket-Accept: "+ key + "\r\n"
	else:
		output = b'Bad Request'
	if not(data):
		print("OUT PEPEGE")
		print(output)
		print(str)
		conn.close()
		break
		pass
	conn.sendall(output.encode())