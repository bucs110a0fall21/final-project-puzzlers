# import pygame


# class Player(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         super().__init__()
#         self.speed = 9
#         self.image = pygame.transform.scale(pygame.image.load('assets/totoro.png'), (90, 54))
#         self.rect = self.image.get_rect()

#         self.rect.x = x
#         self.rect.y = y

#         self.is_jumping = True
#         self.is_falling = True

#     def move_up(self):
#         """
#         sets the moving up function for the player
#         args: self
#         return: none
#         """
#         self.rect.y -= self.speed
#     def move_left(self):
#         """
#         sets moving the player left
#         args: self
#         return: none
#         """
#         self.rect.x -= self.speed
#     def move_right(self):
#         """
#         sets moving the player right
#         args: self
#         return: none
#         """
#         self.rect.x += self.speed
        
#     def update(self):
#         dx = 0
#         dy = 0
#         walk_coodwon = 5

#         key = pygame.key.get_pressed()
#         if key[pygame.K_SPACE] and self.jumped == False:
#             self.vel_y = -15
#             self.jumped = True
#         if key[pygame.K_SPACE] == False:
#             self.jumped = False
#         if key[pygame.K_LEFT]:
#             dx -= 5
#             self.counter += 1
#             self.direction = -1
#         if key[pygame.K_RIGHT]:
#             dx += 5
#             self.counter += 1
#             self.direction = 1
#         if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
#             self.counter = 0
#             self.index = 0
#             if self.direction == 1:
#                 self.image = self.images_right[self.index]
#             if self.direction == -1:
#                 self.image = self.images_left[self.index]

#         self.vel_y += 1
#         if self.vel_y > 10:
#             self.vel_y = 10
#         dy += self.vel_y

#         for tile in platform.tile_list:
#             if tile[i].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
#                 if self.vel_y < 0:
#                     dy = tile[1].bottom - self.rect.top
#                     self.vel_y = 0
#                 elif self.vel_y >= 0:
#                     dy = tile[1].top - self.rect.bottom
#                     self.vel_y = 0