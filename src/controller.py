from src import Player
from src import Friend
# from src import Timer
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

        self.state = "START"
        self.background = pygame.image.load('assets/background.png')
        
        self.run = True

        self.player = Player.Player()
        #self.Friend = Friend.Friend(30, 40)
        
        
        self.Friend = Friend.Friend()

        self.block = pygame.sprite.Group()

        num_SpikeFish = 5 #edit number of enemies
        for i in range(num_SpikeFish):
            x = random.randrange(150, 910)
            y = random.randrange(45, 510)
            self.block.add(SpikeFish.SpikeFish(x, y))

        self.waitstate = True

        self.timer, self.text_timer = 10, '10'.rjust(3)
        self.font_timer = pygame.font.SysFont(None, 30)
        self.font = pygame.font.SysFont(None, 30)

    def mainloop(self):
        while True:
            if(self.state == "GAME"):
                self.gameLoop() 
            elif(self.state == "START"):
                self.startScreen()
            elif(self.state == "GAMEOVER"):
                self.gameOver()
                
    def startScreen(self):
    	  run = True
    	  while run:
    	  	   pos = pygame.mouse.get_pos()
    	  	   startbutton = pygame.Rect(485, self.screen_height//3, 200, 100)
    	  	   instructionsbutton = pygame.Rect(485, self.screen_height//2, 200, 100)
    	  	   self.screen.fill((90, 150, 250))
    	  	   myfont = pygame.font.SysFont('comicsans', 30)
    	  	   message = myfont.render('Finding A Friend', False, (230, 240, 250))
    	  	   self.screen.blit(message, (self.screen_width//4, self.screen_height//2))
    	  	   if startbutton.collidepoint(pos):
    	  	   	if clicked:
    	  	   		self.state = "GAME"
    	  	   		run = False
    	  	   if instructionsbutton.collidepoint(pos):
    	  	   	if clicked:
    	  	   		self.instructions()
    	  	   pygame.draw.rect(self.screen, (60, 100, 170), startbutton)
    	  	   pygame.draw.rect(self.screen, (60, 60, 170), instructionsbutton)
    	  	   clicked = False
    	  	   for event in pygame.event.get():
    	  	   	if event.type == pygame.QUIT:
    	  	   		sys.exit()
    	  	   	if event.type == pygame.KEYDOWN:
    	  	   		if event.key == pygame.K_ESCAPE:
    	  	   			sys.exit()
    	  	   	if event.type == pygame.MOUSEBUTTONDOWN:
    	  	   		if event.button == 1:
    	  	   			clicked = True
    	  	   pygame.display.flip()
        			
    def instructions(self):
    	  self.run = True
    	  while self.run == True:
    	  	   self.screen.fill((90, 150, 250))
    	  	   myfont = pygame.font.SysFont("comicsans", 30)
    	  	   instructionmessage = myfont.render('Use arrow keys to move', False, (230, 240, 250))
    	  	   self.screen.blit(instructionmessage, (self.screen_width//2, self.screen_height//2))
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
            self.block.draw(self.screen)
            pygame.display.flip()

            #Set win condition
            if pygame.sprite.collide_rect(self.player, self.Friend):
                self.state = "GAMEOVER"

            self.timer += 1
            self.clock.tick(60)
            timer = self.font_timer.render(str(self.timer).rjust(3), False, (0, 0, 0))
            update_text_timer = self.screen.blit(timer, (10, 10))
            pygame.display.update(update_text_timer)

            # Makes SpikeFish 'repel' the player from colliding
            blocked = pygame.sprite.spritecollide(self.player, self.block, False)
            if (blocked):
                self.player.rect.x -= 1
                self.player.rect.y -= 1

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