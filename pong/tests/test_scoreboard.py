from unittest import TestCase

import pong.player
import pong.scoreboard


class TestScoreBoard(TestCase):

    def setUp(self) -> None:
        self.left_player = pong.player.Player('left')
        self.right_player = pong.player.Player('right')
        self.score_board = pong.scoreboard.ScoreBoard(self.left_player, self.right_player)

    def test_should_annotate_left_point(self):
        self.left_player.score = 1
        self.right_player.score = 0

        self.assertEqual(' 1 : 0 ', self.score_board.score())

    def test_should_annotate_right_point(self):
        self.left_player.score = 0
        self.right_player.score = 1

        self.assertEqual(' 0 : 1 ', self.score_board.score())

    def test_left_should_be_winner(self):
        self.left_player.score = 1
        self.right_player.score = 0

        self.assertEqual(' left WON! 1 : 0 ', self.score_board.final_board())

    def test_right_should_be_winner(self):
        self.left_player.score = 0
        self.right_player.score = 1

        self.assertEqual(' right WON! 0 : 1 ', self.score_board.final_board())
