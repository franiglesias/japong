import pygame

import pong.ball
import pong.config


class Pad(pygame.sprite.Sprite):
    def __init__(self, side, speed=1):
        super().__init__()

        self.speed = speed

        self.top_region_pct = 10
        self.middle_region_pct = 15

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
        self.dy = -self.speed

    def down(self):
        self.dy = self.speed

    def stop(self):
        self.dy = 0

    def update(self):
        self.rect.y += self.dy

        border_collisions = pygame.sprite.spritecollide(self, self.borders, False)
        for _ in border_collisions:
            self.rect.y -= self.dy
            self.stop()

    def follow(self, the_ball: pong.ball.Ball):
        if the_ball.rect.y > self.rect.y:
            self.down()
        if the_ball.rect.y < self.rect.y:
            self.up()

    def hit(self, ball):
        ball_center_y = ball.rect.y + ball.radius - self.rect.y

        if ball_center_y < self.__top_region_limit():
            ball.bounce_with_pad_top()
        elif ball_center_y > self.__bottom_region_limit():
            ball.bounce_with_pad_bottom()
        elif self.__top_region_limit() <= ball_center_y < self.__upper_middle_limit():
            ball.bounce_middle_pad()
        elif self.__bottom_middle_limit() < ball_center_y <= self.__bottom_region_limit():
            ball.bounce_middle_pad()
        else:
            ball.bounce_with_pad()

    def __top_region_limit(self):
        return self.top_region_pct * self.height // 100

    def __upper_middle_limit(self):
        return (self.middle_region_pct + self.top_region_pct) * self.height // 100

    def __bottom_middle_limit(self):
        return ((100 - self.top_region_pct - self.middle_region_pct) * self.height) // 100

    def __bottom_region_limit(self):
        return ((100 - self.top_region_pct) * self.height) // 100
