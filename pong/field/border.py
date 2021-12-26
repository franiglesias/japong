import pygame
from pygame.sprite import spritecollide

from config import white
from game.ball import Ball
from utils.soundplayer import SoundPlayer


class Border(pygame.sprite.Sprite):
    def __init__(self, y):
        super().__init__()

        self.image = pygame.Surface((800, 10))
        self.image.fill(white)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = 0

        self.balls = None

    def bind_ball(self, ball):
        self.balls = [ball]

    def update(self):
        collisions = spritecollide(self, self.balls, False)
        ball: Ball
        for ball in collisions:
            ball.vertical_bounce()
            self.hit()

    @staticmethod
    def hit():
        SoundPlayer().play('table-hit')
