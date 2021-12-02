from src import Player
from src import Friend
from src import Timer
import pygame
import sys


class Controller:
    def __init__(self):
        pygame.init()
        self.screen_width = 1280
        self.screen_height = 720
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        self.fps = 60
        pygame.font.init()

        self.state = "GAME"
        self.background = pygame.image.load('assets/forestbackground.png')

        self.player = Player.Player(500, 200)
        self.Friend = Friend.Friend(30, 40)

    def mainloop(self):
        while True:
            if(self.state == "GAME"):
                self.gameLoop()
            elif(self.state == "GAMEOVER"):
                self.gameOver()

    def gameLoop(self):
        while self.state == "GAME":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_UP):
                        self.player.move_up()
                    elif(event.key == pygame.K_DOWN):
                        self.player.move_down()
                    elif(event.key == pygame.K_LEFT):
                        self.player.move_left()
                    elif(event.key == pygame.K_RIGHT):
                        self.player.move_right()

            pygame.display.update()
            self.screen.blit(self.background, (0, 0))
            self.player.draw(self.screen)
            self.Friend.draw(self.screen)
            pygame.display.flip()

            #Set win condition
            if pygame.sprite.collide_rect(self.player, self.Friend):
                self.state = "GAMEOVER"

    def gameOver(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()




pygame.quit()