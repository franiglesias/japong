from unittest import TestCase

from game.ball import Ball
from game.direction import Direction


class TestBall(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.ball = Ball((100, 100, 100), 10)

    def test_bounce_with_right_pad(self):
        self.ball.direction = Direction(1, 1)

        self.ball.bounce_with_pad()

        self.assertEqual(-1, self.ball.direction.dx)
        self.assertEqual(1, self.ball.direction.dy)

    def test_bounce_with_left_pad(self):
        self.ball.direction = Direction(-1, 1)

        self.ball.bounce_with_pad()

        self.assertEqual(1, self.ball.direction.dx)
        self.assertEqual(1, self.ball.direction.dy)

    def test_bounce_in_central_right_pad_region_resets_speed(self):
        self.ball.direction = Direction(2, 2)

        self.ball.bounce_with_pad()

        self.assertEqual(-1, self.ball.direction.dx)
        self.assertEqual(1, self.ball.direction.dy)

    def test_bounce_in_central_left_pad_region_resets_speed(self):
        self.ball.direction = Direction(-2, -2)
        self.ball.bounce_with_pad()

        self.assertEqual(1, self.ball.direction.dx)
        self.assertEqual(-1, self.ball.direction.dy)

    def test_bounce_with_border_top(self):
        self.ball.direction = Direction(1, -1)

        ball = self.ball
        ball.vertical_bounce()

        self.assertEqual(1, self.ball.direction.dy)
        self.assertEqual(1, self.ball.direction.dx)

    def test_bounce_with_border_bottom(self):
        self.ball.direction = Direction(1, 1)

        ball = self.ball
        ball.vertical_bounce()

        self.assertEqual(-1, self.ball.direction.dy)
        self.assertEqual(1, self.ball.direction.dx)
