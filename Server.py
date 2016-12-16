import socket
import threading
import sys
import select
import PackageServer
import PackageClient
from collections import defaultdict

list_room = defaultdict(dict)

class BombermanServer:
    def __init__(self):
        self.host = 'localhost'
        self.port = 5000
        self.backlog = 5
        self.size = 1024
        self.server = None
        self.threads = []
        self.list_room=[]

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

    def send(self,data):
        serverpackage=PackageServer.PackageServer()
        data=serverpackage.serialization(data)
        self.client.send(data.encode('utf-8'))

    def run(self):
        running = 1
        while running:
            print ("Client  : ", self.client)
            msg = self.client.recv(1024)
            msg=msg.decode()
            packageserver=PackageServer.PackageServer()
            packageclient=PackageClient.PackageClient()
            data=packageclient.deSerialization(msg)
            if (not data):
                self.client.close()
                running = 0
            print (data)
            if data['code']==1:
                list_player=[]
                list_room[data['room']]['listPlayer']=list_player
                self.send(packageserver.createPackageResponse("Created room " + str(data['room']),True))
                print ("Room created : ",list_room)

            elif data['code']==2:
                if not list_room[data['room']]:
                    self.send(packageserver.createPackageResponse("Not found room "+str(data['room']),False))
                    continue

                if len(list_room[data['room']])>2:
                    self.send(packageserver.createPackageResponse("Room is full", False))
                    continue

                list_room[data['room']]['listPlayer'].append(self.client)
                print("Connected to room : ", list_room[data['room']])
                self.send(packageserver.createPackageResponse("Connected to room " + str(data['room']),True))

            elif data['code']==100:
                print ("Starting room .... ",data['room'])
                pos=-1
                idx=0
                for i in list_room[data['room']]['listPlayer']:
                    print("Listing ... ",i)
                    if (i==self.client):
                        pos=idx
                        break
                    idx+=1

                player_name=""
                x=-1
                y=-1
                if (pos==1):
                    player_name="player1"
                    x=0
                    y=0
                elif (pos==2):
                    player_name = "player2"
                    x = 10
                    y = 15

                data=packageserver.createPackageInitGame(data['room'],player_name,x,y)
                print (data)
                self.send(data)

server=BombermanServer()
server.run()