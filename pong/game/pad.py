from pygame.sprite import Sprite, spritecollide, Group

from config import white
from field.bound_to_ball import BoundToBall
from field.positionable import Positionable
from game.ball import Ball
from game.control.control_engine import ControlEngine
from utils.image import create_image
from utils.soundplayer import SoundPlayer


class Pad(Sprite, Positionable, BoundToBall):
    def __init__(self, side, engine: ControlEngine, height=75, width=25):
        super().__init__()

        self.engine = engine
        self.engine.bind_pad(self)

        self.dy = 0

        self.image = create_image(width, height, white)
        self.rect = self.image.get_rect()

        self.set_position(side.pad_x(), 300 - (75 // 2))

        self.borders = None

        self.regions = [
            TopRegion(height, 10),
            MiddleTopRegion(height, 25),
            MiddleRegion(height, height),
            MiddleBottomRegion(height, 90),
            BottomRegion(height, 100)
        ]

    def up(self):
        self.dy = -self.engine.speed()

    def down(self):
        self.dy = self.engine.speed()

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
