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

        self.player = Player.Player(1100, 650)
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
                    elif(event.key == pygame.K_LEFT):
                        self.player.move_left()
                    elif(event.key == pygame.K_RIGHT):
                        self.player.move_right()

            pygame.display.update()
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.player.image, (self.player.rect.x, self.player.rect.y))
            self.screen.blit(self.Friend.image, (self.Friend.rect.x, self.Friend.rect.y))
            pygame.display.flip()

            #Set win condition
            if pygame.sprite.collide_rect(self.player, self.Friend):
                self.state = "GAMEOVER"

    def gameOver(self):
        myfont = pygame.font.SysFont('comicsans', 30)
        message = myfont.render('Congrats!', False, (0, 0, 0))
        self.screen.blit(message, (1280 / 2, 720 / 2))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()




pygame.quit()