import socket
import base64
import hashlib
import threading
import struct

HOST = 'localhost'
PORT = 6969

def hexdecoder(onebyte):
	decodedbinarray = []

	binarray = struct.pack('????????', (onebyte) >> 7, (onebyte & 64)  >> 6, (onebyte & 32) >> 5, (onebyte & 16) >> 4, (onebyte & 8) >> 3, (onebyte & 4) >> 2, (onebyte & 2) >> 1, (onebyte & 1))

	[decodedbinarray.append(i) for i in binarray]

	return(decodedbinarray)

# class frame():

# 	def __init__(self, FIN=0, RSV1=0, RSV2=0, RSV3=0, MASK, Maskey, Data): 

		

def framedecode(inpframe):
	
	locframe 	= bytearray()
	locframe 	= inpframe
	allbin 		= []
	print(locframe)
	
	for i in locframe:
		allbin.extend(hexdecoder(i))

	return allbin

def framedecompose(inpframe):

	ppg = []
	allbin = framedecode(inpframe)

	FIN = allbin[0]
	RSV1 = allbin[1]
	RSV2 = allbin[1]
	RSV3 = allbin[1]
	
	for i in allbin:
		ppg.append(str(i))

	opcode = [''.join(ppg)]

	print("opcode test")
	print(opcode)	
		

class endpoint():

	def __init__(self):
		self.chan = ''

	def __del__(self):
		print("TITIT")
		self.chan.close()
		print("TIlagi")

	def runforever(self, conn):
		undefined = True
		confirmed = False
		output = ''
		while (undefined):
			data = conn.recv(1024)
			str = data.decode()
			if (str.lower().find("upgrade: websocket") != -1 and str.lower().find("connection: upgrade") != -1 and str.lower().find("http/1.1") != -1 and str.lower().find("get /") != -1):
				proc = str.split("\r\n")
				res = ""
				for i in proc:
					if (i.lower().find("sec-websocket-key") != -1):
						res = i
						break
				res = res.split(":")
				print(res[1].strip().encode())
				print("res")
				print(res)
				strg = res[1].strip()+"258EAFA5-E914-47DA-95CA-C5AB0DC85B11"
				hashobj = hashlib.sha1(strg.encode())
				
				key = base64.b64encode(hashobj.digest()).decode()
				output = "HTTP/1.1 101 Switching Protocols\r\n"+"Upgrade: websocket\r\n"+"Connection: Upgrade\r\n"+"Sec-WebSocket-Accept:"+ key + "\r\n\r\n"
				confirmed = True
				self.chan = conn
			else:
				output = b'Bad Request\r\n'
				undefined = False
				self.chan = False
			
			if not(data):
				self.closeconn()

			if output:
				conn.sendall(output.encode())

			if KeyboardInterrupt:
				self.closeconn()
				break
		if(confirmed):
			print("Connection Established")
		while(confirmed):
			
			data = conn.recv(1024)
			
			print("PepeGOOOO")

			framedecompose(data)

			# print(binaryframe)

			if not(data):
				self.closeconn()
				break

	def closeconn(self):
		pass




# class frame():

# 	def __init__(self, isfin, ):

		
	
def main():
	
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.bind((HOST,PORT))
	sock.listen()
	
	threads = []

	while (True):

		print("pepege")
		conn, _ = sock.accept()

		threadconn = endpoint()
		t = threading.Thread(target=threadconn.runforever, args=[conn])
		threads.append(t)
		t.start()
		
		# if KeyboardInterrupt:
		# 	break

	
	sock.close()

main()
