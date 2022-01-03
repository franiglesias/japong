import pygame

from config import net_color
from utils.image import create_image


class Net(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = create_image(10, 580, net_color)
        self.rect = self.image.get_rect()
        self.__set_position(395, 10)

    def __set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y
