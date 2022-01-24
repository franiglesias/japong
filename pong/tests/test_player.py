from unittest import TestCase

from config import white
from game.ball import Ball
from game.control.computer_control_engine import ComputerControlEngine
from game.pad import Pad
from game.player import Player
from game.side import Left


class TestPlayer(TestCase):
    def test_win_set(self):
        ball = Ball(white, 10)
        engine = ComputerControlEngine(ball)
        pad = Pad(Left(), engine)
        self.player = Player('left', Left())
        self.player.win_set()
        self.assertEqual(1, self.player.sets())
