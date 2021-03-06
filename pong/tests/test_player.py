from unittest import TestCase

import pong.config
from game.ball import Ball
from game.control.computer_control_engine import ComputerControlEngine
from game.player import Player


class TestPlayer(TestCase):
    def test_win_set(self):
        ball = Ball(pong.config.white, 10)
        engine = ComputerControlEngine(ball)
        self.player = Player('left', 'left', engine)
        self.player.win_set()
        self.assertEqual(1, self.player.sets())
