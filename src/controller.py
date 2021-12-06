from src import Player
from src import Friend
from src import Timer
from src import SpikeFish
import random
import pygame
import sys


class Controller:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen_width = 1170
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        self.fps = 60

        self.state = "GAME"
        self.background = pygame.image.load('assets/background.png')

        self.player = Player.Player()
<<<<<<< HEAD
        self.Friend = Friend.Friend(30, 40)
        self.timer, self.text_timer = 10, '10'.rjust(3)
        self.font_timer = pygame.font.SysFont(None, 30)
        self.font = pygame.font.SysFont(None, 30)
=======
        self.Friend = Friend.Friend()
        self.Timer = Timer.Timer()
>>>>>>> 7834c4360732c43b18ce11c8fb67fc9c6be67352

        self.block = pygame.sprite.Group()
        num_SpikeFish = 0 #edit number of enemies
        for i in range(num_SpikeFish):
            x = random.randrange(150, 910)
            y = random.randrange(45, 510)
            self.block.add(SpikeFish.SpikeFish(x, y))

        self.waitstate = True

    def mainloop(self):
        while True:
            if(self.state == "GAME"):
                self.gameLoop()
            elif(self.state == "GAMEOVER"):
                self.gameOver()
                
    def startScreen(self):
        self.screen.fill(90, 150, 250)
        myfont = pygame.font.SysFont('comicsans', 30)
        message = myfont.render('Finding A Friend', False, (230, 240, 250))
        startmessage = myfont.render('Press space to start', False, (230, 240, 250))
        self.screen.blit(message, (self.width//3, self.height//2))
        self.screen.blit(startmessage, (self.width*1.5, self.height//2))
        pygame.display.flip()
        while self.waitstate == True:
            for event in pygame.evemt.get():
                if event.type == pygame.KEYUP:
                    self.waitstate = False
        

    def gameLoop(self):
        while self.state == "GAME":
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_UP):
                        self.player.move("up")
                    elif(event.key == pygame.K_DOWN):
                        self.player.move("down")
                    elif(event.key == pygame.K_LEFT):
                        self.player.move("left")
                    elif(event.key == pygame.K_RIGHT):
                        self.player.move("right")
                if self.player.rect.left < 0:
                    self.player.rect.left = 0
                if self.player.rect.right > self.screen_width:
                    self.player.rect.right = self.screen_width
                if self.player.rect.top <= 0:
                    self.player.rect.top = 0
                if self.player.rect.bottom >= self.screen_height:
                    self.player.rect.bottom = self.screen_height

            pygame.display.update()
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.player.image, (self.player.rect.x, self.player.rect.y))
            self.screen.blit(self.Friend.image, (self.Friend.rect.x, self.Friend.rect.y))
            self.block.draw(self.screen)
            pygame.display.flip()

            #Set win condition
            if pygame.sprite.collide_rect(self.player, self.Friend):
                self.state = "GAMEOVER"

<<<<<<< HEAD
            # collide = pygame.sprite.spritecollide(self.player, self.powerup, False)
            # if collide:
            #     self.powerup.kill()

            # pygame.display.flip()
            self.timer += 1
            self.clock.tick(60)
            timer = self.font_timer.render(str(self.timer).rjust(3), False, (0, 0, 0))
            update_text_timer = self.screen.blit(timer, (10, 10))
            pygame.display.update(update_text_timer)
=======
            # Makes SpikeFish 'repel' the player from colliding
            blocked = pygame.sprite.spritecollide(self.player, self.block, False)
            if (blocked):
                self.player.rect.x -= 1
                self.player.rect.y -= 1
>>>>>>> 7834c4360732c43b18ce11c8fb67fc9c6be67352


    def gameOver(self):
        myfont = pygame.font.SysFont('comicsans', 30)
        message = myfont.render('Congrats!', False, (0, 0, 0))
        finalTime = myfont.render(str(self.Timer.counting_string), True, (0, 0, 0))
        self.screen.blit(finalTime, (1170 / 2, 600 / 2))
        self.screen.blit(message, (1280 / 2, 720 / 2))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


pygame.quit()