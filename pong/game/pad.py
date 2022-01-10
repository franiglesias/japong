from pygame.sprite import Sprite, spritecollide, Group

from config import white
from field.positionable import Positionable
from field.reacts_to_ball import ReactsToBall
from game.ball import Ball
from game.control.control_engine import ControlEngine
from utils.image import create_image
from utils.soundplayer import SoundPlayer


class Pad(Sprite, Positionable, ReactsToBall):
    def __init__(self, side, speed, engine: ControlEngine):
        super().__init__()

        self.speed = speed

        self.engine = engine
        self.engine.bind_pad(self)

        self.dy = 0

        self.image = create_image(25, 75, white)
        self.rect = self.image.get_rect()

        self.set_position(side.pad(), 300)

        self.borders = None

        self.regions = [
            TopRegion(75, 10),
            MiddleTopRegion(75, 25),
            MiddleRegion(75, 75),
            MiddleBottomRegion(75, 90),
            BottomRegion(75, 100)
        ]

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

    def __border_collision(self):
        for _ in spritecollide(self, self.borders, False):
            self.rect.y -= self.dy
            self.stop()

    def __ball_collision(self):
        collisions = spritecollide(self, Group(self.ball), False)

        if len(collisions) > 0:
            self.hit(self.ball)

    def vertical_position(self):
        return self.rect.y

    def handle(self, *events):
        self.engine.handle(events)

    def hit(self, ball: Ball):
        SoundPlayer().play('pad-hit')
        region = PadRegion.where(ball, self)
        region.bounce(ball)


class PadRegion():
    def __init__(self, height, pct):
        self.height = height
        self.pct = pct

    def hit(self, ball: Ball, pad: Pad):
        return ball.y_center() < self.height * self.pct // 100 + pad.rect.y

    def bounce(self, ball):
        ball.bounce_with_pad(1, 1)

    @staticmethod
    def where(ball: Ball, pad: Pad):
        for region in pad.regions:
            if region.hit(ball, pad):
                return region
        return PadRegion(75, 0)


class TopRegion(PadRegion):
    def bounce(self, ball):
        ball.bounce_with_pad(1, -2)


class MiddleTopRegion(PadRegion):
    def bounce(self, ball):
        ball.bounce_with_pad(2, 2)


class MiddleRegion(PadRegion):
    def bounce(self, ball):
        ball.bounce_with_pad(1, 1)


class MiddleBottomRegion(PadRegion):
    def bounce(self, ball):
        ball.bounce_with_pad(2, 2)


class BottomRegion(PadRegion):
    def bounce(self, ball):
        ball.bounce_with_pad(1, 2)
