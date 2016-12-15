import socket
import threading
import sys
import select


class BombermanServer:
    def __init__(self):
        self.host = 'localhost'
        self.port = 5000
        self.backlog = 5
        self.size = 1024
        self.server = None
        self.threads = []

    def open_socket(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((self.host, self.port))
        self.server.listen(5)

    def run(self):
        self.open_socket()
        input = [self.server]
        running = 1
        while running:
            inputready, outputready, exceptready = select.select(input, [], [])

            for s in inputready:

                if s == self.server:
                    sock,addr=self.server.accept()
                    print ("New client connect : ",sock)
                    c = Client(sock,addr)
                    c.start()

        self.server.close()
        for c in self.threads:
            c.join()

class Client(threading.Thread):
    def __init__(self, socket,addr):

        threading.Thread.__init__(self)
        self.client = socket
        self.address = addr
        self.size = 1024

    def run(self):
        running = 1
        while running:
            print ("Client  : ", self.client)
            data = self.client.recv(1024)
            if (not data):
                self.client.close()
                running = 0
            else:
                print(data.decode())



server=BombermanServer()
server.run()