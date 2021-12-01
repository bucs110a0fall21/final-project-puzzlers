import sys
import pygame
from src import puzzle
import os

#Esther wrote
class Controller:
  #creates the screen with a set width and height (square)
  #initializes Sprite functionality
  def __init__(self, width=1280, height=720):
    """
    Initilizes width, height, screen, background, background color and font (Incomplete)
    args: self, width, height
    returns: none
    """
    pygame.init()
    self.width = width
    self.height = height
    self.screen = pygame.display.set_mode((self.width, self.height))
    self.background = pygame.Surface(self.screen.get_size()).convert()
    self.background.fill((255, 0, 0)) #sets background to white
    pygame.display.update()
    pygame.font.init()
    pygame.key.set_repeat(1, 50)

    self.pieces = pygame.sprite.Group() #set each piece into a group
    num_pieces = 8 #Will just use this to control movement for all pieces
    self.state = "Incomplete"

  def handle_collide(self):
    # I referred to each of these images as the location they should be in when the puzzle is solved.
    # This function should spawn them in (random?) incorrect locations
    top_left = pygame.image.load('assets', 'image_part_001.jpg')
    top_mid = pygame.image.load('assets', 'image_part_002.jpg')
    mid_left = pygame.image.load('assets', 'image_part_004.jpg')
    mid_mid = pygame.image.load('assets', 'image_part_005.jpg')
    mid_right = pygame.image.load('assets', 'image_part_006.jpg')
    bottom_left = pygame.image.load('assets', 'image_part_007.jpg')
    bottom_mid = pygame.image.load('assets', 'image_part_008.jpg')
    bottom_right = pygame.image.load('assets', 'image_part_009.jpg')

    #self.screen.blit(top_left, (0, 0)) #repeat for the rest

    #checks to see if you can move an image to a space, if space is occupied, nothing happens
    #collide = pygame.sprite.spritecollide(self.puzzle, self.puzzle2, True)
    if top_left.colliderect(top_mid, mid_left, mid_mid, mid_right, bottom_left, bottom_mid, bottom_right):
      #cancel movement/ don't allow movement

  def mainloop(self):
    """
    sets game states 
    args: self
    returns: none
    """
    while True:
      if(self.state == "Incomplete"):
        self.gameLoop()
      elif(self.state == "Complete"):
        self.gameOver()

  def gameLoop(self):
    while self.state == "Incomplete":
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        #add in code where you click a piece of the image to choose to move
        if event.type == pygame.KEYDOWN:
          if (event.key == pygame.K_UP):
            self.puzzle.move_up()
          elif(event.key == pygame.K_DOWN):
            self.puzzle.move_down()
          elif(event.key == pygame.K_LEFT):
            self.puzzle.move_left()
          elif(event.key == pygame.K_RIGHT):
            self.puzzle.move_right()

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