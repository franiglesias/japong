from pygame.sprite import Sprite

from config import net_color
from field.positionable import Positionable
from utils.image import create_image


class Net(Sprite, Positionable):

    def __init__(self):
        super().__init__()

        self.image = create_image(10, 580, net_color)
        self.rect = self.image.get_rect()
        self.set_position(395, 10)
