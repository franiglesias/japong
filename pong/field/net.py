import pygame

from config import net_color


class Net(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((10, 580))
        self.image.fill(net_color)

        self.rect = self.image.get_rect()
        self.rect.y = 10
        self.rect.x = 395

    def update(self):
        self.image.fill(net_color)
