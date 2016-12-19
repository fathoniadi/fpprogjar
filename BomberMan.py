import pygame
import Bomb
import GameMap
import Player
import State
import socket
import threading
import select
import PackageServer
import PackageClient

class SenderThread(threading.Thread):
    def __init__(self, socket):
        threading.Thread.__init__(self)
        self.client=socket

    def prepare(self,data):
        self.data=data

    def run(self):
        packetclient = PackageClient.PackageClient()
        data = packetclient.serialization(self.data)
        self.client.sendall(data.encode('utf-8'))


class Client(threading.Thread):
    def __init__(self,game):
        threading.Thread.__init__(self)
        self.host = 'localhost'
        self.port = 5000
        self.threads = []
        self.open_socket()
        self.game=game

    def sendall(self,data):
        sender=SenderThread(self.client)
        sender.prepare(data)
        sender.start()

    def open_socket(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host,self.port))

    def receiveOnce(self):
        msg=self.client.recv()
        return (msg.decode())

    def run(self):
        input = [self.client]
        running = 1
        while running:
            inputready, outputready, exceptready = select.select(input, [], [])
            for s in inputready:
                msg=self.client.recv()
                msg=msg.decode()
                packetclient = PackageClient.PackageClient()
                data=packetclient.deSerialization(msg)
                self.game.broadcastReceive(data)

class BomberMan():
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    def __init__(self):
        pass
        pygame.init()
        width, height = 800, 600
        self.player=Player.Player(0,0)
        self.player.x = 0
        self.player.y = 0
        self.player2 = Player.Player(0, 0)
        self.player2.x = 0
        self.player2.y = 0

        self.STATE=State.State.RUNNING
        self.list_bomb = []
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("BomberMan")
        self.client = Client(self)
        self.clock = pygame.time.Clock()
        self.packageclient=PackageClient.PackageClient()


    def initSprite(self):
        self.grass = pygame.transform.scale(pygame.image.load("./assets/grass.png"),(50,50))
        self.wall = pygame.transform.scale(pygame.image.load("./assets/wall.png"), (50, 50))
        self.box = pygame.transform.scale(pygame.image.load("./assets/box.png"), (50, 50))
        self.p1 = pygame.transform.scale(pygame.image.load("./assets/player1.png"), (50, 50))
        self.p2 = pygame.transform.scale(pygame.image.load("./assets/player2.png"), (50, 50))
        self.bomb = pygame.transform.scale(pygame.image.load("./assets/bomb.png"), (50, 50))
        self.explosion = pygame.transform.scale(pygame.image.load("./assets/explosion.png"), (50, 50))
        self.gameover = pygame.transform.scale(pygame.image.load("./assets/gameover.png"), (800, 600))

    def changeState(self,state):
        self.STATE=state

    def startGame(self):
        data=self.packageclient.startGame(self.room)
        self.client.sendall(data)
        response = self.client.receiveOnce()
        response = self.packageclient.deSerialization(response)
        self.player.initPlayer(response)
        if (self.player.file_player=="player1"):
            self.player2.file_player="player2"
        if (self.player.file_player == "player2"):
            self.player2.file_player = "player1"


    def initRoom(self,room):
        data=self.packageclient.createGame(room)
        self.client.sendall(data)
        response = self.client.receiveOnce()

        return (response)

    def connectRoom(self,room):
        data = self.packageclient.connectToRoom(room)
        self.client.sendall(data)
        response=self.client.receiveOnce()
        status = self.packageclient.deSerialization(response)
        if status['success']:
            self.room = room

        return (response)

    def gameOver(self):
        self.screen.blit(self.gameover, [0, 0])
        pygame.display.flip()
        for i in range(10):
            self.clock.tick(10)

        exit()

    def broadcastReceive(self,data):
        print (data)
        if (self.player.file_player=="player1"):
            enemy_x=data['player2X']
            enemy_y = data['player2Y']
            self.player2.x=enemy_x
            self.player2.y=enemy_y
            self.player2.file_player="player2"

        if (self.player.file_player=="player2"):
            enemy_x=data['player1X']
            enemy_y = data['player1Y']
            self.player2.x=enemy_x
            self.player2.y=enemy_y
            self.player2.file_player = "player1"

    def update(self):
        self.initSprite()
        self.gm = GameMap.GameMap()
        self.peta_game = self.gm.createMap("./assets/peta/map.txt")
        self.client.start()

        while(self.STATE==State.State.RUNNING):
            self.clock.tick(15)
            self.screen.fill(0)
            location=self.packageclient.location(self.player.x,self.player.y,self.player.file_player,self.room)
            self.client.sendall(location)

            self.up=pygame.key.get_pressed()[pygame.K_w]
            self.down = pygame.key.get_pressed()[pygame.K_s]
            self.left = pygame.key.get_pressed()[pygame.K_a]
            self.right = pygame.key.get_pressed()[pygame.K_d]
            self.space = pygame.key.get_pressed()[pygame.K_SPACE]

            if (self.space):
                self.peta_game[self.player.x][self.player.y]='!'
                bomb=Bomb.Bomb(self)
                bomb.start()

            if (self.up):
                if (self.player.x-1>=0 and self.peta_game[self.player.x-1][self.player.y]=='0' ):
                    self.player.x=self.player.x-1
            if (self.down):
                if (self.player.x+1<11 and self.peta_game[self.player.x+1][self.player.y]=='0' ):
                    self.player.x = self.player.x + 1
            if (self.left):
                if (self.player.y-1>=0 and self.peta_game[self.player.x][self.player.y-1]=='0' ):
                    self.player.y = self.player.y - 1
            if (self.right):
                if (self.player.y+1<16 and self.peta_game[self.player.x][self.player.y+1]=='0' ):
                    self.player.y = self.player.y + 1

            for i in range(len(self.peta_game)):
                for j in range(len(self.peta_game[i])):

                    if i==self.player.x and j==self.player.y:
                        if (self.player.file_player=="player1"):
                            self.screen.blit(self.p1, [j * 50, i * 50])
                        elif (self.player.file_player == "player2"):
                            self.screen.blit(self.p2, [j * 50, i * 50])

                    elif i == self.player2.x and j == self.player2.y:
                        if (self.player2.file_player == "player1"):
                            self.screen.blit(self.p1, [j * 50, i * 50])
                        elif (self.player2.file_player == "player2"):
                            self.screen.blit(self.p2, [j * 50, i * 50])

                    elif self.peta_game[i][j] == '0':
                        self.screen.blit(self.grass, [j*50, i*50])
                    elif self.peta_game[i][j] == '1':
                        self.screen.blit(self.wall,[j*50,i*50])
                    elif self.peta_game[i][j] == '2':
                        self.screen.blit(self.box,[j*50,i*50])
                    elif self.peta_game[i][j] == '!':
                        self.screen.blit(self.bomb,[j*50,i*50])
                    elif self.peta_game[i][j] == '@' :
                        self.screen.blit(self.explosion,[j*50,i*50])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            pygame.display.flip()

        self.gameOver()