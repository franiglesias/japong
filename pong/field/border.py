from pygame.sprite import spritecollide, Group, Sprite

from config import white
from field.positionable import Positionable
from field.reacts_to_ball import ReactsToBall
from utils.image import create_image
from utils.soundplayer import SoundPlayer


class Border(Sprite, Positionable, ReactsToBall):
    def __init__(self, y):
        super().__init__()

        self.image = create_image(800, 10, white)
        self.rect = self.image.get_rect()
        self.set_position(0, y)

    def update(self):
        collisions = spritecollide(self, Group(self.ball), False)
        if len(collisions):
            self.ball.vertical_bounce()
            self.hit()

    @staticmethod
    def hit():
        SoundPlayer().play('table-hit')
