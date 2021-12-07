from src import Player
from src import Friend
from src import Timer
# from src import Powerup
import pygame
import sys


class Controller:
    def __init__(self):
        pygame.init()
        self.screen_width = 1170
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        self.fps = 60
        pygame.font.init()

        self.state = "GAME"
        self.background = pygame.image.load('assets/background.png')
        
        self.run = True

        self.player = Player.Player()
        self.Friend = Friend.Friend(30, 40)
        
        


        # self.powerup = pygame.sprite.Group()
        # self.powerup.add(Powerup.Powerup(50, 50))
        # self.all_sprites = pygame.sprite.Group(tuple(self.powerup) + (self.player,))

    def mainloop(self):
        while True:
            if(self.state == "GAME"):
                self.gameLoop()
            elif(self.state == "GAMEOVER"):
                self.gameOver()
                
    def startScreen(self):
        position = pygame.mouse.get_pos()
    	  startbutton = pygame.Rect(self.width//3, self.height//2, 200, 100)
    	  instructionsbutton = pygame.Rect(self.width//2, self.height//2, 200, 100)
        self.screen.fill(90, 150, 250)
        myfont = pygame.font.SysFont(comicsans, 30)
        message = myfont.render('Finding A Friend', False, (230, 240, 250))
        self.screen.blit(message, (self.width//4, self.height//2))
        clicked = False
        for event in pygame.event.get():
    	      if event.type == pygame.QUIT:
    	      	sys.exit()
    	      if startbutton.collidepoint(pos):
    	      	if clicked:
    	      		gameLoop()
    	      if instructions.collidepoint(pos):
    	      	if clicked:
    	      		instructions()
    	  pygame.display.flip()
        			
    def instructions(self):
    	  self.run = True
    	  while self.run = True:
    	  	   self.screen.fill(90, 150, 250)
    	    	myfont = pygame.font.SysFont(comicsans, 30)
    	  	   instructionmessage = myfont.render('Use arrow keys to move', False, (230, 240, 250))
    	   	self.screen.blit(instructionmessage, (self.width//2, self.height//2))
    	      for event in pygame.event.get():
    	      	if event.type == pygame.QUIT:
    	      		sys.exit()
               if event.type == pygame.KEYDOWN:
               	if event.key == pygame.K_ESCAPE:
               		self.run = False
            pygame.display.flip()
        

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
            # self.screen.blit(self.powerup.image, (self.powerup.rect.x, self.powerup.rect.y))
            pygame.display.flip()

            #Set win condition
            if pygame.sprite.collide_rect(self.player, self.Friend):
                self.state = "GAMEOVER"

            # collide = pygame.sprite.spritecollide(self.player, self.powerup, False)
            # if collide:
            #     self.powerup.kill()

            # pygame.display.flip()


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