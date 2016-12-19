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
        self.host = '0.0.0.0'
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
                    # ("New client connect : ",sock)
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
        self.room = -1

    def sendall(self,data):
        serverpackage=PackageServer.PackageServer()
        data=serverpackage.serialization(data)
        self.client.sendall(data.encode('utf-8'))
        #hehe
    def run(self):
        input=[]
        input.append(self.client)
        running = 1
        while running:
            inputready, outputready, exceptready = select.select(input, [], [])

            for s in inputready:
                msg = self.client.recv(1024)
                msg=msg.decode()
                packageserver=PackageServer.PackageServer()
                packageclient=PackageClient.PackageClient()
                listMsg=msg.split('}')
                for msg in listMsg:
                    if (msg==""):
                        continue
                    print(msg)
                    msg=msg+"}"
                    print (msg)
                    try:
                        data=packageclient.deSerialization(msg)

                        data['room'] = str(data['room'])
                        if (not data):
                            self.client.close()
                            running = 0

                        if data['code']==1:
                            list_player=[]
                            list_room[data['room']]['listPlayer']=list_player
                            list_room[data['room']]['location']={'player1':{'x':-1,'y':-1,'alive':False },'player2':{'x':-1,'y':-1,'alive':False }}
                            self.sendall(packageserver.createPackageResponse("Created room " + str(data['room']),True))
                            print ("Room created : ",list_room)

                        elif data['code']==2:
                            if not list_room[data['room']]:
                                self.sendall(packageserver.createPackageResponse("Not found room "+str(data['room']),False))
                                continue

                            if len(list_room[data['room']])>2:
                                self.sendall(packageserver.createPackageResponse("Room is full", False))
                                continue

                            list_room[data['room']]['listPlayer'].append(self.client)
                            print ("Connected to room : ", list_room[data['room']])
                            self.sendall(packageserver.createPackageResponse("Connected to room " + str(data['room']),True))

                        elif data['code']==100:
                            #print ("Starting room .... ",data['room'])
                            pos=-1
                            idx=0
                            for i in list_room[data['room']]['listPlayer']:
                                #print("Listing ... ",i)
                                if (i==self.client):
                                    pos=idx
                                    break
                                idx+=1

                            player_name=""
                            x=-1
                            y=-1
                            if (pos==0):
                                player_name="player1"
                                x=0
                                y=0
                            elif (pos==1):
                                player_name = "player2"
                                x = 10
                                y = 15

                            list_room[data['room']]['location'][str(player_name)]['alive']=True
                            data=packageserver.createPackageInitGame(data['room'],player_name,x,y)
                            print (data)
                            self.sendall(data)

                        elif data['code'] == 201:
                            for player in list_room[data['room']]['listPlayer']:
                                if player==self.client:
                                    continue
                                dataBomb=packageserver.createPackageNewBomb(data['x'],data['y'])
                                player.send(packageserver.serialization(dataBomb).encode('utf-8'))

                        elif data['code']==200:
                            list_room[data['room']]['location'][data['playerName']]['x']=data['x']
                            list_room[data['room']]['location'][data['playerName']]['y'] = data['y']

                            data=packageserver.createPackagePlayerLoc("player1",
                                                                 list_room[data['room']]['location']['player1']['alive'],
                                                                 list_room[data['room']]['location']['player1']['x'],
                                                                 list_room[data['room']]['location']['player1']['y'],
                                                                 "player2",
                                                                 list_room[data['room']]['location']['player2']['alive'],
                                                                 list_room[data['room']]['location']['player2']['x'],
                                                                 list_room[data['room']]['location']['player2']['y'])

                            print (data)
                            self.sendall(data)

                    except:
                        pass

server=BombermanServer()
server.run()