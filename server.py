import socket
import base64
import hashlib
import threading
import struct

HOST = 'localhost'
PORT = 6969
OPCODETYPES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    #  |Opcode  | Meaning                             | Reference |
    # -+--------+-------------------------------------+-----------|
    #  | 0      | Continuation Frame                  | RFC 6455  |
    # -+--------+-------------------------------------+-----------|
    #  | 1      | Text Frame                          | RFC 6455  |
    # -+--------+-------------------------------------+-----------|
    #  | 2      | Binary Frame                        | RFC 6455  |
    # -+--------+-------------------------------------+-----------|
    #  | 8      | Connection Close Frame              | RFC 6455  |
    # -+--------+-------------------------------------+-----------|
    #  | 9      | Ping Frame                          | RFC 6455  |
    # -+--------+-------------------------------------+-----------|
    #  | 10     | Pong Frame                          | RFC 6455  |
    # -+--------+-------------------------------------+-----------|

def sendText(str):
	sendframe = frame(FIN=1, OPCODE=1, Data=str.encode())

def listofbintoint(lista):
	res = int("".join(str(x) for x in lista), 2) 
	return res

def inttolistofbin(inta):
	initlist = [int(x) for x in bin(inta)[2:]]
	for x in range(4 - len(initlist)):
		initlist.insert(0, 0)

	return initlist

def hexdecoder(onebyte):
	decodedbinarray = []

	binarray = struct.pack('????????', (onebyte) >> 7, (onebyte & 64)  >> 6, (onebyte & 32) >> 5, (onebyte & 16) >> 4, (onebyte & 8) >> 3, (onebyte & 4) >> 2, (onebyte & 2) >> 1, (onebyte & 1))

	[decodedbinarray.append(i) for i in binarray]

	return(decodedbinarray)

class frame():

	def __init__(self, FIN=0, RSV1=0, RSV2=0, RSV3=0, OPCODE=0, MASK=0, Data=0): 
		headerbytes = []
		headerbytes.append(FIN)
		headerbytes.append(RSV1)
		headerbytes.append(RSV2)
		headerbytes.append(RSV3)
		headerbytes.extend(inttolistofbin(OPCODE))
		headerbytes.append(MASK)
		
		print(headerbytes, "headerbytes")
		header = listofbintoint(headerbytes)
		print(header, "headerint")

def framedecode(inpframe):
	
	locframe 	= bytearray()
	locframe 	= inpframe
	allbin 		= []
	# print(locframe)
	
	for i in locframe:
		allbin.extend(hexdecoder(i))

	return allbin

def arrofinttoint(arrint):
	opc = []
	for i in arrint:
		opc.append(str(i))

	return ''.join(opc)

def framedecompose(inpframe):

	opc = []
	ppg = []
	allbin = framedecode(inpframe)
	
	for i in allbin:
		ppg.append(str(i))

	stringrep = [''.join(ppg)]

	FIN = allbin[0]
	RSV1 = allbin[1]
	RSV2 = allbin[2]
	RSV3 = allbin[3]
	
	OPCODE = inpframe[0] & 15

	# if OPCODE not in OPCODETYPES:
	# 	sendfailpacket()

	MASK = allbin[8]
	
	# if MASK != 1:
	# 	sendfailpacket()

	SMALLLEN = arrofinttoint(allbin[9:16])
	TESTSMALLEN = inpframe[1] & 127
	bytecon = 2
	if TESTSMALLEN > 125:
		if TESTSMALLEN == 126:
			SMALLLEN = arrofinttoint(allbin[16:(16+16)])
			TESTSMALLEN = int.from_bytes(inpframe[2:4], 'big')
			bytecon = 4
		elif TESTSMALLEN == 127:
			SMALLLEN = arrofinttoint(allbin[16:(16+64)])
			TESTSMALLEN = int.from_bytes(inpframe[4:10], 'big')
			bytecon = 10
		else :
			print("LENGTH ERROR")
	MASKINGKEY = inpframe[bytecon:bytecon + 4]
	bytecon2 = bytecon + 4

	DECODED = []
	DECODEDBYTE = bytearray()
	
	# for (var i = 0; i < ENCODED.length; i++) {
	# 	DECODED[i] = ENCODED[i] ^ MASK[i % 4];
	# }

	PAYLOAD = inpframe[bytecon2:bytecon2+TESTSMALLEN]
	print(PAYLOAD, "payload")
	print(len(PAYLOAD), "lenpayload")
	print(PAYLOAD[0], "firstpayload")

	for i in range(len(PAYLOAD)):
		# print("pepegessssss")
		# print(PAYLOAD[i])
		# print(MASKINGKEY[i % 4])
		DECODED.append(PAYLOAD[i] ^ MASKINGKEY[i % 4])

	DECODEDBYTE = bytearray(DECODED)
	print()
	print()
	print("==========================================")
	print("OPCODE test")
	print(FIN, "FIN")
	print(RSV1, "RSV1")
	print(OPCODE, "OPCODE")
	print(MASK, "MASK")
	print(SMALLLEN, "smallen")	
	print(TESTSMALLEN, "testsmallen")
	print(MASKINGKEY, "maskinky")
	print(DECODEDBYTE, "decoded")
	print("OPCODE done")
	print("==========================================")
	print()
	print()

	return(FIN, OPCODE, MASK, DECODEDBYTE)
		

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
			
			data = conn.recv(9999)
			
			print("PepeGOOOO")

			FIN, OPCODE, MASK, DECODEBYTE = framedecompose(data)

			#!echo 
			if DECODEBYTE.decode()[:5] == "!echo":
				print(DECODEBYTE.decode()[6:])
				
				sendText(DECODEBYTE.decode()[6:])

			if not(data):
				self.closeconn()
				break

	def closeconn(self):
		pass
		
	
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
