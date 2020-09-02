import pygame
from pygame.sprite import Sprite
from pygame import Surface
from pong.config import white
from pong.config import red
from pong.config import lighten
import pong.app
import pong.config

GOAL_HIGHLIGHT_IN_SECONDS = 1.5


class Goal(Sprite):

    def __init__(self, x, player):
        super().__init__()

        self.image = Surface((10, 580))
        self.image.fill(white)

        self.rect = self.image.get_rect()
        self.rect.y = 10
        self.rect.x = x

        self.remaining = 0
        self.color = white
        self.player = player

    def hit(self):
        pong.app.app.sideHit.play()
        self.color = red
        self.image.fill(self.color)

        self.remaining = pong.config.FPS * GOAL_HIGHLIGHT_IN_SECONDS

    def update(self):
        if self.remaining > 0:
            self.remaining -= 1
            self.color = lighten(self.color, 2)
        self.image.fill(self.color)
