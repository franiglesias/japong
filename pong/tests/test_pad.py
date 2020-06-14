from unittest import TestCase

import pong.ball
import pong.game.pad


class TestPad(TestCase):
    def setUp(self) -> None:
        self.pad = pong.game.pad.Pad('left')
        self.ball = pong.ball.Ball((100, 100, 100), 10)
        self.pad.rect.y = 100

    def test_ball_hits_in_central_region_left_pad(self):
        self.__given_ball_hits_pad_at(40)
        self.__given_ball_has_speed_of(-2, 2)

        self.pad.hit(self.ball)

        self.assertSpeedEqual(1, 1)

    def test_ball_hits_in_upper_intermediate_region_left_pad(self):
        self.__given_ball_hits_pad_at(12)
        self.__given_ball_has_speed_of(-1, 1)

        self.pad.hit(self.ball)

        self.assertSpeedEqual(2, 2)

    def test_ball_hits_in_lower_intermediate_region_left_pad(self):
        self.__given_ball_hits_pad_at(62)
        self.__given_ball_has_speed_of(-1, 1)

        self.pad.hit(self.ball)

        self.assertEqual(2, self.ball.dx)
        self.assertEqual(2, self.ball.dy)

    def test_ball_hits_in_upper_top_region_left_pad(self):
        self.__given_ball_hits_pad_at(4)
        self.__given_ball_has_speed_of(-1, 1)

        self.pad.hit(self.ball)

        self.assertSpeedEqual(1, -2)

    def test_ball_hits_in_bottom_top_region_left_pad(self):
        self.__given_ball_hits_pad_at(70)
        self.__given_ball_has_speed_of(-1, 1)

        self.pad.hit(self.ball)

        self.assertSpeedEqual(1, 2)

    def test_should_follow_ball_down(self):
        self.ball.rect.y = 200

        self.pad.follow(self.ball)

        self.assertEqual(1, self.pad.dy)

    def test_should_follow_ball_up(self):
        self.ball.rect.y = 20

        self.pad.follow(self.ball)

        self.assertEqual(-1, self.pad.dy)

    def assertSpeedEqual(self, dx, dy):
        self.assertEqual(dx, self.ball.dx)
        self.assertEqual(dy, self.ball.dy)

    def __given_ball_hits_pad_at(self, height):
        self.ball.rect.y = self.pad.rect.y + height - self.ball.radius

    def __given_ball_has_speed_of(self, dx, dy):
        self.ball.dx = dx
        self.ball.dy = dy
