import pygame


class Friend:
    def __init__(self, x, y):
        self.image = pygame.transform.scale(pygame.image.load('assets/friend.png'), (184, 134))

        self.rect = self.image.get_rect()
        self.rect.x = x # Placeholder locations
        self.rect.y = y
