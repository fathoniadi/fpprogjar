import pygame

class Bomb():
    def __init__(self):
        self.timer = 1000

    def taruh(self,x,y):
        self.x=x
        self.y=y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def countdown(self):
        self.timer = self.timer - 1

    def explode(self,peta):
        if (peta[self.x][self.y]!='1' and self.x<11):
            peta[self.x][self.y]='0'
        if (peta[self.x+1][self.y] != '1' and self.x+1<11):
            peta[self.x+1][self.y] = '0'
        if (peta[self.x + 2][self.y] != '1' and self.x+2<11):
            peta[self.x + 2][self.y] = '0'
        if (peta[self.x + 3][self.y] != '1' and self.x+3<11):
            peta[self.x + 3][self.y] = '0'
        if (peta[self.x - 1][self.y] != '1' and self.x-1>=0):
            peta[self.x - 1][self.y] = '0'
        if (peta[self.x - 2][self.y] != '1' and self.x-2>=0):
            peta[self.x - 2][self.y] = '0'
        if (peta[self.x - 3][self.y] != '1' and self.x-3>=0):
            peta[self.x - 3][self.y] = '0'
        if (peta[self.x][self.y + 1] != '1' and self.y+1<16):
            peta[self.x][self.y + 1] = '0'
        if (peta[self.x][self.y + 2] != '1' and self.y+2<16):
            peta[self.x][self.y + 2] = '0'
        if (peta[self.x][self.y + 3] != '1' and self.y+3<16):
            peta[self.x][self.y + 3] = '0'
        if (peta[self.x][self.y - 1] != '1' and self.y-1>=0):
            peta[self.x][self.y - 1] = '0'
        if (peta[self.x][self.y - 2] != '1' and self.y-2>=0):
            peta[self.x][self.y - 2] = '0'
        if (peta[self.x][self.y - 3] != '1' and self.y-3>=0):
            peta[self.x][self.y - 3] = '0'

        return peta

class GameMap():
    def __init__(self):
        self.peta=[]

    def createMap(self,filePath):
        f=open(filePath,"r")
        line=f.read()
        line=line.split("\n")
        for i in range(len(line)):
            line[i]=line[i].split(" ")

        print(line)

        return line

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
        self.x = 0
        self.y = 0

        self.list_bomb=[]
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("BomberMan")

        self.clock = pygame.time.Clock()
        self.initSprite()
        gm=GameMap()
        self.peta_game = gm.createMap("./assets/peta/map.txt")

    def initSprite(self):
        self.grass = pygame.transform.scale(pygame.image.load("./assets/grass.png"),(50,50))
        self.wall = pygame.transform.scale(pygame.image.load("./assets/wall.png"), (50, 50))
        self.box = pygame.transform.scale(pygame.image.load("./assets/box.png"), (50, 50))
        self.p1 = pygame.transform.scale(pygame.image.load("./assets/player1.png"), (50, 50))

    def update(self):
        self.clock.tick(15)
        self.screen.fill(0)
        self.up=pygame.key.get_pressed()[pygame.K_w]
        self.down = pygame.key.get_pressed()[pygame.K_s]
        self.left = pygame.key.get_pressed()[pygame.K_a]
        self.right = pygame.key.get_pressed()[pygame.K_d]
        self.space = pygame.key.get_pressed()[pygame.K_SPACE]

        if (self.space):
            self.peta_game[self.x][self.y]='!'
            bomb=Bomb()
            bomb.taruh(self.x,self.y)

        if (self.up):
            if (self.peta_game[self.x-1][self.y]=='0' and self.x-1>=0):
                self.x=self.x-1
        if (self.down):
            if (self.peta_game[self.x+1][self.y]=='0' and self.x+1<16):
                self.x = self.x + 1
        if (self.left):
            if (self.peta_game[self.x][self.y-1]=='0' and self.y-1>=0):
                self.y = self.y - 1
        if (self.right):
            if (self.peta_game[self.x][self.y+1]=='0' and self.y+1<11):
                self.y = self.y + 1

        for i in range(len(self.peta_game)):
            for j in range(len(self.peta_game[i])):
                if i==self.x and j==self.y:
                    self.screen.blit(self.p1, [j * 50, i * 50])
                elif self.peta_game[i][j] == '0':
                    self.screen.blit(self.grass, [j*50, i*50])
                elif self.peta_game[i][j] == '1':
                    self.screen.blit(self.wall,[j*50,i*50])
                elif self.peta_game[i][j] == '2':
                    self.screen.blit(self.box,[j*50,i*50])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        pygame.display.flip()
