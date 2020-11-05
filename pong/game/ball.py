import random

from pygame import Surface
from pygame.draw import ellipse
from pygame.sprite import Sprite, spritecollide

import pong.config
from pong.field.border import Border
from pong.field.goal import Goal
from pong.game.pad import Pad


class Ball(Sprite):
    def __init__(self, color, radius):
        super().__init__()

        self.color = color
        self.radius = radius
        self.dx = 0
        self.dy = 0
        self.rx = 2
        self.ry = 2
        self.remaining = 0

        self.image = Surface((self.radius * 2, self.radius * 2))

        self.image.fill(pong.config.white)
        self.image.set_colorkey(pong.config.white)
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
        direction = random.choice([(-1, -1), (1, -1), (1, 1), (-1, 1)])
        self.dx = direction[0]
        self.dy = direction[1]

    def vertical_position(self):
        return self.rect.y

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        self._manage_border_collisions()
        self._manage_pad_hits()

        if self.remaining > 0:
            self.remaining -= 1
        else:
            self.rx = 2
            self.ry = 2

        self.image.fill(pong.config.white)
        self.image.set_colorkey(pong.config.white)

        width = self.radius * self.rx
        height = self.radius * self.ry

        y = self.radius - (height / 2)
        x = self.radius - (width / 2)
        ellipse(self.image, self.color, [x, y, width, height])

    def _manage_pad_hits(self):
        pad_collisions = spritecollide(self, self.pads, False)
        pad: Pad
        for pad in pad_collisions:
            self._horiz_rebound()
            self._start_transformation_count_down()
            self.rx = 1.3
            pad.hit(self)

    def _horiz_rebound(self):
        self.rect.x -= self.dx

    def _manage_border_collisions(self):
        border_collisions = spritecollide(self, self.borders, False)
        border: Border
        for border in border_collisions:
            self._vertical_rebound()
            self._start_transformation_count_down()
            self.ry = 1.3
            self.bounce_with_border()
            border.hit()

    def _vertical_rebound(self):
        self.rect.y -= self.dy

    def manage_goals(self):
        goal_collisions = spritecollide(self, self.goals, False)
        goal: Goal
        for goal in goal_collisions:
            goal.hit()
            goal.player.win_point()
            self.restart()

    def bounce_with_border(self):
        self.dy *= -1

    def bounce_with_pad(self):
        self.dx = 1 * -(self.dx // abs(self.dx))
        self.dy = 1 * (self.dy // abs(self.dy))

    def bounce_middle_pad(self):
        self.dx = 2 * -(self.dx // abs(self.dx))
        self.dy = 2 * (self.dy // abs(self.dy))

    def bounce_with_pad_top(self):
        self.dx = 1 * -(self.dx // abs(self.dx))
        self.dy = -2

    def bounce_with_pad_bottom(self):
        self.dx = 1 * -(self.dx // abs(self.dx))
        self.dy = 2

    def _start_transformation_count_down(self):
        self.remaining = pong.config.FPS / 16
