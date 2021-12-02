from src import Player
from src import Friend

import pygame
import sys
import os


# from pygame.locals import *

class Controller:
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 1000
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        self.fps = 60
        pygame.font.init()
        pygame.init()

        self.state = "GAME"
        FOREST = pygame.image.load(os.path.join('assets', 'forestbackground.png'))


    def mainloop(self):
        while self.state == "GAME":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_UP):
                        self.Player.move_up()
                    elif(event.key == pygame.K_DOWN):
                        self.Player.move_down()
                    elif(event.key == pygame.K_LEFT):
                        self.Player.move_left()
                    elif(event.key == pygame.K_RIGHT):
                        self.Player.move_right()

        pygame.display.update()
        self.screen.blit(FOREST, (0,0))



pygame.quit()