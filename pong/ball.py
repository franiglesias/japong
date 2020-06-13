import random

import pygame

import pong
import pong.app.app
import pong.config


class Ball(pygame.sprite.Sprite):
    def __init__(self, color, radius):
        super().__init__()

        self.color = color
        self.radius = radius
        self.dx = 0
        self.dy = 0
        self.rx = 2
        self.ry = 2
        self.remaining = 0

        self.image = pygame.Surface((self.radius * 2, self.radius * 2))

        self.image.fill(pong.config.white)
        self.image.set_colorkey(pong.config.white)
        pygame.draw.ellipse(self.image, self.color, [0, 0, self.radius * self.rx, self.radius * self.ry])

        self.rect = self.image.get_rect()
        self.restart()

        self.borders = None
        self.pads = None

    def restart(self):
        self.rect.x = 400
        self.rect.y = 300

        self._set_random_direction()

    def _set_random_direction(self):
        direction = random.choice([(-1, -1), (1, -1), (1, 1), (-1, 1)])
        self.dx = direction[0]
        self.dy = direction[1]

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        border_collisions = pygame.sprite.spritecollide(self, self.borders, False)
        for _ in border_collisions:
            self.rect.y -= self.dy
            self._start_transformation_count_down()
            self._play_side_hit_sound()
            self.ry = 1.3
            self.bounce_with_border()

        pad_collisions = pygame.sprite.spritecollide(self, self.pads, False)
        for pad in pad_collisions:
            self.rect.x -= self.dx
            self._start_transformation_count_down()
            self._play_pad_hit_sound()
            self.rx = 1.3
            self.bounce_with_pad(pad)

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
        pygame.draw.ellipse(self.image, self.color, [x, y, width, height])

    def bounce_with_border(self):
        self.dy *= -1

    def bounce_with_pad(self, pad):
        self.dx = 1 * -(self.dx // abs(self.dx))
        self.dy = 1 * (self.dy // abs(self.dy))


    @staticmethod
    def _play_pad_hit_sound():
        pong.app.app.playerHit.play()

    @staticmethod
    def _play_side_hit_sound():
        pong.app.app.sideHit.play()

    def _start_transformation_count_down(self):
        self.remaining = pong.config.FPS / 16
