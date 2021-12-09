import pygame


class Friend(pygame.sprite.Sprite):
    def __init__(self):
        """
        initlizes friend rect size and image as well as location
        args: self
        returns: n/a
        """
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('assets/friend.png'), (160, 180))

        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 20
