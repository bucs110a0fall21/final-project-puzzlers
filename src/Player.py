import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 8
        self.image = pygame.transform.scale(pygame.image.load('assets/totoro.png'), (140, 100))
        self.rect = self.image.get_rect()

        self.rect.x = 50
        self.rect.y = 50

    def move(self, direction):
        """
        sets the move function for the player
        args: self
        return: none
        """
        if direction == "up":
            self.rect.y -= self.speed
        elif direction == "down":
            self.rect.y += self.speed
        elif direction == "left":
            self.rect.x -= self.speed
        elif direction == "right":
            self.rect.x += self.speed