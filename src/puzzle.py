#Ashley
class Puzzle(pygame.sprite.Sprite):
  def __init__(self, name, x, y, image):
    self.image = pygame.image.load(image).convert_alpha()
    self.rect = self.image.get_rect()
    self.x = x
    self.y = y
    self.name = name + str(id(self))
    self.speed = 10

   def move_up(self):
        self.rect.y -= self.speed

    def move_down(self):
        self.rect.y += self.speed

    def move_left(self):
        self.rect.x -= self.speed

    def move_right(self):
        self.rect.x += self.speed


