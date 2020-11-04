from unittest import TestCase

import pygame

import pong.config
from app.scene import Scene
from app.window import Window
from pong.game.ball import Ball
from pong.game.control.computer_control_engine import ComputerControlEngine
from pong.game.player import Player
from pong.game.scoring.score_manager import ScoreManager
from pong.game.scoring.scoreboard import ScoreBoard


class TestScoreBoard(TestCase):

    def setUp(self) -> None:
        ball = Ball(pong.config.white, 10)
        engine = ComputerControlEngine(ball)
        self.left_player = Player('left', 'left', engine)
        self.right_player = Player('right', 'right', engine)
        self.score_manager = ScoreManager(self.left_player, self.right_player, (1, 5))
        self.score_board = ScoreBoard(self.score_manager)
        self.scene = Scene(Window(100, 100, 'Test'))

    def test_should_annotate_left_point(self):
        self.left_player.win_point()

        self.assertEqual('1   0', self.score_board.points())

    def test_should_annotate_right_point(self):
        self.right_player.win_point()

        self.assertEqual('0   1', self.score_board.points())
