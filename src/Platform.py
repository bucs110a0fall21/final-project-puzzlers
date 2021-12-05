import pygame
import sys

color = (0, 255, 0)

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, file):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('asserts/block.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.image.set_colorkey(color)
        self.rect.y = y
        self.rect.x = x
                    
