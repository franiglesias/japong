from unittest import TestCase

from game.ball import Ball
from game.control.keyboard_control_engine import KeyboardControlEngine
from game.pad import Pad
from game.side import Left


class TestPad(TestCase):
    def setUp(self) -> None:
        self.ball = Ball((100, 100, 100), 10)
        self.__given_ball_has_speed_of(1, 1)
        self.pad = Pad(Left(), KeyboardControlEngine(('u', 'd')))
        self.pad.rect.y = 100

    def test_ball_hits_in_central_region_left_pad(self):
        self.__given_ball_hits_pad_at(40)

        self.pad.hit(self.ball)

        self.assertSpeedEqual(-1, 1)

    def test_ball_hits_in_upper_intermediate_region_left_pad(self):
        self.__given_ball_hits_pad_at(12)

        self.pad.hit(self.ball)

        self.assertSpeedEqual(-2, 2)

    def test_ball_hits_in_lower_intermediate_region_left_pad(self):
        self.__given_ball_hits_pad_at(62)

        self.pad.hit(self.ball)

        self.assertSpeedEqual(-2, 2)

    def test_ball_hits_in_upper_top_region_left_pad(self):
        self.__given_ball_hits_pad_at(4)

        self.pad.hit(self.ball)

        self.assertSpeedEqual(-1, -2)

    def test_ball_hits_in_bottom_region_left_pad(self):
        self.__given_ball_hits_pad_at(70)

        self.pad.hit(self.ball)

        self.assertSpeedEqual(-1, 2)

    def assertSpeedEqual(self, dx, dy):
        self.assertEqual(dx, self.ball.direction.dx)
        self.assertEqual(dy, self.ball.direction.dy)

    def __given_ball_hits_pad_at(self, height):
        self.ball.rect.y = self.pad.rect.y + height - self.ball.radius

    def __given_ball_has_speed_of(self, dx, dy):
        self.ball.direction.dx = dx
        self.ball.direction.dy = dy
