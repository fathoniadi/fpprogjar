import pygame
import Bomb
import GameMap
import Player
import State
import socket
import threading
import select

class Menu():
    def __init__(self):
        pass
        pygame.init()
        width, height = 800, 600
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("BomberMan")
        self.initSprite()

    def initSprite(self):
        self.menu = pygame.transform.scale(pygame.image.load("./assets/Background_baru.png"), (800, 600))
        self.screen.blit(self.menu,(0,0))

    def update(self): 
	while True:
        	pygame.display.flip()
            
menu=Menu()
menu.update()
