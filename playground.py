import struct

def inttolistofbin(inta):
	initlist = [int(x) for x in bin(inta)[2:]]
	for x in range(4 - len(initlist)):
		initlist.insert(0, 0)

	return initlist

print(inttolistofbin(0))