from unittest import TestCase

from mock import patch

from game.scoring.match import Match
from game.scoring.score_manager import ScoreManager
from game.scoring.scoreboard import ScoreBoard


class TestScoreBoard(TestCase):

    @patch.object(ScoreManager, 'points')
    def test_should_annotate_left_point(self, score_manager_points_will):
        score_manager_points_will.return_value = (1, 0)
        score_board = ScoreBoard(ScoreManager(Match(1, 1)))
        self.assertEqual('1   0', f'{score_board.points(0)}   {score_board.points(1)}')

    @patch.object(ScoreManager, 'points')
    def test_should_annotate_right_point(self, score_manager_points_will):
        score_manager_points_will.return_value = (0, 1)
        score_board = ScoreBoard(ScoreManager(Match(1, 1)))
        self.assertEqual('0   1', f'{score_board.points(0)}   {score_board.points(1)}')
