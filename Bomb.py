import threading
import pygame
import BomberMan
import State

class Bomb(threading.Thread):
    def __init__(self,bomberman):
        self.timer = 10
        self.clock = pygame.time.Clock()
        self.game=bomberman
        self.running=1
        threading.Thread.__init__(self)

    def taruh(self,x,y):
        self.x=x
        self.y=y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def countdown(self):
        self.timer = self.timer - 1

    def getTimer(self):
        return self.timer

    def explode(self,peta):
        for i in range(3):
            if self.x + i >= 11:
                break
            if peta[self.x + i][self.y] == '1':
                break

            peta[self.x + i][self.y] = '@'

        for i in range(3):
            if self.x - i < 0:
                break
            if peta[self.x - i][self.y] == '1':
                break

            peta[self.x - i][self.y] = '@'

        for i in range(3):
            if self.y + i >= 16:
                break
            if peta[self.x][self.y+i] == '1':
                break

            peta[self.x][self.y+i] = '@'

        for i in range(3):
            if self.y - i <0:
                break
            if peta[self.x][self.y-i] == '1':
                break

            peta[self.x][self.y-i] = '@'

        return peta

    def put_grass(self,peta):
        for i in range(3):
            if self.x + i >= 11:
                break
            if peta[self.x + i][self.y] == '1':
                break

            peta[self.x + i][self.y] = '0'

        for i in range(3):
            if self.x - i < 0:
                break
            if peta[self.x - i][self.y] == '1':
                break

            peta[self.x - i][self.y] = '0'

        for i in range(3):
            if self.y + i >= 16:
                break
            if peta[self.x][self.y+i] == '1':
                break

            peta[self.x][self.y+i] = '0'

        for i in range(3):
            if self.y - i <0:
                break
            if peta[self.x][self.y-i] == '1':
                break

            peta[self.x][self.y-i] = '0'

        return peta

    def run(self):
        while(self.running):
            print ("now running...."+str(self.getTimer()))
            self.clock.tick(10)
            if (self.getTimer()>0):
                self.countdown()
            else:
                self.game.peta_game=self.explode(self.game.peta_game)
                for delay in range(3):
                    self.clock.tick(10)

                self.put_grass(self.game.peta_game)
                if self.game.player.isDead(self.x,self.y):
                    self.game.changeState(State.State.GAME_OVER)
                self.running = 0