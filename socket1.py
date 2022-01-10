import socket

SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# First param: Family - Address family - assign type of address the socket can communicate with
# AF_INET - IPV4
# AF_INET6 - IPV6
# AF_UNIX - used for unix domian socket

# Second param : Type 
# SOCK_DGRAM - specifies user datagram protocol (UDP)
# SOCK_STREAM - Uses transmission control protocol (TCP)

HOST = '127.0.0.1'
PORT = 4200
SOCKET.bind((HOST, PORT))
# socket obj.bind((ip, port))

print("Listening at {}".format(SOCKET.getsockname()))

while True:
	data, clientAddress = SOCKET.recvfrom(65535)
	# 65535 Maximum size for udp datagram
	message = data.decode('ascii')
	upperCase = message.upper()
	print('The client at {} says {!r}'.format(clientAddress, message))
	data = upperCase.encode('ascii')
	SOCKET.sendto(data, clientAddress)
	