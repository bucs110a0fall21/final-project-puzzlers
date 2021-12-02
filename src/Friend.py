import pygame


class Friend(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('assets/friend.png')

        self.rect = self.image.get_rect()
        self.rect.x = 184 # Placeholder locations
        self.rect.y = 134
