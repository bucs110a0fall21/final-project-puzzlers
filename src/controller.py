from src import Player
from src import Friend
# from src import Timer
from src import SpikeFish
# from src import Button
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
        self.menubackground = pygame.Surface((self.screen_width, self.screen_height))
        self.fps = 60
        pygame.key.set_repeat(1, 50)

        # self.state = "GAME"
        self.state = "START"
        self.background = pygame.image.load('assets/background.png')

        self.player = Player.Player()
        self.Friend = Friend.Friend()
        # self.button = Button.Button()

        self.block = pygame.sprite.Group()

        num_SpikeFish = 12 #edit number of enemies
        for i in range(num_SpikeFish):
            x = random.randrange(150, 910)
            y = random.randrange(45, 510)
            self.block.add(SpikeFish.SpikeFish(x, y))

        self.waitstate = True

        self.timer, self.text_timer = 10, '10'.rjust(3)
        self.font_timer = pygame.font.SysFont(None, 30)
        self.font = pygame.font.SysFont(None, 30)

    def mainloop(self):
        # ""
        #     Checks state of the game & keeps game going until game is over
        #     args: self
        #     returns: none
        # ""
        while True:
            if(self.state == "GAME"):
                self.gameLoop()
            elif(self.state == "START"):
                self.startScreen()
            elif(self.state == "GAMEOVER"):
                self.gameOver()
    
    def startScreen(self):
        # ""
        #     displays the starting menu screen which includes start and instructions buttons
        #     args: self
        #     return: none
        # ""
        run = True
        startbutton = pygame.Rect(485, 200, 200, 100)
        instructionsbutton = pygame.Rect(485, 350, 200, 100)
        titlefont = pygame.font.SysFont("comicsans", 60)
        message = titlefont.render('Finding A Friend', False, (230, 240, 250))
        startmes = titlefont.render('Start', False, (230, 240, 250))
        instructionsmes = titlefont.render('Instructions', False, (230, 240, 250))
        while run:
            pos = pygame.mouse.get_pos()
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
            if startbutton.collidepoint(pos):
                if clicked:
                    print('start')
                    self.state = "GAME"
                    self.gameLoop()
                    run = False
            if instructionsbutton.collidepoint(pos):
                if clicked:
                    print('instructions')
                    self.instructions()
            self.screen.fill((90, 150, 250))
            pygame.draw.rect(self.screen, (60, 100, 170), startbutton)
            pygame.draw.rect(self.screen, (60, 60, 170), instructionsbutton)
            self.screen.blit(message, (415, self.screen_height//6))
            self.screen.blit(startmes, (530, 230))
            self.screen.blit(instructionsmes, (470, 370))
            pygame.display.flip()
        			
    def instructions(self):
    	#   '''
    	#   Writes out the instructions to be displayed
    	#   args: self
    	#   return: none
    	#   '''
        self.run = True
        while self.run == True:
            self.screen.fill((90, 150, 250))
            myfont = pygame.font.SysFont("comicsans", 30)
            goalmessage = myfont.render('get to your friend as fast as possible!', False, (230, 240, 250))
            instructionmessage = myfont.render('use arrow keys to move', False, (230, 240, 250))
            restartmessage = myfont.render('hit esc to restart game', False, (230, 240, 250))
            enemymessage = myfont.render('avoid the spikefish! they slow you down by repelling you >:)', False, (230, 240, 250))
            returnmessage = myfont.render('hit return to return to menu', False, (230, 240, 250))
            self.screen.blit(returnmessage, (400, self.screen_height//2 + 120))
            self.screen.blit(instructionmessage, (400, self.screen_height//2))
            self.screen.blit(goalmessage, (400, self.screen_height//2 - 120))
            self.screen.blit(restartmessage, (400, self.screen_height//2 +60))
            self.screen.blit(enemymessage, (400, self.screen_height//2 - 60))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.run = False
            pygame.display.flip()

    def gameLoop(self):
        # ""
        #     allows user to move Totoro around screen,
        #     checks for collision with spikeFish and repels user back if collides, 
        #     sets win conditions, 
        #     keep track of time took to reach friend, 
        #     redraws and updates screen
        #     args: self
        #     returns: none
        # ""
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
                    elif(event.key == pygame.K_ESCAPE):
                        self.state = "GAME"
                        self.player.rect.x = 50
                        self.player.rect. y = 50
                        self.timer = 0
                        Controller.gameLoop(self)
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

            #displays and updates the time as soon as game starts
            self.timer += 1
            # self.clock(60)
            timer = self.font_timer.render(str(self.timer/100).rjust(3), False, (0, 0, 0))
            update_text_timer = self.screen.blit(timer, (10, 10))
            pygame.display.update(update_text_timer)

            # Makes SpikeFish 'repel' the player from colliding
            blocked = pygame.sprite.spritecollide(self.player, self.block, False)
            if (blocked):
                self.player.rect.x -= 1
                self.player.rect.y -= 1

            pygame.display.flip()

    def gameOver(self):
        # ""
        #     displays game over screen, allows user to replay game or return to menu
        #     args: self
        #     return: none
        # ""
         myfont = pygame.font.SysFont('comicsans', 40)
         text_time = 0
         run = True

         while run:
             pygame.time.delay(10)
             for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                     run = False
             current_time = pygame.time.get_ticks()
             keys = pygame.key.get_pressed()
             self.screen.fill((240, 250, 240))
             for i in range (1000):
                 text_time += i
             if text_time > current_time:
                 text = myfont.render('congrats! game over', True, (0, 0, 0))
                 text2 = myfont.render('press escape to restart game; return to return to menu', True, (0, 0, 0))
                 self.screen.blit(text, (460, 200))
                 self.screen.blit(text2, (270, 260))
             pygame.display.update()
             if keys[pygame.K_ESCAPE]:
                 self.state = "GAME"
                 self.player.rect.x = 50
                 self.player.rect. y = 50
                 self.timer = 0
                 Controller.gameLoop(self)
             elif keys[pygame.K_RETURN]: #need help getting back to menu screen when return is pressed
                 self.state = "GAME"
                 self.startScreen(self)

pygame.quit()       
