import pygame


class Friend(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('assets/friend.png'), (160, 180))

        self.rect = self.image.get_rect()
        self.rect.x = 1000 # Placeholder locations
        self.rect.y = 20
