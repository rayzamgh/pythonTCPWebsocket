import struct

ganja = 129

print(struct.pack('????????', (ganja >> 7), (ganja & 64)  >> 6, (ganja & 32) >> 5, (ganja & 16) >> 4, (ganja & 8) >> 3, (ganja & 4) >> 2, (ganja & 2) >> 1, ganja & 1))
