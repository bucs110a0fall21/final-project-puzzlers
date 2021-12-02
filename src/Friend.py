import pygame


class Friend:
    def __init__(self, x, y):
        self.image = pygame.image.load('assets/friend.png').convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.x = x # Placeholder locations
        self.rect.y = y
