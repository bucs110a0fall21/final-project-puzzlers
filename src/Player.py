import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.speed = 3
        self.image = pygame.image.load('assets/totoro.png')
        self.rect = self.image.get_rect()

        self.rect.x = 90
        self.rect.y = 54

    def move_up(self):
        """
        sets the moving up function for the player
        args: self
        return: none
        """
        self.rect.y -= self.speed
    def move_down(self):
        """
        sets the moving down function for the player
        args: self
        return: none
        """
        self.rect.y += self.speed
    def move_left(self):
        """
        sets moving the player left
        args: self
        return: none
        """
        self.rect.x -= self.speed
    def move_right(self):
        """
        sets moving the player right
        args: self
        return: none
        """
        self.rect.x += self.speed
