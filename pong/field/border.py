from pygame.sprite import spritecollide, Group, Sprite

from config import white
from field.bound_to_ball import BoundToBall
from field.positionable import Positionable
from utils.image import create_image
from utils.soundplayer import SoundPlayer


class Border(Sprite, Positionable, BoundToBall):
    def __init__(self, x, y, width, height):
        super().__init__()

        self.image = create_image(width, height, white)
        self.rect = self.image.get_rect()
        self.set_position(x, y)

    def update(self):
        collisions = spritecollide(self, Group(self.ball), False)
        if len(collisions):
            self.ball.vertical_bounce()
            self.hit()

    @staticmethod
    def hit():
        SoundPlayer().play('table-hit')
