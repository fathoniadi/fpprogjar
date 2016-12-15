import pygame
import Bomb
import GameMap
import Player
import State

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
        self.list_bomb = []
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("BomberMan")

        self.clock = pygame.time.Clock()
        self.initSprite()
        self.STATE=State.State.RUNNING
        self.gm=GameMap.GameMap()
        self.peta_game = self.gm.createMap("./assets/peta/map.txt")

    def initSprite(self):
        self.grass = pygame.transform.scale(pygame.image.load("./assets/grass.png"),(50,50))
        self.wall = pygame.transform.scale(pygame.image.load("./assets/wall.png"), (50, 50))
        self.box = pygame.transform.scale(pygame.image.load("./assets/box.png"), (50, 50))
        self.p1 = pygame.transform.scale(pygame.image.load("./assets/player1.png"), (50, 50))
        self.bomb = pygame.transform.scale(pygame.image.load("./assets/bomb.png"), (50, 50))
        self.explosion = pygame.transform.scale(pygame.image.load("./assets/explosion.png"), (50, 50))
        self.gameover = pygame.transform.scale(pygame.image.load("./assets/gameover.png"), (800, 600))

    def changeState(self,state):
        self.STATE=state

    def gameOver(self):
        self.screen.blit(self.gameover, [0, 0])
        pygame.display.flip()
        for i in range(10):
            self.clock.tick(10)

        exit()

    def update(self):
        while(self.STATE==State.State.RUNNING):
            self.clock.tick(15)
            self.screen.fill(0)
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
                        self.screen.blit(self.p1, [j * 50, i * 50])
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