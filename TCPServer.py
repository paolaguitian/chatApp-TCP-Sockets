
from socket import socket, AF_INET, SOCK_STREAM

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 12001

serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("Interrupted by CTRL-C")
while True:
	try:
		connectionSocket, addr = serverSocket.accept()
		print("Connection from %s port %s" % addr)
		message = connectionSocket.recv(2048)
		message = message.upper()
		connectionSocket.send(message)
		connectionSocket.close()
	except KeyboardInterrupt:
		print("Interrupted by CTRL-C")
		break
serverSocket.close()