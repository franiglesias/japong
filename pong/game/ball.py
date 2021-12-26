import random

from pygame import Surface
from pygame.draw import ellipse
from pygame.sprite import Sprite, spritecollide

from config import white, FPS
from game.direction import Direction
from game.pad import Pad


class Ball(Sprite):
    def __init__(self, color, radius):
        super().__init__()

        self.color = color
        self.radius = radius
        self.rx = 2
        self.ry = 2
        self.remaining = 0
        self.direction = Direction(0, 0)

        self.image = Surface((self.radius * 2, self.radius * 2))
        self.image.fill(white)
        self.image.set_colorkey(white)
        ellipse(self.image, self.color, [0, 0, self.radius * self.rx, self.radius * self.ry])
        self.rect = self.image.get_rect()

        self.restart()

        self.borders = None
        self.goals = None
        self.pads = None

    def restart(self):
        self.rect.x = 400
        self.rect.y = 300

        self._set_random_direction()

    def _set_random_direction(self):
        self.direction = random.choice([
            Direction(-1, -1),
            Direction(1, -1),
            Direction(1, 1),
            Direction(-1, 1)
        ])

    def vertical_position(self):
        return self.rect.y

    def update(self):
        self.direction.update(self.rect)

        self._manage_pad_hits()

        if self.remaining > 0:
            self.remaining -= 1
        else:
            self.rx = 2
            self.ry = 2

        self.image.fill(white)
        self.image.set_colorkey(white)

        width = self.radius * self.rx
        height = self.radius * self.ry

        y = self.radius - (height / 2)
        x = self.radius - (width / 2)
        ellipse(self.image, self.color, [x, y, width, height])

    def _manage_pad_hits(self):
        pad_collisions = spritecollide(self, self.pads, False)
        pad: Pad
        for pad in pad_collisions:
            self.direction.horiz_rebound(self.rect)
            self._start_transformation_count_down()
            self.rx = 1.3
            pad.hit(self)

    def border_rebound(self):
        self.direction.vertical_rebound(self.rect)
        self.direction.border_bounce()
        self._start_transformation_count_down()
        self.ry = 1.3

    def goal(self):
        self.restart()

    def bounce_with_pad(self):
        self.direction.pad_bounce(1, 1)

    def bounce_middle_pad(self):
        self.direction.pad_bounce(2, 2)

    def bounce_with_pad_top(self):
        self.direction.pad_bounce(1, -2)

    def bounce_with_pad_bottom(self):
        self.direction.pad_bounce(1, 2)

    def _start_transformation_count_down(self):
        self.remaining = FPS / 16
