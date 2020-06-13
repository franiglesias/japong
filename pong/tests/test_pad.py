from unittest import TestCase

import pong.ball
import pong.pad


class TestPad(TestCase):
    def test_ball_hits_in_central_region_left_pad(self):
        ball = pong.ball.Ball((100, 100, 100), 10)
        pad = pong.pad.Pad('left')

        ball_center_y = 140  # [18,57]

        pad.rect.y = 100
        ball.rect.y = ball_center_y - ball.radius

        ball.dx = -2
        ball.dy = 2

        pad.hit(ball)

        self.assertEqual(1, ball.dx)
        self.assertEqual(1, ball.dy)

    def test_ball_hits_in_upper_intermediate_region_left_pad(self):
        ball = pong.ball.Ball((100, 100, 100), 10)
        pad = pong.pad.Pad('left')

        ball_center_y = 112  # [7,21]

        pad.rect.y = 100
        ball.rect.y = ball_center_y - ball.radius

        ball.dx = -1
        ball.dy = 1

        pad.hit(ball)

        self.assertEqual(2, ball.dx)
        self.assertEqual(2, ball.dy)

    def test_ball_hits_in_lower_intermediate_region_left_pad(self):
        ball = pong.ball.Ball((100, 100, 100), 10)
        pad = pong.pad.Pad('left')

        ball_center_y = 162  # [57,68]

        pad.rect.y = 100
        ball.rect.y = ball_center_y - ball.radius

        ball.dx = -1
        ball.dy = 1

        pad.hit(ball)

        self.assertEqual(2, ball.dx)
        self.assertEqual(2, ball.dy)

    def test_ball_hits_in_upper_top_region_left_pad(self):
        ball = pong.ball.Ball((100, 100, 100), 10)
        pad = pong.pad.Pad('left')

        ball_center_y = 104  # [0, 7]

        pad.rect.y = 100
        ball.rect.y = ball_center_y - ball.radius

        ball.dx = -1
        ball.dy = 1

        pad.hit(ball)

        self.assertEqual(1, ball.dx)
        self.assertEqual(-2, ball.dy)

    def test_ball_hits_in_bottom_top_region_left_pad(self):
        ball = pong.ball.Ball((100, 100, 100), 10)
        pad = pong.pad.Pad('left')

        ball_center_y = 170  # [68, 75]

        pad.rect.y = 100
        ball.rect.y = ball_center_y - ball.radius

        ball.dx = -1
        ball.dy = 1

        pad.hit(ball)

        self.assertEqual(1, ball.dx)
        self.assertEqual(2, ball.dy)
