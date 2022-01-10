from pygame.sprite import Sprite

from config import net_color
from field.positionable import Positionable
from utils.image import create_image


class Net(Sprite, Positionable):

    def __init__(self, width=10, height=580, field_with=800):
        super().__init__()

        self.image = create_image(width, height, net_color)
        self.rect = self.image.get_rect()
        self.set_position(self.__x(field_with, width), width)

    def __x(self, field_with, width):
        return (field_with - width) // 2
