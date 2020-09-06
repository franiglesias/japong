from unittest import TestCase

from pong.game.ball import Ball


class TestBall(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.ball = Ball((100, 100, 100), 10)

    def test_bounce_with_right_pad(self):
        self.ball.dx = 1
        self.ball.dy = 1

        self.ball.bounce_with_pad()

        self.assertEqual(-1, self.ball.dx)
        self.assertEqual(1, self.ball.dy)

    def test_bounce_with_left_pad(self):
        self.ball.dx = -1
        self.ball.dy = 1

        self.ball.bounce_with_pad()

        self.assertEqual(1, self.ball.dx)
        self.assertEqual(1, self.ball.dy)

    def test_bounce_in_central_right_pad_region_resets_speed(self):
        self.ball.dx = 2
        self.ball.dy = 2

        self.ball.bounce_with_pad()

        self.assertEqual(-1, self.ball.dx)
        self.assertEqual(1, self.ball.dy)

    def test_bounce_in_central_left_pad_region_resets_speed(self):
        self.ball.dx = -2
        self.ball.dy = -2

        self.ball.bounce_with_pad()

        self.assertEqual(1, self.ball.dx)
        self.assertEqual(-1, self.ball.dy)

    def test_bounce_with_border_top(self):
        self.ball.dx = 1
        self.ball.dy = -1

        self.ball.bounce_with_border()

        self.assertEqual(1, self.ball.dy)
        self.assertEqual(1, self.ball.dx)

    def test_bounce_with_border_bottom(self):
        self.ball.dx = 1
        self.ball.dy = 1

        self.ball.bounce_with_border()

        self.assertEqual(-1, self.ball.dy)
        self.assertEqual(1, self.ball.dx)
