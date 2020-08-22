from unittest import TestCase

import pong.config
from pong.ball import Ball
from pong.game.control.computer_control_engine import ComputerControlEngine
from pong.player import Player
from pong.scoreboard import ScoreBoard


class TestScoreBoard(TestCase):

    def setUp(self) -> None:
        ball = Ball(pong.config.white, 10)
        engine = ComputerControlEngine(ball)
        self.left_player = Player('left', 'left', engine)
        self.right_player = Player('right', 'right', engine)
        self.score_board = ScoreBoard(self.left_player, self.right_player)

    def test_should_annotate_left_point(self):
        self.left_player.win_point()

        self.assertEqual(' 1 : 0 ', self.score_board.score())

    def test_should_annotate_right_point(self):
        self.right_player.win_point()

        self.assertEqual(' 0 : 1 ', self.score_board.score())

    def test_left_should_be_winner(self):
        self.left_player.win_point()

        self.assertEqual(' left WON! 1 : 0 ', self.score_board.final_board())

    def test_right_should_be_winner(self):
        self.right_player.win_point()

        self.assertEqual(' right WON! 0 : 1 ', self.score_board.final_board())
