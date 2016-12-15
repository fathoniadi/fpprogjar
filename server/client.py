from socket import socket, AF_INET, SOCK_STREAM
from time import sleep
host = "127.0.0.1"
port = 8000
CRLF = "\r\n"
RECV_BUFFER = 1024
data = ""

s = socket(AF_INET, SOCK_STREAM)
s.connect((host,port))

counter = 0
while True:
	counter+=1
	print counter
	s.send("From client "+str(counter))
	sleep(1)


s.close()
