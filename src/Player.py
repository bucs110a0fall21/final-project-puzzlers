import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 8
        self.image = pygame.transform.scale(pygame.image.load('assets/totoro.png'), (140, 100))
        self.rect = self.image.get_rect()

        self.rect.x = 50
        self.rect.y = 50

        self.isjump = True
        self.v = 10

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


    # def update(self):
    #     dx = 0
    #     dy = 0
    #     walk_coodwon = 5

        # key = pygame.key.get_pressed()
        # if key[pygame.K_SPACE] and self.jumped == False:
        #     self.vel_y = -15
        #     self.jumped = True
        # if key[pygame.K_SPACE] == False:
        #     self.jumped = False
        # if key[pygame.K_LEFT]:
        #     dx -= 5
        #     self.counter += 1
        #     self.direction = -1
        # if key[pygame.K_RIGHT]:
        #     dx += 5
        #     self.counter += 1
        #     self.direction = 1
        # if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
        #     self.counter = 0
        #     self.index = 0
        #     if self.direction == 1:
        #         self.image = self.images_right[self.index]
        #     if self.direction == -1:
        #         self.image = self.images_left[self.index]

        # self.vel_y += 1
        # if self.vel_y > 10:
        #     self.vel_y = 10
        # dy += self.vel_y

        # for tile in platform.tile_list:
        #     if tile[i].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
        #         if self.vel_y < 0:
        #             dy = tile[1].bottom - self.rect.top
        #             self.vel_y = 0
        #         elif self.vel_y >= 0:
        #             dy = tile[1].top - self.rect.bottom
        #             self.vel_y = 0