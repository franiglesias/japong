from pygame.sprite import Sprite, spritecollide
from pygame.surface import Surface

from config import white
from game.ball import Ball
from game.control.control_engine import ControlEngine
from utils.soundplayer import SoundPlayer


class Pad(Sprite):
    def __init__(self, side, speed, engine: ControlEngine):
        super().__init__()

        self.speed = speed

        self.engine = engine
        self.engine.bind_pad(self)

        self.top_region_pct = 10
        self.middle_region_pct = 15

        self.width = 25
        self.height = 75

        self.dy = 0

        self.image = Surface((self.width, self.height))
        self.image.fill(white)

        self.rect = self.image.get_rect()

        if side == 'left':
            self.margin = 25
        else:
            self.margin = 775 - self.width

        self.rect.y = 300
        self.rect.x = self.margin
        self.borders = None

        self.balls = None

    def bind_ball(self, ball):
        self.balls = [ball]

    def up(self):
        self.dy = -self.speed

    def down(self):
        self.dy = self.speed

    def stop(self):
        self.dy = 0

    def update(self):
        self.rect.y += self.dy

        self.__border_collision()
        self.__ball_collision()

    def __ball_collision(self):
        ball: Ball
        for ball in spritecollide(self, self.balls, False):
            self.hit(ball)

    def __border_collision(self):
        for _ in spritecollide(self, self.borders, False):
            self.rect.y -= self.dy
            self.stop()

    def vertical_position(self):
        return self.rect.y

    def handle(self, *events):
        self.engine.handle(events)

    def hit(self, ball: Ball):
        SoundPlayer().play('pad-hit')
        if self.hit_top(ball):
            ball.bounce_with_pad(1, -2)
        elif self.hit_bottom(ball):
            ball.bounce_with_pad(1, 2)
        elif self.hit_middle_top(ball):
            ball.bounce_with_pad(2, 2)
        elif self.hit_middle_bottom(ball):
            ball.bounce_with_pad(2, 2)
        else:
            ball.bounce_with_pad(1, 1)

    def hit_middle_bottom(self, ball):
        return self.__bottom_middle_limit() < ball.y_center(self.rect.y) <= self.__bottom_region_limit()

    def hit_middle_top(self, ball):
        return self.__top_region_limit() <= ball.y_center(self.rect.y) < self.__upper_middle_limit()

    def hit_bottom(self, ball):
        return ball.y_center(self.rect.y) > self.__bottom_region_limit()

    def hit_top(self, ball):
        return ball.y_center(self.rect.y) < self.__top_region_limit()

    def __top_region_limit(self):
        return self.top_region_pct * self.height // 100

    def __upper_middle_limit(self):
        return (self.middle_region_pct + self.top_region_pct) * self.height // 100

    def __bottom_middle_limit(self):
        return ((100 - self.top_region_pct - self.middle_region_pct) * self.height) // 100

    def __bottom_region_limit(self):
        return ((100 - self.top_region_pct) * self.height) // 100
