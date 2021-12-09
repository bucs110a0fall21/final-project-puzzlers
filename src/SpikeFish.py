import pygame

class SpikeFish(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """
        initilizes the SpikeFish rect size and image as well as location
        args: self, x, y
        returns: n/a
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('assets/block2.png'), (125, 95))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

