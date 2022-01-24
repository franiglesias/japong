from unittest import TestCase

from config import white
from game.ball import Ball
from game.control.computer_control_engine import ComputerControlEngine
from game.pad import Pad
from game.player import Player
from game.scoring.match import Match
from game.scoring.score_manager import ScoreManager
from game.side import Left


class TestScoreManager(TestCase):
    def testLeftPlayerWinsSet(self):
        self.scoreAfterSet(5, 0)
        self.assertEqual(self.left_player, self.score_manager.winner())

    def testShouldNotWinASetIfMinimumPointsNotReached(self):
        self.scoreAfterSet(4, 0)
        self.assertFalse(self.score_manager.end_of_set())

    def testShouldWinASetByTwoOrMorePoints(self):
        self.scoreAfterSet(5, 0)
        self.assertTrue(self.score_manager.end_of_set())
        self.scoreAfterSet(5, 3)
        self.assertTrue(self.score_manager.end_of_set())
        self.scoreAfterSet(7, 5)
        self.assertTrue(self.score_manager.end_of_set())

    def testShouldNotWinSetIfNoEnoughDifference(self):
        self.scoreAfterSet(5, 4)
        self.assertFalse(self.score_manager.end_of_set())
        self.scoreAfterSet(6, 5)
        self.assertFalse(self.score_manager.end_of_set())
        self.scoreAfterSet(7, 6)
        self.assertFalse(self.score_manager.end_of_set())

    def testShouldEndGame(self):
        self.scoreInSets(2, 0)
        self.assertTrue(self.score_manager.end_of_game())
        self.scoreInSets(2, 1)
        self.assertTrue(self.score_manager.end_of_game())
        self.scoreInSets(3, 0)
        self.assertTrue(self.score_manager.end_of_game())

    def test_should_not_end_game(self):
        self.scoreInSets(0, 0)
        self.assertFalse(self.score_manager.end_of_game())
        self.scoreInSets(1, 1)
        self.assertFalse(self.score_manager.end_of_game())
        self.scoreInSets(1, 0)
        self.assertFalse(self.score_manager.end_of_game())

    def test_one_set_match_should_have_only_one_set(self):
        self.left_player = self.preparePlayer()
        self.right_player = self.preparePlayer()
        self.score_manager = ScoreManager(Match(1, 5))
        self.score_manager.register_players(self.left_player, self.right_player)
        self.left_player.win_set()
        self.assertTrue(self.score_manager.end_of_game())

    def scoreAfterSet(self, left, right):
        self.left_player = self.preparePlayer()
        self.right_player = self.preparePlayer()
        for i in range(left):
            self.left_player.win_point()
        for i in range(right):
            self.right_player.win_point()
        self.score_manager = ScoreManager(Match(3, 5))
        self.score_manager.register_players(self.left_player, self.right_player)

    def scoreInSets(self, left, right):
        self.left_player = self.preparePlayer()
        self.right_player = self.preparePlayer()
        for i in range(left):
            self.left_player.win_set()
        for i in range(right):
            self.right_player.win_set()
        self.score_manager = ScoreManager(Match(3, 5))
        self.score_manager.register_players(self.left_player, self.right_player)

    @staticmethod
    def preparePlayer():
        ball = Ball(white, 10)
        engine = ComputerControlEngine(ball)
        pad = Pad(Left(), engine)
        return Player('left', Left())
