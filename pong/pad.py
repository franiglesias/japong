import random

import pygame

import pong.ball
import pong.config


class Pad(pygame.sprite.Sprite):
    def __init__(self, side):
        super().__init__()

        self.width = 25
        self.height = 75

        self.dy = 0

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(pong.config.white)

        self.rect = self.image.get_rect()

        if side == 'left':
            self.margin = 25
        else:
            self.margin = 775 - self.width

        self.rect.y = 300
        self.rect.x = self.margin
        self.borders = None

    def up(self):
        self.dy = -1

    def down(self):
        self.dy = 1

    def stop(self):
        self.dy = 0

    def update(self):
        self.rect.y += self.dy

        border_collisions = pygame.sprite.spritecollide(self, self.borders, False)
        for _ in border_collisions:
            self.rect.y -= self.dy
            self.stop()

    def follow(self, the_ball: pong.ball.Ball):
        if random.randint(0, 10) > 5:
            self.stop()
            return
        if the_ball.rect.y > self.rect.y:
            self.down()
        if the_ball.rect.y < self.rect.y:
            self.up()

    def hit(self, ball):
        ball_y_position_respect_pad = ball.rect.y + ball.radius - self.rect.y

        if ball_y_position_respect_pad < 7:
            ball.bounce_with_pad_top()
        elif ball_y_position_respect_pad > 68:
            ball.bounce_with_pad_bottom()
        elif 7 <= ball_y_position_respect_pad < 18 or 57 < ball_y_position_respect_pad <= 68:
            ball.bounce_middle_pad()
        else:
            ball.bounce_with_pad()
