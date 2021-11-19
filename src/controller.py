import sys
import pygame
from src import puzzle
#Esther wrote
class Controller:
  #creates the screen with a set width and height (square)
  #initializes Sprite functionality
  def __init__(self, width = 600, height = 600):
    pygame.init()
    self.width = width
    self.height = height
    self.screen = pygame.display.set_mode((self.width, self.height))
    self.background = pygame.Surface(self.screen.get_size()).convert()
    self.background.fill((250, 250, 250))#sets background to white
    pygame.font.init()
    pygame.key.set_repeat(1, 50)

  def mainloop(self):
    while True:
      if(self.state == "Incomplete"):
        self.gameLoop()
      elif(self.state == "GAMEOVER"):
        self.gameOver()

  def gameLoop(self):
    while (self.state == "Incomplete"):
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        #add in code where you click a piece of the image to choose to move
        if event.type == pygame.KEYDOWN:
          self.puzzle.move_up()
        elif(event.key == pygame.K_DOWN):
          self.puzzle.move_down()
        elif(event.key == pygame.K_LEFT):
          self.puzzle.move_left()
        elif(event.key == pygame.K_RIGHT):
          self.puzzle.move_right()
        
    #checks to see if you can move an image to a space, if space is occupied, nothing happens
    collide = pygame.sprite.spritecollide(self.puzzle, self.puzzle2, True)
    if (collide):
      for i in collide:
        if(self.puzzle.fight(i)):
          pass()#if collision, image doesn't move
        else:
          self.(#move image in direction the user choses)

  def gameOver(self):
    self.puzzle.kill()
    myfont = pygame.font.SysFont(None, 30)
    message = myfont.render(' Game Over ', False, (0, 0, 0))
    self.screen.blit(message, (self.width / 2, self.height / 2))
    pygame.display.flip()
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()