import pygame
from pygame.sprite import spritecollide, Group

from config import white
from utils.image import create_image
from utils.soundplayer import SoundPlayer


class Border(pygame.sprite.Sprite):
    def __init__(self, y):
        super().__init__()

        self.image = create_image(800, 10, white)
        self.rect = self.image.get_rect()
        self.__set_position(0, y)

        self.ball = None

    def bind_ball(self, ball):
        self.ball = ball

    def update(self):
        collisions = spritecollide(self, Group(self.ball), False)
        if len(collisions):
            self.ball.vertical_bounce()
            self.hit()

    def __set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

    @staticmethod
    def hit():
        SoundPlayer().play('table-hit')
